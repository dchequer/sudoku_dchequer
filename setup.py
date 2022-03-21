from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name = "Sudoku-DCHEQUER",
    version = "0.0.2",
    description = "An Object Oriented Sudoku Game Generator",
    license = "MIT",
    long_description=long_description,
    author = "Diego Chequer",
    author_email = "millychequer@gmail.com",
    url = "https://github.com/dchequer/sudoku_dchequer",
    packages = find_packages(),
    classifiers= [
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9"
    ]
)   