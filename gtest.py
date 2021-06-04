# Tic-Tac-Toe

# -- BASIC INFORMATION --
# Author: Sunil Shastry.
# Project Started: June 4, 2021.

# Guide and Tests file for TicTacToe class functions.

from util.TicTacToe import TicTacToe

tictactoe = TicTacToe()

def print_attributes():
	"""Print all the attributes used in the TicTacToe class."""
	print(tictactoe)
	print()
	winning_num = tictactoe._win
	default_value = tictactoe._default
	print("Winning row/column/diagonal count: {}".format(winning_num))
	print("Default value in the game board {}".format(default_value))
	print()


def test_function(game_list, expected_list, testing_function):
	"""
	Purpose:
		To test TicTacToe class methods.
	Params:
		game_list: A square list consisting of repeated or unrepeated values.
		expected_list: A list of possible outcomes for game_list testing.
		testing_function: Function that undergoes the testing process.
	Tasks:
		Prints test results.
	Return:
		None.
	"""
	function_name = testing_function.__name__
	print(f"Testing: {function_name}() function:")

	test_count = 0
	total_tests = len(game_list)

	for (i, case) in enumerate(game_list):
		test_case = case[0]
		testing_value = case[1]


		expected = expected_list[i]
		result = testing_function(test_case, testing_value)

		if expected != result:
			print(f"TEST FAILED! Expected: {expected}; Result: {result}")
		else:
			print("TEST PASSED!")
			test_count = test_count + 1
	print(f"TESTS COMPLETED: {test_count}/{total_tests} PASSED!")
	print()


rows_cases = [
	([[0, 0, 1], [1, 0, 1], [0, 1, 0]], 0),
	([["hello", "world", "hello"],["world", "world", "world"], ["hello", "world", "world"]], "world"),
	([[True, True, False], [False, True, True], [True, True, True]], True),
	([["10", "10", "10"], ["20", 20, "20"], [30, "30", 30]], "10"),
	([["X", "O", "X"], ["O", "X", "X"], ["X", "O", 10]], "X"),
	([["X", "X", "X"], ["O", "O", "O"], ["O", "O", "O"]], "O")
]
rows_expected = [False, True, True, True, False, True]


columns_cases = [
	([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 1),
	([[1, 0, 0], [0, 0, 0], [0, 1, 0]], 0),
	([["hello", "world", "hello"], ["world", "world", "hello"], ["hello", "world", "hello"]],"world"),
	([[True, False, True], [False, True, True], [False, False, False]], False),
	([["X", "X", "X"], ["O", "X", "O"], ["X", "X", "O"]], "X")
]
columns_expected = [False, True, True, False, True]


diagonals_cases = [
	([[0, 1, 1], [1, 0, 0], [0, 0, 0]], 0),
	([[0, 1, 0], [1, 0, 1], [0, 1, 0]], 1),
	([["world", "world", "world"], ["world", "world", "world"], ["world", "world", "world"]],"hello"),
	([[False, True, False], [False, False, True], [True, True, False]], False),
	([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]], "X")
]
diagonals_expected = [True, False, False, True, True]


print_attributes()

# Rows testing
test_function(rows_cases, rows_expected, tictactoe.check_rows)

# Column testing
test_function(columns_cases, columns_expected, tictactoe.check_columns)

# Diagonals testing
test_function(diagonals_cases, diagonals_expected, tictactoe.check_diagonals)

print("End of testing.")
