from uuid import uuid4
from random import randint
from GameState import GameState


class Guess:
    """The Bet

    Attributes:
        :foo: 
    """

    def __init__(self, value, distance):
        super().__init__()
        self.__value = value
        self.__distance = distance

    @property
    def value(self):
        return self.__value[:]

    @property
    def distance(self):
        return self.__distance[:]
