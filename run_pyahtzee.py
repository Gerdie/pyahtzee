from random import randint

def how_many_users():
    y = 0
    while y == 0:
        players = (raw_input("How many players? \n > "))
        if players.isdigit():
            players = int(players)
            if players <= 0:
                print "Please enter a number greater than 0"
            else:
                return players
        else:
            print "Please enter a number."

how_many_users()

score_display = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Three of a Kind", "Four of a kind", "Full House", "Small Straight (Sequence of 4)", "Large Straight (Sequence of 5)", "Yahtzee", "Chance"]

scoreboard = {}

def populate_scoreboards():
    #for x in range(players): *want to clone scorecard per player*
    for i in score_display:
        if i == "Yahtzee":
            scoreboard[i] = ["null"]
        else:
            scoreboard[i] = "null"
    return scoreboard

populate_scoreboards()

if "null" in scoreboard:
	for each in range(players):
	    def turn():
	        dice = []
            status = 1 #which turn they're on
	        def roll():
	            if dice = []: #first roll
	                # generate 5 random #s from 1-6 
                    # store #s in dice
	                    print dice
	                    status += 1
	                    #user input: roll again?
	                    #if yes:
	                        roll()
	                    #if no:
	                        #user input: how would you like to score this roll?"
	                        #interpret score category
	                        #store result of scoring algorithm in dictionary (will replace "null")
	            else: #2nd, 3rd rolls
	                #user input: which dice to re-roll? convert input to integers
	                #remove selected integers from dice array
	                #generate replacement random #s
	                #append replacement #s to dice array
	                print dice
	                status += 1
	                if status <= 3:
	                    #user input: roll again?
	                    #if yes:
	                        roll()
	                    #if no:
	                        #user input: how would you like to score this roll?"
	                        #interpret score category
	                        #store result of scoring algorithm in dictionary (will replace "null")
	                else:
	                    #user input: how would you like to score this roll?"
	                    #interpret score category
	                    #store result of scoring algorithm in dictionary (will replace "null")
	                