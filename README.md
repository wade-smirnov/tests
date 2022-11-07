## Setup
This project uses version of Python 3.11.*
It also uses [pipenv](https://pipenv.readthedocs.io/) to manage packages.

To set up this project on your local machine:
1. Clone it from this GitHub repository;
2. Install the appropriate version of python;
3. Install `pipenv` using `pip install pipenv` command;
4. Run `pipenv install` to install all needed python dependencies.

## Running Tests
1. Run tests using `pipenv run python -m pytest -v -s`
2. Add pretty report using `pipenv run python -m pytest -v -s --json-report --json-report-indent=4`

## Information
You can specify Blender installation and output folders in `config.py` 
