"""
hockeypy.commands.base_command
------------------------------

This module contains abstract class BaseCommand that specifies interface
for all hockepy (sub)commands.
"""

import abc

class BaseCommand(metaclass=abc.ABCMeta):
    """Abstract class definining the interface each hockepy (sub)command
    should implement."""

    @abc.abstractproperty
    def command(self):
        """Return the command name as expected on the command line."""

    @abc.abstractproperty
    def description(self):
        """Return the command's short description for user."""

    @abc.abstractmethod
    def register_parser(self, subparsers):
        """Register and return the sub-command's parser."""

    @abc.abstractmethod
    def run(self, args):
        """Run the command with the given arguments."""