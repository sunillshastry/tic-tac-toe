# Tic-Tac-Toe

# -- BASIC INFORMATION --
# Author: Sunil Shastry.
# Project Started: June 4, 2021.


# -- BACKGROUND --
# Tic-Tac-Toe is a simple multiplayer game which is best preferred to play with a pencil and a paper between two players. This is an open-source Python application of Tic-Tac-Toe which takes a level above the actual game, a user can play a game of Tic-Tac-Toe against another user, or against the CPU. The main goal of this application is to provide a nice user experience while performing all the important aspects of the game Tic-Tac-Toe.


# -- SYNOPSIS --
# Play a game of Tic-Tac-Toe with another user or with the CPU until one of you wins the game.

# -- MORE ABOUT THE AUTHOR ---
# Tic-Tac-Toe is a simple and open-source project designed and built by Sunil Shastry. Sunil is an undergraduate student at the University of Saskatchewan, Canada; majoring in Computer Science. During his first year, he developed the Tic-Tac-Toe game as a "side-project", applying all the knowledge and experience he learnt throughout the academic year. To contact Sunil about the project or for any contact purpose, please view the contact section below.


from util.Greet import Greet
from util.User import User
from util.CPU import CPU

def available_choices():
	print("1. Play against another user.")
	print("2. Play against the CPU.")
	print("3. Quit game.")
	print()

greet = Greet()
greet.display_header()
greet.display_introduction()
available_choices()

def integer_validation(integer):
	"""Validate to check if a value is integer or not."""
	while True:
		try:
			integer = int(integer)
		except ValueError:
			integer = input("Please enter a valid number: ")
		except:
			integer = input("Error. Please try again: ")
		else:
			break
	return integer



def range_validation(value, *totalranges):
	"""Validate a value within the given range."""
	totalranges = list(totalranges)
	while True:
		if value in totalranges:
			return True
		else:
			return False



def take_choices():
	"""Take initial user input choices and validate them."""
	choice = input("Enter your value (1, 2 or 3): ")
	while True:
		choice = integer_validation(choice)
		required_range = range_validation(choice, 1, 2, 3)
		if required_range:
			break
		else:
			choice = input("Please enter a valid value (1, 2 or 3): ")
	return choice



def take_user_input(clas):
	"""Validate the input required for the row and column index."""
	user_inputs = clas.get_inputs()
	user_row = user_inputs[0]
	user_col = user_inputs[1]
	while True:
		row_range = range_validation(user_row, 1, 2, 3)
		if row_range:
			break
		else:
			print("\nInvalid row. Please enter (1, 2 or 3).")
			user_inputs = clas.get_inputs()
			user_row = user_inputs[0]
			user_col = user_inputs[1]

	while True:
		col_range = range_validation(user_col, 1, 2, 3)
		if col_range:
			break
		else:
			print("\nInvalid column. Please enter (1, 2 or 3).")
			user_inputs = clas.get_inputs()
			user_row = user_inputs[0]
			user_col = user_inputs[1]
	row = user_row - 1
	col = user_col - 1
	return (row, col)



def validate_name(name):
	"""Validate a user's name."""
	while True:
		if len(name) > 0:
			return name.upper()
		else:
			name = input("Please enter a valid name: ")


user_choice = take_choices()



# PLAYER VS PLAYER
if user_choice == 1:
	# Inform game format:
	print("MULTIPLAYER GAME\n")

	# Take Player-1 name and validate it.
	player1_name = input("Player 1 - Enter your name: ")
	player1_name = validate_name(player1_name)

	# Take Player-2 name and validate it.
	player2_name = input("Player 2 - Enter your name: ")
	player2_name = validate_name(player2_name)
	print()

	# Print a fighting showdown.
	print(f"{player1_name.upper()} vs {player2_name.upper()}")

	# Create a new User class
	user = User()

	# Access the board for the game and display it.
	gameboard = user._gameboard
	print()
	user.display_board(gameboard)
	print()

	# Start a infinite loop using while True.
	while True:
		# ************************************************
		# PLAYER1'S TURN.
		print(f"{player1_name}'s turn:")
		user1_inputs = take_user_input(user)
		user1_row = user1_inputs[0]
		user1_col = user1_inputs[1]

		# Validate to set the value in the correct index.
		while True:
			user1_set = user.set_value(gameboard, user1_row, user1_col, user.PLAYER1)
			if user1_set:
				break
			else:
				print("Position already taken.")
				user1_inputs = take_user_input(user)
				user1_row = user1_inputs[0]
				user1_col = user1_inputs[1]

		# Display game board after setting the value.
		print()
		user.display_board(gameboard)
		print()

		# Check if PLAYER1 has won.
		u1_row_check = user.check_rows(gameboard, user.PLAYER1)
		u1_col_check = user.check_columns(gameboard, user.PLAYER1)
		u1_diagonal_check = user.check_diagonals(gameboard, user.PLAYER1)
		if u1_row_check or u1_col_check or u1_diagonal_check:
			print(f"{player1_name} has won!")
			user.new_board()
			greet.display_gratitude(played=True)
			break

		# Check if there is a tie between PLAYER1 and PLAYER2
		tie_game = user.tie(gameboard, user.PLAYER1, user.PLAYER2)
		if tie_game:
			print("Game has ended in a tie!")
			user.new_board()
			greet.display_gratitude(played=True)
			break


		# ************************************************
		# PLAYER2'S TURN:
		print(f"{player2_name}'s turn:")
		user2_inputs = take_user_input(user)
		user2_row = user2_inputs[0]
		user2_col = user2_inputs[1]

		# Validate to set the value in the correct index.
		while True:
			user2_set = user.set_value(gameboard, user2_row, user2_col, user.PLAYER2)
			if user2_set:
				break
			else:
				print("Position already taken.")
				user2_inputs = take_user_input(user)
				user2_row = user2_inputs[0]
				user2_col = user2_inputs[1]

		# Display game board after setting the value.
		print()
		user.display_board(gameboard)
		print()

		# Check if PLAYER2 has won the game.
		u2_row_check = user.check_rows(gameboard, user.PLAYER2)
		u2_col_check = user.check_columns(gameboard, user.PLAYER2)
		u2_diagonal_check = user.check_diagonals(gameboard, user.PLAYER2)
		if u2_row_check or u2_col_check or u2_diagonal_check:
			print(f"{player2_name} has won!")
			user.new_board()
			greet.display_gratitude(played=True)
			break

		# Check if there is a tie between PLAYER1 and PLAYER2.
		tie_game = user.tie(gameboard, user.PLAYER1, user.PLAYER2)
		if tie_game:
			print("Game has ended in a tie!")
			user.new_board()
			greet.display_gratitude(played=True)
			break
	# END OF GAME.


