from setuptools import setup, find_packages
import glob
import os

with open('requirements.txt') as f:
    required = [x for x in f.read().splitlines() if not x.startswith("#") and not x.startswith("git")]
with open('requirements-dev.txt') as f:
    required_dev = [x for x in f.read().splitlines() if not x.startswith("#")]

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'Readme.md'), encoding='utf-8') as f:
    long_description = f.read()

# Note: the _program variable is set in __init__.py.
# it determines the name of the command line tool.
from src import __version__

setup(
    name='underleague-generator',
    version=__version__,
    packages=['underleague_generator'],
    package_dir={'underleague_generator': 'src'},
    description='underleague-generator is a toolbox for generating new underleagues',
    author='Ch4zm of Hellmouth',
    author_email='ch4zm.of.hellmouth@gmail.com',
    license='MIT',
    install_requires=required,
    include_package_data=True,
    tests_require=required_dev,
    keywords=[],
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
