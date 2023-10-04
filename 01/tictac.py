"""Modules for slowing game and random choice cell on field-board"""
import time
from random import choice


imagine_cells = {0: '.', 1: 'X', 2: 'O'}

roles = {'Игрок': 1, 'Компьютер': 2}


class TicTacGame:
    """Logic class of game"""
    def __init__(self):
        self.field = [0] * 9

    @staticmethod
    def hello_msg():
        """Message for begin of game"""
        print('Вы начали игру в крестики-нолики с компьютером, следуйте инструкциям')

    @staticmethod
    def reply_pick_msg():
        """Message to console after computer has pick"""
        return input(
            'Твой черёд: введи номер клетки, отсчитывая от лева и от верха. '
            'Например центр 5, правый нижний угол 9\n')

    def show_board(self):
        """Console imagination of cell's board"""
        for row in range(3):
            print(f'|{imagine_cells[self.field[0 + row * 3]]}'
                  f'|{imagine_cells[self.field[1 + row * 3]]}'
                  f'|{imagine_cells[self.field[2 + row * 3]]}|')

    def check_winner(self, role):
        """Method for determining the winner"""
        return any(
            (
                (self.field[0] == self.field[4] == self.field[8] == roles[role]),
                (self.field[2] == self.field[4] == self.field[6] == roles[role]),
                (self.field[0] == self.field[1] == self.field[2] == roles[role]),
                (self.field[3] == self.field[4] == self.field[5] == roles[role]),
                (self.field[6] == self.field[7] == self.field[8] == roles[role]),
                (self.field[0] == self.field[3] == self.field[6] == roles[role]),
                (self.field[1] == self.field[4] == self.field[7] == roles[role]),
                (self.field[2] == self.field[5] == self.field[8] == roles[role])
            )
        )

    def win_msg(self, role):
        """Message to announce the winner"""
        print('Ты победил :)' if roles[role] == 1 else 'Ты проиграл :(')
        self.show_board()

    def validate_input(self, func):
        """Validate console input data from user"""
        while True:
            arg = func()

            if len(arg) != 1 or not arg.isdigit() or arg == '0':
                print('Ошибка ввода, введи одну цифру от 1 до 9!')

            elif int(arg) not in [
                cell + 1 for cell in range(len(self.field)) if self.field[cell] == 0
            ]:
                print('Ошибка! Клетка уже занята!')
            else:
                return int(arg)

    def computer_pick(self):
        """Fill random empty field by random (by computer)"""
        print('Компьютер сходил')
        self.field[choice([cell for cell in range(len(self.field)) if self.field[cell] == 0])] = 2

    def player_pick(self, cell: int):
        """Fill picked by player cell"""
        self.field[cell - 1] = 1

    def first_pick_msg(self):
        """Another method for fill picked by user cell only for start state"""
        TicTacGame.hello_msg()
        self.show_board()
        return input('Куда хочешь поставить крестик? '
                     'Введи номер клетки, отсчитывая от лева и от верха.\n')

    @staticmethod
    def start_game_player_to_computer():
        """Launch game"""
        current_game = TicTacGame()
        current_game.player_pick(current_game.validate_input(current_game.first_pick_msg))
        current_game.show_board()
        while True:
            time.sleep(1)
            current_game.computer_pick()
            current_game.show_board()
            if current_game.check_winner('Компьютер'):
                current_game.win_msg('Компьютер')
                break
            current_game.player_pick(current_game.validate_input(current_game.reply_pick_msg))
            current_game.show_board()
            if current_game.check_winner('Игрок'):
                current_game.win_msg('Игрок')
                break


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game_player_to_computer()
