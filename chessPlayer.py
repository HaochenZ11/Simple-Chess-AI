#FILE DESCRIPTION:
#chess move generator that returns the recommended move, alternate moves and their corresponding 'score', as well as the decision tree in list form
#uses "chessPlayer_class.py" file which defines the chess board class, as well as stack, queue, and tree data structures
#designed to be called by a "chessPVP.py" file where two users play against each other, or "chessAI.py" where user plays against computer

import chessPlayer_class

def GetPlayerPositions(board, player):
    positions=[]
    if player != 10 and player != 20:
        return False
    if player == 10:
        for i in range(0,len(board),1):
            if board[i] >= 10 and board[i] < 16:
                positions = positions + [i]
    else:
        for i in reversed(range(0,len(board),1)):
            if board[i] >= 20:
                positions = positions + [i]
    return positions

def getPieceType(value): #checks if piece is black
    if value >= 20:
        return 1
    elif value >= 10:
        return 0
    else:
        return -1 #position is empty

def isEdge(board, move): #checks if piece on either edge of board
    left = [0,8,16,24,32,40,48,56]
    right = [7,15,23,31,39,47,55,63]
    for i in left:
        if move == i:
            return True
    for i in right:
        if move == i:
            return True
    return False

def isRightEdge (board, move):
    left = [0,8,16,24,32,40, 48,56]
    for i in left:
        if move == i:
            return True
    return False

def isLeftEdge (board, move):
    right = [7,15,23,31,39,47,55,63]
    for i in right:
        if move == i:
            return True
    return False

def valid(board, move): #checks if position is both on the board and empty
    if move < 64 and move > -1: #within range of board
        if board[move] == 0: #empty spot
            return True
    else:
        return False

def getBishopMoves(board, position, pieceType): #finds valid moves for bishop
    slope = 1 
    moves = []
    while(True): #upleft
        if isLeftEdge(board, position):
            break
        if (position+slope*8+slope) > -1 and (position+slope*8+slope) < 64:
            if getPieceType(board[position+slope*8+slope])==pieceType: #ownpiece
                break
            elif valid(board, position+slope*8+slope): #empty spot and on the board
                moves = moves + [position+slope*8+slope] 
            else: #opponentpiece
                if (position+slope*8+slope) > -1 and (position+slope*8+slope) < 64:
                    moves = moves + [position+slope*8+slope] #eats opponent piece
                break     
            slope = slope + 1
        else:
            break
        if isEdge(board, position+slope*8+slope):
            break        
    slope=1
    while(True): #upright
        if isRightEdge(board, position):
            break
        if (position+slope*8-slope) > -1 and (position+slope*8-slope) < 64:
            if getPieceType(board[position+slope*8-slope])==pieceType: #ownpiece
                break
            elif valid(board, position+slope*8-slope): #empty spot and on the board
                moves = moves + [position+slope*8-slope] 
            else: #opponentpiece
                if (position+slope*8-slope) > -1 and (position+slope*8-slope) < 64:
                    moves = moves + [position+slope*8-slope] #eats opponent piece
                break
        else:
            break
        if isEdge(board, position+slope*8-slope):
            break
        slope = slope + 1 
    slope = 1
    while(True): #downright
        if isRightEdge(board, position):
            break
        if (position-slope*8-slope) > -1 and (position-slope*8-slope) < 64:
            if getPieceType(board[position-slope*8-slope])==pieceType: #ownpiece
                break
            elif valid(board, position-slope*8-slope): #empty spot and on the board
                moves = moves + [position-slope*8-slope] 
            else: #opponentpiece
                if (position-slope*8-slope) > -1 and (position-slope*8-slope) < 64:
                    moves = moves + [position-slope*8-slope] #eats opponent piece
                break
        else:
            break
        if isEdge(board, position-slope*8-slope):
            break        
        slope = slope + 1 
    slope = 1
    while(True): #downleft
        if isLeftEdge(board, position):
            break
        if (position-slope*8+slope) > -1 and (position-slope*8+slope) < 64:
            if getPieceType(board[position-slope*8+slope])==pieceType: #ownpiece
                break
            elif valid(board, position-slope*8+slope): #empty spot and on the board
                moves = moves + [position-slope*8+slope] 
            else: #opponentpiece
                if (position-slope*8+slope) > -1 and (position-slope*8+slope) < 64:
                    moves = moves + [position-slope*8+slope] #eats opponent piece
                break  
        else:
            break
        if isEdge(board, position-slope*8+slope):
            break        
        slope = slope + 1            
    return moves

