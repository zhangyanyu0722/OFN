#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import sys
from shutil import rmtree
from setuptools import find_packages, setup, Command

NAME = 'optical flow navigation'
DESCRIPTION = 'This respository develops two algorithms to\
               control the motion of vehicles using optical flow,\
               which can detect the surrounding world frame by frame.\
               The first algorithm is through tracking features in \
               continuously updated sequences of frames using sparse \
               optical flow, and using these feature tracks to calculate \
               time-to-transit (τ) for the matched features as a feedback \
               signal. Such signals can steer the robot vehicle by \
               balancing average of τ in certain areas. \
               The second algorithm uses dense optical flow by calculating \
               the difference of flow vectors in two regions in one frame \
               to generate a steering signal to control the robot.'

URL = 'https://github.com/zhangyanyu0722/OFN'
EMAIL = 'zhangya@bu.edu'
AUTHOR = 'Yanyu Zhang'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '1.0.0'
REQUIRED = [
    'opencv-contrib-python>=4.2.0.32',
    'opencv-python>=4.2.0.32',
    'numpy>=1.18.1',
    'matplotlib>=3.1.3'
]

EXTRAS = {
    # 'fancy feature': ['django'],
}

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

class UploadCommand(Command):
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

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    # packages=find_packages(),
    package_dir={'': 'src'},
    packages=['optical flow navigation'],
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    cmdclass={
        'upload': UploadCommand,
    },
)