import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Sudoku",
    version = "0.0.2",
    author = "Diego Chequer",
    author_email = "millychequer@gmail.com",
    description = ("An Object Oriented Sudoku Game Generator"),
    url = "https://github.com/dchequer/sudoku_dchequer",
    long_description=read('README'),
    classifiers=[
        "Development Status :: Working",
        "Topic :: Utilities",
        "License :: MIT License",
    ],
)