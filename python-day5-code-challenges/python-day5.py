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
