# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['c:\\Docs Andre\\pyFeed'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [('logoCesumar.png', 'C:\\Docs Andre\\pyFeed\\static\\logoCesumar.png', 'DATA')]
a.datas += [('icon-arvore.png', 'C:\\Docs Andre\\pyFeed\\static\\icon-arvore.png', 'DATA')]
a.datas += [('icon-estrut.png', 'C:\\Docs Andre\\pyFeed\\static\\icon-estrut.png', 'DATA')]
a.datas += [('icon-settings.png', 'C:\\Docs Andre\\pyFeed\\static\\icon-settings.png', 'DATA')]
a.datas += [('icon-txtQuestao.png', 'C:\\Docs Andre\\pyFeed\\static\\icon-txtQuestao.png', 'DATA')]
a.datas += [('frequency_dictionary_pt_82_765.txt', 'C:\\Docs Andre\\pyFeed\\static\\frequency_dictionary_pt_82_765.txt', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='CadQuest',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
