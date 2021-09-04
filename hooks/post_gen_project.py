import subprocess

subprocess.call(['git', 'init'])

{% if cookiecutter.github_remote == 'SSH' %}
subprocess.call(['git', 'remote', 'add', 'origin', 'git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.github_reponame}}.git'])
subprocess.call(['git', 'submodule', 'add', 'git@github.com:Nachtalb/np_plugin.core.git', '{{cookiecutter.module_name}}/core/'])
{% else %}
subprocess.call(['git', 'remote', 'add', 'origin', 'https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_reponame}}.git'])
subprocess.call(['git', 'submodule', 'add', 'https://github.com/Nachtalb/np_plugin.core.git', '{{cookiecutter.module_name}}/core/'])
{% endif %}

subprocess.call(['git', 'submodule', 'update', '--init', '--recursive'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'initial commit'])
