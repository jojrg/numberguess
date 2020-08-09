from uuid import uuid4
from random import randint
from GameState import GameState


class GameTest:
    """The GameService

    Attributes:
        :foo: 
    """
    MAX_ATTEMPTS = 6
    LOWER_BOUND = 1
    UPPER_BOUND = 100

    def __init__(self):
        self.foo = 'Moritz'
        self.name = 'Max'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def foo(self):
        return self.__foo

    @foo.setter
    def foo(self, val):
        self.__foo = val
