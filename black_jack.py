############### Blackjack Project #####################

from art import logo

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def compare(user, computer):
    if computer == user:
        return("It's a Draw!")
    elif computer == 0:
        return("You lose! opponent has a blackjack😎")
    elif user == 0:
        return("You Win🦾 with a blackjack")
    elif user > 21:
        return("You lose, you went overboard")
    elif computer > 21:
        return("You win computer went overboard")
    else:
        if user > computer:
            return("You win with the highest score")
        else:
            return("You lose, computer has the highest score")

def calculate_score(list):
    if len(list) == 2 and sum(list) == 21:
        return 0
    elif 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
        return sum(list)
    return sum(list)

def play_game():

    print(logo)
    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_continue = True
    while game_continue:
        users_score = calculate_score(user_cards)
        computers_score = calculate_score(computer_cards)

        print(f" Your cards: {user_cards}, current score: {users_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if users_score == 0 or computers_score == 0 or users_score > 21:
            game_continue = False

        else: 
            if input("Type 'y' to draw another card and 'n' to pass ") == "y":
                user_cards.append(deal_card())
            else:
                game_continue = False

    while computers_score != 0 and computers_score < 17:
        computer_cards.append(deal_card())
        computers_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {users_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computers_score}")

    print(compare(users_score, computers_score))

while input("Do you want to play the game of Blackjack? Type 'yes' or 'no' ") == "yes":
    play_game()
