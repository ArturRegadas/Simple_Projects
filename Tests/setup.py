import sys
from cx_Freeze import setup, Executable

build_exe_option={'packages': ['os'], 'includes':['tkinter','ttkthemes', 'time', 'threading','pynput'], 'includes_files':['icon (2).ico','comecar.png','definitico.png', 'Entrar.png', ]}

base=None
if sys.platform == 'win32':
    base='Win32GUI'

setup(
    name='Autoclicker',
    version='1.0',
    description='O melhor autoclicker do mercadp',
    option={'build_exe':build_exe_option},
    executables=[Executable(script='autoclick.py', base=base, icon='icon (2).ico')]
)