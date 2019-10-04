try:
    from setuptools import setup
except ImportError :
    raise ImportError("setuptools module required, please go to https://pypi.python.org/pypi/setuptools and follow the instructions for installing setuptools")


setup(
    name='dedupe-variable-number',
    url='https://github.com/dedupeio/dedupe-variable-number',
    version='0.0.1',
    description='Employer variable type for dedupe',
    packages=['dedupe.variables'],
    install_requires=['dedupe'],
    license='The MIT License: http://www.opensource.org/licenses/mit-license.php'
    )
