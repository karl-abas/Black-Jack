# adding colour to decorations
# colour escape code
green = "\033[5;32;40m"
red = 0
yellow = 0


# functions
def decorations(word, decor, colour):
    side = decor * 5
    statement = ("{}{}{}".format(side, word, side))
    decor_tb = decor * len(statement)

    print(colour + decor_tb)
    print(colour + statement)
    print(colour + decor_tb)


#
#
#

# main

decorations("hello", "#", green)
