import random

print("Welcome! Lets play TIC TAC TOE")

board=[' ' for x in range(10)] #creating board of 3X3 size- a list of ' ' empty string initialization

def printBoard(board): #print the board interface after every move
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def Insert(alp,pos):   #Function to insert alph = X or O at the given position
    board[pos] = alp


def IsSpaceFree(pos):
    return(board[pos]==' ') #Function that checks whether the position is free to insert of not

def IsBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True #Function to check whether the board is full or not

def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run = True
    while run:
        pos = input("Please select a position to enter the 'X' between 1 to 9: ")
        try:  #try is used to catch errors, if there is no error then try is executed else except wil be executed
            pos = int(pos)  #since pos input will be a string, it is necessary to convert it in int
            if pos > 0 and pos < 10:    #check validity of pos-1-9
                if IsSpaceFree(pos):   #check whether this space is free to insert or not
                    run = False         #make run false as next chance is of computer
                    Insert('X' , pos)
                else:
                    print('Sorry, this space is occupied.  ')

            else:
                print('Please type a number between 1 and 9: ')

        except:
            print('Please type a number')



def computerMove():    #function returns the move of computer ie that position computer will move on
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0
    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]  #makes a shallow copy of the list board
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
               move = i
               return move

    if 5 in possibleMoves:
        move = 5
        return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move


def selectRandom(list):
    length = len(list)
    r = random.randrange(0,length)  #selcts a random index of the list
    return list[r]



def main():
    printBoard(board)
    while not(IsBoardFull(board)):   #till board is not full

        if not(IsWinner(board , 'O')):  #if computer is not winner then player move
            playerMove()
            printBoard(board)
        else:                       #else if computer has won, then player has lost
            print("Sorry you loose!")
            break

        if not(IsWinner(board , 'X')):  #if player is not winner, then computer move
            move = computerMove()

            if move == 0:        #if no move is possible for computer ie tie game
                print(" ")

            else:
                Insert('O' , move)
                print("Computer placed an 'O' on position" , move , ':')
                printBoard(board)
        else:
            print("You win!")
            break

    if IsBoardFull(board):   # after while loop, if board is full then tie game
        print("Tie game !")



while True:
    x = input("Do you want to play? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
