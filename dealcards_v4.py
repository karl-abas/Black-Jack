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

    if show == "y":
        print(who + " total is {}".format(counter(who_num_deck)))
    else:
        pass()
