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

score_display = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "Three of a Kind", "Four of a Kind", "Full House", "Small Straight (Sequence of 4)", "Large Straight (Sequence of 5)", "Yahtzee", "Chance"]

scoreboard = {}

dice = []

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
            elif category == "Full House":
                result = 0
                dice.sort()
                if dice.count(dice[0]) == 2 and dice.count(dice[2]) == 3:
                    result = 25
                elif dice.count(dice[4]) == 2 and dice.count(dice[0]) == 3:
                    result = 25
                scoreboard["Full House"] = result
            elif category == "Small Straight (Sequence of 4)":
                result = 0
                dice.sort()
                for x in dice:
                    if dice.count(x) > 1:
                        dice.remove(x)
                if dice == [1, 2, 3, 4]:
                    result = 30
                elif dice == [2, 3, 4, 5]:
                    result = 30
                elif dice == [1, 2, 3, 4, 5]:
                    result = 30
                elif dice == [2, 3, 4, 5, 6]:
                    result = 30
                scoreboard["Small Straight (Sequence of 4)"] = result
            elif category == "Large Straight (Sequence of 5)":
                result = 0
                dice.sort()
                if dice == [1, 2, 3, 4, 5]:
                    result = 40
                elif dice == [2, 3, 4, 5, 6]:
                    result = 40
                scoreboard["Large Straight (Sequence of 5)"] = result
            else:
                result = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
                scoreboard["Chance"] = result
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
                else: 
                    print "You don't have a Yahtzee. Please choose another category."
                    score_roll()
        else:
            print "You have already scored this category. Please choose another category."
            score_roll()
    else:
        print "Please enter a valid category."
        score_roll()
        
def roll():
    status = 0
    if status < 3:
        status += 1
        existing = len(dice)
	    for x in range(5 - existing):
	        i = randint(1, 6)
	        dice.append(i)
	    print "You rolled: ", dice[existing:]
	    print "Here are your dice: ", dice
	    if status < 3:
	        if raw_input("Roll again? Y/N: ") == "N":
	            break
	    else: 
	        discards = raw_input("Which dice do you want to re-roll? 1, 2, 3, etc.")
	        discard_list = []
	        for y in discards:
	            if y != " " and y != ",":
	                discard_list.append(int(y))
	        for x in discard_list:
	            if x in dice:
	                dice.remove(x)
	                
def final_score():
    x = scoreboard["Aces"] + scoreboard["Twos"] + scoreboard["Threes"] + scoreboard["Fours"] + scoreboard["Fives"] + scoreboard["Sixes"]
    if x >= 63:
        x += 35
    x += scoreboard["Three of a Kind"] + scoreboard["Four of a Kind"] + scoreboard["Full House"] + scoreboard["Small Straight (Sequence of 4)"] + scoreboard["Large Straight (Sequence of 5)"] + scoreboard["Chance"]
    for i in scoreboard["Yahtzee"]:
        x += i
    print "Your final score is:", x

def turn():
    dice = []
    roll()
    score_roll()
    
how_many_users()

if "null" in scoreboard:
	for each in range(players):
	    turn()
else:
    final_score()
    print "Game Over!"
    
	                