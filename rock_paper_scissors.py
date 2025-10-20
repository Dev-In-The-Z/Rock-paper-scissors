import random #imports the random archive to randomize the computers choice

def get_choices_classic(): #function to get both players choices for classic
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, scissors):").strip().lower()
    while player_choice not in options: #checks if players input is within choices
        print("Invalid answer, please try again!")
        player_choice = input("Enter a choice (rock, paper, scissors):").strip().lower()
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer": computer_choice}
    return choices
    
def get_choices_remix(): #function to get both players choices for remix
    options = ["rock", "paper", "scissors", "lizard", "spock"]
    player_choice = input("Enter a choice (rock, paper, scissors, lizard, spock):").strip().lower()
    while player_choice not in options: #checks if players input is within choices
        print("Invalid answer, please try again!")
        player_choice = input("Enter a choice (rock, paper, scissors, lizard, spock):").strip().lower()
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer": computer_choice}
    return choices
    
player_win = 0 #starting scores for the game
computer_win = 0

def check_win_classic(player, computer, player_win, computer_win): #function to check who won the match for classic
    print(f"You chose {player}, computer chose {computer}.")
    if player == computer:
        return "It's a tie!", player_win, computer_win
    elif player == "rock":  
        if computer == "scissors":
            player_win += 1
            return "Rock smashes scissors. You win!", player_win, computer_win
        else: 
            computer_win += 1
            return "Paper covers rock. You lose!", player_win, computer_win
    elif player == "paper":
        if computer == "rock":
            player_win += 1
            return "Paper covers rock. You win!", player_win, computer_win
        else: 
            computer_win += 1
            return "Scissors cut paper. You lose!", player_win, computer_win
    elif player == "scissors":
        if computer == "paper":
            player_win += 1
            return "Scissors cut paper. You win!", player_win, computer_win
        else: 
            computer_win += 1
            return "Rock smashes scissors. You lose!", player_win, computer_win

def check_win_remix(player, computer, player_win, computer_win): #function to check who won the match
    print(f"You chose {player}, computer chose {computer}.")
    if player == computer:
        return "It's a tie!", player_win, computer_win
        
    elif player == "rock": 
        if computer == "scissors":
            player_win += 1
            return "Rock smashes scissors. You win!", player_win, computer_win
        if computer == "lizard":
            player_win += 1
            return "Rock crushes lizard. You Win", player_win, computer_win
        if computer == "spock":
            computer_win += 1
            return "Spock vaporizes rock. You lose!", player_win, computer_win
        else: 
            computer_win += 1
            return "Paper covers rock. You lose!", player_win, computer_win
            
    elif player == "paper":
        if computer == "rock":
            player_win += 1
            return "Paper covers rock. You win!", player_win, computer_win
        if computer == "spock":
            player_win += 1
            return "Paper disproves Spock. You win!", player_win, computer_win
        if computer == "lizard":
            computer_win+= 1 
            return "Lizard eats paper. You lose!", player_win, computer_win
        else: 
            computer_win += 1
            return "Scissors cut paper. You lose!", player_win, computer_win
            
    elif player == "scissors":
        if computer == "paper":
            player_win += 1
            return "Scissors cut paper. You win!", player_win, computer_win
        if computer == "lizard":
            player_win += 1
            return "Scissors decapitates lizard. You win!", player_win, computer_win
        if computer == "spock":
            computer_win += 1
            return "Spock smashes scissors. You lose!", player_win, computer_win
        else: 
            computer_win += 1
            return "Rock crushes scissors. You lose!", player_win, computer_win
            
    elif player == "lizard":
        if computer == "spock":
            player_win += 1
            return "Lizard poisons Spock. You win!", player_win, computer_win
        if computer == "paper":
            player_win += 1
            return "Lizard eats paper. You win!", player_win, computer_win
        if computer == "scissors":
            computer_win += 1
            return "Scissors decapitates lizard. You lose!", player_win, computer_win
        else:
            computer_win += 1
            return "Rock crushes lizard. You lose!", player_win, computer_win
    elif player == "spock":
        if computer == "scissors":
            player_win += 1
            return "Spock smashes scissors. You win!", player_win, computer_win
        if computer == "rock":
            player_win += 1
            return "Spock vaporizes rock. You win!", player_win, computer_win
        if computer == "lizard":
            computer_win += 1
            return "Lizard poisons Spock. You lose!", player_win, computer_win
        else:
            computer_win += 1
            return "Paper disproves Spock. You lose!", player_win, computer_win
            
version = input("Which version would you like to play? Classic or remix? ").strip().lower() #checks which version the player wants to play
while version != "classic" and version != "remix":
    print("Invalid input. Please try again.")
    version = input("Which version would you like to play? Classic or remix? ").strip().lower()
    
if version == "classic": #plays classic mode
    play_again = "y"   

    while play_again == "y": #Loops game till player choses "n"
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
        choices = get_choices_remix()
        result, player_win, computer_win = check_win_remix(choices["player"], choices["computer"], player_win, computer_win)
        print(result)
        print(f"Score: You: {player_win} Computer: {computer_win}")
        play_again = input("Play again? (y/n)").strip().lower()
        while play_again != "y" and play_again != "n":
                print("Invalid input. Please try again.")
                play_again = input("Play again? (y/n)").strip().lower()
