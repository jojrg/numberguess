from uuid import uuid4
from random import randint
from dto.GameState import GameState


class Guess:
    """The Bet

    Attributes:
        :foo: 
    """

    def __init__(self, val, dist):
        super().__init__()
        self.value = val
        self.distance = dist

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, val):
        self.__distance = val
