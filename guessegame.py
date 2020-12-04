# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:55:15 2020

@author: RANA
"""
#this is a guess the number game
import random
print('hello what is your name?')
name = input()
print('well,' + name + ',i am thinking of a number between 1 and 20.')
secret_number = random.randint(1, 20)

for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())
    
    
    if guess < secret_number:
        print('your guess is too low')
    elif guess > secret_number:
        print('your guess Is too High')
    else:
            break
        
        
    if guess == secret_number:
            print('good job,'+ name +'! you guesses my number in '+ str(guessesTaken) +'guesses!')
    else:
                print('nope. The number i was thinking of was'+ str(secret_number))          
    