from setuptools import setup, find_packages
from os import path

setup(
    name='pyPassGenerator',
    version='1.0',
    description='Generate your random password',
    long_description="""It’s a simple program that it’s able of generate randoms, variables and with custom characters password and... it's written in Python!

                        Documented in https://github.com/xxxtonixxx/pyPasswordGenerator/blob/master/README.md""",
    url='https://github.com/xxxtonixxx/pyPasswordGenerator.git',
    author='Toni Villena',
    author_email='tonivj5@gmail.com',

    license='GNU GPLv2',

    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],

    keywords='password random variable pass generator',
    packages=find_packages('pyPassGenerator'),
    package_dir={'':'pyPassGenerator'},
)
