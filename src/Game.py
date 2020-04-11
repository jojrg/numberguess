from uuid import uuid4
from random import randint
from GameState import GameState


class Game:
    """The GameService

    Attributes:
        :foo: 
    """

    def __init__(self):
        super().__init__()
        self.__gameId = str(uuid4())
        self.__state = GameState.NEW
        self.__secretNumber = None

    @property
    def gameId(self):
        return self.__gameId[:]

    @property
    def secretNumber(self):
        return self.__secretNumber

    def start(self):
        print('Starting Game ..')
        gameId = str(uuid4())
        self.__secretNumber = randint(1, 100)
        self.__state = GameState.STARTED

    def getState(self):
        return __state

    def quit(self):
        print('Quitting Game ..')
        self_state = GameState.QUIT
