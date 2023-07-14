import random

def card_pickup():
    cards = list(range(1, 53))  # Create a list of 52 cards
    
    print("Welcome to 52-Card Pickup!")
    print("Press enter to begin the game.")
    input()  # Wait for the player to press enter
    
    random.shuffle(cards)  # Shuffle the cards
    
    print("52-Card Pickup! The cards are scattered.")
    print("Your task is to pick them all up.")
    print("Press enter when you have collected all the cards.")
    
    input()  # Wait for the player to press enter
    
    print("You collected all the cards! Game over.")



#def
card_pickup()
