# CoLAB paired programming code 2019
# By the Pythons
#
# This code is from paired programming workshops
# --Verified basic function
#
# Contact John T Haworth for questions

guessesTaken = 0
guess = 0

name = input("What is your name? ")
import random
for X in range (1):
    number = (random.randint(1,51))
    int (random.randint(1,51))
    print('Well, ' + name + ', I am thinking of a number between 1 and 50.')

while guessesTaken < 6 and guess != number:
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    
    guessesTaken = guessesTaken + 1
    
    if guess < number:
        print('Your guess was too low')
        
    if guess > number:
        print('Your guess was too high')
        
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good Job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')
    
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
