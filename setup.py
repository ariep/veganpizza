from setuptools import setup

version = '0.1'

install_requires = [
    'python-xlib >= 0.21',
    'PyAutoGUI >= 0.9.36',
    'pyxhook >= 1.0.0',
],

setup(
    name = 'veganpizza',
    version = version,
    description = 'Only vegan pizza please',
    author = 'Arie Peterson',
    author_email = 'arie@skami.nl',
    include_package_data = True,
    install_requires = install_requires,
)
