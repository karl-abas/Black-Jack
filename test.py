import random


def player_deal(pick_amount):

    for i in range(pick_amount):
        players_card.append(deck.pop())


players_card = []

deck = [  ]
door1 = ["incorrect"]
door2 = ["correct"]
door3 = ["incorrect"]
random.shuffle(deck)
player_deal(3)

print(players_card)


def player_deal(pick_amount):

    for i in range(pick_amount):
        user_deck.append(deck.pop())


def dealer_deal(pick_amount):

    for i in range(pick_amount):
        deal_deck.append(deck.pop())
