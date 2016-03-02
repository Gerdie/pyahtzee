def small_score(dice, y):
	result = 0
	for x in dice:
		if x == y:
			result += x
	return result

score_display = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "Three of a Kind", "Four of a Kind", "Full House", "Small Straight (Sequence of 4)", "Large Straight (Sequence of 5)", "Yahtzee", "Chance"]
dice = [5, 1, 5, 4, 5]
players = 1
scoreboard = {}

def populate_scoreboards():
    for i in score_display:
        scoreboard[i] = []
        for x in range(players): #want to clone scorecard per player*
            if i == "Yahtzee":
                scoreboard[i].append(["null"])
            else:
                scoreboard[i].append("null")
    return scoreboard

def score_roll(players, dice):
	scoring = 0
	while scoring == 0:
		print "Categories are: ", score_display
		category = raw_input("How do you want to score this roll? ")
		if category not in scoreboard:
			print "Please enter a valid category."
		else:
			temp = scoreboard[category]
			if temp[players - 1] == "null":
				if category == "Aces":
					temp[players - 1] = small_score(dice, 1)
					scoreboard[category] = temp
					scoring = 1
					return category
				elif category == "Twos":
					temp[players - 1] = small_score(dice, 2)
					scoreboard[category] = temp
					scoring = 1
					return category
				elif category == "Threes":
					temp[players - 1] = small_score(dice, 3)
					scoreboard[category] = temp
					scoring = 1
					return category
				elif category == "Fours":
					temp[players - 1] = small_score(dice, 4)
					scoreboard[category] = temp
					scoring = 1
					return category
				elif category == "Fives":
					temp[players - 1] = small_score(dice, 5)
					scoreboard[category] = temp
					scoring = 1
					return category
				elif category == "Sixes":
					temp[players - 1] = small_score(dice, 6)
					scoreboard[category] = temp
					scoring = 1
					return category
				elif category == "Three of a Kind":
					result = 0
					for x in dice:
						if dice.count(x) >= 3:
							result = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
					temp[players - 1] = result
					scoreboard["Three of a Kind"] = temp
					scoring = 1
					return category
				elif category == "Four of a Kind":
					result = 0
					for x in dice:
						if dice.count(x) >= 4:
							result = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
					temp[players - 1] = result
					scoreboard["Four of a Kind"] = temp
					scoring = 1
					return category
				elif category == "Full House":
					result = 0
					dice.sort()
					if dice.count(dice[0]) == 2 and dice.count(dice[2]) == 3:
						result = 25
					elif dice.count(dice[4]) == 2 and dice.count(dice[0]) == 3:
						result = 25
					temp[players - 1] = result
					scoreboard["Full House"] = temp
					scoring = 1
					return category
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
					temp[players - 1] = result
					scoreboard["Small Straight (Sequence of 4)"] = temp
					scoring = 1
					return category
				elif category == "Large Straight (Sequence of 5)":
					result = 0
					dice.sort()
					if dice == [1, 2, 3, 4, 5]:
						result = 40
					elif dice == [2, 3, 4, 5, 6]:
						result = 40
					temp[players - 1] = result
					scoreboard["Large Straight (Sequence of 5)"] = temp
					scoring = 1
					return category
				else:
					result = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
					temp[players - 1] = result
					scoreboard["Chance"] = temp
					scoring = 1
					return category
			elif category == "Yahtzee":
				if temp[players - 1] == ["null"]:
					if dice.count(dice[0]) == 5:
						result = 50
					else:
						result = 0
					temp[players - 1] = [result]
					scoreboard["Yahtzee"] = temp
					scoring = 1
					return category
				elif temp[players - 1] == [0]:
					print "You have already scored a 0 in Yahtzee. Please choose another category."
				else:
					if dice.count(dice[0]) == 5:
						entire = temp[players - 1]
						entire.append(100)
						temp[players - 1] = entire
						print "Congratulations, you scored a bonus Yahtzee! Take an extra turn."
					else: 
						print "You don't have a Yahtzee. Please choose another category."
			else:
				print "You have already scored this category. Please choose another category."

populate_scoreboards()
print scoreboard
print dice
score_roll(players, dice)
print scoreboard
dice = [5, 5, 5, 5, 5]
score_roll(players, dice)
print scoreboard
score_roll(players, dice)
print scoreboard

