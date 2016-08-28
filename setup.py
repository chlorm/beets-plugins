#!/usr/bin/env python3

from setuptools import setup

setup(
    name='beets-moveall-artifacts',
    version='0.0.0',
    description='',
    author='Cody Opel',
    author_email='codyopel@gmail.com',
    url='https://github.com/chlorm/beets-moveall-artifacts/',
    license='MIT',
    platforms='ALL',
    long_description=_read('README.rst'),
    packages=[
      'moveall',
    ],
    install_requires=[
      'beets>=1.2.19',
    ],
    classifiers=[
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
