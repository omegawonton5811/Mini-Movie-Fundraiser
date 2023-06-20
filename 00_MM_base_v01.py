#func

#y/n
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes or no")
#not blank checker
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Please type a name ")
        else:
            return response

#int check
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")
#main

#vars
MAX_TICKETS = 3
tickets_sold = 0

want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    print("Instructions go here")

#loop

while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' to quit) ")

    if name == 'xxx':
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:

        pass
    elif age <12:
        print("Sorry you are too young for this movie")
        continue
    else:
        print("That looks like a typo, please try again.")
        continue

    tickets_sold += 1
#out
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} ticket/s. There is {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))