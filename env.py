
"""
Environment Variables

Environment variables are variable that are set in the OS context and
can be accessed inside the Python program.

An environemnt variable can be set directly from the terminal using export
or defined in a .env file.
Example:
    // Using the terminal
    $ export API_KEY="0-My_API-7749-Key"
    // Using .env file
    API_KEY=0-My_API-7749-Key

Python uses the getenv function of the os module to retrive the environment
variable.
Example:
    from os import getenv

    api_key = getenv("API_KEY")

Since environment variables are set in the OS context and are meant to
be accessible by programs from any programming language, the obtained
variable can only be a str. This can them be type casted after retrieving
the env variable inside the Python code.


Virtual Environments

It's a good practice to use virtual environments for every python project. This helps
to isolate the project-specific dependencies and prevents them from messing with the
global versions.

You can create virtual environments in your project directory using the builting venv
module: `$ python -m venv .myenv`
Or using the virtualenv package: `$ virtualenv myvenv`

Then activate it: `$ source .myenv/bin/activate` or `$ source myenv/bin/activate`

You can confirm the activation by: `$ which python`

After this, you then upgrade pip, create a .gitignore, and install the project requirements.

`$ python -m pip install --upgrade pip`
`$ echo "*" > .venv/.gitignore`
`$ pip install -r requirements.txt`

You can install FastAPI directly from the terminal or add it to requirements.txt and
install all dependencies together (Preferrable).
`$ pip install fastapi[standard]` --> Intalls fastapi alongside some optional dependencies
 or simply:
 `$ pip install fastapi[standard]`

To deactivate the virtual environement: `$ deactivate`

Running FastAPI App

To run a FastAPI app in a file main.py, we do:
`$ fastapi dev main.py`
"""