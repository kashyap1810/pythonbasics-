#change the number from 1 to 1 million
#game asked to guess the number
#give a clue is the number is higher or lower
#inform the player if he won

from random import randint #random is from dictionary and randint is for random integer already in directory
start=1
end=10000
value=randint(start,end)
print('the computer choose a number b/w',start,'and',end)
guess=None
while guess != value:
    text=input('guess the number:')
    guess=int(text)

    if guess<value:
        print('the number is higher :')
    elif guess>value:
        print('the number is lower :')
    else:
        print('congratulations you guess the number and you won ')