from .core.base import BasePlugin
from .core.utils import command


class Plugin(BasePlugin):
    settings = {}
    metasettings = {}

    @command
    def echo(self, args=[]):
        self.log(' '.join(map(str, args)))
