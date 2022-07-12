from os import path
from io import open
from setuptools import setup

current_path = path.abspath(path.dirname(__file__))

with open(path.join(current_path, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='setw',
    version='0.0.1',
    description='crawl stock exchange daily',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['setw']
)
