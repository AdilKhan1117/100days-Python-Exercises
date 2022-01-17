Using for Loops. These are used to loops blocks of cpde (repeat)

fruits = ["Apple", "Peach", "Pears"]

for fruits in fruits:
  print(fruits) #This will loop around and print each object inside fruits 
  print(fruits + "pie") #This will loop and add 'pie' to each object, like this 
  
  #apple pie
  #peach pie
  #pears pie
  
  Challenge 1:
  Done use 'sum' or 'len', use only for loop, hoever i will show both being used.
  
  Without For loop:
    
  # 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇


#Sum is used to add all numbers within the object
#Len is also used to add up total length of characters however by using split above, we are only adding individual lines of numbers. 

total_heights = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_heights / number_of_students) 
print(average_height)

or this method using 'for loops' 

total_height = 0
for height in student_heights:
  total_height += height
print(total_height) 

number_of_students = 0 
for student in student_heights:
  number_of_students += 1
print(number_of_students)

average_height = round(int(total_height / number_of_students)) 
print(average_height )
#print(number_of_students)


Challenge 2:
  
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

min_student_score = min(student_scores)
max_student_score = max(student_scores)

print(min_student_score)
print(max_student_score)

the min and max field allows you to understand what is the highest value and lowest. however we are going to be using for loop again for this:
  
Challenger 3:
  
  
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇


max_value = None 
for num in student_scores:
  if (max_value is None or num > max_value):
    max_value = num
print("Maximum score:", max_value)

or:


#So starting with a 0 score, the 'for loop', runs a loop to indicate the highest score by calculating going through -
#the numbers and checking if the previous score is higher then the recent one until it finds the highest, the high_score only updates if the score looped is greater than
#score

high_score = 0
for score in student_scores:
  if score > high_score:
    high_score = score
print("Maximum score:", high_score)


Loops and Ranges:
  
#This will print out the numbers from 1 to 9
for number in range (1,10):
  print(number)

 #This will skip 3 numbers 
for number in range (1,10, 3):
  print(number)

 #This will add all the numbers up
total = 0
for number in range (1,101):
  total += number
print(total)


Challenge 3:
  
Calculating sum of all even numbers using range:
  
#to get the even numbers, in the range field start with 2 even number, as we know from the previous days using modulo % 2 == 0 allows us to understand this gives us even numbers
#once we do this by using the if condition we can than use the total += numbers, this simply add 0 + the sum which is calculated to total, it is saying add all the numbers in the range
#if numbers are even. 

total = 0 
for numbers in range(2, 101):
  if (numbers % 2 == 0):
    total += numbers
print(f"{total}")


Challenge 4:
  
Instructions
You are going to write a program that automatically prints the solution to the FizzBuzz game.

Your program should print each number from 1 to 100 in turn.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

`When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
`When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
`And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

#Write your code below this row 👇

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

  
Challenge 5:
  
#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Use empty password string, this allows you to add to this see below the random.choice, adds letters code and inserts it into password
#therange(0, nr_letters) can also be (1, nr_letters + 1) since the characters are starting 1 and 4 letters required it will be 3 so need to add 1 more)
#using the random.choice, this allows you to randomly pick something from letters using choice 

#Can also use append which was used earlier to add the random choice to password see line 189

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for char in range(0, nr_letters):
  password_list += random.choice(letters)

for char in range(0, nr_symbols):
  password_list += random.choice(symbols)

for char in range(0, nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""

for char in password_list:
  password += char

print(f"Your password is {password}")


# 1. In order to randomlise the ordering of the password you need to set the list line 189, this allows you to be able to have the shuffle line 200 and also allows you to contain 
# - all of the values generated from letters, symbols and numbers. 
# 2. using the random choice allows you to randomlise the choice within the variables for example 'letters' will be chosen at random and not in order by using the .random
# 3. to add the random into the password_list, you need to join password_list with random by using the += operator this allows you to simply say password_list equals random.choice(xx)
# 4. random.shuffle is then used to randomlise the ordering of the list so instead of going by order of presedence like letters,symbols and numbers it will randomly going in any order
# 5. now to bring back configuring the password output as a string format instead of a wierd list format you need to create a new var like password = ""
# 6. Finally you need get the outprint into password from the password_list above by using the for loop and adding char into the password variable 
