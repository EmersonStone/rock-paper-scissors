
import random #import random to help the computer generate a random move
import time #allows us to add time between prompts to make it more readable when played


def move_submit(): #defines our function of rock paper scissors


    print("Welcome to the classic game of Rock Paper Scissors!") #welcomes player
    time.sleep(1) #adds a 1 second pause
    name = input ("What is your name?\n") #asks the player for their name
    print(f"Welcome {name}!") #prints welcome and then player name
    time.sleep(1.5) #adds a 1.5 second pause
    Ready_name = input("Are you familiar with the classic rules of Rock Paper Scissors?\n") #asks if the player is familiar with the rules of the game
    

    while Ready_name not in ["yes", "y", "yeah", "sure","yea","Yes","YES","yuh","YUH","Yeah","YEAH","yep","Yep","Sure","SURE"]: # if the player doesnt answer that their familier with the rules, prints instructions
        
        print("Well then here is how Rock Paper Scissors works...") #instructions
        time.sleep(2.4)  #adds a 2.4 second pause
        print("Rock Paper Scissors is classically played between 2 players.") #instructions
        time.sleep(2.4)#adds a 2.4 second pause
        print("Both players have three choices of moves, Those moves are Rock, Paper, or Scissors.") #instructions
        time.sleep(2.4)#adds a 2.4 second pause
        print("Mathmatically this game leaves a random winner. Both players will chose a move.") #instructions
        time.sleep(2.4)#adds a 2.4 second pause
        print("Those moves will go against eachother and a winner will be determined.") #instructions
        time.sleep(2.4)#adds a 2.4 second pause
        print("In this game, Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.") #instructions
        time.sleep(2.4)#adds a 2.4 second pause

        Ready_name = input ("Now that you know how this game is played, Are you ready to play?\n") #asks if the player is now ready to start
        


    print("Awesome! Then lets get started!") #Says lets start
    time.sleep(2) #adds a 2 second pause


    Winner = False #sets up a true false statement to see if a winner has been had yet


    while Winner == False: #while loop saying if their isnt a winner, then run.
        print("Would you like to play Rock, Paper, or Scissors!\n") #asks player for their move
        time.sleep(0.5) #adds 0.5 second pause
        player_move = input ("Your Move:") #prompts for players move
        
        PM = 0 #sets player move to 0 or not yet a valid move
        PMW = ("") #sets their move word to nothing yet
        if player_move in ["Rock","rock","R","r","ROCK","rox"]: #if players move is in these options, set their word to Rock! and move number to 1 which we use as rock
            PMW = ("Rock!")
            PM = 1
        elif player_move in ["Paper","paper","P","p","PAPER"]: #if players move is in these options, set their word to Paper! and move number to 2 which we use as paper
            PMW = ("Paper!")
            PM = 2
        elif player_move in ["Scissors","scissors","S","s","SCISSORS"]: #if players move is in these options, set their word to Scissors! and move number to 3 which we use as scissors
            PMW = ("Scissors!")
            PM = 3
        elif player_move not in [""]: #if the players move isnt in these lists, then their move is invalid and will wait or continue until a valid move is entered
            continue
        

        print(f"You choose to play {player_move}!") #confirms what move was chosen
        time.sleep(2) #adds a 2 second pause
        print("Lets see who wins!") #prompts the game start to see who will win


        time.sleep(2) #adds a 2 second pause
        print("Rock!") #prints game chant 
        time.sleep(1) #adds a 1 second pause
        print("Paper!")#prints game chant 
        time.sleep(1) #adds a 1 second pause
        print("Scissors!")#prints game chant 
        time.sleep(1) #adds a 1 second pause
        print("Shoot!\n")#prints game chant 
        time.sleep(1) #adds a 1 second pause


        CM = 0 #sets computer move number to 0 or nothing
        CMW = ("") #sets computer move word to nothing yet
        computer_random = random.randint(1,3) #makes computer choose a random number between 1, 2, and 3.
        if computer_random == 1: #if computer chooses 1 or rock we print the computers move word as Rock and set its computer move number to 1
            CMW = ("Rock!")
            CM = 1
        elif computer_random == 2: #if computer chooses 2 or paper we print the computers move word as Paper and set its computer move number to 2
            CMW = ("Paper!")
            CM = 2
        elif computer_random == 3: #if computer chooses 3 or scissor we print the computers move word as Scissors and set its computer move number to 3
            CMW = ("Scissors!")
            CM = 3
        

        print(f"You: {PMW}") #prints player move
        time.sleep(1) #adds a 1 second pause
        print(f"Computer: {CMW}") #prints computers move
        time.sleep(1) #adds a 1 second pause


        if PM == 1 and CM == 2: #If player move is rock and computers is paper, prints Computer Wins! and changes winner to true telling game to end because there is a winner 
            print("Computer Wins!")
            Winner = True
        elif PM == 2 and CM == 3: #If player move is paper and computers is scissors, prints Computer Wins! and changes winner to true telling game to end because there is a winner
            print("Computer Wins!")
            Winner = True
        elif PM == 3 and CM == 1: #If player move is scissors and rock is paper, prints Computer Wins! and changes winner to true telling game to end because there is a winner
            print("Computer Wins!")
            Winner = True
        elif PM == CM:
            print("Tie, Replay!")
            time.sleep(2) #adds a 2 second pause
        elif PM == 1 and CM == 3: #If player move is rock and computers is scissors, prints You Win! and changes winner to true telling game to end because there is a winner
            print("You Win!")
            Winner = True
        elif PM == 2 and CM == 1: #If player move is paper and computers is rock, prints You Win! and changes winner to true telling game to end because there is a winner
            print("You Win!")
            Winner = True
        elif PM == 3 and CM == 2: #If player move is scissors and computers is paper, prints You Win! and changes winner to true telling game to end because there is a winner
            print("You Win!")
            Winner = True

move_submit() #calls the function to be run