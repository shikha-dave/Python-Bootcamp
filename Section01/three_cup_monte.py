def myfunc(stringValue):
    newString = ''
    for i in range(0, len(stringValue)):   
        if i % 2 == 0: 
            newString += stringValue[i].upper()
        else:  
            newString += stringValue[i].lower()
    print(newString)

myfunc('longstring')

""" mylist = [' ', 'O', ' ']
from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return      

def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1 or 2: ")
    return int(guess)

myindex = player_guess()

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        return "Correct guess!"
    else:
        return "Wrong guess!"



print("Welcome to the Three Cup Monte Game!")
print("The cups are shuffled...")
print(check_guess(shuffle_list(mylist), myindex)) """