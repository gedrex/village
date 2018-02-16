#!./bin/python3

from setuptools import setup

setup(
    name='Village Master',
    version='0.1',
    description="Still no comment. I'll figure out something.",
    url='http://github.com/gedrex/village',
    author='Gedrex',
    packages=['village_master'],
    python_requires='>=3',
    install_requires=[
        'yaml',
        'ruamel.yaml',
        ]
    zip_safe=False
)
