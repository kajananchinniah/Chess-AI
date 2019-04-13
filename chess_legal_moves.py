import chess_movement_choices as piece_moves
import chess_constants

#Piece legal moves

def isPotentialPositionEmpty(board, pot_position):
    if board[pot_position] == chess_constants.empty_space:
        return True
    return False

def isPotentialPositionAttacking(board, pot_position, enemy_min, enemy_max):
    if enemy_min <= board[pot_position] and board[pot_position] <= enemy_max:
        return True
    return False

def isPotentialPositionOccupiedByPlayerPiece(board, pot_position, player_min, player_max):
    if player_min <= board[pot_position] and board[pot_position] <= player_max:
        return True
    return False

def isMoveWithinRules(pot_position):
    if pot_position == chess_constants.move_not_possible:
        return False
    return True

def getPieceLegalWhitePawnMoves(board, position, enemy_min, enemy_max):
    legalMoves = []
    position_forward = piece_moves.moveForward(position)
    position_diag_forward_right = piece_moves.moveDiagForwardRight(position)
    position_diag_forward_left = piece_moves.moveDiagForwardLeft(position)
    
    if isMoveWithinRules(position_forward) == True and isPotentialPositionEmpty(board, position_forward) == True:
        legalMoves = legalMoves + [position_forward]
        
    if isMoveWithinRules(position_diag_forward_right) == True and isPotentialPositionAttacking(board, position_diag_forward_right, enemy_min, enemy_max) == True:
        legalMoves = legalMoves + [position_diag_forward_right]
        
    if isMoveWithinRules(position_diag_forward_left) == True and isPotentialPositionAttacking(board, position_diag_forward_left, enemy_min, enemy_max) == True:
        legalMoves = legalMoves + [position_diag_forward_left]
        
    return legalMoves 

def getPieceLegalBlackPawnMoves(board, position, enemy_min, enemy_max):
    legalMoves = []
    position_backwards = piece_moves.moveBackwards(position) #All positions are relative to white as the beginning indexes
    position_diag_backwards_left = piece_moves.moveDiagBackwardsLeft(position)
    position_diag_backwards_right = piece_moves.moveDiagBackwardsRight(position)

    if isMoveWithinRules(position_backwards) == True and isPotentialPositionEmpty(board, position_backwards) == True:
        legalMoves = legalMoves + [position_backwards]
        
    if isMoveWithinRules(position_diag_backwards_left) == True  and isPotentialPositionAttacking(board, position_diag_backwards_left, enemy_min, enemy_max) == True:
        legalMoves = legalMoves + [position_diag_backwards_left]
    
    if isMoveWithinRules(position_diag_backwards_right) == True and isPotentialPositionAttacking(board, position_diag_backwards_right, enemy_min, enemy_max) == True:
        legalMoves = legalMoves + [position_diag_backwards_right]
        
    return legalMoves 

