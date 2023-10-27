def q1a1():
    num = int (input ("Enter whole number: "))
    if num % 10 == 2 or num % 10 == 5 or num % 10 == 7:
        print ('Group A')
# q1a1()

def q1a2():
    s = input ("Enter string: ")
    if len(s) != 7:
        print ('Invalid')
    elif s[0] not in 'ABC':
        print ("Invalid")
    else:
        print ("Valid")
# q1a2()

def q1a3():
    s = input ("Enter string: ")
    if 'A' in s[-3:] or 'a' in s[-3:]:
        print ("Group A")
    elif 'B' * 3 in s[-3:] or 'b' * 3 in s[-3:]:
        print ("Group B")
    else:
        print ("Group C")
# q1a3()

def q1b1():
    s = '1254856439'
    for n in s:
        if int (n) % 2 == 1:
            print (n, end = ' ')
# q1b1()

def q1b2():
    s = '1254856439'
    for n in range (len(s) - 1, 1, -1): # excludes the first and last digit
        if s[n] < s[n-1] and s[n] < s[n+1]:
            print (s[n], end = ' ')
# q1b2()

def q2():
    '''
    I would use 2 separate dictionaries for ICT133 and ICT162 students for all 3 tasks, with the key being the student's ID, and the value being the student's score.
    
    For task 1, I would have 2 variables, count133 and count162, both = 0, and do a for loop to count how many students in each dictionary failed.
    Then, I would do count133 - count162 to get the answer.
    
    For task 2, I would run a for range loop on both dictionaries, and check if the same key in both dictionaries failed to meet the passing mark.
    If there are any, return True. Else, return False once the for loop has ended.
    
    For task 3, I'll create an empty list for both modules, list133 and list162. I'll run a for loop on both dictionaries, and if the value is below the pass mark, add them to the respective lists.
    Then, sum the list and divide by the length of list.
    '''
    
def allSameValuesInSequence(seq):
    for n in range(len(seq) - 1):
        if seq[n] != seq[n+1]:
            return False
    return True

def allDifferentValuesInSequence(seq):
    chklist = []
    for n in seq:
        if n not in chklist:
            chklist.append(n)
    if len(chklist) != len(seq):
        return False
    else:
        return True

def readNumbers():
    numlist = []
    while True:
        num = input ("Enter whole number: ")
        if num == '':
            if len(numlist) >= 2:
                break
            else:
                print ("Please enter at least two numbers before ending input session.")
        if num != '':
            numlist.append(int(num))
    return numlist

def q3():
    numbers = readNumbers()
    while True:
        print ('Menu\n' +\
            '1. Read another number sequence\n' +\
                '2. Determine if all numbers are the same\n' +\
                    '3. Determine if all numbers are unique\n' +\
                        '0. Exit')
        
        choice = input ('Enter choice: ')
        if choice == '1':
            numbers = readNumbers()
        elif choice == '2':
            chksame = allSameValuesInSequence(numbers)
            if chksame is True:
                print (f'All numbers are the same in {numbers}')
            else:
                print (f'Not all numbers are the same in {numbers}')
        elif choice == '3':
            chkdiff = allDifferentValuesInSequence(numbers)
            if chkdiff is True:
                print (f'All numbers are different in {numbers}')
            else:
                print (f'Not all numbers are different in {numbers}')
        elif choice == '0':
            print ("Program end.")
            break
        else:
            print ("Invalid choice, please choose again.")
# q3()

def updateSalesToDate():
    itemdict = {}
    salesfile = open ('sales.txt', 'r')
    salestodatefile = open ('salesToDate.txt', 'r')
    sales = salesfile.readlines()
    salestodate = salestodatefile.readlines()
    salesfile.close()
    salestodatefile.close()
    for n in salestodate:
        k, v = n.split()
        itemdict[k] = int (v)
    for n in sales:
        k, v = n.split()
        if k not in itemdict.keys():
            itemdict[k] = int (v)
        else:
            itemdict[k] += int (v)
    print (itemdict)
    fw = open ('salesToDate.txt', 'w')
    for k, v in itemdict.items():
        print (k, v, file = fw)
    fw.close()

def q4a():
    updateSalesToDate()
# q4a()

import random

def getOneSale(pricedict):
    saledict = {}
    for k in pricedict.keys():
        while True:
            choice = input (f'{k.capitalize():10} (Y/N): ').upper()
            if choice == 'Y':
                qty = random.randint (1,15)
                saledict[k] = qty
                break
            elif choice == 'N':
                break
            else:
                print ("Invalid option, please select Y or N.")
    return saledict

def getReceipt(saledict, pricedict):
    total = 0
    fill = ''
    w = 10
    for k, v in saledict.items():
        amount = pricedict[k] * v
        print (f'{v:02d} x {k:{w}} = ${amount:>5.2f}')
        total += float(amount)
    print (f'Total{fill:{w}} = ${total:>5.2f}')
    

def q4b():
    prices = {'pencil': 1.85, 'pen': 1.90, 'notebook': 0.90, 'lead': 2.50}
    sale = getOneSale(prices)
    getReceipt(sale, prices)
# q4b()