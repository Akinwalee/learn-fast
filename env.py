
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
"""