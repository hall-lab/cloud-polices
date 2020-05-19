# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.cli') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('hlcloud/version.py') as f:
    exec(f.read())

install_requires=[
    "click==7.0",
    "google-cloud-storage",
    "pyyaml==5.1",
    "tabulate",
]
test_requires = [
    "mock",
    "pytest"
]

setup(
    name='hlcloud',
    version=__version__,
    description='Hall Lab Cloud Policy CLI',
    long_description=readme,
    author='Eddie Belter',
    author_email='ebelter@wustl.edu',
    license=license,
    url='https://github.com/hall-lab/cloud-policies.git',
    install_requires=install_requires,
    test_requires=test_requires,
    entry_points='''
        [console_scripts]
        hlcloud=hlcloud.cli:hlcloud_cmd
    ''',
    setup_requires=["pytest-runner"],
    tests_require=test_requires,
    packages=find_packages(include=['hlcloud'], exclude=('tests', 'docs')),
    package_data={"hlcloud": ["resources/*"]},
    include_package_data=True,
)
