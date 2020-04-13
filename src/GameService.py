from uuid import uuid4
from Game import Game
from Guess import Guess
from GuessResult import GuessResult

#from blockchain import Blockchain
#from verification import Verification


class GameService:
    """The GameService

    Attributes:
        :foo: 
    """

    def __init__(self):
        super().__init__()
        self._games = {}
        game = Game()
        self._game = game
        self._games[game.gameId] = game

    def processGuess(self, guessedNumber):
        #print('Processing guesses number: {}'.format(guessedNumber))
        distance = guessedNumber - self._game.secretNumber
        guess = Guess(guessedNumber, distance)
        self._game.addGuess(guess)
        guessesTaken = len(self._game.guesses)
        attemptsLeft = Game.MAX_ATTEMPTS - guessesTaken
        if (distance == 0):
            self._game.won()
        elif (attemptsLeft == 0):
            self._game.lost()
        return GuessResult(self._game.state, distance, guessesTaken, self._game.secretNumber)

    def getGameState(self):
        return self._game.state

    def startGame(self):
        self._game.start()

    def quitGame(self):
        self._game.quit()

    def getSecretNumber(self):
        return self._game.secretNumber
