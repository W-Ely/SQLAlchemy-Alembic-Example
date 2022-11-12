# SQLAlchemy + Alembic Example

[SQLALchemy](https://docs.sqlalchemy.org/en/14/) is an ORM that is often paired with web frameworks such as Flask. [Alembic](https://alembic.sqlalchemy.org/en/latest/) is a tool for managing migrations. It is created by the same folks that create SQLAlchemy.

This example decouples SQLAlchemy from the framework to simplify the examples.

## Prereqs
- [Docker](https://www.docker.com/) if you want to use the docker composed Postgres. Alternatively [Postgresql](https://www.postgresql.org/) installed or connectable.
- [Python](https://www.python.org/) >= 3.6

## Setup
1. Create a virtual environment.
```sh
python3 -m venv .venv
```
1. Activate the virtual environment.
```sh
. ./.venv/bin/activate
```
1. Install Python dependencies.
```sh
pip install -r requirements.txt
```

## Playing with the examples.

### Getting Started
1. In one terminal start Postgres from the `docker-compose.yml`
```sh
docker compose up
```
1. In another terminal
activate the virtual environment.
```sh
. ./.venv/bin/activate
```
Then create the first migration with alembic.
```sh
PYTHONPATH=.:$PYTHONPATH alembic revision --autogenerate -m "init"
```
1. Apply revision to the database
```sh
PYTHONPATH=.:$PYTHONPATH alembic upgrade head
```
1. In a third terminal
activate the virtual environment.
```sh
. ./.venv/bin/activate
```
Then interact with the examples in IPython.
```sh
ipython
```
### Interacting in IPython
1. Imports
```python
from app.example import add_dog, get_all_dogs, get_dog
from datetime import datetime, timedelta
```
1. Run the functions
```python
bday = datetime.now() - timedelta(weeks=52)
add_dog("foo", bday, 24, 50)
get_all_dogs()
get_dog("foo")
```

## Changing the Model
Anytime the model(s) change, a new migration needs to be created and applied to the database inorder for the schema to remain in sync between the Python code and database.

If a change has been made to a model that reflects a desired change in the database.
1. Create a new migration from the plain terminal window.
```sh
PYTHONPATH=.:$PYTHONPATH alembic revision --autogenerate -m "<super short description>"
```
1. Apply revision to the database
```sh
PYTHONPATH=.:$PYTHONPATH alembic upgrade head
```
1. Reload the imports in IPython to reflect the changes. This might require exiting and restarting.  

## Notes
- IPython can be annoying. Requiring restarting to pick up changes to files. I've had some luck with the plugin `autoreload`. When you first start up IPython run these 2 lines in the IPython repl.
```IPython
%load_ext autoreload
%autoreload 2
```
This will allow reimporting the changed file to detect the changes and reload.  Milage may vary.

- Postgres config.  If you're using the docker-compose, then the crednetials have sane defaults that will work.  These are set in the `session.py` file.  If you are running Postgres locally or elsewhere, these environment variable will need to be set.
```
PGUSER
PGPASSWORD
PGHOST
PGPORT
PGDATABASE
```
- Alembic is configured through a combination of the `alembic.ini` file in the root directory, the `env.py` and `script.py.mako` files in the alembic directory.  If the directory structure is modified to a different layout, these files might need to be adjusted.
- `PYTHONPATH=.:$PYTHONPATH` - This adds the current directory to the Python path.  This allows Alembic to find the `app` dir as a Python module.  There are various ways this could have been solved.
