from random import randint

SCOREBOARD = {}
DICE = []
SCORE_DISPLAY = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "Three of a Kind", "Four of a Kind", "Full House", "Small Straight (Sequence of 4)", "Large Straight (Sequence of 5)", "Yahtzee", "Chance"]
BONUS_COUNT = 0

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
    for i in SCORE_DISPLAY:
        SCOREBOARD[i] = []
        for x in range(players):     # want to clone scorecard per player*
            if i == "Yahtzee":
                SCOREBOARD[i].append(["null"])
            else:
                SCOREBOARD[i].append("null")
    return SCOREBOARD


def small_score(DICE, y):
    result = 0
    for x in DICE:
        if x == y:
            result += x
        return result


def score_roll(players, DICE):
    scoring = 0
    while scoring == 0:
        print "pass 1/6 ", scoring
        category = raw_input("How do you want to score this roll? ")
        print category
        print "Categories are: ", SCORE_DISPLAY
        if category not in SCOREBOARD:
            print "Please enter a valid category."
        else:
            temp = SCOREBOARD[category]
            if category == "Yahtzee":
                result = 0
                if temp[players] == ["null"]:
                    if DICE.count(DICE[0]) == 5:
                        result = 50
                        temp[players] = result
                        SCOREBOARD["Yahtzee"] = temp
                        return category
                        scoring = 1
                    else:
                        print "You have scored a 0 in Yahtzee."
                        temp[players] = result
                        SCOREBOARD["Yahtzee"] = temp
                        return category
                        scoring = 1
                elif temp[players] == [0]:
                    print "You have already scored a 0 in Yahtzee. Please choose another category."
                else:
                    if DICE.count(DICE[0]) == 5:
                        temp2 = temp[players]
                        temp2.append(100)
                        temp[players] = temp2
                        SCOREBOARD["Yahtzee"] = temp
                        BONUS_COUNT += 1
                        print "Congratulations, you scored a bonus Yahtzee! Take an extra turn."
                        category = "bonus"
                        return category
                    else:
                        print "You don't have a Yahtzee. Please choose another category."
            elif temp[players] == "null":
                print "pass 2"
                if category == "Aces":
                    result = 0
                    for x in DICE:
                        if x == 1:
                            result += x
                    print result
                    temp[players] = result
                    SCOREBOARD["Aces"] = temp
                    print "pass 3 ", SCOREBOARD
                    return category
                    print "pass 4 ", scoring
                    scoring = 1
                    print "pass 5 ", scoring
                elif category == "Twos":
                    result = 0
                    for x in DICE:
                        if x == 2:
                            result += x
                    temp[players] = result
                    SCOREBOARD["Twos"] = temp
                    return category
                    scoring = 1
                elif category == "Threes":
                    result = 0
                    for x in DICE:
                        if x == 3:
                            result += x
                    temp[players] = result
                    SCOREBOARD["Threes"] = temp
                    return category
                    scoring = 1
                elif category == "Fours":
                    result = 0
                    for x in DICE:
                        if x == 4:
                            result += x
                    temp[players] = result
                    SCOREBOARD["Fours"] = temp
                    return category
                    scoring = 1
                elif category == "Fives":
                    result = 0
                    for x in DICE:
                        if x == 5:
                            result += x
                    temp[players] = result
                    SCOREBOARD["Fives"] = temp
                    return category
                    scoring = 1
                elif category == "Sixes":
                    result = 0
                    for x in DICE:
                        if x == 6:
                            result += x
                    temp[players] = result
                    SCOREBOARD["Sixes"] = temp
                    return category
                    scoring = 1
                elif category == "Three of a Kind":
                    result = 0
                    for x in DICE:
                        if DICE.count(x) >= 3:
                            result = DICE[0] + DICE[1] + DICE[2] + DICE[3] + DICE[4]
                    temp[players] = result
                    SCOREBOARD["Three of a Kind"] = temp
                    return category
                    scoring = 1
                elif category == "Four of a Kind":
                    result = 0
                    for x in DICE:
                        if DICE.count(x) >= 4:
                            result = DICE[0] + DICE[1] + DICE[2] + DICE[3] + DICE[4]
                    temp[players] = result
                    SCOREBOARD["Four of a Kind"] = temp
                    return category
                    scoring = 1
                elif category == "Full House":
                    result = 0
                    DICE.sort()
                    if DICE.count(DICE[0]) == 2 and DICE.count(DICE[2]) == 3:
                        result = 25
                    elif DICE.count(DICE[4]) == 2 and DICE.count(DICE[0]) == 3:
                        result = 25
                    else:
                        result = 0
                    temp[players] = result
                    SCOREBOARD["Full House"] = temp
                    return category
                    scoring = 1
                elif category == "Small Straight (Sequence of 4)":
                    result = 0
                    DICE.sort()
                    for x in DICE:
                        if DICE.count(x) > 1:
                            DICE.remove(x)
                    if DICE == [1, 2, 3, 4]:
                        result = 30
                    elif DICE == [2, 3, 4, 5]:
                        result = 30
                    elif DICE == [1, 2, 3, 4, 5]:
                        result = 30
                    elif DICE == [2, 3, 4, 5, 6]:
                        result = 30
                    temp[players] = result
                    SCOREBOARD["Small Straight (Sequence of 4)"] = temp
                    return category
                    scoring = 1
                elif category == "Large Straight (Sequence of 5)":
                    result = 0
                    DICE.sort()
                    if DICE == [1, 2, 3, 4, 5]:
                        result = 40
                    elif DICE == [2, 3, 4, 5, 6]:
                        result = 40
                    temp[players] = result
                    SCOREBOARD["Large Straight (Sequence of 5)"] = temp
                    return category
                    scoring = 1
                else:
                    result = DICE[0] + DICE[1] + DICE[2] + DICE[3] + DICE[4]
                    temp[players] = result
                    SCOREBOARD["Chance"] = temp
                    return category
                    scoring = true
            else:
                print "You have already scored this category. Please choose another category."


def roll():
    DICE = []
    status = 0
    while status < 3:
        status += 1
        existing = len(DICE)
        for x in range(5 - existing):
            i = randint(1, 6)
            DICE.append(i)
        print "You rolled: ", DICE[existing:]
        print "Here are your dice: ", DICE
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
                    if x in DICE:
                        DICE.remove(x)
    return DICE


def final_score(person):
    x = SCOREBOARD["Aces"[person]] + SCOREBOARD["Twos"[person]] + SCOREBOARD["Threes"[person]] + SCOREBOARD["Fours"[person]] + SCOREBOARD["Fives"[person]] + SCOREBOARD["Sixes"[person]]
    if x >= 63:
        x += 35
    x += SCOREBOARD["Three of a Kind"[person]] + SCOREBOARD["Four of a Kind"[person]] + SCOREBOARD["Full House"[person]] + SCOREBOARD["Small Straight (Sequence of 4)"[person]] + SCOREBOARD["Large Straight (Sequence of 5)"[person]] + SCOREBOARD["Chance"[person]]
    for i in SCOREBOARD["Yahtzee"[person]]:
        x += i
    print "Your final score is:", x


def turn(players):
    DICE = roll()
    score_roll(players, DICE)

# players = how_many_users()
#print "You entered ", players, " players"
# populate_scoreboards()
#print scoreboard
null_count = len(SCORE_DISPLAY) * players

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
    
	                