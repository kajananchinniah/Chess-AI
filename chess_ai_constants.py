''' This file contains all the consts used in chess_ai 
'''

#MiniMax constants
minimax_min_val = -10000
minimax_max_val = 10000
minimax_max_depth = 2

#Evaluation Function constants
pawn_weight = 10
knight_weight = 30
bishop_weight = 40
rook_weight = 50
queen_weight = 90
king_weight = 900

legalMovesConst = 0.1
numberThreatsConst = 5

numberThreatConst_pawn_multipler = 1
numberThreatConst_knight_multipler = 1.15
numberThreatConst_bishop_multipler = 1.25
numberThreatConst_rook_multipler = 1.5
numberThreatConst_queen_multipler = 2
numberThreatConst_king_multipler = 3
