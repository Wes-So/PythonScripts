import random
import os
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ace = 11


def deal_card(seed):
    return random.choices(cards, k=seed)

def is_busted(cards):
    cards_total = sum(cards)
    return cards_total > 21
 
def handle_ace(cards):
    ace = 11
    while True:
        idx = cards.index(ace)
        cards[idx] = 1
        if sum(cards) < 21:
            break
    return cards


def play_cards(cards, isCPU):
    continuePlay = True
    player = "Your"

    if isCPU:
        player = "Computer"
        continuePlay = sum(cpu) < 17

    while continuePlay:
        if not isCPU:
            response = (
                input("Type 'y' to get another card, type 'n' to pass: ")).lower()
            if response == 'y':
                cards.append(deal_card(1)[0])
            elif response == 'n':
                break
        else:
            cpu.append(deal_card(1)[0])
            continuePlay = sum(cpu) < 17

        if is_busted(cards):
            if ace in cards:
                cards = handle_ace(cards)
                continuePlay = sum(cpu) < 17
            else:
                break

        if not isCPU:
            print(f"{player} cards: {cards} , current score: {sum(cards)}")

    return cards


def score_cards(cpu, player):
    if is_busted(player) and is_busted(cpu):
        print("Both players went over. Draw.")
    elif is_busted(player):
        print(f"You went over. You lose.")
    elif is_busted(cpu):
        print("Opponent went over. You win")
    elif sum(player) == 21 and len(player) == 2:
        print("Win with a Blackjack")
    elif sum(player) == sum(cpu):
        print(f"Draw.")
    elif sum(player) > sum(cpu):
        print(f"You win.") 
    else:
        print(f"You lose.")


print(logo)
keep_playing = True

while keep_playing:
    player_response = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if player_response != 'y':
        quit()

    os.system('cls')
    print(logo)

    player = deal_card(2) 
    if (sum(player) > 21) and ace in player:
        player = handle_ace(player)

    cpu = deal_card(2) 
    if (sum(cpu) > 21) and ace in cpu:
        cpu = handle_ace(cpu)

    print(f"Your cards: {player}, current score: {sum(player)}")
    print(f"Computer's first card: {cpu[0]}")
    player = play_cards(player, False)
    cpu = play_cards(cpu, True)
    print(f"Your final hand: {player}, final score: {sum(player)}")
    print(f"Computer's final hand: {cpu}, final score: {sum(cpu)}")
    score_cards(cpu, player)


