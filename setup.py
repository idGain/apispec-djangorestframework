from setuptools import setup, find_packages
import os

execfile(os.path.join(os.path.dirname(__file__), 'apispec_drf/version.py'))


setup(
    name='apispec-djangorestframework',
    version=".".join(map(str, VERSION)),
    packages=find_packages(),
    include_package_data=True,

    author='Concentric Sky',
    author_email='django@concentricsky.com',
    description='DjangoRestFramework 3.6.x APISpec generator',
    license='Apache2'
)
