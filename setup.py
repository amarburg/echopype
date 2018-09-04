from __future__ import (absolute_import,
                        division,
                        print_function,
                        unicode_literals)

import os
from codecs import open

import versioneer

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

# Dependencies.
with open('requirements.txt') as f:
    requirements = f.readlines()
install_requires = [t.strip() for t in requirements]
print(install_requires)

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='echopype',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/OSOceanAcoustics/echopype',
    author='Wu-Jung Lee',
    author_email='noanswer@github.com',
    maintainer='Wu-Jung Lee',
    maintainer_email='noanswer@github.com',
    python_requires='>=3',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering'
    ],
    keywords=['Ocean', 'Data', 'Access', 'OOI'],
    include_package_data=True,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=install_requires,
)
