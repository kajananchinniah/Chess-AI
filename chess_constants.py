'''
File contains all constants necessary for the chess game
Note: does not contain AI constants
'''
#Piece Offset Constants
white_offset = 10
black_offset = 20
pawn_offset = 0
knight_offset = 1
bishop_offset = 2
rook_offset = 3 
queen_offset = 4
king_offset = 5
empty_space = 0

#Piece Values
white_pawn = white_offset + pawn_offset
black_pawn = black_offset + pawn_offset

white_knight = white_offset + knight_offset
black_knight = black_offset + knight_offset

white_bishop = white_offset + bishop_offset
black_bishop = black_offset + bishop_offset

white_rook = white_offset + rook_offset
black_rook = black_offset + rook_offset

white_queen = white_offset + queen_offset
black_queen = black_offset + queen_offset

white_king = white_offset + king_offset
black_king = black_offset + king_offset

#Board Constants
len_board = 64
black_first_index = 56
white_first_index = 0

#Player Constants
player_white = 10
player_black = 20
white_min_piece_val = 10
black_min_piece_val = 20
white_max_piece_val = 15
black_max_piece_val = 25
white_piece_list = [10, 11, 12, 13, 14, 15]
black_piece_list = [20, 21, 22, 23, 24, 25]

#Return this if something goes wrong 
error_status = False

#Move constants
forward_addition_constant = 8
backward_addition_constant = -8
right_addition_constant = 1
left_addition_constant = -1

diag_forward_right_addition_constant = 7
diag_forward_left_addition_constant = 9
diag_backwards_left_addition_constant = -7
diag_backwards_right_addition_constant = -9

#These moves are used pretty much exclusively by the knight
one_right_two_down_addition_constant = -15
one_left_two_down_addition_constant = -17
one_right_two_forwards_addition_constant = 17
one_left_two_forwards_addition_constant = 15

two_right_one_forwards_addition_constant = 6
two_right_one_backwards_addition_constant = -10
two_left_one_forwards_addition_constant = 10
two_left_one_backwards_addition_constant = -6


right_addition_constant = 1
left_addition_constant = -1
move_not_possible = -1 

#Move Boundary constants 
forward_move_boundary = 56
backwards_move_boundary = 7
max_index = 63
min_index = 0
knight_backwards_boundary = 15
knight_forward_boundary = 48



