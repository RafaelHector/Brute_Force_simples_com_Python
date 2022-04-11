import random
number = int(input('Input a number that is a password: '))
guess = 0
while (guess != number):
    guess = random.randint(0,99999)
    print(guess)
print('your password is:' + str(number))