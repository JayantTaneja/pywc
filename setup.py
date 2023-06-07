from setuptools import setup

setup(
    name = 'pywc',
    version = '1.0',
    packages = ['cli'],
    entry_points = {
        'console_scripts': [
            'pywc = cli.__main__:main'
        ]
    })
