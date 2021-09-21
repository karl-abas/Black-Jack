# adding colour to decorations
# colour escape code
green = "\033[5;32;40m"
red = 0
yellow = 0

# change text colour at end
# functions
def decorations(word, decor, colour):
    side = decor * 5
    statement = ("{}{}{}".format(side, word, side))
    decor_tb = decor * len(statement)

    print(colour + decor_tb)
    print(colour + statement)
    print(colour + decor_tb)
    print("\033[0;37;40m \n")

#
#
#

# main
print("hello")
decorations("hello", "#", green)

print("hi")