def getPieceLegalKingMoves(board, position, enemy_min, enemy_max):
    legalMoves = []
    position_forward = piece_moves.moveForward(position)
    position_backwards = piece_moves.moveBackwards(position)
    position_right = piece_moves.moveRight(position)
    position_left = piece_moves.moveLeft(position)
    position_diag_forward_right = piece_moves.moveDiagForwardRight(position)
    position_diag_forward_left = piece_moves.moveDiagForwardLeft(position)
    position_diag_backwards_left = piece_moves.moveDiagBackwardsLeft(position)
    position_diag_backwards_right = piece_moves.moveDiagBackwardsRight(position)
    
    if isMoveWithinRules(position_forward) == True and (isPotentialPositionAttacking(board, position_forward, enemy_min, enemy_max) == True or isPotentialPositionEmpty(board, position_forward) == True):
        legalMoves = legalMoves + [position_forward]

    if isMoveWithinRules(position_backwards) == True and (isPotentialPositionAttacking(board, position_backwards, enemy_min, enemy_max) == True or isPotentialPositionEmpty(board, position_backwards) == True):
        legalMoves = legalMoves + [position_backwards]
        
    if isMoveWithinRules(position_right) == True and (isPotentialPositionAttacking(board, position_right, enemy_min, enemy_max) == True or isPotentialPositionEmpty(board, position_right) == True):
        legalMoves = legalMoves + [position_right]
        
    if isMoveWithinRules(position_left) == True and (isPotentialPositionAttacking(board, position_left, enemy_min, enemy_max) == True or isPotentialPositionEmpty(board, position_left) == True):
        legalMoves = legalMoves + [position_left]

    if isMoveWithinRules(position_diag_forward_right) == True and (isPotentialPositionAttacking(board, position_diag_forward_right, enemy_min, enemy_max) == True or isPotentialPositionEmpty(board, position_diag_forward_right) == True):
        legalMoves = legalMoves + [position_diag_forward_right]
        
    if isMoveWithinRules(position_diag_forward_left) == True and (isPotentialPositionAttacking(board, position_diag_forward_left, enemy_min, enemy_max) == True or isPotentialPositionEmpty(board, position_diag_forward_left) == True):
        legalMoves = legalMoves + [position_diag_forward_left]
    
    if isMoveWithinRules(position_diag_backwards_left) == True and (isPotentialPositionAttacking(board, position_diag_backwards_left, enemy_min, enemy_max) == True or isPotentialPositionEmpty(board, position_diag_backwards_left) == True):
        legalMoves = legalMoves + [position_diag_backwards_left]
     
    if isMoveWithinRules(position_diag_backwards_right) == True and (isPotentialPositionAttacking(board, position_diag_backwards_right, enemy_min, enemy_max) == True or isPotentialPositionEmpty(board, position_diag_backwards_right) == True):
        legalMoves = legalMoves + [position_diag_backwards_right]

    return legalMoves    

def getPieceLegalKnightMoves(board, position, enemy_min, enemy_max):
    legalMoves = []
    position_one_right_two_down = piece_moves.moveOneRightTwoBackwards(position)
    position_one_left_two_down = piece_moves.moveOneLeftTwoBackwards(position)
    position_one_right_two_forwards = piece_moves.moveOneRightTwoForwards(position)
    position_one_left_two_forwards = piece_moves.moveOneLeftTwoForwards(position)
    position_two_right_one_forwards = piece_moves.moveTwoRightOneForwards(position)
    position_two_right_one_backwards = piece_moves.moveTwoRightOneBackwards(position)
    position_two_left_one_forwards = piece_moves.moveTwoLeftOneForwards(position)
    position_two_left_one_backwards = piece_moves.moveTwoLeftOneBackwards(position)
    
    if isMoveWithinRules(position_one_right_two_down) == True and (isPotentialPositionAttacking(board, position_one_right_two_down, enemy_min, enemy_max) == True or isPotentialPositionEmpty(board, position_one_right_two_down) == True):
        legalMoves = legalMoves + [position_one_right_two_down]
        
    if isMoveWithinRules(position_one_left_two_down) == True and (isPotentialPositionAttacking(board, position_one_left_two_down, enemy_min, enemy_max) == True or isPotentialPositionEmpty(board, position_one_left_two_down) == True):
        legalMoves = legalMoves + [position_one_left_two_down]
        
    if isMoveWithinRules(position_one_right_two_forwards) == True and (isPotentialPositionAttacking(board, position_one_right_two_forwards, enemy_min, enemy_max) == True or isPotentialPositionEmpty(board, position_one_right_two_forwards) == True):
        legalMoves = legalMoves + [position_one_right_two_forwards]
        
    if isMoveWithinRules(position_one_left_two_forwards) == True and (isPotentialPositionAttacking(board, position_one_left_two_forwards, enemy_min, enemy_max) == True or isPotentialPositionEmpty(board, position_one_left_two_forwards) == True):
        legalMoves = legalMoves + [position_one_left_two_forwards]
        
    if isMoveWithinRules(position_two_right_one_forwards) == True and (isPotentialPositionAttacking(board, position_two_right_one_forwards, enemy_min, enemy_max) == True or isPotentialPositionEmpty(board, position_two_right_one_forwards) == True):
        legalMoves = legalMoves + [position_two_right_one_forwards]
        
    if isMoveWithinRules(position_two_right_one_backwards) == True and (isPotentialPositionAttacking(board, position_two_right_one_backwards, enemy_min, enemy_max) == True or isPotentialPositionEmpty(board, position_two_right_one_backwards) == True):
        legalMoves = legalMoves + [position_two_right_one_backwards]
        
    if isMoveWithinRules(position_two_left_one_forwards) == True and (isPotentialPositionAttacking(board, position_two_left_one_forwards, enemy_min, enemy_max) == True or isPotentialPositionEmpty(board, position_two_left_one_forwards) == True):
        legalMoves = legalMoves + [position_two_left_one_forwards]
        
    if isMoveWithinRules(position_two_left_one_backwards) == True and (isPotentialPositionAttacking(board, position_two_left_one_backwards, enemy_min, enemy_max) == True or isPotentialPositionEmpty(board, position_two_left_one_backwards) == True):
        legalMoves = legalMoves + [position_two_left_one_backwards]
        
    return legalMoves

