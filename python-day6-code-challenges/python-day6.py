Creating Python Functions:
Goal was to move the robot to the flag using function and using for loop to loop 6 times. 
  
def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for char in range(6):
    jump()

    
 While loop:
 Is something or block of code which will keep going whilst its true.
    
 number_of_hurdles = 6
while number_of_hurdles > 0:
  jump()
  number_of_hurdles -= 1
  print(number_of_hurdles)
    
    
    
    
    
    
    
    
    
    
    
    
