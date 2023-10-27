def q1a():
    s = input ("Enter string: ")
    if len(s) != 8:
        print ("Invalid, length must be 8.")
    elif s[0:3].isupper() is not True:
        print ("Invalid, first 3 characters must be uppercase letters.")
    elif s[3:7].isdigit() is not True:
        print ("Invalid, characters 4-7 must be digits.")
    elif s[-1] not in 'SXZ':
        print ("Invalid, last character must be S, X, or Z.")
    else:
        print ("Valid")
# q1a()

def q1b():
    num = int(input("Enter number <= 10: "))
    for n in range (1, num + 1):
        for i in range(1, num + 1):
            print (f'{i * n:>4}', end = '') # prints from left to right
        print () # prints a new line once nested for loop is done
# q1b()

def getDurationInMinutes(duration):
    h, m = duration.split(':')
    totalmin = (int (h) * 60) + int (m)
    return totalmin

def computeCharge(minutes):
    if minutes <= 10:
        return 'No charge.'
    elif minutes <= 60:
        return 'Please pay $1.50'
    else:
        charge = 1.50 + ((minutes - 60) * 0.02)
        
        if charge < 5:
            return f'Please pay ${charge:.2f}'
        else:
            return 'Please pay $5.00'
    
def q2():
    while True:
        dur = input ("Enter duration (h:mm): ")
        if dur == '':
            print ("Program end.")
            break
        h, m = dur.split(':')
        totalmin = getDurationInMinutes(dur)
        charge = computeCharge(totalmin)
        if int (h) == 0:
            print (f'{m} mins parking. {charge}')
        else:
            print (f'{h} hr {m} mins parking. {charge}')
# q2()

def q3a():
    qtyPrice = [2, 1.5, 4, 0.5, 1, 2.5, 3, 2.0]

    qtypricedict = {}

    for n in range(0, len(qtyPrice), 2):
        qtypricedict[qtyPrice[n]] = qtyPrice[n+1]
        
    total = 0
    
    for k, v in qtypricedict.items():
        print (f'{k} x ${v:.2f} = ${k*v:.2f}')
        total += (k*v)
    
    print (f'{len(qtypricedict)} items.')
    print (f'Total price ${total:.2f}')
# q3a()

def q3b():
    numlist = []

    while True:
        if len(numlist) == 5:
            break
        num = int (input ("Enter number: "))
        index = -1
        for n in range (len(numlist)):
            if num <= numlist[n]: # if num is <= any number in the list, assigns the index of that number
                index = n
                break # breaks so that it stops at the first number it's smaller than
        if index == -1: # index does not change if numlist is empty or num is bigger than all numbers in numlist
            numlist.append (num)
        else:
            numlist.insert(index, num)
        print (numlist)
# q3b()

def q4():
    seatingPlan = {}
    f = open ('seating.txt', 'r')
    lines = f.readlines()
    f.close()
    slines = []
    
    for n in lines:
        slines.append(n.strip().split(','))
    
    for n in slines:
        seatingPlan[n[0]] = n[1:]
        
    # print (seatingPlan)
    
    for k, v in seatingPlan.items():
        print (k, end = ' ')
        for n in v:
            print (n, end = ' ')
        print ()
    
    print (' ', end = ' ')
    for n in range (1, len(seatingPlan['A']) + 1):
        print (n, end = ' ')
    print ()
    
    seatnum = input ("Enter seat no.: ").upper()
    seatkey, seatvalue = seatnum[0], seatnum[1]
    seatvalue = int (seatvalue) - 1
    if seatingPlan[seatkey][seatvalue] == 'X':
        print ("Not available")
    else:
        count = 0
        qty = int (input ("Enter number of seats to book: "))
        
        for n in range (len(seatingPlan[seatkey][seatvalue:seatvalue + qty])):
            if seatingPlan[seatkey][n] == 'X':
                print ('Not available')
                break
            else:
                count += 1
                seatingPlan[seatkey][n] = 'X'
                
        if count == qty:
            print ("Seats successfully allocated.")
    
            for k, v in seatingPlan.items():
                print (k, end = ' ')
                for n in v:
                    print (n, end = ' ')
                print ()
            
            print (' ', end = ' ')
            for n in range (1, len(seatingPlan['A']) + 1):
                print (n, end = ' ')
            print ()
# q4()