def getRookMoves(board, position, pieceType): #gets valid moves for the rook
    inc = 1
    moves = []
    while(True): #vertical up
        if (position+8*inc) > -1 and (position+8*inc) < 64:
            if getPieceType(board[position+8*inc])==pieceType: #ownpiece
                break
            elif valid(board,position+8*inc): #empty spot
                moves = moves + [position+8*inc] 
            else: #opponentpiece
                if position+8*inc > -1 and position+8*inc < 64:
                    moves = moves + [position+8*inc] #eats opponent piece
                break
        else:
            break
        inc = inc + 1 
    inc = 1
    while(True): #vertical down
        if (position-8*inc) > -1 and (position -8*inc) < 64:
            if getPieceType(board[position-8*inc]) == pieceType: #ownpiece
                break
            elif valid(board, position-8*inc): #empty spot
                moves = moves + [position-8*inc] 
            else: #opponentpiece
                if position-8*inc > -1 and position-8*inc < 64:
                    moves=moves+[position-8*inc] #eats opponent piece
                break
        else:
            break
        inc = inc + 1
    inc = 1
    while(True): #left
        if isLeftEdge(board, position):
            break
        if (position+inc) > -1 and (position+inc) < 64:
            if getPieceType(board[position+inc]) == pieceType: #ownpiece
                break
            elif valid(board, position+inc): #empty spot
                moves = moves + [position+inc] 
            else: #opponentpiece
                if position+inc > -1 and position+inc < 64:
                    moves = moves + [position+inc] #eats opponent piece
                break 
        else:
            break
        if isEdge(board, position+inc):
            break        
        inc = inc + 1
    inc = 1
    while(True): #right
        if isRightEdge(board, position):
            break
        if (position-inc) > -1 and (position -inc) < 64:
            if getPieceType(board[position-inc])==pieceType: #ownpiece
                break
            elif valid(board, position-inc): #empty spot and on the board
                moves = moves + [position-inc] 
            else: #opponentpiece
                if position-inc > -1 and position-inc < 64:
                    moves = moves + [position-inc] #eats opponent piece
                break  
        else:
            break
        if isEdge(board, position-inc):
            break        
        inc = inc + 1
    return moves

