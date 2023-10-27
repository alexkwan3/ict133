import math

def q1a():
    c = int (input ("Enter longest side: "))
    a = int (input ("Enter shorter side: "))
    bsq = c**2 - a**2
    b = math.sqrt(bsq)
    print (b)
# q1a()

def q1b():
    a = float (input ("Enter side a: "))
    b = float (input ("Enter side b: "))
    c = float (input ("Enter side c: "))
    
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c **2 == a**2:
        print (f"These 3 sides [{a, b, c}] can form a right-angled triangle.")
    else:
        print (f"These 3 sides [{a, b, c}] CANNOT form a right-angled triangle.")
# q1b()

def q2():
    cost = 0
    while True:
        option = input ('<<Cafe Menu>>\n' +\
        'A. Soup of the day\n' +\
            'B. Garden Salad\n' +\
                'C. BLT Sandwich\n' +\
                    'X. Exit\n' +\
                        'Enter your order: ').upper()
        if option == 'X':
            if cost > 20:
                while True:
                    member = input ("Are you a member? (Y/N): ").upper()
                    if member == 'Y':
                        cost = cost * 0.9
                        break
                    elif member == 'N':
                        break
                    else:
                        print ("Invalid option, please select Y or N.")
            print (f"Thank you, please pay ${cost:.2f}")
            break
        elif option == 'A':
            cost += 3.50
        elif option == 'B':
            cost += 4.50
        elif option == 'C':
            cost += 5.50
        else:
            print ('Invalid option, please choose again.')
# q2()

import random

def getDiceValues(num:int):
    dicelist = []
    for n in range (num):
        dice = random.randint(1,6)
        dicelist.append(dice)
    dicelist.sort(reverse=True)
    return dicelist

def q3():
    rounds = 10
    p1 = input ("Enter player 1 name: ").capitalize()
    p2 = input ("Enter player 2 name: ").capitalize()
    p1dice = getDiceValues(rounds)
    p2dice = getDiceValues(rounds)
    
    p1count = 0
    p2count = 0
    for n in range (rounds):
        if p1count == 2:
            print (f'{p1} is the winner!')
            break
        if p2count == 2:
            print (f'{p2} is the winner!')
            break
        if p1dice[n] == p2dice[n]:
            p1count, p2count = 0, 0
            print (f'Round {n+1} - {p1} {p1count} : {p2} {p2count}')
        elif p1dice[n] > p2dice[n]:
            p1count += 1
            p2count = 0
            print (f'Round {n+1} - {p1} {p1count} : {p2} {p2count}')
        else:
            p2count += 1
            p1count = 0
            print (f'Round {n+1} - {p1} {p1count} : {p2} {p2count}')
    else:
        print ('Draw')
# q3()

def countRepeatingChar(word: str):
    countlist = []
    for n in word:
        countlist.append(word.count(n))
    return max(countlist)

def initializeDictionary(filename: str):
    stats = {}
    wordlist = []
    fr = open (filename, 'r')
    lines = fr.readlines()
    # print (lines)
    fr.close()
    for n in lines:
        n = n.split(' ')
        # print (n)
        for i in n:
            i = i.strip()
            wordlist.append(i)
            # print (wordlist)
            stats[countRepeatingChar(i)] = []
            # print (stats)
    for n in wordlist:
        stats[countRepeatingChar(n)].append(n)  
    return stats

def q4():
    worddict = initializeDictionary('Jan2023TOAtxt.txt')
    order = sorted(worddict)
    fw = open ('mcd.txt', 'w')
    for n in range (2, len(order) + 1):
        txt = ''
        for i in worddict[n]:
            txt += f'{i} '
        print (f'{n}: {txt}', file = fw)
    fw.close()
# q4()