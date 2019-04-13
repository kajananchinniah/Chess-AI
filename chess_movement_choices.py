import chess_constants
'''
File contains all possible moves that any piece can make, without considering the board
Board consideration will be done at specific functions for each piece
Functions are all relative to white side
File also contains a checker to see if the position entered is on some boundaries (see the isNotOn_ functions)
'''
#All functions named relative to white side
#File contains all possible moves that any piece can make, without considering the board
#Board consideration is done in specific files of each piece 

def moveForward(position):
    if position < chess_constants.forward_move_boundary and (position + chess_constants.forward_addition_constant) <= chess_constants.max_index:
       return position + chess_constants.forward_addition_constant
    return chess_constants.move_not_possible

def moveBackwards(position):
    if position > chess_constants.backwards_move_boundary and (position + chess_constants.backward_addition_constant) >= chess_constants.min_index:
       return position + chess_constants.backward_addition_constant
    return chess_constants.move_not_possible

def moveDiagForwardRight(position):
    if position < chess_constants.forward_move_boundary and (position + chess_constants.diag_forward_right_addition_constant) < chess_constants.len_board and isNotOnFirstColumn(position):
       return (position + chess_constants.diag_forward_right_addition_constant)
    return chess_constants.move_not_possible 

def moveDiagForwardLeft(position):
    if position < chess_constants.forward_move_boundary and position + chess_constants.diag_forward_left_addition_constant < chess_constants.len_board and isNotOnLastColumn(position):
       return position + chess_constants.diag_forward_left_addition_constant
    return chess_constants.move_not_possible 

def moveDiagBackwardsLeft(position):
    if position > chess_constants.backwards_move_boundary and (position + chess_constants.diag_backwards_left_addition_constant) >= chess_constants.min_index and isNotOnLastColumn(position):
       return position + chess_constants.diag_backwards_left_addition_constant
    return chess_constants.move_not_possible 

def moveDiagBackwardsRight(position):
    if position > chess_constants.backwards_move_boundary and (position + chess_constants.diag_backwards_right_addition_constant) >= chess_constants.min_index and isNotOnFirstColumn(position):
       return position + chess_constants.diag_backwards_right_addition_constant 
    return chess_constants.move_not_possible

def moveRight(position):
    if isNotOnLastColumn(position) and (position + chess_constants.right_addition_constant) < chess_constants.len_board:
       return position + chess_constants.right_addition_constant
    return chess_constants.move_not_possible

def moveLeft(position):
    if isNotOnFirstColumn(position) and (position + chess_constants.left_addition_constant) >= chess_constants.min_index:
       return position + chess_constants.left_addition_constant
    return chess_constants.move_not_possible

def moveOneRightTwoBackwards(position):
    if position > chess_constants.knight_backwards_boundary and isNotOnFirstColumn(position) and (position + chess_constants.one_right_two_down_addition_constant) >= chess_constants.min_index:
       return position + chess_constants.one_right_two_down_addition_constant
    return chess_constants.move_not_possible

def moveOneLeftTwoBackwards(position):
    if position > chess_constants.knight_backwards_boundary and isNotOnLastColumn(position) and (position + chess_constants.one_left_two_down_addition_constant) >= chess_constants.min_index:
        return position + chess_constants.one_left_two_down_addition_constant
    return chess_constants.move_not_possible

def moveOneRightTwoForwards(position):
   if position < chess_constants.knight_forward_boundary and isNotOnLastColumn(position) and (position + chess_constants.one_right_two_forwards_addition_constant) < chess_constants.len_board:
       return position + chess_constants.one_right_two_forwards_addition_constant
   return chess_constants.move_not_possible

def moveOneLeftTwoForwards(position):
    if position < chess_constants.knight_forward_boundary and isNotOnFirstColumn(position) and (position + chess_constants.one_left_two_forwards_addition_constant) < chess_constants.len_board:
        return position + chess_constants.one_left_two_forwards_addition_constant
    return chess_constants.move_not_possible

def moveTwoRightOneForwards(position):
    if isNotOnFirstColumn(position) == True and isNotOnSecondColumn(position) == True and position < chess_constants.forward_move_boundary:
        return position + chess_constants.two_right_one_forwards_addition_constant
    return chess_constants.move_not_possible

def moveTwoRightOneBackwards(position):
    if isNotOnFirstColumn(position) == True and isNotOnSecondColumn(position) == True and position > chess_constants.backwards_move_boundary:
        return position + chess_constants.two_right_one_backwards_addition_constant
    return chess_constants.move_not_possible

def moveTwoLeftOneForwards(position):
    if isNotOnLastColumn(position) == True and isNotOnSecondLastColumn(position) == True and position < chess_constants.forward_addition_constant:
        return position + chess_constants.two_left_one_forwards_addition_constant
    return chess_constants.move_not_possible

def moveTwoLeftOneBackwards(position):
    if isNotOnLastColumn(position) == True and isNotOnSecondLastColumn(position) == True and position > chess_constants.forward_addition_constant:
        return position + chess_constants.two_left_one_backwards_addition_constant
    return chess_constants.move_not_possible

def isNotOnFirstColumn(position):
    if position % 8 == 0:
        return False
    return True

def isNotOnSecondColumn(position):
    if position % 8 == 1:
        return False
    return True

def isNotOnLastColumn(position):
    if position % 8 == 7:
        return False
    return True

def isNotOnSecondLastColumn(position):
    if position % 8 == 6:
        return False
    return True