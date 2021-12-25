Random Module:
# In Python, Modules are simply files with the “. py” extension containing Python code that can be imported inside another Python Program

Example:
In main.py

# To use the module, need to specify the module by putting this command in below
import random 

random_integer = random.randint(1, 10)
print(random_integer)

# Can also create a new file under the file above, for example the python code above is under main.py, we create another file called my_module.pi and can insert a variable 

my_module.py

my_module = pi = 3.14159246

# So now underneath main.py, we can simply do this.
# we have now added another import module, specifying the name of the other file
# we can also print my_module

import random 
import my_module

random_module = random.randint(1, 10)
print(random_module)

print(my_module.pi)

#Can also use random with floats 

import random

random_int = random.randint(1, 10)
print(random_int)

random_float = random.random()
print(random_float)

# With this next one, can use f string to insert in print

random_int1 = random.randint(1, 500)
print(f"your nmuber is {random_int1}")


Challenge 1:
# Create a random module to decide if heads or tails. 
  
import random 

coin = random.randint(0,1)

if coin == 0:
  print("heads")
if coin == 1:
  print("tails")

  
List:
#Remeber list always starts from 0 binary

state1 = ["london", "luton"]

#if you want to modify binary 0 for example luton and change this to luton1, can do so by doing the below
state1[1] = "luton1" 

#if you want print, do this below
print(state1[0])

# if you want to go backward in binart can simply type in the minus key (-)

state = ["London", "Luton", "US", "Canada"]
print(state[-1])

#If you want to add additonal to the end of the list, simply using the append will do this for you

state.append("California")
print(state)


# Can also use the extend argument to add multiple of lines
state.extend(["California", "Seattle"])


Challenge 2:
  
import random

# Split string method
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

#Write your code below this line 👇

#Get the total number of items in list.
num_items = len(names)
#Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")

# Using random.choice can also do a much better job then above as it would select for you the names specified directly under random

person_who_will_pay = random.choice(names)
orint(person_who_will_pay)


#Adding list together

fruits = ["stawberries", "apple", "pears"]
vegetables = ["spinish", "tomatoes", "patatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# How to prevent list index out of range error

fruits = ["stawberries", "apple", "pears"]
fruit_length = len(fruits)

#without the -1, the error list index out of range would be seen, cause by default the list above would be classified as starting from 1 to 3 and not in binary 0 to 2. 
#simply stating -1, would make it stating pears as full as stawberries is 0, apple 1 and pears is now 2.
print(fruits[fruit_length -1])


challenge 3:
  
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0]) 
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

oe can do selected row this way,


challenge 4:
  
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("computer chose: ")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
