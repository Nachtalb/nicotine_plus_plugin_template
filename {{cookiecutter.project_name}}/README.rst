{{cookiecutter.project_name}}
============

A plugin for `Nicotine+`_.

{{cookiecutter.description}}

Plugin created with `Nicotine+ Plugin Template`_ made by `Nachtalb`_.

Installation
------------

Open Nicotine+ settings, go to *General > Plugins* and click *+ Add
Plugins*. After that download the latest `release`_ and extract it into
the plugins folder.

Remove the version from the folder name. The folder name must stay the
same across version upgrades otherwise you will loose any changed
settings.

Now you can enable the *{{cookiecutter.project_name}}* plugin in the previously
opened plugin settings.


Commands
--------

- ``/{{cookiecutter.command_prefix}}-update`` manually check for updates.
- ``/{{cookiecutter.command_prefix}}-reload`` reload the plugin.


Settings
--------

+---------------------+-----------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| Name                | Function                                                                                | Default                                                              |
+=====================+=========================================================================================+======================================================================+
| Check for Updates   | Check for updates on start and periodically                                             | Enabled                                                              |
+---------------------+-----------------------------------------------------------------------------------------+----------------------------------------------------------------------+


Contributing
------------

Pull requests are welcome.


License
-------

`{{cookiecutter.license}}`_

.. _Nicotine+: https://nicotine-plus.github.io/nicotine-plus/
.. _Nicotine+ Plugin Template: https://github.com/Nachtalb/nicotine_plus_plugin_template
.. _Nachtalb: https://github.com/Nachtalb
.. _release: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_reponame}}/releases
.. _{{cookiecutter.license}}: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_reponame}}/blob/master/LICENSE
