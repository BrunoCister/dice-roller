
from random import randint

def diceRoller():

    print('How many dice?')
    diceQuant = input()

    print('What size dice?')
    diceSides = input()

    results = []

    while len(results) < int(diceQuant):
        diceRoll = randint(1, int(diceSides))
        results.append(diceRoll)

    add = sum(results)
    
    print(f'Rolling...\n{diceQuant} x d{diceSides}: {results}\nThe sum of all rolls is {add}.')

diceRoller()

print('Roll again? [Y/N]')
again = input()
while again.upper() == 'Y':
    diceRoller()
    print('Roll again? [Y/N]')
    again = input()
    if again.upper() == 'N':
        break