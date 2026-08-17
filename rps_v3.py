import random #imports the random archive to randomize the computers choice

print("Welcome to Rock, Paper, Scissors!")

#rules for the game modes
rules = "Classic mode:\nRock smashes Scissors\nPaper covers Rock\nScissors cut Paper\n\nRemix Mode:\nRock smashes scissors\nRock crushes Lizard\nPaper covers Rock\nPaper disproves Spock\nScissors cut Paper\nScissors decapitates Lizard\nLizard eats Paper\nLizard poisons Spock\nSpock vaporizes Rock\nSpock smashes Scissors"

rules_classic = "Classic mode:\nRock smashes Scissors\nPaper covers Rock\nScissors cut Paper"

rules_remix = "Remix Mode:\nRock smashes scissors\nRock crushes Lizard\nPaper covers Rock\nPaper disproves Spock\nScissors cut Paper\nScissors decapitates Lizard\nLizard eats Paper\nLizard poisons Spock\nSpock vaporizes Rock\nSpock smashes Scissors"


def get_choices_classic(): #function to get both players choices for classic
	options = ["rock", "paper", "scissors"]
	player_choice = input("Enter a choice (rock, paper, scissors, rules):").strip().lower()
	while player_choice == "rules":
		print(rules_classic)
		player_choice = input("Enter a choice (rock, paper, scissors, rules):").strip().lower()
	while player_choice not in options: #checks if players input is within choices
		print("Invalid answer, please try again!")
		player_choice = input("Enter a choice (rock, paper, scissors, rules):").strip().lower()
	computer_choice = random.choice(options)
	choices = {"player" : player_choice, "computer": computer_choice}
	return choices
	
def get_choices_remix(): #function to get both players choices for remix
	options = ["rock", "paper", "scissors", "lizard", "spock"]
	player_choice = input("Enter a choice (rock, paper, scissors, lizard, spock, rules):").strip().lower()
	while player_choice == "rules":
		print(rules_remix)
		player_choice = input("Enter a choice (rock, paper, scissors, lizard, spock, rules):").strip().lower()
	while player_choice not in options: #checks if players input is within choices
		print("Invalid answer, please try again!")
		player_choice = input("Enter a choice (rock, paper, scissors, lizard, spock, rules):").strip().lower()
	computer_choice = random.choice(options)
	choices = {"player" : player_choice, "computer": computer_choice}
	return choices
	
player_win = 0 #starting scores for the game
computer_win = 0

def check_win_classic(player, computer, player_win, computer_win): #function to check who won the match for classic
	beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
	messages_classic = {
		 ("rock", "scissors"): "Rock smashes scissors. You win!",
		 ("paper", "rock"): "Paper covers rock. You win!",
		 ("scissors", "paper"): "Scissors cut paper. You Win!",
		 ("scissors", "rock"): "Rock smashes scissors. You Lose!",
		 ("rock", "paper"): "Paper covers rock. You Lose!",
		 ("paper", "scissors"): "Scissors cut paper. You Lose!" 
	}
	print(f"You chose {player}. Computer chose {computer}")
	if player == computer:
		return "It's a tie!", player_win, computer_win
	elif beats[player] == computer:
		player_win += 1
		msg = messages_classic[(player, computer)]
		return msg, player_win, computer_win
	elif beats[computer] == player:
		computer_win +=1
		msg = messages_classic[(player,computer)]
		return msg, player_win, computer_win
	
