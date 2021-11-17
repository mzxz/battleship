from random import randint

size = 5
board = [["." for x in range(size)] for y in range(size)]


class Battelship:
    """
    Player's name class
    """
    def __init(self, name,):
        """
        class constructor
        """
        self.name = name


player_name = Battelship()
player_name = input("Please enter your name : \n")


def print_a(board):
    """
    create game board
    """
    for row in board:
        print(" ".join(row))
    return board


print_a(board)


def random_row(board):
    """
    generate random number for row
    """
    return randint(0, len(board) - 1)


def random_col(board):
    """
    generate random number for column
    """
    return randint(0, len(board) - 1)


def user_guesses(board):
    pass
