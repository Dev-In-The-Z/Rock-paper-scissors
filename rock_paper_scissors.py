import random #imports the random archive to randomize the computers choice

def get_choices(): #function to get both players choices
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, scissors):")
    while player_choice not in options: #checks if players input is within choices
        print("Invalid answer, please try again!")
        player_choice = input("Enter a choice (rock, paper, scissors):")
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer": computer_choice}
    return choices
    
player_win = 0 #starting scores for the game
computer_win = 0

def check_win(player, computer, player_win, computer_win): #function to check who won the match
    print(f"You chose {player}, computer chose {computer}.")
    if player == computer:
        return "It's a tie!", player_win, computer_win
    elif player == "rock": 
        if computer == "scissors":
            player_win += 1
            return "You win!", player_win, computer_win
        else: 
            computer_win += 1
            return "You lose!", player_win, computer_win
    elif player == "paper":
        if computer == "rock":
            player_win += 1
            return "You win!", player_win, computer_win
        else: 
            computer_win += 1
            return "You lose!", player_win, computer_win
    elif player == "scissors":
        if computer == "paper":
            player_win += 1
            return "You win!", player_win, computer_win
        else: 
            computer_win += 1
            return "You lose!", player_win, computer_win
    
play_again = "y"   

while play_again == "y": #Loops game till player choses "n"
    choices = get_choices()
    result, player_win, computer_win = check_win(choices["player"], choices["computer"], player_win, computer_win)
    print(result)
    print(f"Score: You: {player_win} Computer: {computer_win}")
    play_again = input("Play again? (y/n)")
