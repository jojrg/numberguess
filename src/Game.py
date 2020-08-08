from uuid import uuid4
from random import randint
from GameState import GameState


class Game:
    """The Game Class

    Attributes:
        :foo: 
    """
    MAX_ATTEMPTS = 6
    LOWER_BOUND = 1
    UPPER_BOUND = 100

    def __init__(self):
        super().__init__()
        self.gameId = str(uuid4())
        self.state = GameState.NEW
        self.secretNumber = None
        self.guesses = []

    @property
    def gameId(self):
        return self.__gameId

    @gameId.setter
    def gameId(self, val):
        self.__gameId = val

    @property
    def secretNumber(self):
        return self.__secretNumber

    @secretNumber.setter
    def secretNumber(self, val):
        self.__secretNumber = val

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    @property
    def guesses(self):
        return self.__guesses[:]

    @guesses.setter
    def guesses(self, value):
        self.__guesses = value

    def addGuess(self, guess):
        self.__guesses.append(guess)

    def start(self):
        print('Starting Game ..')
        gameId = str(uuid4())
        self.secretNumber = randint(self.LOWER_BOUND, self.UPPER_BOUND)
        self.__guesses = []
        self.state = GameState.STARTED

    def quit(self):
        print('Quitting Game ..')
        self.state = GameState.QUIT

    def won(self):
        self.state = GameState.WON

    def lost(self):
        print('setting state to lost')
        self.state = GameState.LOST
