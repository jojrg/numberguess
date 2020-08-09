from dto.Game import Game


class GuessResult:
    """The Bet

    Attributes:
        :foo: 
    """

    def __init__(self, gameState, distance, guessesTaken, secretNumber):
        super().__init__()
        self.state = gameState
        self.distance = distance
        self.guessesTaken = guessesTaken
        self.guessesLeft = Game.MAX_ATTEMPTS - guessesTaken
        self.secretNumber = secretNumber

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, newState):
        self.__state = newState

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, val):
        self.__distance = val

    @property
    def guessesTaken(self):
        return self._guessesTaken

    @guessesTaken.setter
    def guessesTaken(self, val):
        self.__guessesTaken = val

    @property
    def guessesLeft(self):
        return self._guessesLeft

    @guessesLeft.setter
    def guessesLeft(self, val):
        self._guessesLeft = val

    @property
    def secretNumber(self):
        return self._secretNumber

    @secretNumber.setter
    def secretNumber(self, val):
        self._secretNumber = val
