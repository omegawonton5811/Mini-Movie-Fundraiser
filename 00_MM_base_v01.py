import pandas
import random
from datetime import date

#func

def show_instructions():
    print('''\n
    ***** Instructions *****
    
    For each ticket, enter ...
    - The person's name (can't be blank)
    - Age (between 12 and 120)
    - Payment method (cash / credit)
    
    When you have entered all the users, type 'xxx' to quit.
    
    The program will then display the ticket details including the cost of each ticket, the total cost and the total profit.
    
    This information will also be automatically written to a text file.
    
    ********************''')

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

#price calc
def calc_ticket_price(var_age):

    if var_age <16:
        price = 7.5

    elif var_age < 65:
        price = 10.5

    else:
        price = 6.5

    return price

#cash or credit
def string_checker(question, num_letters, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0], valid_responses[1])

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print("Please enter a valid response")

def currency(x):
    return "${:.2f}".format(x)

#main

#vars
MAX_TICKETS = 5
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

all_names = []
all_ticket_costs = []
all_surcharge = []

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

want_instructions = string_checker("Do you want to read the instructions? ", 1, yes_no_list)

if want_instructions == "yes":
    show_instructions()

print()

#loop

while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' to quit) ")

    if name == 'xxx' and len(all_names) > 0:
        break
    elif name == 'xxx':
        print("You must sell at least ONE ticket before quitting")
        continue
        
    age = num_check("Age: ")

    if 12 <= age <= 120:

        pass
    elif age <12:
        print("Sorry you are too young for this movie")
        continue
    else:
        print("That looks like a typo, please try again.")
        continue

    #calc ticket cost
    ticket_cost = calc_ticket_price(age)

    #get payment method
    pay_method = string_checker("Choose a payment method (cash / credit): ", 2, payment_list)

    if pay_method == "cash":
        surcharge = 0
    else:
      surcharge = ticket_cost * 0.05

    tickets_sold += 1

    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

mini_movie_frame = mini_movie_frame.set_index('Name')

today = date.today()

day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "\n---- Mini Movie Fundraiser Ticket Data ({}/{}/{}) ----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)


ticket_cost_heading = "\n---- Ticket Cost / Profit ----"
total_ticket_sales = "Total Ticket Sales: ${:.2f}".format(total)
total_profit = "Total Profit: ${:.2f}".format(profit)

sales_status = "\n*** All the tickets have been sold ***"

winner_heading = "\n---- Raffle Winner ----"
winner_text = "the winner of the raffle is {}.\nThey have won ${:.2f}, their ticket is free!".format(winner_name, total_won)


to_write = [heading, mini_movie_string, ticket_cost_heading, total_ticket_sales, total_profit, sales_status, winner_heading, winner_text]

for item in to_write:
    print(item)

write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

text_file.close()

if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} ticket/s. There is {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))