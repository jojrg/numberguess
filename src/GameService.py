from uuid import uuid4
from Game import Game

#from blockchain import Blockchain
#from verification import Verification


class GameService:
    """The GameService

    Attributes:
        :foo: 
    """

    def __init__(self):
        super().__init__()
        self.__games = {}
        game = Game()
        self.__game = game
        self.__games[game.gameId] = game

    def processGuess(self, guessedNumber):
        print('Processing guesses number: {}'.format(guessedNumber))

    def startGame(self):
        print('Starting Game ..')
        self.__game.start()

    def quitGame(self):
        print('Quitting Game ..')
        self.__game.quit()

    def getSecretNumber(self):
        return self.__game.secretNumber
