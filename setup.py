from setuptools import setup, find_packages

NAME = 'lote'
VERSION = '0.1'

setup(
    name=NAME,
    version=VERSION,
    package_dir={'': 'src'},  # Optional
    packages=find_packages(where='src'),
    setup_requires=['wheel'],
    entry_points={  
        'console_scripts': [
            'lote=lote:main',
        ],
    },
)