from uuid import uuid4
from random import randint
from GameState import GameState


class Game:
    """The GameService

    Attributes:
        :foo: 
    """
    MAX_ATTEMPTS = 6
    LOWER_BOUND = 1
    UPPER_BOUND = 100

    def __init__(self):
        super().__init__()
        self._gameId = str(uuid4())
        self._state = GameState.NEW
        self._secretNumber = None
        self._guesses = []

    @property
    def gameId(self):
        return self._gameId[:]

    @property
    def secretNumber(self):
        return self._secretNumber

    def start(self):
        print('Starting Game ..')
        gameId = str(uuid4())
        self._secretNumber = randint(self.LOWER_BOUND, self.UPPER_BOUND)
        self._guesses = []
        self._state = GameState.STARTED

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def guesses(self):
        return self._guesses

    def addGuess(self, guess):
        self._guesses.append(guess)

    def quit(self):
        print('Quitting Game ..')
        self._state = GameState.QUIT

    def won(self):
        self._state = GameState.WON

    def lost(self):
        print('setting state to lost')
        self.state = GameState.LOST
        #self.state = 4
