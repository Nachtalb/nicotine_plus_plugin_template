# [Nicotine+](https://nicotine-plus.github.io/nicotine-plus/) Plugin Template

Template for easy and fast Nicotine+ plugins development

Before developing read the Features / Usage section to see how it works. Other than that you can take a look at [my N+ plugins](https://github.com/topics/nicotine-plus?q=user%3ANachtalb), the N+ [documented base plugin](https://github.com/nicotine-plus/nicotine-plus/blob/620538d9338acd90c3833919bd664da010270b72/pynicotine/pluginsystem.py#L571) and the [default plugins](https://github.com/nicotine-plus/nicotine-plus/tree/master/pynicotine/plugins) to find the hooks and what they do.

## Main features

- You can use more than one module
- Easier Version management and update checker
- Relaod command so you don't need to click around during development
- Simple to use periodic jobs
- Various convinience methods
- Auto-prefix commands

## Generate New Plugin

Clone the repo, install cookiecutter and run the wizard. You'll get a

```bash
git clone https://github.com/Nachtalb/nicotine_plus_plugin_template.git
cd nicotine_plus_plugin_template
pip install cookiecutter
cookiecutter .
```

## Compatibility

Python version 3.8 and up

## Features / Usage

### Main Plugin

- The main `Plugin` class is in `module_name/__init__.py` where `module_name` is the name you defined in the questionaire
  - Methods:
    - `log(*args, msg_args=[], level=None)`: Log anything to console (`args` can be any type, it will be cast to a string first), `msg_args` a tuple or list of values to insert into the message with `%s`, `%d` etc, `level` level string to define where the message will be posted to (console, chat, info window etc. see N+ base plugin linked above for more info, `with_prefix` put plugin name as prefix to the message
    - `init()`: init method for the plugin. When overriden first this should be a super call
    - `pre_stop()`: method called before the plugin is disabled or N+ is quit
    - `error_window(args*, msg_args=[])`: Wrapper for `log()` to show an error window
    - `info_window(args*, msg_args=[])`: Wrapper for `log()` to show an info window
    - `settings_changed(before, after, change)`: Method called after the user changed some settings. `before` and `after` are the full settings before and after the change, `change` is a dict like `{'before': ..., 'after': ...}` which noly contains the delta
- The plugin will automatically get any information about the repository, command prefix, version number, plugin name etc from the `PLUGININFO` file. So you don't have to care about setting these up on your own.
- Use `PeriodicJobs` from `from .core.threading import PeriodicJob`
  - Arguments:
    - `delay [1]`: how fast to run in seconds. Can be a callable that returns an int
    - `update [None]`: function to call, it can be none if you subclass `PeriodicJob` and define the method yourself
    - `name ['']`: name of the jobn
    - `before_start [None]`: callable to call before the jobs is started. This can be used with `first_round` variable to chain start jobs
  - Methods:
    - `stop(wait=True)`: Stop the job, by default waits for the job to end
    - `pause()`: Pause the job.
    - `resume()`: Resume the job
  - Variables:
    - `self.first_round`: A thread event that will be set after the job has run the first time. Cane be used together with `before_start` to chain jobs
    - `self.last_run`: Unix timestamp of last job execution

### Default commands

- `/prefix-update`: The plugin comes with an automatic update check from the start. It will periodically ask github for any new updates and will prompt the user. This can be disabled with a checkbox in the plugin preferences.
- `/prefix-reload`: Reload the plugin code without the need to click throught the settings menu

- During development of the project the commands will be prefix with an additional `d`. So if you entered `foo` the command will be `/dfoo`. When releasing a new version this will automatically change to `/foo`

#### `@command`

The `@command` decorator from `from .core.utils import command` is designed to make life easier. Not only eases it the registration of commands but also parses user arguments and makes sure that Nicotine+ doesn't freeze.

- No interaction with `__publiccommands__` or `__privatecommands__` needed.
- The decorator makes the `initiator` and `args` arguments optionl thus you can call the methods from other places in your script without much thought. You have to use only keyword arguments tho otherwhise the first two positional arguments will be interpreted as `initiator` and `argstring` (`argstring` will be parsed to `args`).

##### Sample usage

In this example the command prefix was set to: `ab`

```python
from .core.base import BasePlugin
from .core.utils import command

class Plugin(BasePlugin):

    # No arguments are given, infere command name "foo". With the  prefix said
    # above the command will be /ab-foo.  # "args" is a list of parsed
    # arguments given by the user - numbers will be int or float.
    @command
    def foo(self, args):
        ...

    # "initiator" where the command was run from. This will either be the user
    # name of the partner in the private chat or the room name in the public
    # chat.
    @command
    def foo(self, initiator):
        ...

    # The user may use the command like "/aa-foo a_flag", "/aa-foo a_flag=True"
    # or "/aa-foo -a_flag" to set the argument to True
    @command
    def foo(self, a_flag=False):
        ...

    # The user may use the command like "/aa-foo a_int=123" to define a number.
    # Because we set the type to "int" floats like "12.3" or strings like "bar"
    # will be ignored.
    @command
    def foo(self, a_int: int = None):
        ...

    # By default commands are available in both private and public chat. We can
    # disable it for either chat - here we disable it for public chats.
    @command(public=False)
    def foo(self):
        ...

    # When the commandname is infered "_" will be replaced with "-". This
    # making the command "/ab-foo-bar"
    @command()
    def foo_bar(self):
        ...

    # The command doesn't need to be foo - it can be whatever you wish.
    @command('custom-name')
    def foo(self):
        ...

    # Disable the prefix. The command will be "/foo"
    @command(with_preix=False)
    def foo(self):
        ...

    # No command is created if the command name is infered from the method name and
    # starts with "_"
    @command()
    def _bar(self):
        ...

    # Usually the commands are run in a separata thread to prevent Nicotine+
    # from freezing during the execution. You can disable that behaviour.
    @command(threaded=False)
    def foo(self):
        ...
```

### Utils

`from .core.utils import ...`

- `get(url, data=None, headers={}, timeout=30)` a easy to use version of `urllib.request.urlopen` as it allows to set `headers` and `data` directly, where when not defined `headers` is auto filled with a common user agent. It returns a `Response` which auto decodes the content to `response.content` and returns a dict if possible with parsing json with `response.json`
- `log(*msg, msg_args=[], level=None, prefix=None)`: Simple to use logging method that accespts anything. You can set a prefix with `prefix=` the other arguments work the same as the `log` method descirbed in the main plugin
- `command(func)`: `@command` wrapper as specified in aboves section
- `str2num(string)`: A simple to use string to int/float converted without error throwsing. If the string cannot be parsed to a number the string will be returned again.
- `startfile(file)`: Start a file with the default application on the pc

### PLUGININFO / Releaser

- Instead of writing a plugin description painstakingly into `PLUGININFO` yourself where you have to escape `"` chars and replace new lines with `\n` you can use `DESCRIPTION` instead. This file will be minimized and put into `PLUGININFO` during releasing.
- To release a new vewion use the `./releaser` script (it uses the [fish shell](https://fishshell.com/) which is not POSIX compatible so it won't work with bash)
  - It will minimize the `DESCRIPTION` and put it into the `PLUGININFO`
  - It will increase the version by `0.0.1` by default. Change that if needed
  - After the release the version will be `x.x.x.dev0`
