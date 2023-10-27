def Q1A():
    sys, dia = input ("Enter blood pressure: ").split('/')
    sys, dia = int(sys), int(dia)
    if sys < 120 and dia < 80:
        print ("Your blood pressure is normal.")
    elif sys <= 129 and dia < 80:
        print ("Your blood pressure is elevated.")
    elif sys <= 139:
        if dia <= 89:
            print ("You have Stage 1 Hypertension.")
        else:
            print ("You have Stage 2 Hypertension.")
    elif sys < 180:
        print ("You have Stage 2 Hypertension.")
    else:
        print ("Hypertensive Crisis!! Consult your doctor immediately.")
# Q1A()


def Q1B():
    while True:
        bp = input ("Enter blood pressure readings (mmHg): ")
        if bp == '':
            print ("Thank you and keep monitoring your blood pressure.")
            break
        sys, dia = bp.split('/')
        sys, dia = int(sys), int (dia)
        if sys < 1 or dia < 1:
            print ("You have entered invalid BP numbers. ")
        elif sys < 90 and dia < 60:
            print ('Your blood pressure is low.')
        elif sys < 120 and dia < 80:
            print ("Your blood pressure is normal.")
        elif sys <= 129 and dia < 80:
            print ("Your blood pressure is elevated.")
        elif sys <= 139:
            if dia <= 89:
                print ("You have Stage 1 Hypertension.")
            else:
                print ("You have Stage 2 Hypertension.")
        elif sys < 180:
            print ("You have Stage 2 Hypertension.")
        else:
            print ("Hypertensive Crisis!! Consult your doctor immediately.")
# Q1B()


def ticketEntry():
    num = []
    for n in range (6):
        pick = int (input (f"Enter number {n+1}: "))
        num.append(pick)
    return num


def ticketValidator(num):
    numlist = []
    for n in num:
        if n > 0 and n < 50 and n not in numlist:
            numlist.append(n)
    if len(numlist) != 6:
        return False
    return True


def Q2a():
    num = ticketEntry()
    print (ticketValidator(num))
# Q2a()


import random

def quickPick():
    num = random.sample(range(1,50), 6)
    return num


def Q2b():
    numlist = quickPick()
    print (numlist)
    print (ticketValidator(numlist))
# Q2b()


def Q2c():
    while True:
        choice = input (f'TOTO Menu\n1. Ticket Entry\n2. Quick Pick\n0. Exit\nEnter choice: ')
        if choice == '1':
            num = ticketEntry()
            valid = ticketValidator(num)
            if valid == True:
                print (f'Your TOTO ticket {num} is valid.')
            else:
                print (f'{num} is an invalid TOTO ticket.')
        elif choice == '2':
            print (f'This is your lucky ticket: {quickPick()}')
        elif choice == '0':
            print ("Good luck to you!")
            break
        else:
            print ("Invalid option.")
# Q2c()


import math

def readPricing(filename, pricing):
    fr = open(filename, 'r')
    lines = fr.readlines()
    fr.close()
    for n in lines:
        key, value = n.split()
        if key.isdigit() == True:
            pricing[int(key)] = float (value)
        else:
            pricing[key] = float (value)
    return pricing


def showPricing(charPricing, fontPricing, fontsize):
    price_string = f'Pricing for font size {fontsize}pts'
    print (price_string)
    print ('=' * len(price_string))
    for i, (k, v) in enumerate(charPricing.items()): # i = index, k = key, v = value
        v = math.ceil(v * fontPricing[fontsize]) # multiplies the price and rounds up to nearest integer
        print (f'{k} {v:.0f}\t', end='') # suppresses the new line
        if i % 7 == 6: # print a new line every 7 indices
            print ()
        
              
def Q3a():
    character_price = {}
    font_price = {}
    readPricing('characters.txt', character_price)
    readPricing('fonts.txt', font_price)
    while True:
        fontsize = int (input("Enter font size: "))
        if fontsize not in font_price.keys():
            print ("Invalid font size.")
        else:
            break
    showPricing(character_price, font_price, fontsize)
# Q3a()


def quote(character_price, font_price):
    char_price = []
    characters = input ("Enter characters: ")
    characters = characters.replace(' ', '')
    for n in characters:
        if n in character_price.keys():
            char_price.append (character_price[n])      
    if len(characters) != len(char_price):
        print ("1 or more characters is invalid.")
    else:
        fontsize = int (input("Enter font size: "))
        if fontsize not in font_price.keys():
            print ("Invalid font size.")
        else:
            total = sum(char_price)
            cost = total / 100 * font_price[fontsize]
            discount = cost * 0.95
            free_character = cost - min(char_price) / 100
            print (f'Price: ${cost:.2f}')
            if cost > 8:
                if min(discount, free_character) == discount:
                    print (f'After 5% discount: ${discount:.2f}')
                else:
                    print (f'After 1 free character: ${free_character:.2f}')
       
        
def addupdatecharacter(character_price):
    character = input ("Enter character: ")
    if character in character_price.keys():
        print (f'Current price is {character_price[character]} cents')
        new_price = float (input ("Enter new price (cents): "))
        character_price[character] = new_price
    else:
        character_price[character] = float (input(f"Enter price for {character}: "))
    return character_price


