from uuid import uuid4
from random import randint
from GameService import GameService
from GuessResult import GuessResult
from GameState import GameState
from Game import Game
#from blockchain import Blockchain
#from verification import Verification


class CliController:
    """The node which runs the local blockchain instance.

    Attributes:
        :id: The id of the node.
        :blockchain: The blockchain which is run by this node.
    """

    def __init__(self):
        # self.id = str(uuid4())
        self.id = 'MAX'
        self._gameService = GameService()
        self._ended = False
        # self.blockchain = Blockchain(self.id)

    @property
    def ended(self):
        return self._ended

    def main(self):
        while not self.ended:
            if (self._gameService.getGameState() == GameState.STARTED):
                self.handleGuess()
            else:
                self.mainMenu()

    def mainMenu(self):
        print('Please choose/ Bitte auswählen')
        print('1: Neues Spiel ..')
        print('q: Beenden')
        user_choice = input('Deine Auswahl: ')
        if user_choice == '1':
            self._gameService.startGame()
            secretNumber = self._gameService.getSecretNumber()
            print('-------------------------------------')
            print('Neues Spiel - neues Glück!!')
            print('Ich habe mir eine Zahl zwischen {} und {} ausgedacht .. '.format(
                Game.LOWER_BOUND, Game.UPPER_BOUND))
            print('Finde sie heraus. Du hast {} Versuche. Viel Glück!'.format(
                Game.MAX_ATTEMPTS))
            print('-------------------------------------\n')
        elif user_choice == 'q':
            self._ended = True
            print('Auf Wiedersehen - bis zur nächsten Raterunde!')

    def handleGuess(self):
        number_input = int(input('Dein Zahlentipp: '))
        guessResult = self._gameService.processGuess(number_input)
        if (guessResult.state == GameState.STARTED):
            if (guessResult.distance > 0):
                print('\n\nMeine Zahl ist kleiner!')
            else:
                print('\n\nMeine Zahl ist größer')
            print('Du hast noch {} Versuche\n'.format(
                guessResult.guessesLeft))
        elif (guessResult.state == GameState.WON):
            print('\n\n!!! G R A T U L A T I O N !!!\n\nDu hast die Zahl erraten. Sie ist: {}  ! :-)))'.format(
                guessResult.secretNumber))
            print('Anzahl der Versuche: {}'.format(
                guessResult.guessesTaken))
        elif (guessResult.state == GameState.LOST):
            print('\n\n\n!! L E I D E R   V E R L O R E N !!\n :-(((  Die gesuchte Zahl ist: {}!'.format(
                guessResult.secretNumber))
        else:
            raise Exception('Error: invalid state')


ctl = CliController()
ctl.main()
