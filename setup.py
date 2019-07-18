# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.cli') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('hlcloud/version.py') as f:
    exec(f.read())

setup(
    name='hlcloud',
    version=__version__,
    description='Hall Lab Cloud Policy CLI',
    long_description=readme,
    author='Eddie Belter',
    author_email='ebelter@wustl.edu',
    license=license,
    url='https://github.com/hall-lab/cloud-policies.git',
    install_requires=[
        'click==7.0',
        'pyyaml==5.1',
    ],
    entry_points='''
        [console_scripts]
        hlcloud=hlcloud.cli:hlcloud_cmd
    ''',
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
)