def GetPieceLegalMoves(board, position): #returns list of available moves (position is index of current piece)
    piece = 0
    moves = []
    pieceType = 1
    if board[position] == 0: #error because position is empty
        return []
    if board[position] >= 20:
        pieceType = 1 #black piece
        piece = board[position] - 20
    else:
        pieceType = 0 #white piece
        piece = board[position] - 10
    
    if piece == 0: #pawn (only moves in one direction)
        if pieceType == 0: #white pawn
            if (position +8) > -1 and (position +8) < 64:
                if board[position+8] == 0:
                    moves=moves+[position+8]
            if (position +7) > -1 and (position +7) < 64:
                if board[position+7] != 0 and pieceType != getPieceType(board[position+7]): #opponent
                    if not isRightEdge(board, position):
                        moves=moves+[position+7]
            if (position +9) > -1 and (position +9) < 64:
                if board[position+9] != 0 and pieceType != getPieceType(board[position+9]): #opponent
                    if not isLeftEdge(board, position):
                        moves=moves+[position+9]
        else: #black pawn
            if (position -8) > -1 and (position -8) < 64:
                if board[position-8] == 0:  
                    moves=moves+[position-8]
            if (position -7) > -1 and (position -7) < 64:
                if board[position-7] != 0 and pieceType != getPieceType(board[position-7]): #opponent
                    if not isLeftEdge(board, position):
                        moves=moves+[position-7]
            if (position -9) > -1 and (position -9) < 64:
                if board[position-9] != 0 and pieceType != getPieceType(board[position-9]): #opponent
                    if not isRightEdge(board, position):
                        moves=moves+[position-9]    
    elif piece == 1: #knight (can eat or jump to empty spot but needs edge trappintg)
        if position+17 > -1 and position +17 < 64:
            if getPieceType(board[position+17]) != pieceType and not isLeftEdge(board, position): #not own piece
                moves=moves+[position+17]
        if position+15 > -1 and position +15 < 64:
            if getPieceType(board[position+15]) != pieceType and not isRightEdge(board, position):
                moves=moves+[position+15]
        if position+10 > -1 and position +10 < 64:
            if getPieceType(board[position+10]) != pieceType and not isLeftEdge(board, position) and not isLeftEdge(board, position+1):
                moves=moves+[position+10]
        if position+6 > -1 and position +6 < 64:
            if getPieceType(board[position+6]) != pieceType and not isRightEdge(board, position) and not isRightEdge(board, position-1):
                moves=moves+[position+6]
        if position-15 > -1 and position-15  < 64:
            if getPieceType(board[position-15]) != pieceType and not isLeftEdge(board, position):
                moves=moves+[position-15]
        if position-17 > -1 and position -17 < 64:
            if getPieceType(board[position-17]) != pieceType and not isRightEdge(board, position):
                moves=moves+[position-17]
        if position-6 > -1 and position -6 < 64:
            if getPieceType(board[position-6]) != pieceType and not isLeftEdge(board, position) and not isLeftEdge(board, position+1):
                moves=moves+[position-6]
        if position-10 > -1 and position -10 < 64:
            if getPieceType(board[position-10]) != pieceType and not isRightEdge(board, position) and not isRightEdge(board, position-1):
                moves=moves+[position-10]
    elif piece == 2:#bishop
        moves=getBishopMoves(board, position, pieceType) 
    elif piece == 3:#rook
        moves=getRookMoves(board, position, pieceType)  
    elif piece == 4:#queen (rook and bishop moves combined)
        moves=getRookMoves(board,position, pieceType)
        moves = moves + getBishopMoves(board,position, pieceType)
    else:#king (error trapped) 
        if position+1 > -1 and position +1 < 64:
            if getPieceType(board[position+1]) != pieceType and not isLeftEdge(board, position): #either empty or opponent
                moves = moves +[position+1]
        if position+8 > -1 and position +8 < 64:
            if getPieceType(board[position+8]) != pieceType: #either empty or opponent
                moves = moves +[position+8]
        if position-8 > -1 and position-8 < 64:
            if getPieceType(board[position-8]) != pieceType: #either empty or opponent
                moves = moves +[position-8]
        if getPieceType(board[position-1]) != pieceType and not isRightEdge(board, position): #either empty or opponent
            if (position-1) > -1 and (position-1) <64:
                moves = moves +[position-1] 
        if position-9 > -1 and position -9 < 64 and not isRightEdge(board, position):
            if getPieceType(board[position-9]) != pieceType: #either empty or opponent
                moves = moves +[position-9]  
        if (position-7) > -1 and (position-7) < 64 and not isLeftEdge(board, position):
            if getPieceType(board[position-7]) != pieceType: #either empty or opponent
                moves = moves +[position-7]
        if (position+9) > -1 and (position+9) < 64 and not isLeftEdge(board, position):
            if getPieceType(board[position+9]) != pieceType: #either empty or opponent
                moves = moves +[position+9] 
        if (position+7) > -1 and (position+7) < 64 and not isRightEdge(board, position):
            if getPieceType(board[position+7]) != pieceType: #either empty or opponent
                moves = moves +[position+7]  
    return moves

def IsPositionUnderThreat(board, position, player): #checks if piece could be captured by next opponent move
    #1 for black and 0 for white
    l = []
    pType = 0
    if player ==10:
        pType = 0
    else:
        pType = 1
        
    for i in range(0,64,1): #searches whole board
        if board[i]!=0 and getPieceType(board[i])!=pType: #not empty and is opponent
            l = GetPieceLegalMoves(board, i)
            for j in l:
                if j == position:
                    return True
    return False

