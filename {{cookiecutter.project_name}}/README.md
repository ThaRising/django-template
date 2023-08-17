# {{ cookiecutter.project_pretty }}

Website and API for a Django Project.

## Developing

Install Dependencies (requires Poetry):

```bash
poetry install
```

Activate Virtual-Environment:

```bash
source $(poetry env info --path)/bin/activate
```

Setup pre-commit Hooks:

```bash
pre-commit install
```

To manually format all files, run:

```bash
make
```

## Running

To run the project, first run all migrations:

```bash
make m
```

Next, you can start the associated webserver and open it in your browser:

```bash
make rn
```

To delete the data associated with the project, simply `unmigrate` the data like so:

```bash
make um
# To re-create the app without data, run:
make m
```

## Other

To create a new Django-Unicorn component, run:

```bash
python manage.py startunicorn app_name component_name
```
