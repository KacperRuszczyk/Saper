import random
def mina():
    #randomowa pozycja miny
    return [random.randint(0, 4),  random.randint(0, 4)]

def take_num():
    y_input = input("Enter the field number Y:")
    x_input = input("Enter the field number X:")
    try:
        x = int(x_input) - 1
        y = int(y_input) - 1
    except ValueError:
        print("That's not an int!")
        take_num()
    else:
        return [x, y]
    
def isanumber(a):
    try:
        float(repr(a))
        bool_a = True
    except:
        bool_a = False

    return bool_a

def make_mine(board):
    miny = []
    i = 0
    #tu powstaje 8 min
    while i < 8 :
        m = mina()
        if m not in miny: 
            miny.append(m)
            i += 1
    for y in range(5):
        for x in range(5):
            if [x, y] in miny:
                board[x][y] = '#'
                
    #tu powstaja cyferki wokol nich
    for y in range(5):
        for x in range(5):
            if board[x][y] == '#':
                if x + 1 < 0 or y + 1 < 0:
                    pass
                elif x+1 > 4 or y+1 > 4:
                    pass
                else:
                    if isanumber(board[x+1][y]):
                        board[x+1][y] += 1
                    if isanumber(board[x][y+1]):
                        board[x][y+1] += 1
                    if isanumber(board[x - 1][y]):
                        board[x - 1][y] += 1 
                    if isanumber(board[x][y-1]):
                        board[x][y-1]+=1
                        
    #gdzie zostaly zera sa spacje 
    for y in range(5):
        for x in range(5):
            if board[x][y] == 0:
                board[x][y] = ' '
            else:
                board[x][y] = str(board[x][y])
    return board


def show(board, memory):
    game_over = False
    print('-------------------')
    for y in range(5):
        for x in range(5):
            if [x, y] in memory:
                if board[x][y] == '#':
                    game_over = True
                print(board[y][x], end=" | ")
            else:
                print('-', end=" | ")
        print('\n')
    if game_over:
        raise NameError('GAME OVER')
    
def saper():
    memory = []
    board = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]
              ]
    board = make_mine(board)
    show(board, memory)
    while True:
        memory.append(take_num())
        show(board, memory)
    return board
