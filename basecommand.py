#!/usr/bin/python -tt

import sys
import copy
import argparse

from utils import get_summary


__all__ = ['Argument', 'CommandError', 'Command']


class Argument(object):
    """ Class that stores the args/kwargs when to add an argument.
    """
    def __init__(self, *args, **kwargs):
        self.args = copy.deepcopy(args)
        self.kwargs = copy.deepcopy(kwargs)


class CommandError(Exception):
    """ Base Command exception.
    """
    pass

class Command(object):
    """ Command base class for parsing command line strings.
    """
    name = None
    alias = None
    usage = None
    description = None
    arguments = []
    subcommands = {}

    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            if not hasattr(self, key):
                raise TypeError("__init__() got an unexpected \
                                 keyword argument '%s'" % key)
            setattr(self, key, value)

        parser_kw = {
            'prog': self.name,
            'usage': self.usage,
            'description': self.description,
            'formatter_class': argparse.RawDescriptionHelpFormatter,
            'add_help': False,
        }

        self.parser = argparse.ArgumentParser(**parser_kw)

        arggroup_name = '%s arguments' % self.name
        self.arggroup = self.parser.add_argument_group(arggroup_name)

        for argument in self.arguments:
            if isinstance(argument, Argument):
                self.arggroup.add_argument(*argument.args, **argument.kwargs)

        if self.subcommands:
            summary = get_summary(self.subcommands, title='subcommands:')
            description = [self.parser.description, summary]
            self.parser.description = '\n\n'.join(description)

    def parse_args(self, args):
        """
        Parse command line string into python data type.

        If this command has subcommands, Lazy Parsing will be taken. In this
        case, unknown arguments will be reserved for subcommands. This method
        returns a tuple which consists of known arguments, valid subcommand
        and reserved arguments.
        """

        if not self.subcommands:
            return (self.parser.parse_args(args), None, [])

        cmd_args, cmd_else = self.parser.parse_known_args(args)

        if not cmd_else or cmd_else[0] == 'help':
            self.parser.print_help()
            sys.exit(0)

        sub_name = cmd_else[0]
        sub_argv = cmd_else[1:]

        if sub_name not in self.subcommands:
            for name, subcmd in self.subcommands.iteritems():
                if sub_name in (name, subcmd.alias):
                    sub_name = name
                    break
            else:
                raise CommandError("unknown command '%s'" % sub_name)

        return (cmd_args, sub_name, sub_argv)

    def main(self, args=None):
        """
        Control the workflow of command.

        This method calls the 'run' method after parsing arguments. If this
        command doesn't have subcommands, it will end with the result of the
        'run' method. If not, it will continue to call subcommand and return
        the result of subcommand execution.
        """
        if args is None:
            args = sys.argv[1:]

        try:
            cmd_args, sub_name, sub_argv = self.parse_args(args)
        except CommandError, err:
            sys.stderr.write("%s: error: %s\n" % (self.parser.prog, err))
            sys.exit(1)

        status = self.run(cmd_args)

        if sub_name:
            subcmd = self.subcommands[sub_name]
            subcmd = subcmd(name='%s %s' %(self.name, sub_name))
            status = subcmd.main(sub_argv)

        return status

    def run(self, cmd_args):
        """
        Execute operations for known arguments.

        User should rewrite this method to handle known arguments.
        """
        raise NotImplementedError
