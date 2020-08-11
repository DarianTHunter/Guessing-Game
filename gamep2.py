#Python 2 Code
    #this is where our modules are imported
import random

#gives order to randomly choose a number
number = random.randint(1, 10)

#initial server response
player_name = raw_input ("Hello, What's your name?")

#tells server how many guesses the user gets
number_of_guesses = 0

#prompts user to guess for a number between 1 and 10
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

#while loop with if and else statements
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print 'Your guess is too low'
    if guess > number:
        print 'Your guess is too high'
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))

