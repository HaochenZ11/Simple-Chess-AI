#one player plays against the AI
from chessPlayer import *
import chessPlayer_class

x=chessPlayer_class.chessBoard()
check1 = False
check2 = False
done = False
valid = False
validmove = False
validpiece = False
randmoves=[]

def printBoard(board):
    accum="---- BLACK SIDE ----\n"
    max=63
    for j in range(0,8,1):
        for i in range(max-j*8,max-j*8-8,-1):
            accum=accum+'{0: <5}'.format(board[i])
        accum=accum+"\n"
    accum=accum+"---- WHITE SIDE ----"
    return accum

def choosePiece(valid, b):
    while not (valid):
        print("Please enter white piece: ")
        try:
            wpiece = int(input())
            if wpiece > -1 and wpiece < 64:
                valid = True        
                if getPieceType(b[wpiece])!=0: #not a white piece
                    valid = False   
            moves = GetPieceLegalMoves(b, wpiece)
            if (moves == [] and valid == True):
                print("Piece cannot move. Please choose another piece.\n")
                choosePiece(False, b)
        except:
            print("Invalid input. Please enter an integer between 1 and 64.\n")
            valid = False
    return wpiece

while not (done):
    x.printBoard()
    b=x.getBoard()
    
    #white piece player input
    valid = False
    validmove = False
    validpiece = False
    randmoves=[]
    
    wpiece = choosePiece(valid, b)
        
    validmove = False
    while not (validmove):
        print("Please enter a location: ")
        try:
            wpos = int(input())
            moves = GetPieceLegalMoves(b, wpiece)
            print(moves)
            for i in moves:
                if i == wpos:
                    validmove=True
                    break
            if(validmove == False): 
                print("Invalid move.\n")
            if wpiece > -1 and wpiece < 64 and validmove:
                #print(validmove)
                validmove = True  
        except:
            print("Invalid input. Please enter an integer between 1 and 64.\n")
            valid = False
            validmove = False
    
    x.move(wpiece, wpos)
    x.printBoard()
    
    #black piece player input  
    print("Black is moving")
    r=chessPlayer(b, 20)
    bpiece = r[1][0]
    bpos = r[1][1]
    print("black moved", bpiece, bpos)
    x.move(bpiece, bpos)
    
    randmoves=randMoves(b, 20)
    
    if gameOver(b):
        x.printBoard()
        print("Game Over")
        done = True