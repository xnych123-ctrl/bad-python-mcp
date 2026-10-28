"""deliberately bad: package-name absolute import -> PYTHON_IMPORT_ABSOLUTE_PACKAGE"""

from badpy.helper import Greeter


def greet_loudly(name):
    return Greeter().greet(name).upper()
