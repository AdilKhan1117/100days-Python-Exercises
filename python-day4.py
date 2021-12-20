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
