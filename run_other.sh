python --version &>/dev/null
if [ $? -ne 0 ]; then
    echo "Python is not installed. Please install Python 3.10 or later."
    exit 1
fi

PYTHON_VERSION=$(python -c 'import platform; print(platform.python_version())')

MAJOR=$(echo $PYTHON_VERSION | cut -d '.' -f 1)
MINOR=$(echo $PYTHON_VERSION | cut -d '.' -f 2)

if [ "$MAJOR" -lt 3 ] || { [ "$MAJOR" -eq 3 ] && [ "$MINOR" -lt 10 ]; }; then
    echo "Python version is lower than 3.10. Please install Python 3.10 or later."
    exit 1
fi

if [ -f "listmanager.py" ]; then
    python listmanager.py
else
    echo "File listmanager.py not found. Please make sure it exists in this directory."
    exit 1
fi