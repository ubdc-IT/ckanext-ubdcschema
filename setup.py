from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-ubdcschema',
    version=version,
    description="UBDC dcat schema for datasets",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Michael Comerford',
    author_email='michael.comerford@glasgow.ac.uk',
    url='https://github.com/ubdc-IT/ckanext_ubdcschema',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.ubdcschema'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        ubdc_dcatSchema=ckanext.ubdcschema.plugin:ExampleIDatasetFormPlugin
    ''',
)
