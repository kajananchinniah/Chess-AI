import chess_constants
import chess_legal_moves
import time

"""
File contains all logic for the chess game
Functions include:
    init_chess
        - returns the board at starting position, board indices represented by list of 64 elements (0-63 indices uses)
        - returns a list
    getPlayPositions(board, player)
        - returns a list of all positions occupied by a player. White = 10, Black = 20
        - returns a list
    getPieceLegalMoves(board, position)
        - returns all possible legal moves that a piece at a particular position can take
        - returns a list of all these moves
"""
#Initializes the chess board with all pieces at their respective starting position
#Board is represented by a list of 64 elements (indices 0-63)
def init_chess():
   board = []
   for i in range(0, chess_constants.len_board, 1):
      board = board + [chess_constants.empty_space]

   #manually setting up first row for black and white 
   board[0] = chess_constants.white_offset + chess_constants.rook_offset
   board[1] = chess_constants.white_offset + chess_constants.knight_offset
   board[2] = chess_constants.white_offset + chess_constants.bishop_offset
   board[3] = chess_constants.white_offset + chess_constants.queen_offset
   board[4] = chess_constants.white_offset + chess_constants.king_offset 
   board[5] = chess_constants.white_offset + chess_constants.bishop_offset
   board[6] = chess_constants.white_offset + chess_constants.knight_offset
   board[7] = chess_constants.white_offset + chess_constants.rook_offset
   
   board[chess_constants.black_first_index + 0] = chess_constants.black_offset + chess_constants.rook_offset
   board[chess_constants.black_first_index + 1] = chess_constants.black_offset + chess_constants.knight_offset
   board[chess_constants.black_first_index + 2] = chess_constants.black_offset + chess_constants.bishop_offset
   board[chess_constants.black_first_index + 3] = chess_constants.black_offset + chess_constants.queen_offset
   board[chess_constants.black_first_index + 4] = chess_constants.black_offset + chess_constants.king_offset 
   board[chess_constants.black_first_index + 5] = chess_constants.black_offset + chess_constants.bishop_offset
   board[chess_constants.black_first_index + 6] = chess_constants.black_offset + chess_constants.knight_offset
   board[chess_constants.black_first_index + 7] = chess_constants.black_offset + chess_constants.rook_offset
   
   #Sets up second row for white and black respectively
   for i in range(8, 16, 1):
      board[i] = chess_constants.white_offset + chess_constants.pawn_offset
      board[chess_constants.len_board - 1 - i] = chess_constants.black_offset + chess_constants.pawn_offset

   return board

#Returns a list of all the positions that a player occupies. 
def getPlayerPositions(board, player):
   if (len(board) != chess_constants.len_board):
      return chess_constants.error_status #error status 

   if ((player != chess_constants.player_white) and (player != chess_constants.player_black)):
      return chess_constants.error_status

   positions = []
   for i in range(0, chess_constants.len_board, 1):
      if ((chess_constants.white_min_piece_val <= board[i]) and (board[i] <= chess_constants.white_max_piece_val) and (player == chess_constants.player_white)):
         positions = positions + [i]

      if ((chess_constants.black_min_piece_val <= board[i]) and (board[i] <= chess_constants.black_max_piece_val) and (player == chess_constants.player_black)):
         positions = positions + [i]
         
      else:
         continue
     
   return positions

#Gets all legal moves at a particular position 
def getPieceLegalMoves(board, position):
   if position < chess_constants.min_index or position > chess_constants.max_index:
       return chess_constants.error_status

   if board[position] == 0:
       return []
   
   if chess_constants.white_min_piece_val <= board[position] and board[position] <= chess_constants.white_max_piece_val:
       player_min = chess_constants.white_min_piece_val
       player_max = chess_constants.white_max_piece_val
       enemy_min = chess_constants.black_min_piece_val
       enemy_max = chess_constants.black_max_piece_val
        
   elif chess_constants.black_min_piece_val <= board[position] and board[position] <= chess_constants.black_max_piece_val:
       player_min = chess_constants.black_min_piece_val
       player_max = chess_constants.black_max_piece_val
       enemy_min = chess_constants.white_min_piece_val
       enemy_max = chess_constants.white_max_piece_val
    
   if board[position] == chess_constants.white_pawn:
       return chess_legal_moves.getPieceLegalWhitePawnMoves(board, position, enemy_min, enemy_max)
   
   if board[position] == chess_constants.black_pawn:
       return chess_legal_moves.getPieceLegalBlackPawnMoves(board, position, enemy_min, enemy_max)
       
   if board[position] == chess_constants.white_king or board[position] == chess_constants.black_king:
       return chess_legal_moves.getPieceLegalKingMoves(board, position, enemy_min, enemy_max)
       
   if board[position] == chess_constants.white_knight or board[position] == chess_constants.black_knight:
       return chess_legal_moves.getPieceLegalKnightMoves(board, position, enemy_min, enemy_max)

   if board[position] == chess_constants.white_rook or board[position] == chess_constants.black_rook:
       return chess_legal_moves.getPieceLegalRookMoves(board, position, enemy_min, enemy_max, player_min, player_max)
   
   if board[position] == chess_constants.white_bishop or board[position] == chess_constants.black_bishop:
       return chess_legal_moves.getPieceLegalBishopMoves(board, position, enemy_min, enemy_max, player_min, player_max)
   
   if board[position] == chess_constants.white_queen or board[position] == chess_constants.black_queen:
       return chess_legal_moves.getPieceLegalQueenMoves(board, position, enemy_min, enemy_max, player_min, player_max)

def IsPositionUnderThreat(board, position, player):
   check = []
   if player == chess_constants.player_black:
      check = chess_constants.white_piece_list
      
   elif player == chess_constants.player_white:
      check = chess_constants.black_piece_list

   for i in range(0, len(board), 1):
       tmp = []
       if board[i] in check:
          tmp = getPieceLegalMoves(board, i)
          if position in tmp:
             return True
   return False

def printBoard(board):
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   return accum
