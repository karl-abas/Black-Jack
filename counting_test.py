# function ask for how many times to pick and whos deck to put it in

def counter(add):
    count = sum(add)
    return count


deck = []
x = ""
while x != "x":

    y = int(input("what number would you like to add"))
    deck.append(y)
    print(counter(deck))
