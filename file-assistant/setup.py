from setuptools import setup
from py2app.build_app import py2app

APP = ['organizer_gui.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)