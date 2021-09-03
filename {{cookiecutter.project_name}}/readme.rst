{{cookiecutter.project_name}}
============

A plugin for `Nicotine+`_.

{{cookiecutter.description}}


Installation
------------

Open Nicotine+ settings, go to *General > Plugins* and click *+ Add
Plugins*. After that download the latest `release`_ and extract it into
the plugins folder.

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
.. _release: https://github.com/{{cookiecutter.repo}}/releases
.. _{{cookiecutter.license}}: https://github.com/{{cookiecutter.repo}}/blob/master/LICENSE
