def number_checker(question, mini, maxi, error_message):

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low/ too high give
            if mini < response <= maxi:
                return response

            else:
                print(error_message)
        except ValueError:
            print(error_message)


answer = number_checker("how much would you like to bet from 1 to 10", 1, 10, "please enter a number between 1 to 10")
print("you entered {}".format(answer))
