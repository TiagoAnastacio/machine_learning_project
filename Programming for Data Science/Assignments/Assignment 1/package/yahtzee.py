# Yahtzee Game Logic Exercise
# Implement the logic for each function as described in the docstrings
import random
def roll_dice(n=5):
    '''
    This function is used to roll the first dice when the round starts
    '''
    results = []   #creates a list where the different dice will be append
    for i in range(n): # the for loop will simulate the throw of the dice and appends to the list previous created
        results.append(random.randint(1,6))
    return results

def create_empty_scorecard():
    '''
    This function creates the empty yahtzee card
    '''
    scores = {
        '1' : None,
        '2' : None,
        '3' : None,
        '4' : None,
        '5' : None,
        '6' : None,
        'three_of_a_kind' : None,
        'four_of_a_kind': None,
        'full_house': None,
        'four_straight' : None,
        'five_straight' : None,
        'yahtzee' : None,
        'chance' : None       
    }
    return scores


def select_keep(dice):
    '''
    This function will enable the user to select which dices wants to keep before rerolling the ones that were not kept
    '''
    while True: # this line of code together with the except at the end is used so if the input of the user is invalid, the user is asked to give a valid input
        try:
            dice_to_keep = input('Which dice to keep?') # asks the user which dice to keep
            dice_move_forward = [] # to this empty list will be append the dice selected by the user
            dummy_dice = dice.copy() # here we create a copy of the list dice, so we can eliminate items in the future for loop without changing the original list
            dice_to_keep = dice_to_keep.replace(' ', '') # will clean the answer from the user
            for i in dice_to_keep: # it will evaluate each die chosen by the user
                i = int(i) # as the answer comes in a string there is the need to turn each choice into an integer to compare with the list of individual die from the previous roll
                if i in dummy_dice:      # this if statetement aims to check if the number chosen in the input from the user is in the current roll
                    dice_move_forward.append(i) # appends to the list so we can keep that die
                    dummy_dice.remove(i) # removes so it is not possible to select more times a number than the number of times that number is available
                else:
                    raise ValueError('Not Valid Selection') # so the user knows the choice was not valid and is asked to do again
            return dice_move_forward

        except ValueError as e:
            print(f'{e} Try again.' )

def reroll(dice, kept):
    '''
    The function will enable the user to reroll the dice that were not chosen
    '''
    for i in range(len(dice) - len(kept)): # so the number of dice to reroll is calculated
        kept.append(random.randint(1,6)) # appends to the dice kept from the previous roll the new dice
    return kept  


def has_straight(dice, length):
    '''
    Function will evaluate if there is a sequence in the dice we have in hand
    '''
    dummy_dice = dice.copy() # this creates a new list with the same values as dice
    dummy_dice = set(dummy_dice) # takes dice that are repeated
    dummy_dice = list(dummy_dice) # transforms back in list without the dice repeated
    dummy_dice.sort() # sorts the list 
    is_there_sequence = 0 
    for idx, i in enumerate(dummy_dice): # the for loop will evaluate if there is a sequence for each die that we have in hand
        check_length = list(range(i, i + length, 1)) # creates a list for each die, that will be the number represented in each die and will create a list with a sequence after that number
        if check_length == dummy_dice[idx: idx + length]: # if both lists matches is there sequence becomes 1
            is_there_sequence += 1
    if is_there_sequence > 0:
        return True
    else:
        return False # if there is a sequence it will return true


