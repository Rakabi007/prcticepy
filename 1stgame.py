# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 23:11:24 2020

@author: RANA
"""

import random
def gamewin(system, user_input):
    if system == user_input:
        
        return None
    if system =='s':
        if user_input =='w':
            return False
        elif user_input =='g':
            return True
    elif system == 'w':
        if user_input =='g':
          return False
    elif user_input == 's':
          return True
    elif system =='g':
       if user_input =='s':
          return False
    elif user_input =='w':
         return True

print("computer turn : Snake('s') Water('w') or Gun('g')")
randNo = random.randint(1, 3)
if randNo == 1:
    system = 's'
elif randNo== 2:
    system =='w'
if randNo == 3:
    system == 'g'
       
user_input = input("your Turn : Snake('s') water('w') or Gun('g')")
a = gamewin(system, user_input)
print (f"computer chose {system}")
print (f"your turn {user_input}")
if a == None:
   print("the is a tie!")
elif a:
   print("you win!")
else:
   print("you lose!")