def gameOver(board): #checks if the game is over (king captured)
    check1 = False
    check2 = False
    for i in board: #checks for end of game
        if i == 15:
            check1 = True
        if i == 25:
            check2 = True
    if (check1 == False or check2 == False):
        return True
    return False

def randMoves(b, player): #generates a list of all possible moves that don't result in capture
    r=[]
    if player == 10:
        opp = 20
    else:
        opp = 10
    positions = GetPlayerPositions(b, player)
    
    for p in positions: #for each piece on the board
        moves = GetPieceLegalMoves(b, p)
        for i in moves:
            if not(IsPositionUnderThreat(b, i, player)):
                r = r + [[p, i]]
    return r

def endGame (board, player, bScore, wScore): #checks if both sides have queen
    qw = False
    qb = False
    if player ==10: #assigns "own" and "opponent" labels
        opp = 20
    else:
        opp = 10
        
    for i in board: #checks existence of queen piece on board
        if i-player == 4:
            qw = True
        if i-opp == 4:
            qb = True
            
    if bScore <= 21000 or wScore < 21000:
        return True
    
    if not qw and not qb:
        return True
    
    return False

def eval(board, player): #evaluates board score for one player
    p=GetPlayerPositions(board, player)
    kpos, total = 0
    wScore, bScore, pawnScore, knightScore, bishopScore, rookScore, queenScore, kingScore, boardScore = 0
    pawns, knights, bishops, rooks, queen, king = []

    if player == 10:
        offset = 10
        opp = 20
        oppOffset = 20
    else:
        offset = 20
        opp = 10
        oppOffset = 10
    o=GetPlayerPositions(board, opp)
    
    #king safety 
    for i in range(0, 64, 1):
        if board[i] - offset == 5:
            kpos = i
    if IsPositionUnderThreat(board, kpos, player):
        kingScore = kingScore - 1000
        
    #material board score (max = 23900)
    for i in p:
        if board[i] -offset == 0: #pawn
            wScore = wScore +100
        elif board[i] - offset == 1: #knight
            wScore = wScore + 300
        elif board[i] - offset == 2: #bishop
            wScore = wScore + 300
        elif board[i] - offset == 3: #rook
            wScore = wScore + 500
        elif board[i] - offset == 4: #queen
            wScore = wScore + 900 
        else:
            wScore = wScore+ 20000 #king       
    for i in o:
        if board[i] -oppOffset == 0:
            bScore = bScore +100
        elif board[i] - oppOffset == 1:
            bScore = bScore + 300
        elif board[i] - oppOffset == 2:
            bScore = bScore + 300
        elif board[i] - oppOffset == 3:
            bScore = bScore + 500
        elif board[i] - oppOffset == 4:
            bScore = bScore + 900 
        else:
            bScore = bScore+ 20000   
    
    boardScore = wScore - bScore
   
    #pawn table (for white player) (max = 600)
    pawn2Table = [
         0,  0,  0,  0,  0,  0,  0,  0,
        75, 75, 75, 75, 75, 75, 75, 75,
        25, 25, 29, 29, 29, 29, 25, 25,
         4,  8, 12, 21, 21, 12,  8,  4,
         0,  4,  8, 17, 17,  8,  4,  0,
         4, -4, -8,  4,  4, -8, -4,  4,
         4,  8,  8,-17,-17,  8,  8,  4,
         0,  0,  0,  0,  0,  0,  0,  0
    ]
    pawnTable = [
        0,  0,  0,  0,  0,  0,  0,  0,
        4,  8,  8, -17,-17, 8,  8,  4,
        4, -4, -8,  4,  4, -8, -4,  4,
        0,  4,  8, 17, 17,  8,  4,  0,
        4,  8, 12, 21, 21, 12,  8,  4,
        25, 25, 29, 29, 29, 29, 25, 25,
        75, 75, 75, 75, 75, 75, 75, 75,
        0,  0,  0,  0,  0,  0,  0,  0
    ]
    if player == 10: #evaluates pawnScore based on pawn tables (optimized positions)
        for i in range (0,64,1):
            if board[i] - offset == 0:
                pawns = pawns+[i]
        for i in pawns:
            pawnScore = pawnScore + pawnTable[i]
    else:
        for i in range (0,64,1):
            if board[i] - offset == 0:
                pawns = pawns+[i]
        for i in pawns:
            pawnScore = pawnScore + pawn2Table[i]  
            
    #knight piece-table (max = 40)       
    knight2Table = [
        -50,-40,-30,-30,-30,-30,-40,-50,
        -40,-20,  0,  0,  0,  0,-20,-40,
        -30,  0, 10, 15, 15, 10,  0,-30,
        -30,  5, 15, 20, 20, 15,  5,-30,
        -30,  0, 15, 20, 20, 15,  0,-30,
        -30,  5, 10, 15, 15, 10,  5,-30,
        -40,-20,  0,  5,  5,  0,-20,-40,
        -50,-40,-30,-30,-30,-30,-40,-50
    ]
    knightTable = [
        -50,-40,-30,-30,-30,-30,-40,-50,
        -40,-20,  0,  5,  5,  0,-20,-40,
        -30,  0, 10, 15, 15, 10,  0,-30,
        -30,  5, 15, 20, 20, 15,  5,-30,
        -30,  0, 15, 20, 20, 15,  0,-30,
        -30,  5, 10, 15, 15, 10,  5,-30,
        -40,-20,  0,  0,  0,  0,-20,-40,
        -50,-40,-30,-30,-30,-30,-40,-50
    ]
    if player == 10: #evalutes knightScore based on knight tables
        for i in range (0,64,1):
            if board[i] - offset == 1:
                knights = knights+[i]
        for i in knights:
            knightScore = knightScore + knightTable[i]
    else:
        for i in range (0,64,1):
            if board[i] - offset == 1:
                knights = knights+[i]
        for i in knights:
            knightScore = knightScore + knight2Table[i]  
            
    #bishop piece-square table (max = 20)
    bishop2Table = [
        -20,-10,-10,-10,-10,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5, 10, 10,  5,  0,-10,
        -10,  5,  5, 10, 10,  5,  5,-10,
        -10,  0, 10, 10, 10, 10,  0,-10,
        -10, 10, 10, 10, 10, 10, 10,-10,
        -10,  5,  0,  0,  0,  0,  5,-10,
        -20,-10,-10,-10,-10,-10,-10,-20
    ]
    bishopTable = [
        -20,-10,-10,-10,-10,-10,-10,-20,
        -10,  5,  0,  0,  0,  0,  5,-10,
        -10, 10, 10, 10, 10, 10, 10,-10,
        -10,  0, 10, 10, 10, 10,  0,-10,
        -10,  5,  5, 10, 10,  5,  5,-10,
        -10,  0,  5, 10, 10,  5,  0,-10,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -20,-10,-10,-10,-10,-10,-10,-20
    ]
    if player == 10: #evalues bishopScore based on table of optimized positions
        for i in range (0,64,1):
            if board[i] - offset == 2:
                bishops = bishops+[i]
        for i in bishops:
            bishopScore = bishopScore + bishopTable[i]
    else:
        for i in range (0,64,1):
            if board[i] - offset == 2:
                bishops = bishops+[i]
        for i in bishops:
            bishopScore = bishopScore + bishop2Table[i]  
            
    #rook piece-square table (max = 20)        
    rook2Table = [
         0,  0,  0,  0,  0,  0,  0,  0,
         5, 10, 10, 10, 10, 10, 10,  5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
         0,  0,  0,  5,  5,  0,  0,  0  
    ]
    rookTable = [
        0,  0,  0,  5,  5,  0,  0,  0,
        5,  0,  0,  0,  0,  0,  0, -5,
       -5,  0,  0,  0,  0,  0,  0, -5,
       -5,  0,  0,  0,  0,  0,  0, -5,
       -5,  0,  0,  0,  0,  0,  0, -5,
       -5,  0,  0,  0,  0,  0,  0, -5,
        5, 10, 10, 10, 10, 10, 10,  5,
        0,  0,  0,  0,  0,  0,  0,  0
    ]
    if player == 10: #evaluates rookScore based on table of optimized positions
        for i in range (0,64,1):
            if board[i] - offset == 3:
                rooks = rooks+[i]
        for i in rooks:
            rookScore = rookScore + rookTable[i]
    else:
        for i in range (0,64,1):
            if board[i] - offset == 3:
                rooks = rooks+[i]
        for i in rooks:
            rookScore = rookScore + rook2Table[i] 
            
    #queen piece-square table (max = 5)
    queen2Table = [
        -20,-10,-10, -5, -5,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5,  5,  5,  5,  0,-10,
         -5,  0,  5,  5,  5,  5,  0, -5,
          0,  0,  5,  5,  5,  5,  0, -5,
        -10,  5,  5,  5,  5,  5,  0,-10,
        -10,  0,  5,  0,  0,  0,  0,-10,
        -20,-10,-10, -5, -5,-10,-10,-20
    ]
    queenTable = [
        -20,-10,-10, -5, -5,-10,-10,-20
        -10,  0,  5,  0,  0,  0,  0,-10,
        -10,  5,  5,  5,  5,  5,  0,-10,
          0,  0,  5,  5,  5,  5,  0, -5,
         -5,  0,  5,  5,  5,  5,  0, -5,
        -10,  0,  5,  5,  5,  5,  0,-10,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -20,-10,-10, -5, -5,-10,-10,-20
    ]
    if player == 10: #evaluates queenScore based on table of optimized positions
        for i in range (0,64,1):
            if board[i] - offset == 4:
                queen = queen+[i]
        for i in queen:
            queenScore = queenScore + queenTable[i]
    else:
        for i in range (0,64,1):
            if board[i] - offset == 4:
                queen = queen+[i]
        for i in queen:
            queenScore = queenScore + queen2Table[i]  
    
    #king piece-square tables (max = 30 for midgame, 40 for endgame)
    kingMid2Table = [
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -20,-30,-30,-40,-40,-30,-30,-20,
        -10,-20,-20,-20,-20,-20,-20,-10,
         20, 20,  0,  0,  0,  0, 20, 20,
         20, 30, 10,  0,  0, 10, 30, 20    
    ]
    kingMidTable = [
        20, 30, 10,  0,  0, 10, 30, 20,
        20, 20,  0,  0,  0,  0, 20, 20,
       -10,-20,-20,-20,-20,-20,-20,-10,
       -20,-30,-30,-40,-40,-30,-30,-20,
       -30,-40,-40,-50,-50,-40,-40,-30,
       -30,-40,-40,-50,-50,-40,-40,-30,
       -30,-40,-40,-50,-50,-40,-40,-30,
       -30,-40,-40,-50,-50,-40,-40,-30
    ]
    kingEnd2Table = [
        -50,-40,-30,-20,-20,-30,-40,-50,
        -30,-20,-10,  0,  0,-10,-20,-30,
        -30,-10, 20, 30, 30, 20,-10,-30,
        -30,-10, 30, 40, 40, 30,-10,-30,
        -30,-10, 30, 40, 40, 30,-10,-30,
        -30,-10, 20, 30, 30, 20,-10,-30,
        -30,-30,  0,  0,  0,  0,-30,-30,
        -50,-30,-30,-30,-30,-30,-30,-50
    ]
    kingEndTable = [
        -50,-30,-30,-30,-30,-30,-30,-50,
        -30,-30,  0,  0,  0,  0,-30,-30,
        -30,-10, 20, 30, 30, 20,-10,-30,
        -30,-10, 30, 40, 40, 30,-10,-30,
        -30,-10, 30, 40, 40, 30,-10,-30,        
        -30,-10, 20, 30, 30, 20,-10,-30,
        -30,-20,-10,  0,  0,-10,-20,-30,
        -50,-40,-30,-20,-20,-30,-40,-50
    ]
    if player == 10: #evaluates kingScore based on table of optimized positions
        for i in range (0,64,1):
            if board[i] - offset == 5:
                king = king + [i]
        for i in king:
            if endGame(board, player, wScore, bScore):
                kingScore = kingScore + kingEndTable[i]
            else:
                kingScore = kingScore + kingMidTable[i]
    else:
        for i in range (0,64,1):
            if board[i] - offset == 5:
                king = king+[i]
        for i in king:
            if endGame(board, player, wScore, bScore):
                kingScore = kingScore + kingEnd2Table[i] 
            else:
                kingScore = kingScore + kingMid2Table[i] 
    total = boardScore + pawnScore + knightScore + bishopScore + rookScore + queenScore + kingScore + 1000 #total score of pieces
    total = total/1000
    return total

