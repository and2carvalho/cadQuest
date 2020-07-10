# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['%userprofile%\\My Documents\\cadQuest'],
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
a.datas += [('logoCesumar.png', '%userprofile%\\My Documents\\cadQuest\\static\\logoCesumar.png', 'DATA')]
a.datas += [('icon-arvore.png', '%userprofile%\\My Documents\\cadQuest\\static\\icon-arvore.png', 'DATA')]
a.datas += [('icon-estrut.png', '%userprofile%\\My Documents\\cadQuest\\static\\icon-estrut.png', 'DATA')]
a.datas += [('icon-settings.png', '%userprofile%\\My Documents\\cadQuest\\static\\icon-settings.png', 'DATA')]
a.datas += [('icon-txtQuestao.png', '%userprofile%\\My Documents\\cadQuest\\static\\icon-txtQuestao.png', 'DATA')]
a.datas += [('frequency_dictionary_pt_82_765.txt', '%userprofile%\\My Documents\\cadQuest\\pyFeed\\static\\frequency_dictionary_pt_82_765.txt', 'DATA')]
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
