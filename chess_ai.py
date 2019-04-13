import chess_constants
import chess
import tree
import chess_ai_constants as ai_consts

'''
This file contains the functions related to the AI:
    isPositionUnderThreatNumber(board, position, player)
        - returns the number of threats to a player
    startMiniMax(board, player)
        - initializes the minimax algorithm relative to the maximizing player. 
        - returns a list containing the following information:
            1) Whether a move was selected (T/F)
            2) a list containing the selected move (index 0 is the curr_pos, index 1 is the move to pos)
            3) a list containing all the possible moves it evaluated
            4) the evaluation's trees level order traversal 
    
    maxi_board(board, player, depth) and mini_board(board, player, depth)
        - returns the evaluation function value and the tree it's been created
        - These are maximize and minimize the player respectively, and continue the minimax algorithm until the max depth is reached
        
    eval_func(board, player)
        - is a heurestic that evaluates the score of the board relative to the maximizing player
        - returns a sum that corrosponds to 'how good' the board is for the player
        
    pickMove(board, player)
        - returns startMiniMax 
'''

#TODO: clean this section

def isPositionUnderThreatNumber(board, position, player):
    '''
    Reminder: piece list goes index to piece mapping is: 0 -> pawn, 1 -> knight, 2 -> bishop, 3 -> rook, 
    4 -> queen, and 5 -> king
    '''
    
    check = []
    numberThreats = 0
    if player == chess_constants.player_black:
      check = chess_constants.white_piece_list
    elif player == chess_constants.player_white:
      check = chess_constants.black_piece_list
      
    for i in range(0, len(board), 1):
        tmp = []
        if board[i] in check:
            tmp = chess.getPieceLegalMoves(board, i)
            if position in tmp:
                numberThreats = numberThreats + 1
    return numberThreats 

def pickMove(board, player):
    return startMiniMax(board, player)
#startMiniMax corrosponds to a depth of 0
def startMiniMax(board, player):
    tmp_board = list(board)
    value = ai_consts.minimax_min_val
    selected_move = []
    candidateMoves = []
    root = eval_func(board, player)
    t = tree.tree(root)
    L = chess.getPlayerPositions(board, player)
    for curr_pos in L:
        tmp = chess.getPieceLegalMoves(board, curr_pos)
        if tmp == []:
            continue
        for i in tmp:
           if i == []:
               continue
           
           tmp_board[i] = tmp_board[curr_pos]
           tmp_board[curr_pos] = chess_constants.empty_space
           temp_value = mini_board(tmp_board, player, 1)   #The 1 corrosponds to a starting depth of 1
           tmp_board = list(board)
           t.addSuccessor(temp_value[1])
           if temp_value[0] > value:
              value = temp_value[0]
              selected_move = [curr_pos, i]
           candidateMoves = candidateMoves + [[[curr_pos, i], temp_value[0]]]
    if selected_move == []:
        return [False, selected_move, candidateMoves, t.Get_LevelOrder()]
    
    return [True, selected_move, candidateMoves, t.Get_LevelOrder()]

def maxi_board(board, player, depth):
    if depth == ai_consts.minimax_max_depth:
        rval = eval_func(board, player)
        return [rval, tree.tree(rval)] 

    tmp_board = list(board)
    root = eval_func(board, player)
    t = tree.tree(root)
    L = chess.getPlayerPositions(board, player)
    value = ai_consts.minimax_min_val
    for curr_pos in L:
       tmp = chess.getPieceLegalMoves(board, curr_pos)
       if tmp == []:
          continue
         
       for i in tmp:
          tmp_board[i] = tmp_board[curr_pos]
          tmp_board[curr_pos] = 0
          temp_value = mini_board(tmp_board, player, depth + 1)
          tmp_board = list(board)
          t.addSuccessor(temp_value[1])
          if temp_value[0] > value:
             value = temp_value[0]
                  
    return [value, t]
    
def mini_board(board, player, depth):
    tmp_board = list(board)
    if depth == ai_consts.minimax_max_depth:
        rval = eval_func(board, player)
        return [rval, tree(rval)] 
    
    if player == chess_constants.player_white:
        enemy = chess_constants.player_black
    else:
        enemy = chess_constants.player_white
                        
    root = eval_func(board, player)
    t = tree.tree(root)
    L = chess.getPlayerPositions(board, enemy)
    value = ai_consts.minimax_max_val
    for curr_pos in L:
        tmp = chess.getPieceLegalMoves(board, curr_pos)
        if tmp == []:
            continue
        for i in tmp:
            if i == []:
                continue
            tmp_board[i] = tmp_board[curr_pos]
            tmp_board[curr_pos] = chess_constants.empty_space
            temp_value = maxi_board(tmp_board, player, depth + 1)
            tmp_board = list(board)
            t.addSuccessor(temp_value[1])
            if temp_value[0] < value:
                value = temp_value[0]
    return [value, t]
    