#TODO: Should collapse all logic of propogating in one direction to a single function that takes in a direction
#Since much of this code is used over and over again
def getPieceLegalRookMoves(board, position, enemy_min, enemy_max, player_min, player_max):
    legalMoves = []
    
    #Getting forwards moves
    tempPosition = piece_moves.moveForward(position)
    while(True):
        if position >= chess_constants.forward_move_boundary:
            break
        
        if tempPosition > chess_constants.max_index or tempPosition == chess_constants.move_not_possible:
            break
        
        if tempPosition >= chess_constants.forward_move_boundary:
            legalMoves = legalMoves + [tempPosition]
            break
        
        if isPotentialPositionAttacking(board, tempPosition, enemy_min, enemy_max) == True:
            legalMoves = legalMoves + [tempPosition]
            break
        
        if isPotentialPositionOccupiedByPlayerPiece(board, tempPosition, player_min, player_max) == True:
            break
        
        if isPotentialPositionEmpty(board, tempPosition) == True:
            legalMoves = legalMoves + [tempPosition]
        
        tempPosition = piece_moves.moveForward(tempPosition)
        
    #Getting all backwards moves    
    tempPosition = piece_moves.moveBackwards(position)
    while(True):
        if position <= chess_constants.backwards_move_boundary:
            break
        
        if tempPosition < chess_constants.min_index or tempPosition == chess_constants.move_not_possible:
            break
        
        if isPotentialPositionAttacking(board, tempPosition, enemy_min, enemy_max) == True:
            legalMoves = legalMoves + [tempPosition]
            break

        if isPotentialPositionOccupiedByPlayerPiece(board, tempPosition, player_min, player_max) == True:
            break
        
        if isPotentialPositionEmpty(board, tempPosition) == True:
            legalMoves = legalMoves + [tempPosition]
        
        tempPosition = piece_moves.moveBackwards(tempPosition)
        
    #All left moves
    tempPosition = piece_moves.moveLeft(position)
    while(True):
        if piece_moves.isNotOnFirstColumn(position) == False:
            break
        
        if tempPosition < chess_constants.min_index or tempPosition == chess_constants.move_not_possible:
            break
        
        if isPotentialPositionAttacking(board, tempPosition, enemy_min, enemy_max) == True:
            legalMoves = legalMoves + [tempPosition]
            break
        
        if isPotentialPositionOccupiedByPlayerPiece(board, tempPosition, player_min, player_max) == True:
            break
        
        if isPotentialPositionEmpty(board, tempPosition) == True:
            legalMoves = legalMoves + [tempPosition]
            
        tempPosition = piece_moves.moveLeft(tempPosition)
        
    #All right moves
    tempPosition = piece_moves.moveRight(position)
    while(True):
        if piece_moves.isNotOnLastColumn(position) == False:
            break
        
        if tempPosition > chess_constants.max_index or tempPosition == chess_constants.move_not_possible:
            break
        
        if isPotentialPositionAttacking(board, tempPosition, enemy_min, enemy_max) == True:
            legalMoves = legalMoves + [tempPosition]
            break
        
        if isPotentialPositionOccupiedByPlayerPiece(board, tempPosition, player_min, player_max) == True:
            break
        
        if isPotentialPositionEmpty(board, tempPosition) == True:
            legalMoves = legalMoves + [tempPosition]
            
        tempPosition = piece_moves.moveRight(tempPosition)
        
    return legalMoves

