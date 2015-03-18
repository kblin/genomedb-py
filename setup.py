from setuptools import setup, find_packages
from genomedb import __version__

setup(
    name = "genomedb",
    version = __version__,
    packages = find_packages(),

    # metadata required by pypi
    author = "Kai Blin",
    author_email = "kblin@biosustain.dtu.dk",

    # automatic script creation
    entry_points = {
        'console_scripts': [
            'genomedb = genomedb.application:main',
        ]
    }
)
