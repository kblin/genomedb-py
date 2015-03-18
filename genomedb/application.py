# vim: set fileencoding=utf-8 :

import argparse
from genomedb import __version__
from genomedb.add import setup_add_args

_version = "genomedb {version}".format(version=__version__)

def main():
    parser = argparse.ArgumentParser(prog="genomedb", version=_version)

    parser.add_argument('--db', dest='db',
                        default=argparse.SUPPRESS,
                        help="URI of the database to use")

    subparsers = parser.add_subparsers(title="subcommands")
    setup_add_args(subparsers)
    args = parser.parse_args()
    args.func(args)
