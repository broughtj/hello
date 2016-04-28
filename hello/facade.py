from .person import Person
from .greet import Greet

class HelloFacade(object):

    """Docstring for HelloFacade. """

    def __init__(self, first_name, last_name):
        self._person = Person(first_name, last_name)
        message = "Hello, {0} {1}".format(self._person.first_name, self._person.last_name)
        self._greeter = Greet(message)

    def salutation(self):
        print(self._greeter.greet()) 
