Day 3 Orojects:

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
