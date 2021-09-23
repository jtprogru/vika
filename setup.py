import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="vika",
    version="0.0.1",
    author="Michael Savin",
    author_email="jtprogru@gmail.com",
    description=("Some helpers functions."),
    license="WTFPL",
    keywords="password generator",
    url="https://github.com/jtprogru/vika",
    packages=['vika', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
