from random import choice
def Q1Ai():
    n = 20
    n1 = n2 = 0
    for _ in range (n):
        coin = choice('HT')
        if coin == 'H':
            n1 += 1
        else:
            n2 += 1
    if 0.45 <= n1/(n1 + n2) <= 0.55:
        fair = True
    else:
        fair = False
    print (fair)
# Q1Ai()


def Q1Aii():
    s = input ("Enter string: ")
    halfpoint = len(s) // 2
    firsthalf = s[:halfpoint]
    if len(s) % 2 != 0:
        halfpoint += 1
    secondhalf = s[halfpoint:]
    if firsthalf.count('a') == secondhalf.count('a'):
        print ("SAME")
    elif firsthalf.count('a') < secondhalf.count('a'):
        print ("FIRST HALF FEWER")
    else:
        print ("FIRST HALF MORE")
# Q1Aii()


def Q1Bi():
    s = 'mississippi'
    os = ''
    
    for i in range (len(s)-1):
        if s[i] != s[i+1]:
            os += s[i]
        print (s[i], os)
            
    if s[-1] != os[-1]:
        os += s[-1]
        
    print (os)
             
    # for i in range (len(s)):
    #     if i != len(s) - 1 and s[i] != s[i+1]:
# Q1Bi()


def Q1Bii():
    w1 = 'solve'
    w2 = 'live'
    w1List = list (w1)
    for c in w2:
        if c in w1List:
            w1List.remove(c)
        else:
            print ("Impossible")
            break
    else: # completed the loop without breaking
        print ("Possible")
# def Q1Bii()


def Q2a():
    staffSalaryList = [['p111', 2000], 
                       ['p123', 3000],
                       ['p023', 4000]]
    staffSalaryList[0][1] = 2500
    for r in range (len(staffSalaryList)):
        if staffSalaryList [r][0] == 'p123':
            staffSalaryList [r][1] = 3600
            print ('Updated!')
            break
    else:
        print ("Unable to locate")
    total = 0
    
    for r in range(len(staffSalaryList)):
        total += staffSalaryList[r][1]
    avg = total / len(staffSalaryList)
    
    for r in range (len(staffSalaryList)):
        if staffSalaryList[r][1] > avg:
            print (staffSalaryList[r][0])
    
    staffSalaryList.sort()
    sortList = sorted (staffSalaryList)
    ss = sorted(sortList, reverse = True, key = lambda elem: elem[1])
    
    staffSalaryList.sort()
    staffSalaryList.sort(reverse=True, key = lambda elem: elem[1])
    
    for r in range(len(staffSalaryList)):
        print (staffSalaryList[r][0], staffSalaryList[r][1])
# Q2a()


def Q2b():
    staffSalaryList = [['p111', 2000], 
                       ['p123', 3000],
                       ['p023', 2500]]
    
    staffSalaryDict = {}
    for row in staffSalaryList:
        staffSalaryDict[row[0]] = row[1]
    
    staffSalaryDict = {}
    for k, v in staffSalaryList: # list unpacking
        staffSalaryDict[k] = v
    
    staffSalaryDict = {k:v for k, v in staffSalaryList}
    
    print (len(staffSalaryDict))
    
    k = 'p123'
    if k in staffSalaryDict:
        staffSalaryDict[k] = 3600
        print ("Updated")
    else:
        print ("Unable to locate")
        
    sl = list(staffSalaryDict.items())
    
    sl.sort()
    sl.sort(reverse=True, key = lambda elem: elem[1])
    
    for r in range(len(sl)):
        print (sl[r][0], sl[r][1])
# Q2b()

# def addNumbers(x, y, z = 10): # assign default value, default value must always be after non-default value
#     return x + y + z

# print (addNumbers(1, 2, 3))

# print (addNumbers(1, 2))

def checkSequence(s):
    if not s:
        return True
    
    slist = s.split(',')
    start = int (slist[0])
    
    for count, c in enumerate (slist, start):
        print (count, c)
        if c != '-' and int(c) != count:
            return False
    return True

def q4a():
    print (checkSequence('2,-,-,5,6,-,-'))  
    print (checkSequence('1, 2,-,-,6,-,-,-'))
# q4a()

def q4b():
    f = open ('data.txt')
    f2 = open ('output.txt', 'w')
    
    for line in f:
        f2.write(f'{checkSequence(line.strip())}\n')
    
    f.close()
    f2.close()
# q4b()

from random import randint
def generateSequence(length):
    if length <= 0:
        return ''
    
    start = randint (1, 20)
    lst = [str(start)]
    count = 0
    for _ in range(length-1):
        if count == 0:
            pop = ['-', str(start +1)]
        else:
            pop = ['-', str(start + count + 1), str(start + count + 2)]
        c = choice(pop)
        if c == '-':
            count += 1
        else:
            start = int(c)
            count = 0
        lst.append(c)
        print (c, lst)
        
    return ','.join(lst)

def q4c():
    generateSequence(3)
    generateSequence(5)
# q4c()

def q4d():
    while True:
        length = int (input ('Enter length of sequence to generate and 0 to end: '))
        if length < 0:
            print ('Length of sequence must be a positive number.')
        elif length == 0:
            print ("Program end.")
            break
        else:
            s = generateSequence(length)
            print (f'{s} : {checkSequence(s)}')
# q4d()