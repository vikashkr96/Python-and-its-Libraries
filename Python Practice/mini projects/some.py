import random

v = random.randint(1,5)
c = int(input('ENTER A NUMBER : '))
if c == v:
    print('YOU GUESSED RIGHT')
else:
    print('YOU GUESSED WRONG')
print("The number is ", v)
import os
print(os.getcwd())


