"""This module uses py2exe and converts all scripts and linked packages
into executable Windows programs.

Other features:
    - automatically increasing version number
      (version number stored in file VERSION)
    - puts all files created with py2exe into single zip file
"""
from distutils.core import setup
import sys
import os
# noinspection PyUnresolvedReferences
import py2exe
import zipfile
import shutil

version_file = open('VERSION')
version = [int(float(n)) for n in version_file.read().strip().split('.')]
version[-1] += 1
new_version = str(version[0])
for n in version[1:]:
    new_version += '.'+str(n)
version = new_version
version_file = open('VERSION', 'w')
version_file.write(version)
version_file.close()

sys.argv.append('py2exe')
sys.argv.append('-d')
sys.argv.append(os.path.join('dist', 'v'+version))

fireweed_data_files = []
for files in os.listdir('org_chart_from_exchange/images'):
    f1 = 'org_chart_from_exchange/images/' + files
    if os.path.isfile(f1): # skip directories
        f2 = 'images', [f1]
        fireweed_data_files.append(f2)
for files in os.listdir('org_chart_from_exchange/images/icons'):
    f1 = 'org_chart_from_exchange/images/icons/' + files
    if os.path.isfile(f1): # skip directories
        f2 = 'images/icons', [f1]
        fireweed_data_files.append(f2)
f2 = '', ['VERSION']
fireweed_data_files.append(f2)

if sys.platform in ['win32', 'cygwin', 'win64']:
    setup(
        name="Fireweed",
        windows=[{
            'script': "org_chart_from_exchange/__init__.py",
            'icon_resources': [(1, "org_chart_from_exchange/images/org_chart_from_exchange.ico")],
            'dest_base': "Fireweed_"+version,
            'version': version,
            'description': "Field, Reservoir, Well Electronic Dashboard (Fireweed)",
            # 'author': 'Sergey Farin',
            'copyright': "Copyright 2015",
            'original_filename': "Fireweed.exe",
            'product_name': "Fireweed"
        }],
        zipfile="lib/shared.zip",
        requires=['py2exe'],
        # data_files=matplotlib.get_py2exe_datafiles(),
        # data_file=['org_chart_from_exchange/gui/images/fireweed_ico.png'],
        data_files = fireweed_data_files,
        # [('images', ['org_chart_from_exchange/images/fireweed_ico.png',
        #                          'org_chart_from_exchange/images/icons']),
    # 'org_chart_from_exchange/gui/images/fireweed_ico.png',
    #         ('lib', [
    #           # "C:\Apps\Programs\WinPython-32bit-3.4\python-3.4.2\Lib\site-packages\PyQt4\plugins\imageformats\qico4.dll"
    #             'C:\Apps\Programs\WinPython-32bit-3.4\python-3.4.2\Lib\site-packages\PyQt4\plugins\imageformats\qjpeg4.dll',
    #             'C:\Apps\Programs\WinPython-32bit-3.4\python-3.4.2\Lib\site-packages\PyQt4\plugins\imageformats\qgif4.dll',
    #             'C:\Apps\Programs\WinPython-32bit-3.4\python-3.4.2\Lib\site-packages\PyQt4\plugins\imageformats\qico4.dll',
    #             'C:\Apps\Programs\WinPython-32bit-3.4\python-3.4.2\Lib\site-packages\PyQt4\plugins\imageformats\qmng4.dll',
    #             'C:\Apps\Programs\WinPython-32bit-3.4\python-3.4.2\Lib\site-packages\PyQt4\plugins\imageformats\qsvg4.dll',
    #             'C:\Apps\Programs\WinPython-32bit-3.4\python-3.4.2\Lib\site-packages\PyQt4\plugins\imageformats\qtiff4.dll'
    #
    #           ])
        #],
        options={
            'py2exe': {
                'excludes': [
                    'scipy',
                    'tkinter',
                    '_wx',
                    '_gtkagg',
                    '_tkagg',
                    '_ssl',
                    'PyQt4',
                    'doctest',
                    'pdb',
                    # 'email',
                    'pydoc',
                    'pydoc_data',
                    # 'distutils',
                    'setuptools',
                    # 'unittest',
                    # 'difflib',
                    # 'inspect',
                    'tornado',
                    'IPython'],
                'dll_excludes': [
                    'libgdk-win32-2.0-0.dll',
                    'libgobject-2.0-0.dll'
                    ],
                "includes": ["sip"]}}
    )

zipf = zipfile.ZipFile(os.path.join("dist","Fireweed_"+version+".zip"), 'w')
os.chdir(os.path.join("dist",'v'+version))
for root, dirs, files in os.walk(os.getcwd()):
	for file in files:
		if root == os.getcwd():
			zipf.write(os.path.join(file))
		else:
			zipf.write(os.path.join(root[len(os.getcwd())+1:], file))

zipf.close()
os.chdir('..')
# shutil.rmtree(os.path.join('v'+version))