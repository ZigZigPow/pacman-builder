# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas = [
    ("sounds\\theme.mp3", "sounds"),
    ("sounds\\pac.mp3", "sounds"),
    ("sounds\\lose.mp3", "sounds"),
    ("sounds\\level-win-6416.mp3", "sounds"),
    ("mazes\\maze.txt", "mazes"),
]
binaries = []
hiddenimports = []
tmp_ret = collect_all("pygame")
datas += tmp_ret[0]
binaries += tmp_ret[1]
hiddenimports += tmp_ret[2]


block_cipher = None


pacman_a = Analysis(
    ["pacman.py"],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pacman_pyz = PYZ(pacman_a.pure, pacman_a.zipped_data, cipher=block_cipher)

pacman_exe = EXE(
    pacman_pyz,
    pacman_a.scripts,
    [],
    exclude_binaries=True,
    name="pacman",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    pacman_exe,
    pacman_a.binaries,
    pacman_a.zipfiles,
    pacman_a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="pacman_game",
)
