#!/usr/bin/env python3
"""
Notion to PDF Export Script for Vercel Serverless Function
This is a simplified version optimized for serverless execution
"""

import sys
import argparse
import os
import requests
from datetime import datetime

# Try importing reportlab, install if needed
try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib.enums import TA_JUSTIFY
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
    from reportlab.lib import colors
    from reportlab.pdfgen import canvas
except ImportError:
    print("ERROR: reportlab not installed", file=sys.stderr)
    sys.exit(1)


class WatermarkedCanvas(canvas.Canvas):
    """Custom canvas that adds watermark to every page"""
    
    def __init__(self, *args, watermark_text="", **kwargs):
        super().__init__(*args, **kwargs)
        self.watermark_text = watermark_text
    
    def showPage(self):
        """Override to add watermark before showing page"""
        if self.watermark_text:
            self.saveState()
            self.setFont('Helvetica', 50)
            self.setFillColorRGB(0.9, 0.9, 0.9, alpha=0.3)
            self.translate(4.25*inch, 5.5*inch)
            self.rotate(45)
            self.drawCentredString(0, 0, self.watermark_text)
            self.restoreState()
        super().showPage()


def fetch_notion_page(token, page_id):
    """Fetch page metadata from Notion API"""
    url = f"https://api.notion.com/v1/pages/{page_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def fetch_notion_blocks(token, block_id):
    """Fetch blocks from Notion API"""
    url = f"https://api.notion.com/v1/blocks/{block_id}/children"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    
    all_blocks = []
    has_more = True
    start_cursor = None
    
    while has_more:
        params = {"page_size": 100}
        if start_cursor:
            params["start_cursor"] = start_cursor
        
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        all_blocks.extend(data.get('results', []))
        has_more = data.get('has_more', False)
        start_cursor = data.get('next_cursor')
    
    return all_blocks


def get_page_title(page_data):
    """Extract title from page metadata"""
    title_prop = page_data.get('properties', {}).get('title', {})
    if not title_prop:
        title_prop = page_data.get('properties', {}).get('Name', {})
    
    title_array = title_prop.get('title', [])
    if title_array:
        return title_array[0].get('plain_text', 'Untitled')
    return 'Untitled'


def parse_rich_text(rich_text_array):
    """Convert Notion rich text to formatted string"""
    if not rich_text_array:
        return ""
    
    result = ""
    for text_obj in rich_text_array:
        content = text_obj.get('plain_text', '')
        annotations = text_obj.get('annotations', {})
        
        if annotations.get('bold'):
            content = f"<b>{content}</b>"
        if annotations.get('italic'):
            content = f"<i>{content}</i>"
        if annotations.get('code'):
            content = f"<font name='Courier'>{content}</font>"
        
        result += content
    
    return result


def block_to_flowable(block, styles):
    """Convert a Notion block to a ReportLab flowable"""
    block_type = block.get('type')
    flowables = []
    
    if block_type == 'paragraph':
        text = parse_rich_text(block['paragraph'].get('rich_text', []))
        
        # Check for page break markers
        if text.strip().upper() in ['PAGE BREAK', 'PAGEBREAK', '--- PAGE BREAK ---']:
            flowables.append(PageBreak())
        elif text.strip():
            flowables.append(Paragraph(text, styles['Normal']))
    
    elif block_type == 'heading_1':
        text = parse_rich_text(block['heading_1'].get('rich_text', []))
        flowables.append(Paragraph(text, styles['Heading1']))
    
    elif block_type == 'heading_2':
        text = parse_rich_text(block['heading_2'].get('rich_text', []))
        flowables.append(Paragraph(text, styles['Heading2']))
    
    elif block_type == 'heading_3':
        text = parse_rich_text(block['heading_3'].get('rich_text', []))
        flowables.append(Paragraph(text, styles['Heading3']))
    
    elif block_type == 'bulleted_list_item':
        text = parse_rich_text(block['bulleted_list_item'].get('rich_text', []))
        style = ParagraphStyle(name='Bullet', parent=styles['Normal'], leftIndent=20)
        flowables.append(Paragraph(f"• {text}", style))
    
    elif block_type == 'toggle':
        text = parse_rich_text(block['toggle'].get('rich_text', []))
        if 'PAGE BREAK' in text.upper():
            flowables.append(PageBreak())
        else:
            style = ParagraphStyle(name='Toggle', parent=styles['Normal'], leftIndent=20)
            flowables.append(Paragraph(f"▶ {text}", style))
    
    return flowables


def export_to_pdf(token, page_id, output_path, watermark=None, page_size='letter', include_page_numbers=True):
    """Export Notion page to PDF"""
    
    # Fetch page data
    page_data = fetch_notion_page(token, page_id)
    page_title = get_page_title(page_data)
    
    # Fetch blocks
    blocks = fetch_notion_blocks(token, page_id)
    
    # Set page size
    size = letter if page_size == 'letter' else A4
    
    # Create PDF
    if watermark:
        doc = SimpleDocTemplate(
            output_path,
            pagesize=size,
            canvasmaker=lambda *args, **kwargs: WatermarkedCanvas(
                *args, watermark_text=watermark, **kwargs
            )
        )
    else:
        doc = SimpleDocTemplate(output_path, pagesize=size)
    
    # Build story
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    story.append(Paragraph(page_title, styles['Title']))
    story.append(Spacer(1, 0.3*inch))
    
    # Metadata
    export_date = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    story.append(Paragraph(f"<i>Exported from Notion on {export_date}</i>", styles['Normal']))
    story.append(Spacer(1, 0.5*inch))
    
    # Convert blocks
    for block in blocks:
        flowables = block_to_flowable(block, styles)
        story.extend(flowables)
    
    # Build PDF
    doc.build(story)
    
    return output_path


def main():
    parser = argparse.ArgumentParser(description='Export Notion page to PDF')
    parser.add_argument('--token', required=True, help='Notion API token')
    parser.add_argument('--page-id', required=True, help='Notion page ID')
    parser.add_argument('--output', required=True, help='Output PDF path')
    parser.add_argument('--watermark', help='Watermark text')
    parser.add_argument('--page-size', default='letter', choices=['letter', 'a4'], help='Page size')
    parser.add_argument('--page-numbers', action='store_true', help='Include page numbers')
    
    args = parser.parse_args()
    
    try:
        export_to_pdf(
            token=args.token,
            page_id=args.page_id,
            output_path=args.output,
            watermark=args.watermark,
            page_size=args.page_size,
            include_page_numbers=args.page_numbers
        )
        print(f"SUCCESS: {args.output}")
    except Exception as e:
        print(f"ERROR: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
