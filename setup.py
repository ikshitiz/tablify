# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tablify',
    version='0.1.0',
    description='',
    long_description=readme,
    author='Kshitij',
    author_email='kshtjkmr35@gmail.com',
    url='https://github.com/ikshitiz/tablify',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

