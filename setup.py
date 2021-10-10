from setuptools import setup
from cli import __version__
setup(
    name = 'PDF-Utility-CLI',
    version = __version__,
    packages = ['cli'],
    entry_points = {
        'console_scripts': [
            'pdfutilc = cli.__main__:main'
        ]
    }
)