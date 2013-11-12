#!/usr/bin/python -tt

import sys
import argparse

from basecommand import Command, Argument

class CreateCommand(Command):
    """ Mic create command.
    """
    name = 'create'
    alias = 'cr'
    usage = '%(prog)s <KSFILE> [OPTS]'
    description = 'create an image'

    arguments = [
        Argument(
            'ksfile',
            type=str,
            default=None,
            help='Specify kickstart file'
        ),
        Argument(
            '-h', '--help',
            dest='help',
            action='help',
            help='Show help info'
        ),
        Argument(
            '--logfile',
            type=str,
            dest='logfile',
            default=None,
            help='Path of logfile'
        ),
        Argument(
            '-c', '--config',
            type=str,
            dest='config',
            default=None,
            help='Specify config file for mic'
        ),
        Argument(
            '-k', '--cachedir',
            type=str,
            action='store',
            dest='cachedir',
            default=None,
            help='Cache directory to store the downloaded'
        ),
        Argument(
            '-o', '--outdir',
            type=str,
            action='store',
            dest='outdir',
            default=None,
            help='Output directory'
        ),
        Argument(
            '-A', '--arch',
            type=str,
            dest='arch',
            default=None,
            help='Specify repo architecture'
        ),
        Argument(
            '--release',
            type=str,
            dest='release',
            default=None,
            metavar='RID',
            help='Generate a release of RID with all necessary'
                 ' files, when @BUILD_ID@ is contained in '
                 'kickstart file, it will be replaced by RID'
        ),
        Argument(
            '-record-pkgs',
            type=str,
            dest='record_pkgs',
            default=None,
            help='Record the info of installed packages, '
                 'multiple values can be specified which '
                 'joined by ",", valid values: "name", '
                 '"content", "license", "vcs"'
        ),
        Argument(
            '--pkgmgr',
            type=str,
            dest='pkgmgr',
            default=None,
            help='Specify backend package manager'
        ),
        Argument(
            '--local-pkgs-path',
            type=str,
            dest='local_pkgs_path',
            default=None,
            help='Path for local pkgs(rpms) to be installed'
        ),
        Argument(
            '--runtime',
            type=str,
            dest='runtime',
            default=None,
            help='Specify  runtime mode, avaiable: bootstrap, native'
        ),
        Argument(
            '--taring-to',
            type=str,
            dest='pack_to',
            default=None,
            help=argparse.SUPPRESS
        ),
        Argument(
            '--pack-to',
            type=str,
            dest='pack_to',
            default=None,
            help='Pack the images together into the specified'
                 ' achive, extension supported: .zip, .tar, '
                 '.tar.gz, .tar.bz2, etc. by default, .tar '
                 'will be used'
        ),
        Argument(
            '--copy-kernel',
            action='store_true',
            dest='copy_kernel',
            help='Copy kernel files from image /boot directory'
                 ' to the image output directory.'
        ),
        Argument(
            '--install-pkgs',
            type=str,
            action='store',
            dest='install_pkgs',
            default=None,
            help='Specify what type of packages to be installed,'
                 ' valid: source, debuginfo, debugsource'
        ),
        Argument(
            '--tmpfs',
            action='store_true',
            dest='enabletmpfs',
            help='Setup tmpdir as tmpfs to accelerate, experimental'
                 ' feature, use it if you have more than 4G memory'
        ),
        Argument(
            '--repourl',
            action='append',
            dest='repourl',
            default=[],
            help=argparse.SUPPRESS
        ),
    ]

    def run(self, cmd_args):
        print >> sys.stdout, 'run CREATE with the following args:'
        print >> sys.stdout, cmd_args

if __name__ == '__main__':
    cmd = CreateCommand(name=__file__)
    ret = cmd.main()
    if ret:
        sys.exit(ret)
