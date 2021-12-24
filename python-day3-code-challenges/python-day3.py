Day 3 Project:
  
  
  
Challenge 1:

# 🚨 Don't change the code below 👇

number = int(input("Which number do you want to check? "))

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:

print("This is a odd number")

else:

print("This is an even number")

== (Equal)

!= (Not equal to)

< (less than)

> . (Greater than)

>. = (Greater than or equal to)

bmi = round(weight / height ** 2)

if bmi == 18:

     print(f"hello {bmi}")

elif bmi 25:

     print(f"by {bmi}")

else:

     print(f"hello again {bmi}") 

    
    
Challenge 2:

# 🚨 Don't change the code below 👇

height = float(input("enter your height in m: "))

weight = float(input("enter your weight in kg: "))

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = float(round(weight / height ** 2))

if bmi < 18.5:

print(f"Your BMI is {bmi}, you are underweight")

elif bmi > 18.5:

print(f"Your BMI is {bmi}, you have a normal weight")

elif bmi > 25:

print(f"Your BMI is {bmi}, you are slightly overweight")

elif bmi > 30:

print(f"Your BMI is {bmi}, you are obese")

elif bmi > 35:

print(f"Your BMI is {bmi}, you are clinically obese")



Challenge 3:

# 🚨 Don't change the code below 👇

year = int(input("Which year do you want to check? "))

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:

  if year % 100 == 0:

     if year % 400 == 0:

    print("Leap year")

  else:

  print("not a leap year")

  else:

  print("leap year")

else:

print("not a leap year")

it goes in order as in leap year is attached to % 4 and not leap year to %100 and so on for %400 for leap year and finally else statements 



Challenge 4:

print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:

print("You can ride the rollercoaster!")

age = int(input("What is your age? "))

if age < 12:

bill = 5

print("Child tickets are $5.")

elif age <= 18:

bill = 7

print("Youth tickets are $7.")

else:

bill = 12

print("Adult tickets are $12.")

wants_photo = input("Do you want a photo taken? Y or N. ")

if wants_photo == "Y":

bill += 3

print(f"Your final bill is ${bill}")

else:

print("Sorry, you have to grow taller before you can ride.")



Challenge 5:

# 🚨 Don't change the code below 👇print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ")

add_pepperoni = input("Do you want pepperoni? Y or N ")

extra_cheese = input("Do you want extra cheese? Y or N ")# 🚨 Don't change the code above 

#Write your code below this line 👇
##Added variable bill, this allow you to use this to add calculation for the bill##

bill = 0

#Using the += allows you to add the bill current value plus whichever value you specify#

if size == "S":  

   bill += 15

if size == "M":  

    bill += 20

else:  bill += 25

if add_pepperoni == "Y":  

if size == "S":    

bill += 2 

else:  

bill += 3
if extra_cheese == "Y":  

bill += 1
print(f"Your final bill is: ${bill}")

Logical operators

And x and y

Or x or y 

Not not x 




Challenge 6:

# 🚨 Don't change the code below 👇

print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")

name2 = input("What is their name? \n")# 🚨 

Don't change the code above 👆
#Write your code below this line 👇
name = name1 + name2 = name.lower()
t = object_lower.count("t")

r = object_lower.count("r")

u = object_lower.count("u")

e = object_lower.count("e")
l = object_lower.count("l")

o = object_lower.count("o")

v = object_lower.count("v")

e = object_lower.count("e")

true = t + r + u + e

love = l + o + v + e

# if you need to include the int, you can do it this way, so this is int for the whole line however -# you need to put str next to love also for it to be as a string

love_score = int(str(true) + str(love))
if (love_score <= 10) or (love_score >= 90): 

print(f"your score is {love_score}, you go together ")

elif (love_score >= 40) and (love_score <= 50):  

print(f"your score is {love_score}, you are alright together. ")

else:  print(f"Your score is {love_score}")

  
  
Challenge 7:

Welcome to the coding club: Final Project
  
print("Welcome to the coding club")

#If you have a comma for example, intentionally i had put a comman stating 'hello's', just so i could show, you cannot have all double quotes as golang and python are inputs -
#This needs to be in this format

path1 = input('Hello\'s peeps, welcome to the coding club, where do you want to go ? "golang" or "python" \n').lower() #lower was used so if anyone typed in caps it would user lower case instead

# If you can see the lines are indented according to the action the condition is taking place.
if path1 == "python":
  path2 = input("do you want to purchase a course, no or yes ? ")
  if path2 == "yes":
    path3 = input('If so, from which site ? "udemy", "pluralight", "linuxacademy" ')
    if path3 == "udemy":
      print("good choice")
    elif path3 == "pluralsight":
      print("wrong choice")
    elif path3 == "linuxacademy":
      print("its okay")
    else:
      ("keep searching")
  else:
    print("see you soon")
else:
  ("wrong choice")
#the above else block is accoring to the first line of code, line 11, else block.
