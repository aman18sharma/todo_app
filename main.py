def enter_your_name():
    user_prompt = "What is your name? "
    name = input(user_prompt)
    print("Hello " + name.capitalize() + "!")

while True:
    enter_your_name()
    break

countries = []

while True:
    country = input("Enter the country: ")
    countries.append(country)
    print(countries)
    break

todos = []
while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            file = open("todos.txt", "a")
            file.writelines(todo + "\n")
            file.close()
        case 'show':
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()
            for index, todo in enumerate(todos):
                row = f"{index + 1}-{todo.capitalize()}"
                print(row)
        case 'edit':
            number = int(input('Enter a number to edit todo: '))
            number -= 1
            new_todo = input("Enter a new todo: ")
            todos.__setitem__(number, new_todo)
        case 'complete':
            todo = int(input("Enter number to complete todo: "))
            todos.pop(todo - 1)
            print('Todo completed successfully!')
        case 'exit':
            print('\n\nBye Bye!!!')
            break
        case whatever:
            print('Incorrect input')


# In the coding area, we have defined a country variable.
#
# You should write a match-case block that checks the value of the country variable and:
#
# Prints out Hello if the value of country is "USA".
#
# Prints out Namaste if the value of country is "India".
#
# Prints out Hallo if the value of country is "Germany".

country = "India"
match country:
    case 'USA':
        print('Hello')
    case 'India':
        print('Namaste')
    case 'Germany':
        print('Hallo')

# Complete the code by adding a for-loop that makes the program produce the following output:
# John Smith
# Sen Plakay
# Dora Ngacely
#
members = ["john smith", "sen plakay", "dora ngacely"]

for member in members:
    print(member.title())

# Loop over the colors items and print out the item in every loop. So, the expected output of your code would be:
#
# 11
# 34
# 98
# 43
# 45
# 54
# 54

colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    print(color)

# The programmer is trying to loop over the buttons list and print out each item with the first letter capitalized. However,
# the programmer has done something wrong. Try to find and fix the issue.
# for i in buttons:
#     print(i.capitalize())
#
# buttons = ["cancel", "reply", "submit"]

# Solution
buttons = ["cancel", "reply", "submit"]
for i in buttons:
    print(i.capitalize())
# Create a program that:
# 1. Prompts the user to input a (dollar) amount.
# 2. Calculates the corresponding amount in euros, given an exchange rate of 2.
# 3. Prints out the amount in euros.

rate = 2
dollar_amount = input('Enter a amount in USD($) to exchange in Euro: ')
dollar_amount = float(dollar_amount)
print(dollar_amount * rate)

# The ranking list given in the coding area represents the ranking of three athletes, John, Sen, and Lisa. John won 1st place, Sen got 2nd, and Lisa 3rd.
# Your task is to create a program that:
#     1. Contains the above list.
#     2. Prompts the user to input a rank number.
#     3. Returns the person who has the given rank.
#
ranking = ['John', 'Sen', 'Lisa']
rank = input('Enter rank to get the athlete name: ')
rank = int(rank) - 1
athlete_name = ranking.__getitem__(rank)
print(athlete_name)


# We have defined the same ranking list as in the previous exercise:
#     This time you should create a program that:
#         1. Contains the above list.
#         2 Prompts the user to input the person's name.
#         3. Returns the rank that person has.

ranking = ['John', 'Sen', 'Lisa']
athlete_name = input('Enter athlete name to get the athlete rank: ')
rank = ranking.index(athlete_name)
print(rank + 1)

filenames = ['document', 'report', 'presentation']

for i, filename in enumerate(filenames):
    row = f"{i}-{filename.capitalize()}" + ".txt"
    print(row)

# We have a list of two IPs in the code area.
#     Extend the code so your program:
#         1. Prompts the user to input an index (e.g., 0 or 1).
#         2. Depending on the user input, the program should return either You chose 100.122.133.111 or You chose 100.122.133.111
#             Note: In order for the system to mark your exercise as correct, your code should return the exact output (i.e., upper case Y in You chose and no spaces or other characters after the IP.

ips = ['100.122.133.105', '100.122.133.111']
user_prompt = int(input('Enter the index of the IP you want: '))
print('You chose', ips[user_prompt])


# Bug-Fixing Exercise 1
# Supposedly, the following program should:
#     1. Prompt the user to input an index (e.g., 0, 1, or 2).
#     2. Print out the item with that index.
#         However, there is a bug with the program which you should try to fix.

menu = ["pasta", "pizza", "salad"]
user_choice = int(input("Enter the index of the item: "))
message = f"You chose {menu[user_choice]}."
print(message)
from functions import *

todos = []
while True:
    user_action = input("Type add, show, edit, complete, temperature or exit: ").strip()
    if 'add' in user_action:
        write_todo()
    elif 'show' in user_action:
        get_todos()
    elif 'edit' in user_action:
        number = int(input('Enter a number to edit todo: '))
        number -= 1
        new_todo = input("Enter a new todo: ")
        todos.__setitem__(number, new_todo)
    elif 'complete' == user_action:
        todo = int(input("Enter number to complete todo: "))
        todos.pop(todo - 1)
        print('Todo completed successfully!')
    elif 'temperature' == user_action:
        todo = int(input("Enter water temperature: "))
        water_state(todo)
    elif 'exit' == user_action:
            print('\n\nBye Bye!!!')
            break
    else:
        print('Incorrect input')

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentange = value/total_value * 100
    print("This is " + f"{percentange}" + "%")
except ValueError:
    print('You need to enter a number. Run the program again.')

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentange = value / total_value * 100
    print("This is " + f"{percentange}" + "%")
except ZeroDivisionError:
    print('You total value cannot be zero.')

foo(10)
