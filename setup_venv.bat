@echo off
set VENV_NAME=venv

py -m pip install --upgrade pip

echo Creating virtual environment...
python -m venv %VENV_NAME%
if %errorlevel% neq 0 (
    echo Failed to create virtual environment.
    exit /b %errorlevel%
)
echo Virtual environment created successfully.


echo Activating virtual environment...
call %VENV_NAME%\Scripts\activate
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    exit /b %errorlevel%
)

echo Installing Pygame...
python -m pip install pygame
if %errorlevel% neq 0 (
    echo Failed to install Pygame.
    exit /b %errorlevel%
)

echo Installing PyInstaller...
python -m pip install pyinstaller
if %errorlevel% neq 0 (
    echo Failed to install PyInstaller.
    exit /b %errorlevel%
)

echo Virtual environment setup complete.
call %VENV_NAME%\Scripts\activate.bat
