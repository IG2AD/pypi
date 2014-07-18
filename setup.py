from setuptools import setup
import os

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='example_pypi_project',
    version='0.0',
    author = "Daniel Shirley",
    author_email = "aditaa05@gmail.com",
    description = ("An test of how to create, document, and publish "
                                   "to the cheese shop"),
    license = "GPL v2",
    keywords = "example documentation tutorial",
    url = "https://github.com/aditaa/pypi"
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README.md'),
    )