def evaluate(dice):
    '''
    This function returns the score for each category based on the current dice roll. 
    It evaluates number categories (1-6), three/four of a kind, full house, straights, yahtzee and chance.   
    '''
    scores = create_empty_scorecard() #creates a temporary scorecard to evaluate the hand 
    
    total = sum(dice) #sum of all dice (to be used in several categories below)
    
    counts = {} #dictionary to count the occurrences of each value
    for i in dice:
        if i in counts:
            counts[i] += 1 #if already appears we increase the count by 1
        else:
            counts[i] = 1 #if its the first occurrence (start at 1)
            
    for i in range(1, 7):
        scores[str(i)] = dice.count(i) * i #multiplies each value (i) by its occurrences (dice.count(i))

    for value in counts.values(): 
        if value >= 5: #if a given number appears 5 times in the dice roll
            scores["yahtzee"] = 50 #Yahtzee: 5 of the same number 
            scores["four_of_a_kind"] = total #a given number appearing 5 times implies appearing 4 times
            scores["three_of_a_kind"] = total #a given number appearing 5 times implies appearing 3 times
        if value >= 4: #if a given number appears 4 times in the dice roll
            scores["four_of_a_kind"] = total #four_of_a_kind: 4 of the same number 
            scores["three_of_a_kind"] = total #a given number appearing 4 times implies appearing 3 times
        elif value >= 3: #if a given number appears 3 times in the dice roll
            scores["three_of_a_kind"] = total #three_of_a_kind: 3 of the same number
    
    if 2 in counts.values() and 3 in counts.values(): #having exactly 2 times of one number and 3 times of another 
        scores["full_house"] = 25 
    
    if has_straight(dice,5): #checking for a sequence of 5 using has_straight function above
            scores["four_straight"] = 30
            scores["five_straight"] = 40 #if there is a sequence of 5, there is also a sequence of 4
    elif has_straight(dice,4): #checking for a sequence of 4 using has_straight function above
        scores["four_straight"] = 30
    
    scores["chance"] = total #total of all dice (no restrictions)
    
    return scores

def choose_score(scores, used):
    '''
    Used to choose the option we want to turn permanent in the scorecard
    '''
    
    while True: # this line together with try and except aims to allow the user to correct his answer, if the answer is not valid
        try:
            raw = input('Which one to fill?') #asks the user which category he wants to fill
            raw = raw.lower().replace(' ', '') #aims to clean the answer a bit in order to allow different ways of writting
            if raw in used.keys() and used[raw] == None: # checks if the answer is valid, in this case the category in our scorecard needs to be not chosen, and the input needs to match to one of the categories 
                used[raw] = scores[raw] # if the input fills the above condition, the choice will become permanent in the main game score card
                return used #returns the maincard
            elif raw in used.keys() and used[raw] != None: # raise a message based on the error from the input
                raise ValueError('Input already selected')
            else:
                raise ValueError('Input not valid check for spelling mistakes')
            
        except ValueError as e:
            print(f'{e} Try again.')    
            
def display_scorecard(card):
    '''
    Displays the updated scorecard after each round
    '''
    upper_section_score = 0 # to future check the score of the upper_section
    card_points = 0 # check total in the future
            
    for key, value in card.items(): # for loop aims to check sum the upper section total
        if key in ('1', '2', '3', '4', '5', '6'):
            upper_section_score +=(value or 0) # value,0 is used so if the category is None, None becomes 0 for the sum
    bonus = 35 if upper_section_score >= 63 else 0       # creates the bonus if the upper section is above 63
    for key, value in card.items(): # prints each category and the corresponding points in the scorecard, and used to check the total points
        print(f'{key}: {value}')
        card_points += (value or 0) # value,0 is used so if the category is None, None becomes 0 for the sum
    
    print(f'Upper Section Score: {upper_section_score}') # prints the upper section total
    print(f'Bonus: {bonus}') # prints the bonus score
    print(f"Total Score: {bonus+card_points}") # prints the total

def play_round(card):
    '''
    Plays one single round of the yahtzee game
    '''
    rolling_the_first_dice = roll_dice() #pass the roll dice to create the 5 throws
    print(f"Your current hand is:{rolling_the_first_dice}") 
    evaluate_the_first_throw = evaluate(rolling_the_first_dice) #here the roll will be evaluated and the user will be able to see the score in the different categories
    print(f"Your current scorecard is:\n{evaluate_the_first_throw}")
    choosing_after_first_throw = select_keep(rolling_the_first_dice) #here the user will be able to choose the dices to keep
    first_reroll = reroll(rolling_the_first_dice,choosing_after_first_throw) # reroll the dice not chosen
    print(f"Your current hand is:{first_reroll}")
    evaluate_the_second_throw = evaluate(first_reroll) #here the seocnd throw is evaluated and the possible scores are shown 
    print(f"Your current scorecard is:\n{evaluate_the_second_throw}")
    choosing_after_second_throw = select_keep(first_reroll) #here the user is able to choose after the rerolling
    second_reroll = reroll(first_reroll, choosing_after_second_throw) #final reroll
    print(f"Your final hand is:{second_reroll}")
    evaluate_the_third_throw = evaluate(second_reroll) #evaluates the third roll
    print(f"Your final scorecard is:\n{evaluate_the_third_throw}")
    chosen_score = choose_score(evaluate_the_third_throw, card) #choice of the category for that round
    display_scorecard(chosen_score) #display the scorecard after the round 