def createTree(myTree, board, player,val): #creates tree of possible next moves
    p= GetPlayerPositions(board, player)
    temp=list(board)
    a = 0
    b = 0
    greatest=0
    if player == 10:
        alt = 20
        end = [56, 57, 58, 59, 60, 61, 62, 63]
    else:
        alt = 10
        end = [0, 1, 2, 3, 4, 5, 6, 7]

    if val == 0: #makes 3 layers of tree
        return myTree

    for i in p: #i is the index of piece
        m = GetPieceLegalMoves(board, i)
        for j in m: #j is possible new indices  
            value = boardEval(board, i, j, player)
            subTree = chessPlayer_class.tree([value,i,j]) #creates subtree first with possible next moves
            temp[j] = temp[i]
            temp[i]=0
            if temp[j] - player == 0: #pawn move
                for i in end:
                    if j == end:
                        temp[j] = player+5
            myTree.AddSuccessor(createTree(subTree, temp, alt, val-1))
            temp[i] = temp[j] #reverts the board back to original state
            temp[j] = 0       
    return myTree

def boardEval(board, pIndex, move ,player): #returns integer evaluation of the state of the board for a given player
    temp = list(board)
    temp[move] = temp[pIndex]
    temp[pIndex] = 0
    value = eval(temp, player)
    return value

