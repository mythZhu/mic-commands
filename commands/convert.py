#!/usr/bin/python -tt

import sys
import argparse

from basecommand import Command, Argument

class ConvertCommand(Command):
    """ Mic convert command.
    """
    name = 'convert'
    alias = 'ch'
    usage = '%(prog)s [OPTS] <IMAGE> <FORMAT>'
    description = 'convert image format'

    arguments = [
        Argument(
            'image',
            type=str,
            default=None,
            help='Specify source image file'
        ),
        Argument(
            'format',
            type=str,
            default=None,
            help='Specify target image format'
        ),
        Argument(
            '-h', '--help',
            dest='help',
            action='help',
            help='Show help info'
        ),
        Argument(
            '-S', '--shell',
            dest='shell',
            action='store_true',
            default=False,
            help='Launch shell before packaging the converted image'
        ),
    ]

    def run(self, cmd_args):
        print >> sys.stdout, 'run CONVERT with the following args:'
        print >> sys.stdout, cmd_args

if __name__ == '__main__':
    cmd = ConvertCommand(name=__file__)
    ret = cmd.main()
    if ret:
        sys.exit(ret)
