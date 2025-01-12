import random


Coin = ['H', 'T']
TotalSimulations = 10000
numberOfSimulationsWithStreaks = 0
for i in range(TotalSimulations):
    CoinFlips = []
    count = 0
    headOrTail = ''
    heads = 0
    tails = 0
    isSequence = False
    while count < 100:
        headOrTail = random.choice(Coin)
        CoinFlips.append(headOrTail)
        if heads == 6 or tails == 6:
            heads = 0
            tails = 0
            isSequence = True
        if headOrTail == 'H':
            heads += 1
            tails = 0
        elif headOrTail == 'T':
            tails += 1
            heads = 0
        if heads == 1 or tails == 1:
            startIndex = count
        count += 1

    if isSequence:
        numberOfSimulationsWithStreaks += 1

streakChance = (numberOfSimulationsWithStreaks * 100) / TotalSimulations
print(f'Chance of streak: {streakChance}%')
