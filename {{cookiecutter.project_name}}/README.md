# {{cookiecutter.project_name}}

[**Quickstart**](#Usage)
| [**Install guide**](#installation)

## Introduction

{{cookiecutter.description}}

## Installation

## Usage

{% if tests %}
## Testing
The following command runs the test suite with pytest, and generates a html report using pytest-html:
```sh
make tests
```
{% endif %}

{% if license  != "Unlicense" %}
## Licencing information

This software is available under {{cookiecutter.license}} licence. See file LICENSE.txt for details on the usage and distribution terms. 
{% endif %}

## Referencing

[HYGEOS](https://hygeos.com/en/)