def q1a():
    
    def add1(a, b):
        # k = a + b # replace a with any other variable name and it is the same
        a = a + b # a is a new variable, therefore does not change the original variable a
        print ('In add1: ', a, b)
        
    def add2(a, b):
        a.append(b) # appends to the list because it is not a new variable
        print ('In add2: ', a, b)
    
    def main():
        a = [1]
        b = [2]
        add1(a, b)
        print ('In main: ', a, b)
        a = [1]
        b = [2]
        add2 (a, b)
        print ('In main: ', a, b)
    # main()
    
    '''
    outputs(i):
    In add1: [1, 2] [2]
    In main: [1] [2]
    In add2: [1, [2]] [2]
    In main: [1, [2]] [2]
    Explanations(ii) in comments above
    '''
# q1a()

def q1b():
    '''
    (i).
    (ii). no because it will result in an infinite loop as the value a will keep increasing. 
    '''
    
    a, b = 1, 9
    while True:
        if abs(a * a - b) < 0.00000000000001:
            break
        a = (a + b / a) / 2
        # a = (a + b) / 2
    print (a)
# q1b()

def q1c():
    a = '123456'
    for i in range (len(a) - 1, -1, -1):
        print (a[i::2])
        # print (i)
    
    '''
    (i). 543210
    (ii). it is printing the string starting from 4-0, ending in index 5, in steps of 2.
    (iii). 6, 5, 46, 35, 246, 135'''
# q1c()

def getGameOutcome(p1, p2):
    if p1 == p2:
        return 0
    if p1 == 0:
        if p2 == 1:
            return 1
        if p2 == 2:
            return 2
    if p1 == 1:
        if p2 == 0:
            return 2
        if p2 == 2:
            return 1
    if p1 == 2:
        if p2 == 0:
            return 1
        if p2 == 1:
            return 2

from random import choice

def chooseShapes(seq):
    p1 = choice(seq)
    p2 = choice(seq)
    return p1, p2

def q2():
    game = {'names': ['John', 'Peter'], 'Winners': [1, 0, 2, 1, 1, 2, 0, 1, 1, 0]}
    
    print ("Game Summary")
    print (f"Number of games drawn: {game['Winners'].count(0)}")
    print (f"Number of games John won: {game['Winners'].count(1)}")
    print (f"Number of games Peter won: {game['Winners'].count(2)}")
    
    shapeskv = {'Shapes': ('scissors', 'paper', 'stone')}
    
    numgame = 10 # choose how many games to play
    
    for n in range (numgame):
        seq = (0, 1, 2)
        p1, p2 = chooseShapes(seq)
        print (f"P1: {shapeskv['Shapes'][p1]}\nP2: {shapeskv['Shapes'][p2]}")
        winner = getGameOutcome(p1, p2)
        if winner == 0:
            print ("Draw")
        else:
            print (f'Winner: Player {winner}')
        game['Winners'].append(winner) # appends to the dictionary key 'Winners'
    
    print (game)
# q2()