def check_win_remix(player, computer, player_win, computer_win): #function to check who won the match
	beats = {"rock": ["scissors", "lizard"], "paper": ["rock", "spock"], "scissors": ["paper", "lizard"], "lizard": ["paper", "spock"], "spock": ["scissors", "rock"]}
	messages_remix = {
	# Player wins
	("rock", "scissors"): "Rock smashes scissors. You win!",
	("rock", "lizard"): "Rock crushes lizard. You win!",
	("paper", "rock"): "Paper covers rock. You win!",
	("paper", "spock"): "Paper disproves Spock. You win!",
	("scissors", "paper"): "Scissors cut paper. You win!",
	("scissors", "lizard"): "Scissors decapitates lizard. You win!",
	("lizard", "paper"): "Lizard eats paper. You win!",
	("lizard", "spock"): "Lizard poisons Spock. You win!",
	("spock", "scissors"): "Spock smashes scissors. You win!",
	("spock", "rock"): "Spock vaporizes rock. You win!",
	("scissors", "rock"): "Rock smashes scissors. You lose!",
	("lizard", "rock"): "Rock crushes lizard. You lose!",
	("rock", "paper"): "Paper covers rock. You lose!",
	("spock", "paper"): "Paper disproves Spock. You lose!",
	("paper", "scissors"): "Scissors cut paper. You lose!",
	("lizard", "scissors"): "Scissors decapitates lizard. You lose!",
	("paper", "lizard"): "Lizard eats paper. You lose!",
	("spock", "lizard"): "Lizard poisons Spock. You lose!",
	("scissors", "spock"): "Spock smashes scissors. You lose!",
	("rock", "spock"): "Spock vaporizes rock. You lose!",
}
	print(f"You chose {player}. Computer chose {computer}")
	if player == computer:
		return "It's a tie!", player_win, computer_win
	elif computer in beats[player]:
		player_win += 1
		msg = messages_remix[(player, computer)]
		return msg, player_win, computer_win
	elif player in beats[computer]:
		computer_win +=1
		msg = messages_remix[(player,computer)]
		return msg, player_win, computer_win
version = input("Which version would you like to play? \nClassic or remix? (Type 'rules' to display rules for both game modes) ").strip().lower() #checks which version the player wants to play
while version == "rules":
	print(rules)
	version = input("Which version would you like to play? \nClassic or remix? (Type 'rules' to display rules for both game modes) ").strip().lower()
while version != "classic" and version != "remix":
	print("Invalid input. Please try again.")
	version = input("Which version would you like to play? Classic or remix? Type 'rules' to display rules for both game modes)").strip().lower()
	
if version == "classic": #plays classic mode
	play_again = "y"   

	while play_again == "y": #Loops game till player choses "n"
	
		if player_win > 0 or computer_win > 0: #asks if score wants to be reset
			reset = input("Would you like to reset the score? (y/n) ").strip().lower()
			while reset != "y" and reset != "n":
				print("Invalid response. Please try again.")
				reset = input("Would you like to reset the score? (y/n) ").strip().lower()
			if reset == "y":
				player_win = 0
				computer_win = 0
				print("Score Reset!")
				
		choices = get_choices_classic()
		result, player_win, computer_win = check_win_classic(choices["player"], choices["computer"], player_win, computer_win)
		print(result)
		print(f"Score: You: {player_win} Computer: {computer_win}")
		play_again = input("Play again? (y/n)").strip().lower()
		while play_again != "y" and play_again != "n":
				print("Invalid input. Please try again.")
				play_again = input("Play again? (y/n)").strip().lower()
else: #plays remix version
	play_again = "y"

	while play_again == "y": #Loops game till player choses "n"
	
		if player_win > 0 or computer_win > 0: #asks if score wants to be reset
			reset = input("Would you like to reset the score? (y/n) ").strip().lower()
			while reset != "y" and reset != "n":
				print("Invalid response. Please try again.")
				reset = input("Would you like to reset the score? (y/n) ").strip().lower()
			if reset == "y":
				player_win = 0
				computer_win = 0
				print("Score Reset!")
				
		choices = get_choices_remix()
		result, player_win, computer_win = check_win_remix(choices["player"], choices["computer"], player_win, computer_win)
		print(result)
		print(f"Score: You: {player_win} Computer: {computer_win}")
		play_again = input("Play again? (y/n)").strip().lower()
		while play_again != "y" and play_again != "n":
				print("Invalid input. Please try again.")
				play_again = input("Play again? (y/n)").strip().lower()
