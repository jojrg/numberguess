from Game import Game


class GuessResult:
    """The Bet

    Attributes:
        :foo: 
    """

    def __init__(self, gameState, distance, guessesTaken, secretNumber):
        super().__init__()
        self._state = gameState
        self._distance = distance
        self._guessesTaken = guessesTaken
        self._guessesLeft = Game.MAX_ATTEMPTS - guessesTaken
        self._secretNumber = secretNumber

    @property
    def state(self):
        return self._state

    @property
    def distance(self):
        return self._distance

    @property
    def guessesTaken(self):
        return self._guessesTaken

    @property
    def guessesLeft(self):
        return self._guessesLeft

    @property
    def secretNumber(self):
        return self._secretNumber
