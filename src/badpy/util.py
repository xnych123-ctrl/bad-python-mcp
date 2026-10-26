"""deliberately bad: relative import -> PYTHON_IMPORT_RELATIVE"""

from .helper import Greeter


def build_greeting(name):
    return Greeter().greet(name)
