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
print(f"welcome To Battelship Game:\n {player_name}")
print('='*22)
print("Pleas start the program again! ")
print("Also choose int number between 0 to 4!")
print('='*22)


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
    """
    Main function for user gesses, and cheack game in all situations
    """
    ship_row = random_row(board)
    ship_col = random_col(board)
    user_guesses = 0
    while True:
        print("=" * 22)

        try:
            guess_ship_row = int(input('Guess ship Row:\n '))
            guess_ship_col = int(input('Guess ship Col:\n '))
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n ")
            print("Pleas start the program again! ")
            print("Also choose int number between 0 to 4!")
            return False

        if guess_ship_row == ship_row and guess_ship_col == ship_col:
            board[ship_row][ship_col] = '*'

            print('Congoratulation! You sank The battleship!')
            print_a(board)
            break

        elif guess_ship_row not in range(5) or guess_ship_col not in range(5):
            print("That's out of range.")

        elif board[guess_ship_row][guess_ship_col] == 'X':
            print("You guessed that one already.")

        else:
            print('You missed my battelship')
            board[guess_ship_row][guess_ship_col] = 'X'
            print_a(board)

            user_guesses = user_guesses + 1
            print(f"It's your turn: {user_guesses}")

            if user_guesses == 4:
                print_a(board)
                print("Game is over! You have run out of turns!")
                print(ship_row)
                print(ship_col)
                break


user_guesses(board)


