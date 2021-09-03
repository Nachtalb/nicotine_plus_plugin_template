from .base import BasePlugin


class Plugin(BasePlugin):
    settings = {}
    metasettings = {}
    __publiccommands__ = []
    __privatecommands__ = []
