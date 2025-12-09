#!/bin/bash

# Vercel Python Setup
echo "==================================="
echo "Setting up Python environment..."
echo "==================================="

# Check Python availability
if command -v python3 &> /dev/null; then
    echo "✓ Python3 found:"
    python3 --version
    PYTHON_PATH=$(which python3)
    echo "  Path: $PYTHON_PATH"
else
    echo "✗ Python3 not found, trying python..."
    if command -v python &> /dev/null; then
        python --version
        PYTHON_PATH=$(which python)
        echo "  Path: $PYTHON_PATH"
    else
        echo "✗ No Python found!"
        exit 1
    fi
fi

# Install Python dependencies
echo ""
echo "==================================="
echo "Installing Python dependencies..."
echo "==================================="

pip3 install --user -r requirements.txt || pip install --user -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Python packages installed successfully"
else
    echo "✗ Failed to install Python packages"
    exit 1
fi

# Verify installations
echo ""
echo "==================================="
echo "Verifying Python packages..."
echo "==================================="
python3 -c "import reportlab; print(f'✓ reportlab {reportlab.Version}')" 2>/dev/null || \
python -c "import reportlab; print(f'✓ reportlab {reportlab.Version}')"

python3 -c "import requests; print(f'✓ requests {requests.__version__}')" 2>/dev/null || \
python -c "import requests; print(f'✓ requests {requests.__version__}')"

# Build Nuxt
echo ""
echo "==================================="
echo "Building Nuxt application..."
echo "==================================="

npm run build

if [ $? -eq 0 ]; then
    echo ""
    echo "==================================="
    echo "✓ Build completed successfully!"
    echo "==================================="
else
    echo ""
    echo "==================================="
    echo "✗ Build failed!"
    echo "==================================="
    exit 1
fi

