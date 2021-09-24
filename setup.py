import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements


def read_dev_requirements():
    with open('requirements-dev.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return {'dev': requirements}


setup(
    name="vika",
    version="0.0.1",
    author="Michael Savin",
    author_email="jtprogru@gmail.com",
    description=("Some helpers functions."),
    license="WTFPL",
    keywords="password generator",
    url="https://github.com/jtprogru/vika",
    packages=find_packages(),
    include_package_date=True,
    install_requires=read_requirements(),
    extras_require=read_dev_requirements(),
    entry_points="""
        [console_scripts]
        vika=vika.cli:cli
    """,
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
