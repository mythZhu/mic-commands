#!/usr/bin/python -tt

from create import CreateCommand
from chroot import ChrootCommand
from convert import ConvertCommand

__all__ = ['commands', 'CreateCommand', 'ChrootCommand', 'ConvertComamnd']

commands = {
    CreateCommand.name: CreateCommand,
    ChrootCommand.name: ChrootCommand,
    ConvertCommand.name: ConvertCommand,
}
