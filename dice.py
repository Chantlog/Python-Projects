import random

numDice = int(input("How many dice would you like to roll?"))

diceDictionary = {
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0
}

for x in range(numDice):
    num = random.randrange(1,7)
    diceDictionary[num] += 1

for x in range(1,7):
    print( "%s : %s" %(x,diceDictionary[x]))

exit = False
while not exit:
    input()
    exit = True
