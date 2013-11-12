#!/usr/bin/python -tt

import sys
import argparse

from basecommand import Command, Argument

class ChrootCommand(Command):
    """ Mic chroot command.
    """
    name = 'chroot'
    alias = 'ch'
    usage = '%(prog)s [OPTS] <IMAGE> [COMMAND [ARGS]...]'
    description = 'chroot into an image'

    arguments = [
        Argument(
            'image',
            type=str,
            default=None,
            help='Specify image file'
        ),
        Argument(
            '-h', '--help',
            dest='help',
            action='help',
            help='Show help info'
        ),
        Argument(
            '-s', '--saveto',
            dest='saveto',
            action='store',
            default=None,
            help='Save the unpacked image to specified directory'
        ),
    ]

    def run(self, cmd_args):
        print >> sys.stdout, 'run CHROOT with the following args:'
        print >> sys.stdout, cmd_args

if __name__ == '__main__':
    cmd = ChrootCommand(name=__file__)
    ret = cmd.main()
    if ret:
        sys.exit(ret)
