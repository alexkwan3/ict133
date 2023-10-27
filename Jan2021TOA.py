def q1a1():
    num = int (input ("Enter whole number: "))
    if num // 10 == 1 or num % 10 == 1:
        print ("Valid")
    else:
        print ("Invalid")
# q1a1()

def q1a2():
    s = input ("Enter string: ")
    if s[0] == s[1] == s[2]:
        print ("Group A")
    elif s[0] == s[2] != s[1]:
        print ("Group B")
    else:
        print ("Group C")
# q1a2()

def q1a3():
    # nList = [1, 3, 2]
    nList = []
    while True:
        num = input ("Enter number: ")
        if num == '':
            break
        else:
            nList.append(int(num))
    print (nList[::2])
    total = sum(nList[::2])
    print (total)
    if total % 2 == 0:
        print ('Sum of digits in even positions is even.')
    else:
        print ('Sum of digits in even positions is odd.')
# q1a3()

def q1b1():
    s = input ("Enter string: ")
    for n in s[::-1]:
        print (int (n) - 1)
# q1b1()

def q1b2():
    s = input ("Enter string: ")
    for n in range (len(s)-1):
        if int(s[n]) + int(s[n+1]) > 12:
            return False
    return True
# print (q1b2())

def q2():
    '''
    I will use a dictionary to store both collections, with the product name as key and prices as value.
    
    Task 1: Create 2 variables that = 0. Run a for loop, add the prices into the variable that = 0. 
    Divide by the respective len(dict) to get the average price for both stores.
    Take average X - average Y to get the difference.
    
    Task 2: Create an empty dictionary cheaperX = {}. Run a for loop on dictX, if v < dictY[k], cheaperX[k] = v.
    Run a for loop on cheaperX to display the name and prices of the items that are cheaper in store X.
    
    Task 3: Create variable item = input ('Enter product name: '). If item in dictX.keys() and item in dictY.keys(), 
    print (dictX[item], dictY[item])
    '''
    
import random

def roll():
    total = 0
    nlist = []
    while True:
        if len(nlist) == 3:
            break
        num = random.randint(1,6)
        if num not in nlist:
            nlist.append(num)
    total = sum(nlist)
    return total

def playGame(plist, maxLimit):
    dvalues = []
    highest = 0
    highestlist = []
    for n in range (len(plist)):
        dice = roll()
        dvalues.append(dice)
        if dice <= maxLimit and dice >= highest:
            highest = dice
    for n in range (len(dvalues)):
        if dvalues[n] == highest:
            highestlist.append(plist[n])
    txt = ''
    for n in highestlist:
        txt += f'{n} '
    return txt

def q3():
    playerList = ['A', 'B', 'C', 'D', 'E']
    maxLimit = 12
    while True:
        print ('Menu\n' +\
            '1. Change max limit for sum of 3 rolls\n' +\
            '2. Play Game\n' +\
            '0. Exit')
        choice = input ("Enter choice: ")
        if choice == '1':
            limit = int (input ("Enter new max limit: "))
            if limit < 10:
                print ("Please enter a number that is at least 10.")
            else:
                maxLimit = limit
                print (f'New max limit: {maxLimit}')
        elif choice == '2':
            game = playGame(playerList, maxLimit)
            print (game)
        elif choice == '0':
            print ("Game end.")
            break
        else:
            print ("Invalid choice.")
# q3()

def getProductDict():
    productdict = {}
    fr = open ('products.txt', 'r')
    lines = fr.readlines()
    fr.close()
    for n in lines:
        code, price, name = n.split(',')
        productdict[code] = [price, name.strip()]
    return productdict

def writeProductToFile(pdict):
    pdict2 = {}
    fw = open ('products.txt', 'w')
    for k, v in pdict.items():
        pdict2[float(v[0])] = [k, v[1]]
    pkeys = sorted(pdict2.keys())
    for n in pkeys:
        print (f'{pdict2[n][0]}, {n:.2f}, {pdict2[n][1]}', file = fw)
    fw.close()
    
def q4():
    products = getProductDict()
    print (products)
    
    while True:
        pcode = input ("Enter product code: ").upper()
        if pcode == '':
            print ('Program end.')
            break
        while True:
            newprice = float (input ("Enter new price: "))
            if newprice < 0:
                print ("Price must be a positive value.")
            else:
                break
        if pcode in products.keys():
            products[pcode][0] = newprice
            print (f'Updating entry {pcode} with new price {newprice:.2f}')
        else:
            pname = input ("Enter product name: ").capitalize()
            products[pcode] = [newprice, pname]
    
    print (products)
    writeProductToFile(products)    
# q4()