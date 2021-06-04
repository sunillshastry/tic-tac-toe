# Tic-Tac-Toe

# -- BASIC INFORMATION --
# Author: Sunil Shastry.
# Project Started: June 4, 2021.

functions_info = {
	"integer_validation": 
		["Function helps to validate and check if a value is integer or not.", "main.py",["integer"]],

	"range_validation": 
		["Function helps to validate a value within the given range.", "main.py", ["value",  
		"totalranges"]],

	"take_choices":
		["Functions helps in taking initial user input choices for main menu", "main.py", []],

	"take_user_input":
		["Function performs validation of the input required for the row and column index.", "main.py", ["clas"]],

	"validate_name":
		["Used to validate a user's name.", "main.py", ["name"]],

	"display_board":
		["Function displays the list in a Tic-Tac-Toe format.", "TicTacToe.py", ["board"]],

	"set_value":
		["Function sets a value in a list if the position is empty, else returns False.",  
		"TicTacToe.py", ["board", "row", "column", "value"]],

	"check_rows":
		["Function checks if a row satisfies a win in Tic-Tac-Toe.","TicTacToe.py",["board","value"]],

	"check_columns":
		["Function checks if a column satisfies a win in Tic-Tac-Toe.", "TicTacToe.py", ["board",
		"value"]],

	"check_diagonals":
		["Function checks if a diagonal satisfies a win in Tic-Tac-Toe.", "TicTacToe.py", ["board", "value"]],

	"tie":
		["Function checks for a a tie.", "TicTacToe.py", ["board", "value1", "value2"]],

	"display_header":
		["Function displays a nice formatted header for the main menu.", "Greet.py", []],

	"display_introduction":
		["Function displays a welcome message and an option for the next stage.", "Greet.py", []],

	"display_gratitude":
		["Function thanks the user for playing and accessing the game", "Greet.py", []],

	"validate_input":
		["Function validates if the input is within the range of a Tic-Tac-Toe game.", "User.py", ["row", "column"]],

	"get_inputs":
		["Function takes and validates the inputs from a user.", "User.py", []],

	"new_board":
		["Function creates a new board for new game.", "User.py", []],

	"generate_index":
		["Function generates a random index for the CPU.", "CPU.py", []],

	"[CPU] get_inputs":
		["Function takes and validates the inputs from a user.", "CPU.py", []],

	"[CPU] new_board":
		["Function creates a new board for new game.", "CPU.py", []]
}

def function_help():
	for function in functions_info.keys():
		key = functions_info[function]
		function_use = key[0]
		function_location = key[1]
		function_param = key[2]

		print(f"Function name: {function}():")
		print(f"Function's use: {function_use}")
		print(f"Function's location: {function_location}")
		print(f"Function's parameters: {function_param}")
		print()


def helper():
	author = "Sunil Shastry"
	date = "June 4, 2021."
	project_name = "TicTacToe by Sunil."
	about_the_author = "Sunil Shastry is an undergraduate student at the University of Saskatchewan, Canada; majoring in Computer Science. During his first year, he developed the Tic-Tac-Toe game as a \"side-project\", applying all the knowledge and experience he learnt throughout the academic year. To contact Sunil about the project or for any contact purpose, please view the contact section below."
	game_info = "Tic-tac-toe, or X's and O's, is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a diagonal, horizontal, or vertical row is the winner. It is a solved game with a forced draw assuming best play from both players."
	file_names = ["main.py", "TicTacToe.py", "User.py", "CPU.py", "Greet.py", "gtest.py", "helper.py", "required_packages.txt", "README.md"]

	print("Welcome to the helper() function. Here you can view what each function and file is assigned to perform, or you can view more about the project and it's author.")
	print()
	print("To view the author, type: author")
	print("To view the project's date of creation, type: date")
	print("To view the project's name, type: project")
	print("To view more about the author, type: author_info")
	print("To view more about original Tic-Tac-Toe game, type: original")
	print("To view all the functions used in this project, type: functions")
	print("To view all the files created in the project, type: files")
	print("To quit, type: quit")

	while True:
		choice = input("What do you wish to do? - ")
		if choice == "quit":
			print("Thanks for accessing the helper.py file!")
			break
		elif choice == "files":
			print(file_names)
		elif choice == "functions":
			function_help()
		elif choice == "original":
			print(game_info)
		elif choice == "author_info":
			print(about_the_author)
		elif choice == "project":
			print(project_name)
		elif choice == "date":
			print(date)
		elif choice == "author":
			print(author)

  
helper()