# PLAYER VS CPU
elif user_choice == 2:
	# Display game format.
	print("CPU GAME\n")

	# Take player's name and validate it.
	player_name = input("Please enter your name: ")
	player_name = validate_name(player_name)

	# Print a fighting showdown.
	print(f"{player_name.upper()} vs CPU")
	print()

	# Create a new class CPU
	cpu = CPU()

	# Access the game board for the match and display it.
	cpuboard = cpu._gameboard
	print()
	cpu.display_board(cpuboard)
	print()

	# Start a infinite loop using while True.
	while True:
		print(f"{player_name}'s turn:")
		player_inputs = take_user_input(cpu)
		player_row = player_inputs[0]
		player_col = player_inputs[1]

		# Validate to set the value in the correct index.
		while True:
			player_set = cpu.set_value(cpuboard, player_row, player_col, cpu.PLAYER)
			if player_set:
				break
			else:
				print("Position already taken.")
				player_inputs = take_user_input(cpu)
				player_row = player_inputs[0]
				player_col = player_inputs[1]

		# Display game board after setting the value.
		print()
		cpu.display_board(cpuboard)
		print()

		# Check if the Player has won.
		player_row_check = cpu.check_rows(cpuboard, cpu.PLAYER)
		player_col_check = cpu.check_columns(cpuboard, cpu.PLAYER)
		player_diagonals_check = cpu.check_diagonals(cpuboard, cpu.PLAYER)
		if player_row_check or player_col_check or player_diagonals_check:
			print(f"{player_name} has won!")
			cpu.new_board()
			greet.display_gratitude(played=True)
			break

		# Check if there is a tie between the player and CPU
		game_tie = cpu.tie(cpuboard, cpu.PLAYER, cpu.CPU)
		if game_tie:
			print("Game has ended in a tie!")
			cpu.new_board()
			greet.display_gratitude(played=True)
			break


		# CPU's turn to play.
		print("CPU's turn:")

		# Generate random indexes for CPU's turn.
		cpu_indexes = cpu.generate_index()
		cpu_row = cpu_indexes[0]
		cpu_col = cpu_indexes[1]

		# Validate to set CPU's values in the correct index.
		while True:
			cpu_set = cpu.set_value(cpuboard, cpu_row, cpu_col, cpu.CPU)
			if cpu_set:
				print(f"CPU has chosen row: {cpu_row} and column: {cpu_col}")
				break
			else:
				cpu_indexes = cpu.generate_index()
				cpu_row = cpu_indexes[0]
				cpu_col = cpu_indexes[1]

		# Display the board after setting values.
		print()
		cpu.display_board(cpuboard)
		print()

		# Check if CPU has won the game.
		cpu_row_check = cpu.check_rows(cpuboard, cpu.CPU)
		cpu_col_check = cpu.check_columns(cpuboard, cpu.CPU)
		cpu_diagonals_check = cpu.check_diagonals(cpuboard, cpu.CPU)
		if cpu_row_check or cpu_col_check or cpu_diagonals_check:
			print("CPU has won!")
			cpu.new_board()
			greet.display_gratitude(played=True)
			break

		# Check if there is a tie between CPU and Player.
		game_tie = cpu.tie(cpuboard, cpu.PLAYER, cpu.CPU)
		if game_tie:
			print("Game has ended in a tie!")
			cpu.new_board()
			greet.display_gratitude(played=True)
			break

# User wants to quit before playing.
elif user_choice == 3:
	greet.display_gratitude(played=False)



