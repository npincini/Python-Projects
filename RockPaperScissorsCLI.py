import random #Python library for the random selection of the computer.

def Game(GameNumber, PlayerScore, ComputerScore): #Creating the game function to be recalled

    # Insert code for computer choice
    ComputerChoiceNum = (random.randrange(1, 4)) #Rock(1), Paper(2), Scissors(3). Use the random function to pick an option

    print("\n- - -\nGame:",GameNumber, "\n")
    print("Rock!\nPaper!\nScissors!\n")
    PlayerChoice = input("You picked, ") #ask for player input in the game

    #depending on PlayerChoice and ComputerScoreNum, selects outcome
    if (PlayerChoice == "Rock" or PlayerChoice == "rock" or PlayerChoice == "rock!" or PlayerChoice == "Rock!"):
        if ComputerChoiceNum == 1:
            print("\nThe computer played Rock.\nIt's a tie!\n")
        elif ComputerChoiceNum == 2:
            print("\nThe Computer played Paper.\nYou lost!\n")
            ComputerScore = ComputerScore + 1
        elif ComputerChoiceNum == 3:
            print("\nThe Computer played Scissors.\nYou win!\n")
            PlayerScore = PlayerScore + 1

    elif (PlayerChoice == "Paper" or PlayerChoice == "paper" or PlayerChoice == "paper!" or PlayerChoice == "Paper!"):
        if ComputerChoiceNum == 2:
            print("\nThe Computer played Paper.\nIt's a tie!\n")
        elif ComputerChoiceNum == 3:
            print("\nThe Computer played Scissors.\nYou lost!\n")
            ComputerScore = ComputerScore + 1
        elif ComputerChoiceNum == 1:
            print("\nThe Computer played Rock.\nYou win!")
            PlayerScore = PlayerScore + 1

    elif (PlayerChoice == "Scissors" or PlayerChoice == "scissors" or PlayerChoice == "Scissors!" or PlayerChoice == "scissors!" or PlayerChoice == "Scissor" or PlayerChoice == "scissor" or PlayerChoice == "Scissor!" or PlayerChoice == "scissor!"):
        if ComputerChoiceNum == 3:
            print("\nThe Computer played Scissors.\nIt's a tie!\n")
        elif ComputerChoiceNum == 1:
            print("\nThe Computer played Rock.\nYou lost!\n")
            ComputerScore = ComputerScore + 1
        elif ComputerChoiceNum == 2:
            print("\nThe Computer played Paper.\nYou win!\n")
            PlayerScore = PlayerScore + 1

    else:
        print("Yeah, either you can't spell or that object isn't in the rulebook! I reckon that counts as a win for the Computer!\n") #Code can't read user input so adjust for mistake
        ComputerScore = ComputerScore + 1

    print("The score is now:\nYou (" , PlayerScore , ") - (" , ComputerScore , ") Computer\n")

    GameAgain = input("Would you like to play again? [y/n]")
    if GameAgain == "y" or GameAgain == "": #if "y" or ENTER is pressed then continue
        GameNumber = GameNumber + 1
        Game(GameNumber, PlayerScore, ComputerScore) #Call the fame function again for a new one
    else:
        print("\nWell I guess that's a no then! You played", GameNumber, "game(s) and the final score was:\nYou (" , PlayerScore , ") - (" , ComputerScore , ") Computer")
        EndGame = input("[Press Enter to end the game]")
        exit()

# ----------------------------------------------
# Start of Game setting variables for setup and calling the Game function
GameNumber = 1
PlayerScore = 0
ComputerScore = 0
print("Welcome to Rock / Paper / Scissors \nLet the game begin!")
StartGame = input("[Press Enter to begin the game]")
Game(GameNumber, PlayerScore, ComputerScore)
