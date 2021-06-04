# Tic-Tac-Toe

# -- BASIC INFORMATION --
# Author: Sunil Shastry.
# Project Started: June 4, 2021.


from .TicTacToe import TicTacToe
from random import randint

class CPU(TicTacToe):
	_default = "*"
	_gameboard = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
	PLAYER = "X"
	CPU = "O"


	def __init__(self):
		pass



	def __repr__(self):
		return "CPU is an extended module of TicTacToe. CPU module allows one user to enter their respective value, validates it, and CPU takes it's turn and ultimately returns the winner of the game."



	def generate_index(self):
		"""Generates a random index for the CPU."""
		row_index = randint(0, 2)
		column_index = randint(0, 2)
		return (row_index, column_index)



	def get_inputs(self):
		"""Takes and validates the inputs from a user."""
		row_index = input("Enter row number (1, 2, 3): ")
		column_index = input("Enter column number (1, 2, 3): ")
		while True:
			try:
				row_index = int(row_index)
				column_index = int(column_index)
			except ValueError:
				print("Please enter a number!")
				row_index = input("Enter row number (1, 2, 3): ")
				column_index = input("Enter column number (1, 2, 3): ")
			else:
				break
		return (row_index, column_index)



	def new_board(self):
		"""Creates a new board when game is finished."""
		self._gameboard = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