def getPieceLegalBishopMoves(board, position, enemy_min, enemy_max, player_min, player_max):
    legalMoves = []
    
    tempPosition = piece_moves.moveDiagForwardLeft(position)
    while(True):
        if piece_moves.isNotOnLastColumn(position) == False:
            break
        
        if position >= chess_constants.forward_move_boundary:
            break
        
        if tempPosition > chess_constants.max_index or tempPosition == chess_constants.move_not_possible:
            break
        
        if isPotentialPositionAttacking(board, tempPosition, enemy_min, enemy_max) == True:
            legalMoves = legalMoves + [tempPosition]
            break
        
        if isPotentialPositionOccupiedByPlayerPiece(board, tempPosition, player_min, player_max) == True:
            break
        
        if isPotentialPositionEmpty(board, tempPosition) == True:
            legalMoves = legalMoves + [tempPosition]
        
        tempPosition = piece_moves.moveDiagForwardLeft(tempPosition)

        
    tempPosition = piece_moves.moveDiagBackwardsRight(position)
    while(True):
        if position <= chess_constants.backwards_move_boundary:
            break
        
        if piece_moves.isNotOnFirstColumn(position) == False:
            break
        
        if tempPosition < chess_constants.min_index or tempPosition == chess_constants.move_not_possible:
            break
        
        if isPotentialPositionAttacking(board, tempPosition, enemy_min, enemy_max) == True:
            legalMoves = legalMoves + [tempPosition]
            break
        
        if isPotentialPositionOccupiedByPlayerPiece(board, tempPosition, player_min, player_max) == True:
            break
        
        if isPotentialPositionEmpty(board, tempPosition) == True:
            legalMoves = legalMoves + [tempPosition]
            
        tempPosition = piece_moves.moveDiagBackwardsRight(tempPosition)
        
    tempPosition = piece_moves.moveDiagForwardRight(position)
    while(True):
        if piece_moves.isNotOnFirstColumn(position) == False:
            break
        
        if position >= chess_constants.forward_move_boundary:
            break
        
        if tempPosition > chess_constants.max_index or tempPosition == chess_constants.move_not_possible:
            break
        
        if isPotentialPositionAttacking(board, tempPosition, enemy_min, enemy_max) == True:
            legalMoves = legalMoves + [tempPosition]
            break
        
        if isPotentialPositionOccupiedByPlayerPiece(board, tempPosition, player_min, player_max) == True:
            break
        
        if isPotentialPositionEmpty(board, tempPosition) == True:
            legalMoves = legalMoves + [tempPosition]
            
        tempPosition = piece_moves.moveDiagForwardRight(tempPosition)

    tempPosition = piece_moves.moveDiagBackwardsLeft(position)
    while(True):
        
        if piece_moves.isNotOnLastColumn(position) == False:
            break
        
        if position <= chess_constants.backwards_move_boundary:
            break
        
        if tempPosition < chess_constants.min_index or tempPosition == chess_constants.move_not_possible:
            break
        
        if isPotentialPositionAttacking(board, tempPosition, enemy_min, enemy_max) == True:
            legalMoves = legalMoves + [tempPosition]
            break
        
        if isPotentialPositionOccupiedByPlayerPiece(board, tempPosition, player_min, player_max) == True:
            break
        
        if isPotentialPositionEmpty(board, tempPosition) == True:
            legalMoves = legalMoves + [tempPosition]
            
        tempPosition = piece_moves.moveDiagBackwardsLeft(tempPosition)
        
    return legalMoves 

def getPieceLegalQueenMoves(board, position, enemy_min, enemy_max, player_min, player_max):
    legalMoves = []
    legalMoves = legalMoves + getPieceLegalRookMoves(board, position, enemy_min, enemy_max, player_min, player_max)
    legalMoves = legalMoves + getPieceLegalBishopMoves(board, position, enemy_min, enemy_max, player_min, player_max)
    return legalMoves
    