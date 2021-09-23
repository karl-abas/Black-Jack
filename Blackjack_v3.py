import random
import os
import time

# (changes) - user can change the colour of the decorations from a list, making the instructions more detailed,
# move everything to the right by 1 space, remove instructions after finnish reading
os.system("color")
# colour escape code
green = "\033[5;32;40m"
red = "\033[1;31;40m"
yellow = "\033[1;33;40m"
cyan = "\033[1;36;40m"
light_blue = "\033[1;34;40m"


# functions


def question_check(question, answer_list, error_message):
    valid = False
    while not valid:

        response = input(question).lower().strip()

        for item in answer_list:
            if response == item[0] or response == item:
                answer = item
                return answer

        # output error if item not in list
        print(error_message)
        print()


def number_checker(question, mini, maxi, error_message):
    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low/ too high give
            if mini <= response <= maxi:
                return response

            else:
                print(error_message)
        except ValueError:
            print(error_message)


def instruction():
    decorations(" INSTRUCTIONS ", "#", yellow)
    print("at the start you can choose the number of decks you want to play with\n"
          " you can put up to $10 in the bank. the amount of money you put in the ban is the amount you will play with for the entire game\n"
          "\n"
          "at the start of every game you must make a bet from $1 to the amount in your bank\n"
          "you are given 2 cards at the start\n"
          "the goal of the game is to get a total higher than the dealer without going higher than 21\n"
          "\n")
    time.sleep(5)
    decorations("card value", "#", green)

    print("'K', 'Q', 'J'= 10\n"
          "number cards are equal to their number\n"
          "'A' = 11 or 1\n"
          "\n"
          "\n")
    time.sleep(5)
    decorations(" moves ", "#", yellow)
    print("hit - pick up one card\n"
          "stay - end turn\n"
          "double up - bet will double but pick up one card\n"
          "")


def deal(pick_amount, who_deck, who_num_deck, who, show):
    for i in range(pick_amount):
        card = deck.pop()
        who_deck.append(card)
        s = counter(who_num_deck)
        if card == "J" or card == "Q" or card == "K":
            who_num_deck.append(10)
        elif card == "A":
            if s + 11 <= 21:
                who_num_deck.append(11)
            else:
                who_num_deck.append(1)
        else:
            who_num_deck.append(card)

    if show == "Y":
        print(who + " total is {}".format(counter(who_num_deck)))
    else:
        pass


def counter(add):
    count = sum(add)
    return count


def decorations(word, decor, colour):
    side = decor * 5
    statement = ("{} {} {}".format(side, word, side))
    decor_tb = decor * len(statement)
    # adds colour to the text
    print(colour + decor_tb)
    print(colour + statement)
    print(colour + decor_tb)
    # print everything after the decor as default
    print("\033[0;37;40m \n")


# ##########################LISTS###################################

# reset list
reset_user_deck = ["hit", "stay", "double up"]

#
yes_no = ["yes", "no"]
# moves

cards_amount = ["2", "3", "4", "5"]
# cards
# user cards

# dealer cards

# main

# instructions
decorations(" WELCOME TO BLACKJACK ", '#', red)

instruct = question_check("do you want the instructions\n", yes_no, "please answer 'yes' or 'no'")
if instruct == "yes":
    instruction()
    print()
else:
    print()

deck_amount = number_checker("how many decks do you want to play with from 1-5\n", 1, 5,
                             "please pick a whole number from 1-5")
bank = number_checker("\nhow much would you like to put into the bank from 1-10\n", 1, 10,
                      "please pick a whole number between 1 and 10\n")

# ######################################where the loop starts?##################################

go = "yes"

while go == "yes":
    user_deck = []
    user_num_deck = []
    deal_deck = []
    dealer_num_deck = []
    available_moves = ["hit", "stay", "double up"]

    print("you have ${:.2f} in the bank".format(bank))

    bet = number_checker("how much would you like to bet for this round\n", 1, bank,
                         "please pick a whole number between 1 and the amount in the bank")
    print("you bet ${:.2f} for this round".format(bet))
    # shuffle deck
    deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "J", "K", "Q"] * (int(deck_amount) * 4)
    random.shuffle(deck)
    # deal 2 cards
    deal(2, user_deck, user_num_deck, "user", "Y")
    print(user_deck)
    print()
    deal(1, deal_deck, dealer_num_deck, "dealer First card", "Y")
    deal(1, deal_deck, dealer_num_deck, "dealer", "N")
    print()
    # show total of user

    user_bust = "no"
    if bet * 2 > bank:
        # removes double up option when when bet x2 is greater than the bank
        if available_moves == reset_user_deck:
            available_moves.pop(2)
    game = "yes"
    while game == "yes":
        # count user total
        user_total = counter(user_num_deck)
        # blackjack for user
        if user_total == 21:
            print("BlackJack!!!")
            game = "no"
        # bust user when total is above 21
        elif user_total > 21:
            user_bust = "yes"
            print("bust")
            game = "no"

            # user pick a choice
        else:
            print("you can either {}".format(available_moves))
            # hit
            q = question_check("what would you like to do\n", available_moves, "please pick an available move")
            if q == "hit":
                deal(1, user_deck, user_num_deck, "user", "Y")
                print(user_deck)

            # stay
            if q == "stay":
                game = "no"
            if q == "double up":
                bet *= 2
                deal(1, user_deck, user_num_deck, "user", "Y")
                print(user_deck)
                game = "no"
    # deal for dealer
    # rig game?
    # don't deal dealers if user is bust
    if user_bust != "yes":
        d = "yes"
    else:
        d = "no"
    # deal dealer
    while d == "yes":
        dealer_total = counter(dealer_num_deck)
        if dealer_total > 21:
            print(" dealer bust ")
            d = "no"
        elif dealer_total <= 15:

            print("dealer picked a card")
            deal(1, deal_deck, dealer_num_deck, "dealer", "Y")
            print()
            # stop picking
        elif dealer_total >= 18:
            print("dealer is deciding\n...")
            time.sleep(4)
            print("dealer stays")
            d = "no"
        else:
            print("dealer is deciding\n...")
            time.sleep(5)
            if random.randint(0, 100) >= 50:

                deal(1, deal_deck, dealer_num_deck, "dealer", "Y")
            else:
                d = "no"

    # comparing dealer and users total
    user_total = counter(user_num_deck)
    dealer_total = counter(dealer_num_deck)

    # compare with dealer
    # dealer got higher than or equal to user but less than 22
    print()
    if 22 > dealer_total >= user_total:
        decorations("dealer wins", "-", red)
        bank -= bet
    # user got higher than dealer and less than 22
    elif 22 > user_total > dealer_total:
        decorations("you win", "!", light_blue)
        bank += bet
    # user got higher than 21
    elif user_total > 21:
        decorations(" dealer wins ", "-", red)
        bank -= bet
    # dealer bust but not user
    elif dealer_total > 21:
        decorations("you win", "!", light_blue)
        bank += bet
    print("you had {} and your total was {} dealer had {} and their total was {}".format(user_deck,
                                                                                         counter(user_num_deck),
                                                                                         deal_deck,
                                                                                         counter(
                                                                                             dealer_num_deck)))
    # restart

    # ask if you want to continue
    if bank == 0:
        print("you do not have enough money in the bank")
        go = "no"
    else:
        c = question_check("do you want to keep playing?\n", yes_no, "please answer 'yes' or 'no'")
        if c == "no":

            go = "no"


# end game
print()
decorations("THANK YOU FOR PLAYING", "#", yellow)
print(bank)
print("your total is ${:.2f}. thank you for playing".format(bank))
