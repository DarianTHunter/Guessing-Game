# #Python 2 Code

import random

#gives order to randomly choose a number
number = random.randint(1, 10)

#initial server response
player_name = raw_input("Hi, Im Ralph. What's your name? ")

#tells server how many guesses the user gets
number_of_guesses = 0

#prompts user to guess for a number between 1 and 10
print('How do you do '+ player_name+ '? Would you like to guess how many fingers im holding up?:')

#while loop with if and else statements
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print ('Your almost there')
    if guess > number:
        print ('You just missed it')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries! Great job!')
else:
    print('You were so close, The number was ' + str(number))
#     #this is where our modules are imported

# import random

# #gives order to randomly choose a number
# number = random.randint(1, 10)

# #initial server response
# player_name = raw_input ("Hi, Im Ralph. What's your name? ")

# print('Hi ' + player_name+ '! ')

# player_response = raw_input ("Would you like to play a game?: ")
# true = yes

# if player_response == true
# number_of_guesses = 0

#     print('Awesome' + player_name+ '! Guess how many fingers im holding up!?')

# else:

#     print('Well i didnt really want to play with you either')

    
# #while loop with if and else statements
# while number_of_guesses < 5:
#     guess = int(input())
#     number_of_guesses += 1
#     if guess < number:
#         print 'Your almost there'
#     if guess > number:
#         print 'You just missed it'
#     if guess == number:
#         break
# if guess == number:
#     print'You guessed the number in ' + str(number_of_guesses) + ' tries! Great job!'
# else:
#     print'You were so close, The number was ' + str(number)


