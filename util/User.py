# Tic-Tac-Toe

# -- BASIC INFORMATION --
# Author: Sunil Shastry.
# Project Started: June 4, 2021.

from .TicTacToe import TicTacToe

class User(TicTacToe):
	_default = "*"
	_gameboard = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
	PLAYER1 = "X"
	PLAYER2 = "O"


	def __init__(self):
		pass



	def __repr__(self):
		return "User is an extended module of TicTacToe. User module allows the users to enter their respective value, validates it, and ultimately returns the winner of the game."



	def validate_input(self, row, column):
		"""Validates if the input is within the range of a Tic-Tac-Toe game."""
		if (row >= 1 and row <= 3) and (column >= 1 and column <= 3):
			return True
		else:
			return False



	def get_inputs(self):
		"""Takes and validates the inputs from a user."""
		row_index = input("Enter row number (1, 2, 3): ")
		column_index = input("Enter column number (1, 2, 3): ")
		while True:
			try:
				row_index = int(row_index)
				column_index = int(column_index)
			except ValueError:
				print("\nPlease enter a number!")
				row_index = input("Enter row number (1, 2, 3): ")
				column_index = input("Enter column number (1, 2, 3): ")
			else:
				break
		return (row_index, column_index)



	def new_board(self):
		"""Creates a new board when game is finished"""
		self._gameboard = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]


