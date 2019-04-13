import chess
import chess_ai
import time

'''
Contains all the functions required to play chess
'''
#TODO: clean this later

def playChess():
    print('Enter W to play as white, B to play as black. Anything else will corrospond to AI vs AI')
    play_as_white = False
    play_as_black = False
    play_mode = input()
    if play_mode == 'W':
        play_as_white = True
    if play_mode == 'B':
        play_as_black = True
        
    L = chess.init_chess()
    done = False
    while (done == False):
       print("\n-----\n")
       print(chess.printBoard(L))
       white_move_done = False
       while white_move_done == False:
          start = time.time()
          if play_as_white == True:
              white_piece_move = int(input("Capital player, enter the position of the piece to be moved"))
              white_piece_move_to = int(input("Capital player, enter the position where you want to move the piece"))
          else:
              tmp = chess_ai.pickMove(L,10)
              white_piece_move = tmp[1][0]
              print(tmp[1])
              white_piece_move_to = tmp[1][1]
              
          l = chess.getPieceLegalMoves(L, white_piece_move)
          if (white_piece_move_to in l and ((10 <= L[white_piece_move]) and L[white_piece_move] <= 19)):
             L[white_piece_move_to] = L[white_piece_move]
             L[white_piece_move] = 0
             end = time.time()
             print(end - start)
             white_move_done = True
          else:
             print("Invalid move; try again")
         
       print("\n-----\n")
       print(chess.printBoard(L))
       black_move_done = False
       while black_move_done == False:
          start = time.time()
          if play_as_black == True:
              black_piece_move = int(input("Capital player, enter the position of the piece to be moved"))
              black_piece_move_to = int(input("Capital player, enter the position where you want to move the piece"))
          else:
             tmp = chess_ai.pickMove(L,20)
             black_piece_move = tmp[1][0]
             print(tmp[1])
             black_piece_move_to = tmp[1][1]
             
          if ((20 <= L[black_piece_move]) and L[black_piece_move] <= 29):
             L[black_piece_move_to] = L[black_piece_move]
             L[black_piece_move] = 0
             end = time.time()
             print(end - start)
             black_move_done = True
          else:
             print("Invalid move; try again")
playChess()


