Day 3 Orojects:

print("Welcome to the coding club")

path1 = input('Hello\'s peeps, welcome to the coding club, where do you want to go ? "golang" or "python" \n').lower()

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
