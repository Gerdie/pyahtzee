pyahtzee
========

Program outline:

1. 	User input = How many players?
	store integer in players

2. 	Create scoreboard dictionary for each player
	Indexes = score categories like "Ones", "Three of a Kind", "Yahtzee", etc.
	Values = "null" EXCEPT scoreboard["Yahtzee"]
	scoreboard["Yahtzee"] = ["null"]
	
3. Create scoring algorithm for each category, reading results of dice array
	
4. 	Set up:

	if "null" in scoreboard:
	    for each in range(player):
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
	                
