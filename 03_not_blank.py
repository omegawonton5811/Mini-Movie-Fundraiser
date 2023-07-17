#func

#not blank checker
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Please type a name ")
        else:
            return response

#main
while True:
    name = not_blank("Enter your name (or 'xxx' to quit) ")
    if name == "xxx":
        break

print("We are done")