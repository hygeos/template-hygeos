#!/usr/bin/env python
import os
import shutil
import subprocess

from pathlib import Path
from sys import exit

def check(res):
    if res.returncode != 0:
        print("An error happened in the subprocess responsible for git init")
        exit(1)

def delete_resource(resource):
    if os.path.isfile(resource):
        # print("removing file: {}".format(resource))
        os.remove(resource)
    elif os.path.isdir(resource):
        # print("removing directory: {}".format(resource))
        shutil.rmtree(resource)

res = subprocess.run(f'git init -q -b main .', shell=True)
check(res)
res = subprocess.run('git add README.md && git commit -q -m "First commit"', shell=True)
check(res)

# {% if cookiecutter.license  == "Unlicense" %}
delete_resource('LICENCE.txt')
# {% endif %}

# {% if not cookiecutter.__tests %}
delete_resource('tests')
delete_resource('pytest.ini')
# {% endif %}

# cleanup void.txt files 
# -> they are used to commit the folder
# -> this allow to visualize the template structure from the repo
path = Path.cwd()
for item in path.iterdir():
        if item.is_dir():
            void = item / "void.txt"
            if void.is_file(): void.unlink()

print("> project {{cookiecutter.project_name}} has been succesfully created !")