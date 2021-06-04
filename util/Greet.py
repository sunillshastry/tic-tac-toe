# Tic-Tac-Toe

# -- BASIC INFORMATION --
# Author: Sunil Shastry.
# Project Started: June 4, 2021.

class Greet:
	def __init__(self):
		pass


	def __repr__(self):
		return "The Greet module provides some greetings to a user and displays a few text messages in a nicely formatted manner using the Pyfiglet module."


	def display_header(self):
		"""Displays a nice formatted header for the main menu."""
		tic_tac_toe = " _____ _         _____             _____          \n|_   _(_) ___   |_   _|_ _  ___   |_   _|__   ___ \n  | | | |/ __|____| |/ _` |/ __|____| |/ _ \\ / _ \\\n  | | | | (_|_____| | (_| | (_|_____| | (_) |  __/\n  |_| |_|\\___|    |_|\\__,_|\\___|    |_|\\___/ \\___|\n\n"
		print(tic_tac_toe)


	def display_introduction(self):
		"""Display a welcome message and an option for the next stage."""
		print("Welcome to the Tic-Tac-Toe game!")
		print("Choose to play against a user or the CPU.")


	def display_gratitude(self, played=True):
		"""Function appreciates user's time in playing our game."""
		if played:
			print("Thank you for playing the game. We hope to see you again soon!")
		else:
			print("Thank you for accessing the game. We hope to see you again soon!")
