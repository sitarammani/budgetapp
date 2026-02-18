# -*- mode: python -*-
import sys
import os
from PyInstaller.utils.hooks import collect_data_files

datas = [('categories.csv', '.'), ('category_rules.csv', '.')]
if os.path.exists('.gmail_oauth_config'):
    datas.append(('.gmail_oauth_config', '.'))

a = Analysis([
    'start.py',
],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=['pandas', 'openpyxl', 'xlsxwriter', 'requests', 'bootstrap_ollama', 'natural_language_query', 'manage_rules', 'generate_reports_email'],
    hookspath=[],
    runtime_hooks=[],
    excludes=['mistral', 'model', 'models'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
p = PYZ(a.pure, a.zipped_data,
         cipher=None,
)
exe = EXE(p, a.scripts, [],
          exclude_binaries=True,
          name='budgetapp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='budgetapp'
)
