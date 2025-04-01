#!/usr/bin/env python
import os
import shutil
import subprocess

from pathlib import Path

def delete_resource(resource):
    if os.path.isfile(resource):
        # print("removing file: {}".format(resource))
        os.remove(resource)
    elif os.path.isdir(resource):
        # print("removing directory: {}".format(resource))
        shutil.rmtree(resource)

subprocess.run(f'git init -b main .', shell=True)
subprocess.run('git add README.md && git commit -m "First commit"', shell=True)

# {% if cookiecutter.license  == "Unlicense" %}
delete_resource('LICENCE.txt')
# {% endif %}

# {% if not cookiecutter.tests %}
delete_resource('tests')
delete_resource('pytest.ini')
# {% endif %}

print("> {{cookiecutter.project_name}} has been succesfully created !")