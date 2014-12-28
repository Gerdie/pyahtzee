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

score_display = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "Three of a Kind", "Four of a kind", "Full House", "Small Straight (Sequence of 4)", "Large Straight (Sequence of 5)", "Yahtzee", "Chance"]

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

def score_roll():
    category = raw_input("How do you want to score this roll? ")
    print "Categories are: ", score_display
    if category in scoreboard:
        if scoreboard[category] == "null":
            if category == "Aces":
                result = 0
                for x in dice:
                    if x == 1:
                        result += x
                scoreboard["Aces"] = result
            elif category == "Twos":
                result = 0
                for x in dice:
                    if x == 2:
                        result += x
                scoreboard["Twos"] = result
            elif category == "Threes":
                result = 0
                for x in dice:
                    if x == 3:
                        result += x
                scoreboard["Threes"] = result
            elif category == "Fours":
                result = 0
                for x in dice:
                    if x == 4:
                        result += x
                scoreboard["Fours"] = result
            elif category == "Fives":
                result = 0
                for x in dice:
                    if x == 5:
                        result += x
                scoreboard["Fives"] = result
            elif category == "Sixes":
                result = 0
                for x in dice:
                    if x == 6:
                        result += x
                scoreboard["Sixes"] = result
            elif category == "Three of a Kind":
                result = 0
                for x in dice:
                    if dice.count(x) >= 3:
                        result = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
                scoreboard["Three of a Kind"] = result
            elif category == "Four of a Kind":
                result = 0
                for x in dice:
                    if dice.count(x) >= 4:
                        result = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
                scoreboard["Four of a Kind"] = result
            elif category == "Small Straight (Sequence of 4)":
                result = 0
                for x in dice:
                    if dice.count(x) > 1:
                        dice.remove(x)
                if dice.sort() == [1, 2, 3, 4]:
                    result = 30
                elif dice.sort() == [2, 3, 4, 5]:
                    result = 30
                elif dice.sort() == [1, 2, 3, 4, 5]:
                    result = 30
                scoreboard["Small Straight (Sequence of 4)"] = result
            elif category == "Large Straight (Sequence of 5)":
                result = 0
                if dice.sort() == [1, 2, 3, 4, 5]:
                    result = 40
                scoreboard["Large Straight (Sequence of 5)"] = result
            else:
                scoreboard["Chance"] = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
        elif category == "Yahtzee":
            result = 0
            if scoreboard["Yahtzee"] == ["null"]:
                if dice.count(dice[0]) == 5:
                     result = 50
                scoreboard["Yahtzee"] = [result]
            elif scoreboard["Yahtzee"] == [0]:
                print "You have already scored a 0 in Yahtzee. Please choose another category."
                score_roll()
            else:
                if dice.count(dice[0]) == 5:
                    scoreboard["Yahtzee"].append(100)
            print "Your score for %s is " %(category), result
        else:
            print "You have already scored this category. Please choose another category."
            score_roll()
    else:
        print "Please enter a valid category."
        score_roll()
    

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
	                