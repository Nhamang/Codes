import random as rand

computerHands = ["rock", "paper", "scissors", "lizard", "spock"]
computerNum = rand.randrange(2)

def playRound(p1Hand, p2Hand):
    print("Player 1: ", p1Hand, " Player 2: ", p2Hand, " Winner: ", end='')
	
	'''
	Finds the winner or if draw. rules are: 
	Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard 
	Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard 
	Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock 
	(and as it always has) Rock crushes Scissors
	'''
	
    if((p1Hand == 'scissors' and (p2Hand == 'paper' or p2Hand == 'lizard')) or 
    (p1Hand == 'paper' and (p2Hand == 'rock' or p2Hand == 'spock')) or
    (p1Hand == 'rock' and (p2Hand == 'lizard' or p2Hand == 'scissors')) or
    (p1Hand == 'lizard' and (p2Hand == 'spock' or p2Hand == 'paper')) or
    (p1Hand == 'spock' and (p2Hand == 'scissors' or p2Hand == 'rock'))):
        print("Player 1")
        return 1
    elif((p2Hand == 'scissors' and (p1Hand == 'paper' or p1Hand == 'lizard')) or 
    (p2Hand == 'paper' and (p1Hand == 'rock' or p1Hand == 'spock')) or
    (p2Hand == 'rock' and (p1Hand == 'lizard' or p1Hand == 'scissors')) or
    (p2Hand == 'lizard' and (p1Hand == 'spock' or p1Hand == 'paper')) or
    (p2Hand == 'spock' and (p1Hand == 'scissors' or p1Hand == 'rock'))):
        print("Player 2")
        return 2
    else:
        print("Draw")
        return 0

		
#Starts a singleplayer game
def playSingle():
    
    playerWins = 0
    computerWins = 0
    print("Player 2 is a computer")
    
	#Run's game as long as the player wishes to play
    while True:
        user = str(input("Choose hand rock/paper/scissors/lizard/spock or stop: "))
        user = user.lower()
        
		#Stops the game when correct input is given
		if(user == 'stop'):
            if(input("Are you sure you wish to end the game y/n?: ").lower() == 'y'):
                break;
            
        user = checkInput(user)
        outcome = playRound(user, computerHands[rand.randrange(3)])
        
        if(outcome == 1):
            playerWins += 1
        elif(outcome == 2):
            computerWins += 1
    
	#Prints the winner of all the games
    if(playerWins > computerWins):
        print("Player beat computer with: ", playerWins, "-", computerWins)
    elif(playerWins < computerWins):
        print("Player lost to computer with: ", playerWins, "-", computerWins)
    else:
        print("It was a draw with: ", playerWins, "-", computerWins)

		
#Starts a multiplayer game
def playGameMulti():
    
    player1Wins = 0
    player2Wins = 0
	
	#Let's the game run for as long as the user wishes to play
    while True:
        player1 = str(input("Player 1 choose hand rock/paper/scissors/lizard/spock or stop: "))
    
		#Stops game if player 1 gives the correct input
        if(player1.lower() == 'stop'):
            if(input("Are you sure you wish to end the game y/n?: ").lower() == 'y'):
                break;
            
        player1 = checkInput(player1.lower())
        cleanScreen()
    
        player2 = str(input("Player 2 choose hand rock/paper/scissors/lizard/spock: "))
        player2 = checkInput(player2.lower())
    
        outcome = playRound(player1, player2)
        
		#Adds score to winners score
        if(outcome == 1):
            player1Wins += 1
        elif(outcome == 2):
            player2Wins += 1

	#Prints the winner of all the games
    if(player1Wins > player2Wins):
        print("Player 1 beat Player 2 with: ", player1Wins, "-", player2Wins)
    elif(player1Wins < player2Wins):
        print("Player 2 beat Player 1 with: ", player2Wins, "-", player1Wins)
    else:
        print("It was a draw with: ", player1Wins, "-", player2Wins)

#Cleans the screen so player 2 cant see what player 1 enters
def cleanScreen():
    for i in range(0, 50):
        print("")
        
#Checks that the users input is a valid one
def checkInput(playerInput):
    playerOutput = playerInput
    while True:
        if playerOutput in computerHands:
            break;
        else:
            playerOutput = input("Choose hand rock/paper/scissors/lizard/spock: ")
            playerOutput = playerOutput.lower()
    
    return playerOutput
    

noPlayer = input("Singleplayer(s) or Multiplayer(M)?: ")
noPlayer = noPlayer.lower()

if(noPlayer == 'm'):
    playGameMulti()
else:
    playSingle()
