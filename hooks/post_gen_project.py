#!/usr/bin/env python
import os
import shutil


def delete_resource(resource):
    if os.path.isfile(resource):
        # print("removing file: {}".format(resource))
        os.remove(resource)
    elif os.path.isdir(resource):
        # print("removing directory: {}".format(resource))
        shutil.rmtree(resource)

# {% if license  == "Unlicense" %}
delete_resource('LICENCE.txt')
# {% endif %}

# {% if not tests %}
delete_resource('tests')
# {% endif %}

print("{{cookiecutter.project_name}} has been succesfully created !")