from random import randint

scoreboard = {}
dice = []
score_display = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "Three of a Kind", "Four of a Kind", "Full House", "Small Straight (Sequence of 4)", "Large Straight (Sequence of 5)", "Yahtzee", "Chance"]

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

def score_roll(players):
    category = raw_input("How do you want to score this roll? ")
    print "Categories are: ", score_display
    if category in scoreboard:
        if scoreboard[category[players]] == "null":
            if category == "Aces":
                result = 0
                for x in dice:
                    if x == 1:
                        result += x
                scoreboard["Aces"[players]] = result
            elif category == "Twos":
                result = 0
                for x in dice:
                    if x == 2:
                        result += x
                scoreboard["Twos"[players]] = result
            elif category == "Threes":
                result = 0
                for x in dice:
                    if x == 3:
                        result += x
                scoreboard["Threes"[players]] = result
            elif category == "Fours":
                result = 0
                for x in dice:
                    if x == 4:
                        result += x
                scoreboard["Fours"[players]] = result
            elif category == "Fives":
                result = 0
                for x in dice:
                    if x == 5:
                        result += x
                scoreboard["Fives"[players]] = result
            elif category == "Sixes":
                result = 0
                for x in dice:
                    if x == 6:
                        result += x
                scoreboard["Sixes"[players]] = result
            elif category == "Three of a Kind":
                result = 0
                for x in dice:
                    if dice.count(x) >= 3:
                        result = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
                scoreboard["Three of a Kind"[players]] = result
            elif category == "Four of a Kind":
                result = 0
                for x in dice:
                    if dice.count(x) >= 4:
                        result = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
                scoreboard["Four of a Kind"[players]] = result
            elif category == "Full House":
                result = 0
                dice.sort()
                if dice.count(dice[0]) == 2 and dice.count(dice[2]) == 3:
                    result = 25
                elif dice.count(dice[4]) == 2 and dice.count(dice[0]) == 3:
                    result = 25
                scoreboard["Full House"[players]] = result
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
                scoreboard["Small Straight (Sequence of 4)"[players]] = result
            elif category == "Large Straight (Sequence of 5)":
                result = 0
                dice.sort()
                if dice == [1, 2, 3, 4, 5]:
                    result = 40
                elif dice == [2, 3, 4, 5, 6]:
                    result = 40
                scoreboard["Large Straight (Sequence of 5)"[players]] = result
            else:
                result = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
                scoreboard["Chance"[players]] = result
        elif category == "Yahtzee":
            result = 0
            if scoreboard["Yahtzee"[players]] == ["null"]:
                if dice.count(dice[0]) == 5:
                     result = 50
                scoreboard["Yahtzee"[players]] = [result]
            elif scoreboard["Yahtzee"[players]] == [0]:
                print "You have already scored a 0 in Yahtzee. Please choose another category."
                score_roll()
            else:
                if dice.count(dice[0]) == 5:
                    scoreboard["Yahtzee"[players]].append(100)
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
                status = 3
        else: 
            discards = raw_input("Which dice do you want to re-roll? 1, 2, 3, etc.")
            discard_list = []
            for y in discards:
                if y.isdigit():
                    discard_list.append(int(y))
            for x in discard_list:
                if x in dice:
                    dice.remove(x)
	                
def final_score(person):
    x = scoreboard["Aces"[person]] + scoreboard["Twos"[person]] + scoreboard["Threes"[person]] + scoreboard["Fours"[person]] + scoreboard["Fives"[person]] + scoreboard["Sixes"[person]]
    if x >= 63:
        x += 35
    x += scoreboard["Three of a Kind"[person]] + scoreboard["Four of a Kind"[person]] + scoreboard["Full House"[person]] + scoreboard["Small Straight (Sequence of 4)"[person]] + scoreboard["Large Straight (Sequence of 5)"[person]] + scoreboard["Chance"[person]]
    for i in scoreboard["Yahtzee"[person]]:
        x += i
    print "Your final score is:", x

def turn(players):
    dice = []
    roll()
    score_roll(players)
    
players = how_many_users()
populate_scoreboards()

print scoreboard

for category in scoreboard:
    if "null" in scoreboard[category]:
        for each in range(players):
            #loop works to here
            for category2 in scoreboard:
                print "scoreboard searched for category2", category2
                if scoreboard[category2[each]] == "null" or scoreboard[category2[each]] == ["null"]: 
                    print "Your turn, Player", each + 1
                    turn(each)
    else:
        for each in range(players):
            print "Player %r, your score is:" % (each + 1), final_score(each)
        print "Game Over!"
    
#still need: 1. add player-specific indexes to score functions for each player; 
#2. add "Your turn, player!" to top of each turn, use player # to access index in scoreboard
#3. add exception at end for bonuses
#4. add winner function / ranking function
    
	                