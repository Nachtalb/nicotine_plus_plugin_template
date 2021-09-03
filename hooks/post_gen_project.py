import subprocess

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'initial commit'])
{% if cookiecutter.github_remote == 'SSH' %}
subprocess.call(['git', 'remote', 'add', 'origin', 'git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.github_reponame}}.git'])
{% else %}
subprocess.call(['git', 'remote', 'add', 'origin', 'https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_reponame}}.git'])
{% endif %}
