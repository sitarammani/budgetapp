# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Spending Report & Analysis System
Creates a standalone executable with all dependencies bundled
"""

import os
from pathlib import Path

block_cipher = None

# Get the directory where this spec file is located
spec_dir = Path(__file__).parent

a = Analysis(
    [str(spec_dir / 'app.py')],
    pathex=[str(spec_dir)],
    binaries=[],
    datas=[
        (str(spec_dir / 'categories.csv'), '.'),
        (str(spec_dir / 'category_map.csv'), '.'),
        (str(spec_dir / 'category_rules.csv'), '.'),
    ],
    hiddenimports=[
        'pandas',
        'openpyxl',
        'xlsxwriter',
        'requests',
        'pdfplumber',
        'google.auth',
        'google.api_core',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Spending-Report-System',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