def eval_func(board, player): 
   '''
   Reminder: piece list goes index to piece mapping is: 0 -> pawn, 1 -> knight, 2 -> bishop, 3 -> rook, 
   4 -> queen, and 5 -> king
   '''
   if player == chess_constants.player_white:
      player_vals = chess_constants.white_piece_list
      enemy_vals = chess_constants.black_piece_list
      enemy = chess_constants.player_black

   elif player == chess_constants.player_black:
      enemy_vals = chess_constants.white_piece_list
      player_vals = chess_constants.black_piece_list
      enemy = chess_constants.player_white

   eval_sum = 0
   for i in range(0, len(board), 1):
      if (board[i] == player_vals[0]):
         eval_sum = eval_sum + ai_consts.pawn_weight
         eval_sum = eval_sum + ai_consts.legalMovesConst*len(chess.getPieceLegalMoves(board, i)) 
         eval_sum = eval_sum - ai_consts.numberThreatsConst*ai_consts.numberThreatConst_pawn_multipler*isPositionUnderThreatNumber(board, i, player)
        
      if (board[i] == player_vals[1]):
         eval_sum = eval_sum + ai_consts.knight_weight
         eval_sum = eval_sum + ai_consts.legalMovesConst*len(chess.getPieceLegalMoves(board, i))
         eval_sum = eval_sum - ai_consts.numberThreatConst_knight_multipler*ai_consts.numberThreatsConst*isPositionUnderThreatNumber(board, i, player)
             
      if (board[i] == player_vals[2]):
         eval_sum = eval_sum + ai_consts.bishop_weight
         eval_sum = eval_sum + ai_consts.legalMovesConst*len(chess.getPieceLegalMoves(board, i))
         eval_sum = eval_sum - ai_consts.numberThreatConst_bishop_multipler*ai_consts.numberThreatsConst*isPositionUnderThreatNumber(board, i, player)
             
      if (board[i] == player_vals[3]):
         eval_sum = eval_sum + ai_consts.rook_weight
         eval_sum = eval_sum + ai_consts.legalMovesConst*len(chess.getPieceLegalMoves(board, i))
         eval_sum = eval_sum - ai_consts.numberThreatConst_rook_multipler*ai_consts.numberThreatsConst*isPositionUnderThreatNumber(board, i, player)
        
      if (board[i] == player_vals[4]): 
         eval_sum = eval_sum + ai_consts.queen_weight 
         eval_sum = eval_sum + ai_consts.legalMovesConst*len(chess.getPieceLegalMoves(board, i))
         eval_sum = eval_sum - ai_consts.numberThreatConst_queen_multipler*ai_consts.numberThreatsConst*isPositionUnderThreatNumber(board, i, player)
             
      if (board[i] == player_vals[5]):
         eval_sum = eval_sum + ai_consts.king_weight
         eval_sum = eval_sum + ai_consts.legalMovesConst*len(chess.getPieceLegalMoves(board, i))
         eval_sum = eval_sum - ai_consts.numberThreatConst_king_multipler*ai_consts.numberThreatsConst*isPositionUnderThreatNumber(board, i, player)

      if (board[i] == enemy_vals[0]):
         eval_sum = eval_sum - ai_consts.pawn_weight
         eval_sum = eval_sum - ai_consts.legalMovesConst*len(chess.getPieceLegalMoves(board, i))
         eval_sum = eval_sum + ai_consts.numberThreatConst_pawn_multipler*ai_consts.numberThreatsConst*isPositionUnderThreatNumber(board, i, enemy)
             
      if (board[i] == enemy_vals[1]):
         eval_sum = eval_sum - ai_consts.knight_weight
         eval_sum = eval_sum - ai_consts.legalMovesConst*len(chess.getPieceLegalMoves(board, i))
         eval_sum = eval_sum + ai_consts.numberThreatConst_knight_multipler*ai_consts.numberThreatsConst*isPositionUnderThreatNumber(board, i, enemy)
             
      if (board[i] == enemy_vals[2]):
         eval_sum = eval_sum - ai_consts.bishop_weight
         eval_sum = eval_sum - ai_consts.legalMovesConst*len(chess.getPieceLegalMoves(board, i)) 
         eval_sum = eval_sum + ai_consts.numberThreatConst_bishop_multipler*ai_consts.numberThreatsConst*isPositionUnderThreatNumber(board, i, enemy)
             
      if (board[i] == enemy_vals[3]):
         eval_sum = eval_sum - ai_consts.rook_weight
         eval_sum = eval_sum - ai_consts.legalMovesConst*len(chess.getPieceLegalMoves(board, i))
         eval_sum = eval_sum + ai_consts.numberThreatConst_rook_multipler*ai_consts.numberThreatsConst*isPositionUnderThreatNumber(board, i, enemy)
             
      if (board[i] == enemy_vals[4]):
         eval_sum = eval_sum - ai_consts.queen_weight
         eval_sum = eval_sum - ai_consts.legalMovesConst*len(chess.getPieceLegalMoves(board, i))
         eval_sum = eval_sum + ai_consts.numberThreatConst_queen_multipler*ai_consts.numberThreatsConst*isPositionUnderThreatNumber(board, i, enemy)
             
      if (board[i] == enemy_vals[5]):
         eval_sum = eval_sum - ai_consts.king_weight
         eval_sum = eval_sum - ai_consts.legalMovesConst*len(chess.getPieceLegalMoves(board, i))
         eval_sum = eval_sum + ai_consts.numberThreatConst_king_multipler*ai_consts.numberThreatsConst*isPositionUnderThreatNumber(board, i, enemy)
             
   return eval_sum
