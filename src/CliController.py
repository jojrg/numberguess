from uuid import uuid4
from random import randint
from GameService import GameService
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
        self.__numbers = []
        self.__gameService = GameService()
        # self.blockchain = Blockchain(self.id)

    def get_user_choice(self):
        """Prompts the user for its choice and return it."""
        user_input = input('Your choice: ')
        return user_input

    def get_number_input(self):
        """Prompts the user for its choice and return it."""
        number_input = int(input('Your Number: '))
        return number_input

    def listen_for_input(self):
        """Starts the node and waits for user input."""
        waiting_for_input = True

        # A while loop for the user input interface
        # It's a loop that exits once waiting_for_input becomes False or when break is called
        while waiting_for_input:
            print('Please choose/ Bitte auswählen')
            print('1: Start a new game')
            print('2: Guess Number')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                self.__gameService.startGame()
                secretNumber = self.__gameService.getSecretNumber()
                print('The secret number is {}'.format(secretNumber))
            elif user_choice == '2':
                print('You choose option 2')
                self.__gameService.processGuess(self.get_number_input())
            elif user_choice == 'q':
                self.__gameService.quitGame()
                waiting_for_input = False
            else:
                print('Input was invalid, please pick a value from the list!')
        else:
            print('und tschüss kleiner Exo!')

        print('Done!')


ctl = CliController()
ctl.listen_for_input()
