from distutils.core import setup

DESCRIPTION = "General tools for Astronomical Time Series in Python"
LONG_DESCRIPTION = """
nufftpy: Non-Uniform FFT in Python
==================================

This is a pure python implementation of the NUFFT.
For more information, visit http://github.com/jakevdp/nufftpy
"""
NAME = "nufftpy"
AUTHOR = "Jake VanderPlas"
AUTHOR_EMAIL = "jakevdp@uw.edu"
MAINTAINER = "Jake VanderPlas"
MAINTAINER_EMAIL = "jakevdp@uw.edu"
URL = 'http://github.com/jakevdp/nufftpy'
DOWNLOAD_URL = 'http://github.com/jakevdp/nufftpy'
LICENSE = 'BSD 3-clause'

import nufftpy
VERSION = nufftpy.__version__

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      url=URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=['nufftpy',
                'nufftpy.tests',
            ],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'],
     )
