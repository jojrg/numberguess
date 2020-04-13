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
        # self.blockchain = Blockchain(self.id)

    def get_user_choice(self):
        """Prompts the user for its choice and return it."""
        user_input = input('Deine Auswahl: ')
        return user_input

    def get_number_input(self):
        """Prompts the user for its choice and return it."""
        number_input = int(input('Dein Zahlentipp: '))
        return number_input

    def handleGuess(self):
        guessResult = self._gameService.processGuess(
            self.get_number_input())
        if (guessResult.state == GameState.STARTED):

            if (guessResult.distance > 0):
                print('\nMeine Zahl ist kleiner!')
            else:
                print('\nMeine Zahl ist größer')
            print('Du hast noch {} Versuche\n'.format(
                guessResult.guessesLeft))
        elif (guessResult.state == GameState.WON):
            print('\nGratuliere!! Du hast die Zahl erraten. Sie ist: {}  ! :-)))'.format(
                guessResult.secretNumber))
            print('Anzahl deiner Tipps: {}'.format(
                guessResult.guessesTaken))
        elif (guessResult.state == GameState.LOST):
            print('\nLeider verloren! Die gesuchte Zahl ist: {}!'.format(
                guessResult.secretNumber))
        else:
            raise Exception('Error: invalid state')

    def listen_for_input(self):
        """Starts the node and waits for user input."""
        waiting_for_input = True

        # A while loop for the user input interface
        # It's a loop that exits once waiting_for_input becomes False or when break is called
        while waiting_for_input:
            print('Please choose/ Bitte auswählen')
            print('1: Neues Spiel ..')
            if (self._gameService.getGameState() == GameState.STARTED):
                print('2: Tipp abgeben')
            print('q: Beenden')
            user_choice = self.get_user_choice()
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

                self.handleGuess()
                #print('The secret number is {}'.format(secretNumber))
            elif user_choice == '2':
                self.handleGuess()
            elif user_choice == 'q':
                self._gameService.quitGame()
                waiting_for_input = False
            else:
                print('Unzulässige Eingabe!')
        else:
            print('Auf Wiedersehen - bis zur nächsten Raterunde!')

        print('Ende')


ctl = CliController()
ctl.listen_for_input()
