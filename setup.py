#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'backports.weakref==1.0rc1',
    'bleach==1.5.0',
    'cycler==0.10.0',
    'funcsigs==1.0.2',
    'html5lib==0.9999999',
    'Markdown==2.6.8',
    'matplotlib==2.0.2',
    'mock==2.0.0',
    'numpy==1.13.1',
    'pbr==3.1.1',
    'protobuf==3.3.0',
    'pyparsing==2.2.0',
    'python-dateutil==2.6.1',
    'pytz==2017.2',
    'scipy==0.19.1',
    'six==1.10.0',
    'tensorflow==1.2.1',
    'Werkzeug==0.12.2',
]

setup_requirements = [
    'pytest-runner',
    # TODO(mattberjon): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='asc',
    version='0.3.0',
    description="Acoustic Scene Classification using Convolutional Neural Network",
    long_description=readme + '\n\n' + history,
    author="Matthieu Berjon",
    author_email='matthieu@berjon.net',
    license='GPLv2',
    url='https://github.com/mattberjon/asc',
    packages=find_packages(include=['asc']),
    entry_points={
        'console_scripts': [
            'asc=asc.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='asc',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    extras_require={
            ':python_version=="2.7"': [
                'functools32>=3.2<=3.99',
                'subprocess32==3.2.7',
            ],
    },
)
