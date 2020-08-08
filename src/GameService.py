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
    games = {}

    @classmethod
    def registerGame(cls):
        """ Creates a new Game instance, stores it in games dictionary and return the gameid"""
        newGame = Game()
        cls.games[newGame.gameId] = newGame
        return newGame.gameId

    @classmethod
    def processGuess(cls, gameId, guessedNumber):
        """ processes a guess, sets the game state and returns a GuessResult """
        #print('Processing guesses number: {}'.format(guessedNumber))
        game = cls.games[gameId]
        distance = guessedNumber - game.secretNumber
        guess = Guess(guessedNumber, distance)
        game.addGuess(guess)
        guessesTaken = len(game.guesses)
        attemptsLeft = Game.MAX_ATTEMPTS - guessesTaken
        if (distance == 0):
            game.won()
        elif (attemptsLeft == 0):
            game.lost()
        return GuessResult(game.state, distance, guessesTaken, game.secretNumber)

    @classmethod
    def getGameState(cls, gameId):
        return cls.games[gameId].state

    @classmethod
    def startGame(cls, gameId):
        print('Processing GameService.startGame, gameid: {}'.format(gameId))
        game = cls.games[gameId]
        print('Processing game, game: {}'.format(game))
        print('game id: {}'.format(game.gameId))
        cls.games[gameId].start()

    @classmethod
    def quitGame(cls, gameId):
        cls.games[gameId].quit()

    @classmethod
    def getSecretNumber(cls, gameId):
        return cls.games[gameId].secretNumber
