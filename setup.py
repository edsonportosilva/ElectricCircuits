# Authors: CircuitPy contributors
# License: BSD 3-Clause

from setuptools import setup

# Taken from scikit-commpy setup.py
DISTNAME = 'CircuitPy'
DESCRIPTION = 'Electric Circuit Analysis with Python'
LONG_DESCRIPTION = open('README.md', encoding="utf8").read()
MAINTAINER = 'Edson Porto da Silva'
MAINTAINER_EMAIL = 'edsonporto88@gmail.com'
URL = 'https://github.com/edsonportosilva/ElectriCircuits'
LICENSE = 'BSD 3-Clause'
VERSION = '0.1.0'

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["circuit/*"]

setup(
    name=DISTNAME,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found
    #recursively.)
    packages=['circuit'],
    install_requires=[
          'numpy',
          'scipy',
          'matplotlib',
          'sympy',
    ],
    #'package' package must contain files (see list above)
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data={'circuit': files},
    #'runner' is in the root.
    scripts=["runner"],
    test_suite='nose.collector',
    tests_require=['nose'],

    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Teaching',
        'Intended Audience :: Electrical Engineering',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ],
    python_requires='>=3.2',