"""
hackthederivative
-----------------

A handful of functions used to demonstrate the complex step
approach to finite differencing.
"""
from setuptools import setup

setup(
    name='hackthederivative',
    version='0.0.1',
    packages=['hackthederivative'],
    url='http://github.com/eriktaubeneck/hack-the-derivative',
    license='MIT',
    author='Erik Taubeneck',
    author_email='erik.taubeneck@gmail.com',
    description=('A handful of functions used to demonstrate the complex'
                 ' step approach to finite differencing.'),
    long_description=__doc__,
    py_modules=['hackthederivative'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English ',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
