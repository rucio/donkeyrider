import io
import os
import sys
from shutil import rmtree
from setuptools import setup, find_packages, Command


# Package Info
NAME = 'donkeyrider'
MODULE_SRC_DIR = 'src'
DESCRIPTION = 'The Rucio Testing framework'
URL = 'https://github.com/rucio/donkeyrider'
EMAIL = 'imptodefeat@gmail.com'
AUTHOR = 'Mayank Sharma'


thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
REQUIRED = ['Click']
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        REQUIRED = f.read().splitlines()

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Load the package's __version__.py module as a dictionary.
about = {}
with open(os.path.join(here, '__version__.py')) as f:
    exec(f.read(), about)


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        sys.exit()


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests')),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    entry_points={
        'console_scripts': ['donkeyrider=src.infrastructure.cli.main:cli'],
    },
    install_requires=REQUIRED,
    package_data={'': ['__version__.py']},
    include_package_data=True,
    license='Apache Software License',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7'
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)