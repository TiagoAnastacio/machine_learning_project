# Yahtzee Game Logic Exercise
# Implement the logic for each function as described in the docstrings

def roll_dice(n=5):
    results = []
    for i in range(n):
        results.append(random.randint(1,6))
    return results

def create_empty_scorecard():
    scorecard = {
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
    return scorecard


def select_keep(dice):
    while True:
        try:
            dice_to_keep = input('Which dice to keep?')
            dice_move_forward = []
            dummy_dice = dice.copy() # here we create a copy of the list dice, so we can eliminate items in the future for loop without changing the original list
            dice_to_keep = dice_to_keep.replace(' ', '')
            for i in dice_to_keep:
                i = int(i)
                if i in dummy_dice:      
                    dice_move_forward.append(i)
                    dummy_dice.remove(i)
                else:
                    raise ValueError('Not Valid Selection')
            return dice_move_forward

        except ValueError as e:
            print(f'{e} Try again.' )

def reroll(dice, kept):
    for i in range(len(dice) - len(kept)):
        kept.append(random.randint(1,6))
    return kept  


def has_straight(dice, length):
    dummy_dice = dice.copy()
    dummy_dice = set(dummy_dice)
    dummy_dice = list(dummy_dice)
    dummy_dice.sort()
    is_there_sequence = 0
    for idx, i in enumerate(dummy_dice):
        check_length = list(range(i, i + length, 1))
        if check_length == dummy_dice[idx: idx + length]:
            is_there_sequence += 1
    if is_there_sequence > 0:
        return True
    else:
        return False


def evaluate(dice):
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
    total = sum(dice) 
    
    counts = {} #conta quantas vezes x número aparece
    for i in dice:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
            
    for i in range(1, 7):
        scores[str(i)] = dice.count(i) * i #multiplicar o valor do dado por quantas vezes ele aparece

    for value in counts.values():
        if value >= 5:
            scores["yahtzee"] = 50
            scores["four_of_a_kind"] = total
            scores["three_of_a_kind"] = total
        if value >= 4:
            scores["four_of_a_kind"] = total
            scores["three_of_a_kind"] = total
        elif value >= 3:
            scores["three_of_a_kind"] = total
    
    if 2 in counts.values() and 3 in counts.values():
        scores["full_house"] = 25
    
    if has_straight(dice,5):
            scores["four_straight"] = 30
            scores["five_straight"] = 40
    elif has_straight(dice,4):
        scores["four_straight"] = 30
    
    scores["chance"] = total
    
    return scores


def choose_score(scores, used):
    
    while True:
        try:
            raw = input('Which one to fill?')
            raw = raw.lower().replace(' ', '')
            if raw in used.keys() and used[raw] == None and scores[raw] != 0:
                used[raw] = scores[raw] 
                return used
            elif raw in used.keys() and (used[raw] != None or scores[raw] == 0):
                raise ValueError('Input already selected or score 0')
            else:
                raise ValueError('Input not valid check for spelling mistakes')
            
        except ValueError as e:
            print(f'{e} Try again.')   

def display_scorecard(card):
    upper_section_score = 0
    card_points = 0
    for key, value in card.items():
        if value == None:
            card[key] = 0
    for key, value in card.items():
        if key in ('1', '2', '3', '4', '5', '6'):
            upper_section_score += value
    if upper_section_score  >= 63:
        bonus = 35
    else:
        bonus = 0        
    for key, value in card.items():
        print(f'{key}: {value}')
        card_points += value
    
    print(f'Upper Section Score: {upper_section_score}')
    print(f'Bonus: {bonus}')
    print(f"Total Score: {bonus+upper_section_score+card_points}")


def play_round(card):
    rolling_the_first_dice = roll_dice()
    print(f"Your current hand is:{rolling_the_first_dice}")
    evaluate_the_first_throw = evaluate(rolling_the_first_dice)
    print(f"Your current scorecard is:\n{evaluate_the_first_throw}")
    choosing_after_first_throw = select_keep(rolling_the_first_dice)
    first_reroll = reroll(rolling_the_first_dice,choosing_after_first_throw)
    print(f"Your current hand is:{first_reroll}")
    evaluate_the_second_throw = evaluate(first_reroll)
    print(f"Your current scorecard is:\n{evaluate_the_second_throw}")
    choosing_after_second_throw = select_keep(first_reroll)
    second_reroll = reroll(first_reroll, choosing_after_second_throw)
    print(f"Your final hand is:{second_reroll}")
    evaluate_the_third_throw = evaluate(second_reroll)
    print(f"Your final scorecard is:\n{evaluate_the_third_throw}")
    chosen_score = choose_score(evaluate_the_third_throw, card)
    display_scorecard(chosen_score)
