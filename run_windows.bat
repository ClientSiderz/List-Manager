@echo off
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python 3.10 or later.
    pause
    exit /b
)

for /f "tokens=2 delims==" %%I in ('python -c "import platform; print(platform.python_version())"') do set PYTHON_VERSION=%%I

for /f "tokens=1,2 delims=." %%a in ("%PYTHON_VERSION%") do (
    set MAJOR=%%a
    set MINOR=%%b
)

IF %MAJOR% LSS 3 (
    echo Python version is lower than 3.10. Please install Python 3.10 or later.
    pause
    exit /b
) ELSE IF %MAJOR% EQU 3 IF %MINOR% LSS 10 (
    echo Python version is lower than 3.10. Please install Python 3.10 or later.
    pause
    exit /b
)

if exist listmanager.py (
    python listmanager.py
) else (
    echo File listmanager.py not found. Please make sure it exists in this directory.
    pause
)