**Data Types:**

print("hello"[0]) = H 

print(123 + 345) = 4568



whereas, string is not required

print("123") + ("345") = 123345



**Interger**

#In Python 100,000 should be like this 100_000

print(10_000 + 10_000)



**Floats**

print(1.5 + 1.5) = 3.0



**Boolean: No quotation mark**

True 

False



**Len does not work with integers** 

if your not sure ever what type of data type this is 

you can always do this:  This would identify the type of format the code is in i.e if its a str,int or float.


print(type(num_char))

num_char = len(input("how old are you ? "))

new_numb = str(num_char)


print("what is your name" " " + new_numb )

To comment out lines just do this:

**command button on mac**

**then this backslash /**

**Needed to turn string into interger as remember a string concatenates number and a integer** 



Coding Challenge 1:

  
# 🚨 Don't change the code below 👇

two_digit_number = input("Type a two digit number: ")

# 🚨 Don't change the code above 👆

####################################

#Write your code below this line 👇


first_number = two_digit_number[0]

second_number = two_digit_number[1]

result = int(first_number) + int(second_number)

print(result)



Coding challenge 2:
**Calculating Maths** 

# 🚨 Don't change the code below 👇

height = input("enter your height in m: ")

weight = input("enter your weight in kg: ")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height_new = float(height)

weight_new = int(weight)

bmi_calculate = weight_new / height_new ** 2

print(int(bmi_calculate))


Challenge 3:
  
  
**Rounding numbers:**

print(round(8/3))

print(round(8/3, 2)) to round it off nearest 2 

print(8//3) does the same thing as rounding it off to the nearest number 



**Using this function** 

score = 4/2

score /=2

print(score)



**using string in print, must use the F string to print the score** 

score = 0

print(f"how are you ? + {score}")


challenge 3:
  
 
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${final_amount}")
