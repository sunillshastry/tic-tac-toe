# Tic-Tac-Toe

# -- BASIC INFORMATION --
# Author: Sunil Shastry.
# Project Started: June 4, 2021.

class TicTacToe:
	_win = 3
	_default = "*"


	def __init__(self):
		pass


	def __repr__(self):
		return "TicTacToe module allows the user(s) or the CPU to enter their respective value, validates it, and ultimately returns the winner of the game."



	def display_board(self, board):
		"""Displays the list in a Tic-Tac-Toe format."""
		for row in board:
			for (i, item) in enumerate(row):
				if i == 0:
					print(f"| {item}", end=" ")
				elif i == 1:
					print(f"| {item}", end=" | ")
				elif i == 2:
					print(item, end=" |")
			print()



	def set_value(self, board, row, column, value="*"):
		"""Sets the value in a list if position is empty, else returns False."""
		if board[row][column] == self._default:
			board[row][column] = value
			return True
		else:
			board[row][column] == self._default
			return False



	def check_rows(self, board, value=0):
		"""Checks if a row satisfies a win in Tic-Tac-Toe."""
		for row in board:
			counter = 0
			for item in row:
				if item == value:
					counter = counter + 1

			if counter == self._win:
				return True
		return False



	def check_columns(self, board, value=0):
		"""Checks if the column satisfies a win in Tic-Tac-Toe."""
		column_board = []
		col_counter = 0
		while col_counter < len(board):
			column_list = [row[col_counter] for row in board]
			column_board.append(column_list)
			col_counter = col_counter + 1

		for row in column_board:
			counter = 0
			for item in row:
				if item == value:
					counter = counter + 1

			if counter == self._win:
				return True
		return False



	def check_diagonals(self, board, value=0):
		"""Checks if a diagonal satisfies a win in Tic-Tac-Toe."""
		start = 0
		end = len(board) - 1

		upward_list = []
		downward_list = []

		for row in board:
			up_value = row[start]
			down_value = row[end]

			upward_list.append(up_value)
			downward_list.append(down_value)

			start = start + 1
			end = end - 1

		diagonals = [upward_list, downward_list]

		for row in diagonals:
			counter = 0
			for item in row:
				if item == value:
					counter = counter + 1
			if counter == self._win:
				return True
		return False



	def tie(self, board, value1, value2):
		"""Checks if there is a tie between two players."""
		total_item_len = sum([len(row) for row in board])
		counter = 0
		for row in board:
			for item in row:
				if item == value1 or item == value2:
					counter = counter + 1
		if counter == total_item_len:
			return True
		else:
			return False

