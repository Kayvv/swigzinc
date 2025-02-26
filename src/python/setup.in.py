""" Zinc Library: An advanced visualisation library for FE models

The Zinc library is an advanced visualisation library for FE models.  The
Zinc library understands a representation of mathematical fields, including
finite element, image-based and CAD.  It also understands fields derived by
mathematical operators.
"""

classifiers = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Science/Research
License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)
Programming Language :: Python
Operating System :: Microsoft :: Windows
Operating System :: Unix
Operating System :: MacOS :: MacOS X
Topic :: Scientific/Engineering :: Medical Science Apps.
Topic :: Scientific/Engineering :: Visualization
Topic :: Software Development :: Libraries :: Python Modules
"""

from setuptools import setup
from setuptools.dist import Distribution

doclines = __doc__.split("\n")


class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

    def has_ext_modules(self):
        return True


setup(
    name='@PYPI_PACKAGE_NAME@',
    version='@Zinc_VERSION@',
    author='Zinc developers',
    author_email='h.sorby@auckland.ac.nz',
    packages=['cmlibs', 'cmlibs.zinc'],
    package_data={'cmlibs.zinc': [@SETUP_PY_PACKAGE_FILES_STR@]},
    url='https://cmlibs.org',
    license='Mozilla Public License 2.0 (MPL 2.0)',
    description=doclines[0],
    classifiers=classifiers.split("\n"),
    long_description=open('README.txt').read(),
    long_description_content_type='text/x-rst',
    distclass=BinaryDistribution,
    include_package_data=True,
    zip_safe=False,
)
