from random import randint

scoreboard = {}
dice = []
score_display = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "Three of a Kind", "Four of a Kind", "Full House", "Small Straight (Sequence of 4)", "Large Straight (Sequence of 5)", "Yahtzee", "Chance"]
bonus_count = 0

def how_many_users():
    y = 0
    while y == 0:
        players = (raw_input("How many players? \n > "))
        if players.isdigit():
            players = int(players)
            if players <= 0:
                print "Please enter a number greater than 0"
            else:
                y = 1
        else:
            print "Please enter a number."
    return players

def populate_scoreboards():
    for i in score_display:
        scoreboard[i] = []
        for x in range(players): #want to clone scorecard per player*
            if i == "Yahtzee":
                scoreboard[i].append(["null"])
            else:
                scoreboard[i].append("null")
    return scoreboard

def small_score(dice, y):
	result = 0
	for x in dice:
		if x == y:
			result += x
	return result

def score_roll(players, dice):
	scoring = 0
	while scoring == 0:
		print "pass 1/6 ", scoring
		category = raw_input("How do you want to score this roll? ")
		print category
		print "Categories are: ", score_display
		if category not in scoreboard:
			print "Please enter a valid category."
		elif category == "Yahtzee":
				temp = scoreboard[category]
				result = 0
                if temp[players] == ["null"]:
                    if dice.count(dice[0]) == 5:
                         result = 50
                    temp[players] = result
                    scoreboard["Yahtzee"] = temp
                    return category
                    scoring = 1
                elif temp[players] == [0]:
                    print "You have already scored a 0 in Yahtzee. Please choose another category."
                else:
                    if dice.count(dice[0]) == 5:
                        temp2 = temp[players]
                        temp2.append(100)
                        temp[players] = temp2
                        scoreboard["Yahtzee"] = temp
                        bonus_count += 1
                        print "Congratulations, you scored a bonus Yahtzee! Take an extra turn."
                        category = "bonus"
                        return category
                    else: 
                        print "You don't have a Yahtzee. Please choose another category."
		elif temp[players] == "null":
			print "pass 2"
			if category == "Aces":
				result = 0
				for x in dice:
					if x == 1:
						result += x
				print result
				temp[players] = result
				scoreboard["Aces"] = temp
				print "pass 3 ", scoreboard
				return category
				print "pass 4 ", scoring
				scoring = 1
				print "pass 5 ", scoring
			elif category == "Twos":
				result = 0
				for x in dice:
					if x == 2:
						result += x
				temp[players] = result
				scoreboard["Twos"] = temp
				return category
				scoring = 1
			elif category == "Threes":
				result = 0
				for x in dice:
					if x == 3:
						result += x
				temp[players] = result
				scoreboard["Threes"] = temp
				return category
				scoring = 1
			elif category == "Fours":
				result = 0
				for x in dice:
					if x == 4:
						result += x
				temp[players] = result
				scoreboard["Fours"] = temp
				return category
				scoring = 1
			elif category == "Fives":
				result = 0
				for x in dice:
					if x == 5:
						result += x
				temp[players] = result
				scoreboard["Fives"] = temp
				return category
				scoring = 1
			elif category == "Sixes":
				result = 0
				for x in dice:
					if x == 6:
						result += x
				temp[players] = result
				scoreboard["Sixes"] = temp
				return category
				scoring = 1
			elif category == "Three of a Kind":
				result = 0
				for x in dice:
					if dice.count(x) >= 3:
						result = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
				temp[players] = result
				scoreboard["Three of a Kind"] = temp
				return category
				scoring = 1
			elif category == "Four of a Kind":
				result = 0
				for x in dice:
					if dice.count(x) >= 4:
						result = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
				temp[players] = result
				scoreboard["Four of a Kind"] = temp
				return category
				scoring = 1
			elif category == "Full House":
				result = 0
				dice.sort()
				if dice.count(dice[0]) == 2 and dice.count(dice[2]) == 3:
					result = 25
				elif dice.count(dice[4]) == 2 and dice.count(dice[0]) == 3:
					result = 25
				temp[players] = result
				scoreboard["Full House"] = temp
				return category
				scoring = 1
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
				temp[players] = result
				scoreboard["Small Straight (Sequence of 4)"] = temp
				return category
				scoring = 1
			elif category == "Large Straight (Sequence of 5)":
				result = 0
				dice.sort()
				if dice == [1, 2, 3, 4, 5]:
					result = 40
				elif dice == [2, 3, 4, 5, 6]:
					result = 40
				temp[players] = result
				scoreboard["Large Straight (Sequence of 5)"] = temp
				return category
				scoring = 1
			else:
				result = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
				temp[players] = result
				scoreboard["Chance"] = temp
				return category
				scoring = true
		else:
			print "You have already scored this category. Please choose another category."
        
def roll():
    dice = []
    status = 0
    while status < 3:
        status += 1
        existing = len(dice)
        for x in range(5 - existing):
            i = randint(1, 6)
            dice.append(i)
        print "You rolled: ", dice[existing:]
        print "Here are your dice: ", dice
        if status < 3:
            if raw_input("Roll again? Y/N: ") == "N":
                status = 3
            else:
                discards = raw_input("Which dice do you want to re-roll? 1, 2, 3, etc. ")
                discard_list = []
                for y in discards:
                    if y.isdigit():
                        discard_list.append(int(y))
                for x in discard_list:
                    if x in dice:
                        dice.remove(x)
    return dice
	                
def final_score(person):
    x = scoreboard["Aces"[person]] + scoreboard["Twos"[person]] + scoreboard["Threes"[person]] + scoreboard["Fours"[person]] + scoreboard["Fives"[person]] + scoreboard["Sixes"[person]]
    if x >= 63:
        x += 35
    x += scoreboard["Three of a Kind"[person]] + scoreboard["Four of a Kind"[person]] + scoreboard["Full House"[person]] + scoreboard["Small Straight (Sequence of 4)"[person]] + scoreboard["Large Straight (Sequence of 5)"[person]] + scoreboard["Chance"[person]]
    for i in scoreboard["Yahtzee"[person]]:
        x += i
    print "Your final score is:", x

def turn(players):
    dice = roll()
    score_roll(players, dice)
    
players = how_many_users()
#print "You entered ", players, " players"
populate_scoreboards()
#print scoreboard
null_count = len(score_display) * players

while null_count > 0:
    for x in range(players):
        print "Your turn, Player", x + 1
        turn(x)
        null_count -= 1
winner = {}
for y in range(players):
    print "Player %r, your score is:" % (y + 1), final_score(y)
    """winner[each + 1] = final_score(each)
winner.sort()"""
print "Game Over!"


"""for category in scoreboard:
    if "null" in scoreboard[category]:
        for each in range(players):
            #loop works to here
            for category2 in scoreboard:
                print "scoreboard searched for category2", category2
                if scoreboard[category2[each]] == "null" or scoreboard[category2[each]] == ["null"]: 
                    print "Your turn, Player", each + 1
                    turn(each)
                else:
                    pass
    else:"""
#4. add winner function / ranking function
    
	                