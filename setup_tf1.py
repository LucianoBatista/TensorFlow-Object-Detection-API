"""Setup script for object_detection with TF1.0."""
import os
from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'pillow',
    'lxml',
    'matplotlib',
    'Cython',
    'contextlib2',
    'tf-slim',
    'six',
    'pycocotools',
    'lvis',
    'scipy',
    'pandas'
    'tensorflow<=1.15.0'
]

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False
except ImportError:
    bdist_wheel = None

setup(
    name='tf1_tensorflow_object_detection_api',
    maintainer='forskamse',
    maintainer_email='forskamse@gmail.com',
    url='https://github.com/forskamse/TensorFlow-Object-Detection-API',
    version='1.15.0',
    cmdclass={'bdist_wheel': bdist_wheel},
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=(
        [p for p in find_packages() if p.startswith('object_detection')] +
        find_packages(where=os.path.join('.', 'slim'))),
    package_dir={
        'datasets': os.path.join('slim', 'datasets'),
        'nets': os.path.join('slim', 'nets'),
        'preprocessing': os.path.join('slim', 'preprocessing'),
        'deployment': os.path.join('slim', 'deployment'),
        'scripts': os.path.join('slim', 'scripts'),
    },
    description='Tensorflow Object Detection Library with TF1.0',
    python_requires='>3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