def addupdatefont(font_price):
    font_size = int (input ("Enter font: "))
    if font_size in font_price.keys():
        print (f'Current price ratio is {font_size}:{font_price[font_size]}')
        new_price = float (input ("Enter new price ratio: "))
        font_price[font_size] = new_price
    else:
        font_price[font_size] = float (input(f"Enter price ratio for {font_size}: "))
    return font_price
   
        
def Q3b():
    character_price = {}
    font_price = {}
    readPricing('characters.txt', character_price)
    readPricing('fonts.txt', font_price)
    monkeystring = 'MonkeyPrint Embroidery Services'
    while True:
        print (monkeystring)
        print ('=' * len(monkeystring))
        print (f"1. Display Pricing Table\n2. Request for Quote\n3. Add/Update Characters' Pricings\n4. Add/Update Font Sizes' Pricings\n0. Exit")
        choice = input ("Enter selection: ")
        if choice == '1':
            Q3a()
        elif choice == '2':
            quote (character_price,font_price)
        elif choice == '3':
            fw = open ('characters.txt', 'w')
            character_price = addupdatecharacter(character_price)
            for k, v in character_price.items():
                print (k,v, file = fw)
            fw.close()
        elif choice == '4':
            fw = open ('fonts.txt', 'w')
            font_price = addupdatefont(font_price)
            for k, v in font_price.items():
                print (k,v, file = fw)
            fw.close()
        elif choice == '0':
            print ("Program end.")
            break
        else:
            print ("Invalid selection.")
# Q3b()


import random

def getNewBoard(size):
    board = []
    for n in range (size):
        board.append(['-'] * size)
    return board


def getPlayerNames():
    player_names = []
    for n in range (2):
        while True:
            name = input (f"Enter player {n+1}'s name: ")
            if name not in player_names:
                player_names.append(name)
                break
            else:
                print ("Player names must be unique.")
    return player_names
        

def printBoard(board):
    rows = len (board)
    cols = len (board)
    print (' ', end = '')
    for n in range (len(board)):
        print ('', n, end = '')
    print ()
    for r in range (rows):
        print (r, end = ' ')
        for c in range (cols):
            print (board[r][c], end = ' ')
        print () # gives a \n to end the columns print


def getNextTile(playerName, symbol, size):
    while True:
        squares = input (f'{playerName}, place your {symbol} tile: ')
        if len(squares) != 5:
            print ("Invalid input.")
        else:
            square1, square2 = squares.split()
            numlist = [int (square1[0]), int (square1[1]), int (square2[0]), int (square2[1])]
            checklist = []
            for n in numlist:
                if n <= size - 1:
                    checklist.append(n)
            if len(numlist) != len(checklist):
                print ("Wrong tile coordinates! Please re-enter.")
            else:
                return square1, square2
        

def validateTile(square1, square2, size):
    row1, col1, row2, col2 = int (square1[0]), int (square1[1]), int (square2[0]), int (square2[1])
    if row1 == row2 and max(col1, col2) - min(col1, col2) == 1:
        return True
    elif col1 == col2 and max(row1, row2) - min(row1, row2) == 1:
        return True
    else:
        return False


def placeTile(board, symbol, square1, square2):
    row1, col1, row2, col2 = int (square1[0]), int (square1[1]), int (square2[0]), int (square2[1])
    if board [row1][col1] == '-' and board [row2][col2] == '-':
        return True
    return False


def isGameAlive(board):
    size = len(board)
    for r in range (size-1):
        for c in range (size-1):
            if board [r][c] == '-' and board [r][c+1] == '-':
                return True
            if board [r][c] == '-' and board [r+1][c] == '-':
                return True        
    return False


def Q4():
    names = getPlayerNames()
    # names = ['a', 'b']
    symbol = ['O', 'X']
    while True:
        size = int (input ("Size of game board: "))
        if size < 3 or size % 2 == 0:
            print ("Invalid board size.")
        else:
            break
    # size = 5
    board = getNewBoard(size)
    printBoard(board)
    index = random.randrange(2)
    while True:
        sq1, sq2 = getNextTile(names[index], symbol[index], size)
        if validateTile(sq1, sq2, size) == True:
            if placeTile(board, symbol[index], sq1, sq2) == True:
                board [int (sq1[0])][int (sq1[1])], board [int (sq2[0])][int (sq2[1])] = symbol[index], symbol[index]
                printBoard(board)
                index = (index + 1) % len(names)
                if isGameAlive(board) == False:
                    sum_x = 0
                    sum_o = 0
                    for i, j in enumerate (board):
                        sum_x += j.count('X')
                        sum_o += j.count('O')
                    if sum_x > sum_o:
                        print (f'{names[symbol.index("X")]} {sum_x} - {names[symbol.index("O")]} {sum_o}')
                        print (f'{names[symbol.index("X")]} is the winner!')
                        break
                    elif sum_o > sum_x:
                        print (f'{names[symbol.index("O")]} {sum_o} - {names[symbol.index("X")]} {sum_x}')
                        print (f'{names[symbol.index("O")]} is the winner!')
                        break
                    else:
                        print ("It's a tie! Rematch...")
                        board = getNewBoard(size)
            else:
                print ("One or more squares occupied.")
        else:
            print ("The 2 squares selected cannot form a valid domino-tile.")      
# Q4()