call activate.bat
pyinstaller pacman.spec --clean --noconfirm --distpath .
deactivate
pause