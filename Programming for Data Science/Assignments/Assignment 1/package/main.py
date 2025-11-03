%load main.py
from yahtzee import *

def main():
    """Main game loop for Yahtzee."""
    name = input('Enter your name please:')
    print(f"Welcome to Yahtzee, {name}!")
  
    # Initialize scorecard
    card = create_empty_scorecard() 

    # Play 13 rounds 
    for i in range(13):
        play_round(card)
        if i != 12:
            print(f'---------------Round: {i+1}--------------\n ')
        else:
            print(f'---------------Final Scorecard-------------- ')
    
    # Calculate final score
    upper = sum((card[i] or 0) for i in ('1','2','3','4','5','6'))
    bonus = 35 if upper >= 63 else 0
    total = bonus + sum((value or 0) for value in card.values())
    
    print(f"\nGame over! Final score: {total}\nWell Done, {name}!")

if __name__ == "__main__":
    main()
