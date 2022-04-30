from setuptools import setup
from Cython.Build import cythonize

setup(
    name = "Bee Package Manager (BPM)",
    version = '0.1',
    description = "An open-source package manager for GNU/Linux",
    author = "Maeve Garside",
    author_email = "60114762+MolassesLover@users.noreply.github.com",
    url = 'https://github.com/MolassesLover/Bee',
    packages = ['beepm'],
    ext_modules = cythonize('Source/Main.py'),
)