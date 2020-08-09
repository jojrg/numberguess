from uuid import uuid4
from random import randint
from service.GameService import GameService
from dto.GuessResult import GuessResult
from dto.GameState import GameState
from dto.Game import Game


class CliController:
    """ Command line based client class for NumberGuess game """

    def __init__(self):
        # self.id = str(uuid4())
        self.__ended = False
        self.__currentGameId = None

    def main(self):
        self.mainMenu()
        while not self.__ended:
            if (GameService.getGameState(self.__currentGameId) == GameState.STARTED):
                self.handleGuess()
            else:
                self.mainMenu()

    def mainMenu(self):
        print('Please choose/ Bitte auswählen')
        print('1: Neues Spiel ..')
        print('q: Beenden')
        user_choice = input('Deine Auswahl: ')
        if user_choice == '1':
            self.__currentGameId = GameService.registerGame()
            GameService.startGame(self.__currentGameId)
            secretNumber = GameService.getSecretNumber(self.__currentGameId)
            print('-------------------------------------')
            print('Neues Spiel - neues Glück!!')
            print('Ich habe mir eine Zahl zwischen {} und {} ausgedacht .. '.format(
                Game.LOWER_BOUND, Game.UPPER_BOUND))
            print('Finde sie heraus. Du hast {} Versuche. Viel Glück!'.format(
                Game.MAX_ATTEMPTS))
            print('-------------------------------------\n')
        elif user_choice == 'q':
            self.__ended = True
            print('Auf Wiedersehen - bis zur nächsten Raterunde!')

    def handleGuess(self):
        number_input = int(input('Dein Zahlentipp: '))
        guessResult = GameService.processGuess(
            self.__currentGameId, number_input)
        if (guessResult.state == GameState.STARTED):
            if (guessResult.distance > 0):
                print('\n\nMeine Zahl ist kleiner!')
            else:
                print('\n\nMeine Zahl ist größer')
            print('Du hast noch {} Versuche\n'.format(
                guessResult.guessesLeft))
        elif (guessResult.state == GameState.WON):
            # writing game to a json file
            GameService.saveGame(self.__currentGameId)
            print('\n\n!!! G R A T U L A T I O N !!!\n\nDu hast die Zahl erraten. Sie ist: {}  ! :-)))'.format(
                guessResult.secretNumber))
            print('Anzahl der Versuche: {}'.format(
                guessResult.guessesTaken))
        elif (guessResult.state == GameState.LOST):
           # writing game to a json file
            GameService.saveGame(self.__currentGameId)
            print('\n\n\n!! L E I D E R   V E R L O R E N !!\n :-(((  Die gesuchte Zahl ist: {}!'.format(
                guessResult.secretNumber))
        else:
            raise Exception('Error: invalid state')


if __name__ == '__main__':
    ctl = CliController()
    ctl.main()