def evalTree(board, player): #evaluates the tree to get best moves
    x = chessPlayer_class.tree([0,0,0])
    val = 3
    alpha = -10000000
    beta = 10000000
    bestMove=[]
    t = createTree(x, board, player,val)
    ab = alphabeta(x, 3, alpha, beta, True) #alphabeta pruning of tree to find best move
    
    for i in x.store[1]:
        if i.store[0][0] == ab:
            bestMove = i.store[0]
   
    return bestMove, x

def alphabeta(tree, depth, alpha, beta, maximizingPlayer): #alpha-beta pruning (recursive)
    if depth == 0 or tree.store[1] == []: #base case     
        return tree.store[0][0]
    if maximizingPlayer:
        value = -float("inf")
        for i in tree.store[1]:
            value = max(value, alphabeta(i, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break #beta cutoff
        tree.store[0][0] = value
        return value
    else:
        value = float("inf")
        for i in tree.store[1]:
            value = min(value, alphabeta(i, depth - 1, alpha,beta, True))
            beta = min(beta, value)
            if alpha >=beta:
                break #alpha cut-off 
        tree.store[0][0] = value
        return value

#MAIN FUNCTION
def chessPlayer(board, player): #returns info on validity, suggested move, all possible moves & score, and the tree in list form
    r = []
    status = True
    move = [] #2 list
    candidateMoves = [] #list of other moves (each a 2 list), [[move 2-list], float]
    x = chessPlayer_class.tree([0,0,0])
    move, eTree = evalTree(board, player)
    move = move[1:]
    eTreeList = eTree.Get_LevelOrder() #outputs the tree level-by-level into a list
    
    if (player != 10 and player !=20) or len(board) != 64: #invalid parameters
        status = False
        return [status, [], [], []]
    for i in eTree.store[1]:
        i.store = [i.store[0][1:]]+[i.store[0][0]]
        candidateMoves = candidateMoves + [i.store]
    r = [status] + [move] + [candidateMoves] + [eTreeList]
    return r

x = chessPlayer_class.chessBoard() #instantiates chess board



