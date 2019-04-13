import time
#Uncomment line 916 to play verse the AI as the white player
#Uncomment line 917 to see AI vs AI
#TODO: this code requires a lot of cleaning was done in a rush (but it works fine)

class queue:
   def __init__(self):
      self.size = -1
      self.arr = []

   def enqueue(self, val):
      self.arr = self.arr + [val]
      self.size = self.size + 1
      return True

   def dequeue(self):
      if (len(self.arr) == 0):
         return False

      temp = self.arr[0]
      self.arr = self.arr[1:len(self.arr)]
      self.size = self.size - 1
      return temp

   def empty(self):
      if (len(self.arr) == 0):
         return True
      return False

class tree:
    def __init__(self, node):
        self.store = [node, []]
        
    def addSuccessor(self, x):
        self.store[1] = self.store[1] + [x]
        
    def Get_LevelOrder(self):
      x = queue()
      out = []
      x.enqueue(self.store)
      while x.empty() == False:
         r = x.dequeue()
         out = out + [r[0]]
         for i in range(0, len(r[1]), 1):
            x.enqueue((r[1][i]).store)
      return out


def init_chess():
   offset_white = 10
   offset_black = 20
   piece_value = [0, 3, 1, 2, 5, 4] 
   #corrosponds to pawn, rook, bishop, knight, queen, king
   len_board = 64
   first_index_black = 56

   board = []
   for i in range(0, 64, 1):
      board = board + [0]

   for i in range(0, 5, 1):
      board[i] = offset_white + piece_value[i + 1]
      board[first_index_black + i] = offset_black + piece_value[i + 1]

   for i in range(5, 8, 1):
      board[i] = offset_white + piece_value[8 - i]
      board[first_index_black + i] = offset_black + piece_value[8 - i]

   for i in range(8, 16, 1):
      board[i] = offset_white + piece_value[0]
      board[len_board - 1 - i] = offset_black + piece_value[0]

   return board

def GetPlayerPositions(board, player):
   if (len(board) != 64):
      return -1

   if ( (player != 10) and (player != 20) ):
      print(player)
      return -1

   positions = []
   for i in range(0, len(board), 1):
      if (( (10 <= board[i]) and (board[i] <= 19)) and player == 10):
         positions = positions + [i]

      if (( (20 <= board[i]) and (board[i] <= 29)) and player == 20):
         positions = positions + [i]

      else:
         continue
   return positions

def GetPieceLegalMoves(board, position):
   if position < 0 or position > 63:
      return -1
   if board[position] == 0:
      return []
   legalMoves = []
   
   if ((10 <= board[position]) and (board[position] <= 19)):
      player_min = 10
      player_max = 19
      enemy_min = 20
      enemy_max = 29

   elif ((20 <= board[position]) and (board[position] <= 29)):
      player_min = 20
      player_max = 29
      enemy_min = 10
      enemy_max = 19
      
   if board[position] == 10:
      if (position < 56):
         if ( ((position + 8) < 64) and (board[position + 8] == 0)):
            legalMoves = legalMoves + [position + 8]
   
         if ( ((position + 9) < 64) and ((position) % 8) != 7):
            if ((20 <= board[position + 9]) and (board[position + 9] <= 29)):
               legalMoves = legalMoves + [position + 9]
    
         if ( ((position + 7) < 64) and (position % 8) != 0):
            if ((20 <= board[position + 7]) and (board[position + 7] <= 29)):
               legalMoves = legalMoves + [position + 7]
    
   if board[position] == 20:
      if (position > 7):
         if ( ((position - 8) > 0) and (board[position - 8] == 0)):
            legalMoves = legalMoves + [position - 8]

         if ( (position - 7) > 0 and ((position) % 8) != 7):
            if ( (10 <= board[position - 7]) and (board[position - 7] <= 19)):
               legalMoves = legalMoves + [position - 7]

         if ( ((position - 9) > 0) and (position % 8) != 0):
            if ((10 <= board[position - 9]) and (board[position - 9] <= 19)):
               legalMoves = legalMoves + [position - 9]
               

   if board[position] == 15 or board[position] == 25:
      if (( (position + 8) < 64) and (position < 56)):
         if ((board[position + 8] == 0) or ( (enemy_min <= board[position + 8]) and (board[position + 8] <= enemy_max))):
            legalMoves = legalMoves + [position + 8]

      if ( ((position - 8) > 0) and (position > 7)):
         if ((board[position - 8] == 0) or ( (enemy_min <= board[position - 8]) and (board[position - 8] <= enemy_max))):
            legalMoves = legalMoves + [position - 8]

      if ( ((position)% 8) != 7):
         if (( (position + 1) < 64) and ((board[position + 1] == 0) or ( (enemy_min <= board[position + 1]) and (board[position + 1] <= enemy_max)))):
            legalMoves = legalMoves + [position + 1]

         if ( ((position + 9) < 64) and (position < 56) and (position%8 != 7)):
            if ((board[position + 9] == 0) or ( (enemy_min <= board[position + 9]) and (board[position + 9] <= enemy_max))): 
               legalMoves = legalMoves + [position + 9]

         if ( ((position - 7) > 0) and (position > 7) and (position%8 != 7)):
            if ((board[position - 7] == 0) or ( (enemy_min <= board[position - 7]) and (board[position - 7] <= enemy_max))):
               legalMoves = legalMoves + [position - 7]

      if ( (position % 8) != 0):
         if (((position - 1) > 0) and ((board[position - 1] == 0) or ( (enemy_min <= board[position - 1]) and (board[position - 1] <= enemy_max)))):
            legalMoves = legalMoves + [position - 1]
          
         if position < 56 and position%8 != 0:
            if ((board[position + 7] == 0) or ( (enemy_min <= board[position + 7]) and (board[position + 7] <= enemy_max))):
               legalMoves = legalMoves + [position + 7]

         if (((position - 9) > 0) and (position > 7) and position%8 != 0):
            if ((board[position - 9] == 0) or ( (enemy_min <= board[position - 9]) and (board[position - 9] <= enemy_max))):
               legalMoves = legalMoves + [position - 9]

   if board[position] == 11 or board[position] == 21:
      if ( (position > 15) ):
         if (( (position % 8) != 0) and ((position-17)>0)):
            if ((board[position - 17] == 0) or ( (enemy_min <= board[position - 17]) and (board[position - 17] <= enemy_max))):
               legalMoves = legalMoves + [position - 17]

         if ( ((position-15) > 0) and  ( (position) % 8) != 7):
            if ((board[position - 15] == 0) or ( (enemy_min <= board[position - 15]) and (board[position - 15] <= enemy_max))):
               legalMoves = legalMoves + [position - 15] 
      
      if  ( (position < 48) ):
         if ( ((position+17) < 64) and (position % 8) != 7):
            if ((board[position + 17] == 0) or ( (enemy_min <= board[position + 17]) and (board[position + 17] <= enemy_max))):
               legalMoves = legalMoves + [position + 17]

         if ( ((position+15) < 64) and ( (position) % 8) != 0):
            if ((board[position + 15] == 0) or ( (enemy_min <= board[position + 15]) and (board[position + 15] <= enemy_max))):
               legalMoves = legalMoves + [position + 15]

      if ( position % 8 != 0 and position % 8 != 1):
         if position < 56 and ((board[position + 6] == 0) or ( (enemy_min <= board[position + 6]) and (board[position + 6] <= enemy_max))):
            legalMoves = legalMoves + [position + 6]

         if position > 7 and ((board[position - 10] == 0) or ( (enemy_min <= board[position - 10]) and (board[position - 10] <= enemy_max))): 
            legalMoves = legalMoves + [position - 10]
      
      if ( ((position) % 8 != 7) and (position) % 8 != 6):
         if position < 56 and ((board[position + 10] == 0) or ( (enemy_min <= board[position + 10]) and (board[position + 10] <= enemy_max))):
            legalMoves = legalMoves + [position + 10]

         if position > 7 and ((board[position - 6] == 0) or ( (enemy_min <= board[position - 6]) and (board[position - 6] <= enemy_max))):
            legalMoves = legalMoves + [position - 6]

   if (board[position] == 13 or board[position] == 23):         
      tempPosition = position + 8
      while (True): 
         if position >= 56:
             break
         
         if (tempPosition > 63):
            break

         if (tempPosition >= 56):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((enemy_min <= board[tempPosition]) and (board[tempPosition] <= enemy_max)):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((player_min <= board[tempPosition]) and (board[tempPosition] <= player_max)):
            break

         if (board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
         tempPosition = tempPosition + 8

      tempPosition = position - 8
      while (True):
          
         if position <= 7:
             break
         
         if (tempPosition < 0):
            break

         if ((enemy_min <= board[tempPosition]) and (board[tempPosition] <= enemy_max)):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((player_min <= board[tempPosition]) and (board[tempPosition] <= player_max)):
            break

         if (tempPosition <= 7 and board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
            break

         if (board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
         tempPosition = tempPosition - 8

      tempPosition = position - 1
      while (True):
          
         if position%8 == 0:
             break
         
         if tempPosition < 0:
            break

         if ((enemy_min <= board[tempPosition]) and (board[tempPosition] <= enemy_max)):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((player_min <= board[tempPosition]) and (board[tempPosition] <= player_max)):
            break
        
         if (tempPosition % 8 == 0 and board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
            break

         if (board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
         tempPosition = tempPosition - 1

      tempPosition = position + 1
      while (True):
         if position%8 == 7:
             break
         
         if (tempPosition > 63):
            break

         if ((enemy_min <= board[tempPosition]) and (board[tempPosition] <= enemy_max)):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((player_min <= board[tempPosition]) and (board[tempPosition] <= player_max)):
            break
        
         if (tempPosition % 8 == 7 and board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
            break

         if (board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
         tempPosition = tempPosition + 1

   if ( (board[position] == 12) or (board[position] == 22)):
      tempPosition = position + 9 
      while (True):
         if position % 8 == 7:
             break
         if position >= 56:
             break
         
         if tempPosition > 63:
            break

         if ((enemy_min <= board[tempPosition]) and (board[tempPosition] <= enemy_max)):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((player_min <= board[tempPosition]) and (board[tempPosition] <= player_max)):
            break
        
         if ((tempPosition % 8 == 7 or tempPosition >= 56) and board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
            break

         if (board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
         tempPosition = tempPosition + 9

      tempPosition = position - 9
      while (True):
         if position <= 7:
             break
         if position%8 == 0:
             break
         
         if tempPosition < 0:
            break

         if ((enemy_min <= board[tempPosition]) and (board[tempPosition] <= enemy_max)):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((player_min <= board[tempPosition]) and (board[tempPosition] <= player_max)):
            break
        
         if ((tempPosition % 8 == 0 or tempPosition <= 7) and board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
            break

         if (board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
         tempPosition = tempPosition - 9
      
      tempPosition = position + 7
      while (True):
         if position % 8 == 0:
             break
         
         if position >= 56:
             break
         
         if tempPosition > 63:
            break

         if ((enemy_min <= board[tempPosition]) and (board[tempPosition] <= enemy_max)):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((player_min <= board[tempPosition]) and (board[tempPosition] <= player_max)):
            break
        
         if ((tempPosition % 8 == 0 or tempPosition >= 56) and board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
            break

         if (board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
         tempPosition = tempPosition + 7

      tempPosition = position - 7
      while (True):
         if position % 8 == 7:
             break
         if position <= 7:
             break
         
         if tempPosition < 0:
            break

         if ((enemy_min <= board[tempPosition]) and (board[tempPosition] <= enemy_max)):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((player_min <= board[tempPosition]) and (board[tempPosition] <= player_max)):
            break
         
         
         if ((tempPosition % 8 == 7 or tempPosition <= 7) and board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
            break

         if (board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
         tempPosition = tempPosition - 7

   if ( (board[position] == 14) or (board[position] == 24)):
      tempPosition = position + 8
      while (True): 
         if position >= 56:
             break
         
         if (tempPosition > 63):
            break

         if (tempPosition >= 56):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((enemy_min <= board[tempPosition]) and (board[tempPosition] <= enemy_max)):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((player_min <= board[tempPosition]) and (board[tempPosition] <= player_max)):
            break

         if (board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
         tempPosition = tempPosition + 8

      tempPosition = position - 8
      while (True):
         if position <= 7:
             break
         
         if (tempPosition < 0):
            break

         if ((enemy_min <= board[tempPosition]) and (board[tempPosition] <= enemy_max)):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((player_min <= board[tempPosition]) and (board[tempPosition] <= player_max)):
            break

         if (tempPosition <= 7 and board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
            break

         if (board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
         tempPosition = tempPosition - 8

      tempPosition = position - 1
      while (True):
         if position % 8 == 0:
             break
         
         if tempPosition < 0:
            break

         if ((enemy_min <= board[tempPosition]) and (board[tempPosition] <= enemy_max)):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((player_min <= board[tempPosition]) and (board[tempPosition] <= player_max)):
            break
        
         if (tempPosition % 8 == 0 and board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
            break

         if (board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
         tempPosition = tempPosition - 1

      tempPosition = position + 1
      while (True):
         if position % 8 == 7:
             break
         
         if (tempPosition > 63):
            break

         if ((enemy_min <= board[tempPosition]) and (board[tempPosition] <= enemy_max)):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((player_min <= board[tempPosition]) and (board[tempPosition] <= player_max)):
            break
        
         if (tempPosition % 8 == 7 and board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
            break

         if (board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
         tempPosition = tempPosition + 1  
         
      tempPosition = position + 9 
      while (True):
         if position % 8 == 7:
             break
         
         if position >= 56:
             break
         
         if tempPosition > 63:
            break

         if ((enemy_min <= board[tempPosition]) and (board[tempPosition] <= enemy_max)):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((player_min <= board[tempPosition]) and (board[tempPosition] <= player_max)):
            break
        
         if ((tempPosition % 8 == 7 or tempPosition >= 56) and board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
            break

         if (board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
         tempPosition = tempPosition + 9

      tempPosition = position - 9
      while (True):
         if position % 8 == 0:
             break
         if position <= 7:
             break
         
         if tempPosition < 0:
            break

         if ((enemy_min <= board[tempPosition]) and (board[tempPosition] <= enemy_max)):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((player_min <= board[tempPosition]) and (board[tempPosition] <= player_max)):
            break
        
         if ((tempPosition % 8 == 0 or tempPosition <= 7) and board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
            break

         if (board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
         tempPosition = tempPosition - 9
      
      tempPosition = position + 7
      while (True):
         if position % 8 == 0:
             break
         if position >= 56:
             break
         
         if tempPosition > 63:
            break

         if ((enemy_min <= board[tempPosition]) and (board[tempPosition] <= enemy_max)):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((player_min <= board[tempPosition]) and (board[tempPosition] <= player_max)):
            break
        
         if ((tempPosition % 8 == 0 or tempPosition >= 56) and board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
            break

         if (board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
         tempPosition = tempPosition + 7

      tempPosition = position - 7
      while (True):
         if position % 8 == 7:
             break
         
         if position <= 7:
             break
         
         if tempPosition < 0:
            break

         if ((enemy_min <= board[tempPosition]) and (board[tempPosition] <= enemy_max)):
            legalMoves = legalMoves + [tempPosition]
            break

         if ((player_min <= board[tempPosition]) and (board[tempPosition] <= player_max)):
            break
         
         if ((tempPosition % 8 == 7 or tempPosition <= 7) and board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
            break

         if (board[tempPosition] == 0):
            legalMoves = legalMoves + [tempPosition]
         tempPosition = tempPosition - 7
   return legalMoves

def IsPositionUnderThreat(board, position, player):
   check = []
   if player == 20:
      check = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

   elif player == 10:
      check = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

   for i in range(0, len(board), 1):
       tmp = []
       if board[i] in check:
          tmp = GetPieceLegalMoves(board, i)
          if position in tmp:
             return True
   return False

def isPositionUnderThreatNumber(board, position, player):
    check = []
    numberThreats = 0
    if player == 20:
      check = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    elif player == 10:
      check = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
      
    for i in range(0, len(board), 1):
        tmp = []
        if board[i] in check:
            tmp = GetPieceLegalMoves(board, i)
            if position in tmp:
                numberThreats = numberThreats + 1
    return numberThreats 
      
def PrintBoard(board):
   L = []
   for i in range(0, 64, 1):
      if ( (i != 0) and (i % 8 == 0)):
         print(L)
         L = []
      if board[i] == 10:
         L = L + ['P'] 
      if board[i] == 20:
         L = L + ['p']
      if board[i] == 21:
         L = L + ['n']
      if board[i] == 11:
         L = L + ['N']
      if board[i] == 22:
         L = L + ['b']
      if board[i] == 12:
         L = L + ['B']
      if board[i] == 23:
         L = L + ['r']
      if board[i] == 13:
         L = L + ['R']
      if board[i] == 14:
         L = L + ['Q']
      if board[i] == 24:
         L = L + ['q']
      if board[i] == 25:
         L = L + ['k']
      if board[i] == 15:
         L = L + ['K']
      if board[i] == 0:
         L = L + [i]
      if i == 63:
         print(L)
         break

def pickMove(board, player):
    tmp_board = list(board)
    value = -10000
    selected_move = []
    candidateMoves = []
    root = eval_func(board, player)
    t = tree(root)
    L = GetPlayerPositions(board, player)
    for curr_pos in L:
        tmp = GetPieceLegalMoves(board, curr_pos)
        if tmp == []:
            continue
        for i in tmp:
           tmp_board[i] = tmp_board[curr_pos]
           tmp_board[curr_pos] = 0
           temp_value = mini_board(tmp_board, player, 0)  
           tmp_board = list(board)
           t.addSuccessor(temp_value[1])
           if temp_value[0] > value:
              value = temp_value[0]
              selected_move = [curr_pos, i]
           candidateMoves = candidateMoves + [[[curr_pos, i], temp_value[0]]]
    if selected_move == []:
        return [False, selected_move, candidateMoves, t.Get_LevelOrder()]
    
    return [True, selected_move, candidateMoves, t.Get_LevelOrder()]

def chessPlayer(board, player):
    rval = pickMove(board, player)
    return rval

def maxi_board(board, player, depth):
    if depth == 1:
        rval = eval_func(board, player)
        return [rval, tree(rval)] 

    tmp_board = list(board)
    if player == 10:
        enemy = 20
    else:
        enemy = 10
        
    root = eval_func(board, player)
    t = tree(root)
    L = GetPlayerPositions(board, player)
    value = -10000
    for curr_pos in L:
       tmp = GetPieceLegalMoves(board, curr_pos)
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
    if depth == 1:
        rval = eval_func(board, player)
        return [rval, tree(rval)] 
    
    if player == 10:
        enemy = 20
    else:
        enemy = 10
                        
    root = eval_func(board, player)
    t = tree(root)
    L = GetPlayerPositions(board, enemy)
    value = 10000
    for curr_pos in L:
        tmp = GetPieceLegalMoves(board, curr_pos)
        if tmp == []:
            continue
        for i in tmp:
            tmp_board[i] = tmp_board[curr_pos]
            tmp_board[curr_pos] = 0
            temp_value = maxi_board(tmp_board, player, depth + 1)
            tmp_board = list(board)
            t.addSuccessor(temp_value[1])
            if temp_value[0] < value:
                value = temp_value[0]
    return [value, t]
    
def eval_func(board, player):   
   if (player == 10):
      player_vals = [10, 11, 12, 13, 14, 15]
      enemy_vals = [20, 21, 22, 23, 24, 25]
      enemy = 20

   elif (player == 20):
      enemy_vals = [10, 11, 12, 13, 14, 15]
      player_vals = [20, 21, 22, 23, 24, 25]
      enemy = 10

   legalMovesConst = 0.1
   numberThreatsConst= 5
   eval_sum = 0
   for i in range(0, 64, 1):
      if (board[i] == player_vals[0]):
         eval_sum = eval_sum + 10 + legalMovesConst*len(GetPieceLegalMoves(board, i)) - numberThreatsConst*isPositionUnderThreatNumber(board, i, player)
             
      if (board[i] == player_vals[1]):
         eval_sum = eval_sum + 30 + legalMovesConst*len(GetPieceLegalMoves(board, i)) - 1.15*numberThreatsConst*isPositionUnderThreatNumber(board, i, player)
             
      if (board[i] == player_vals[2]):
         eval_sum = eval_sum + 40 + legalMovesConst*len(GetPieceLegalMoves(board, i)) - 1.25*numberThreatsConst*isPositionUnderThreatNumber(board, i, player)
             
      if (board[i] == player_vals[3]):
         eval_sum = eval_sum + 50 + legalMovesConst*len(GetPieceLegalMoves(board, i)) - 1.5*numberThreatsConst*isPositionUnderThreatNumber(board, i, player)
        
      if (board[i] == player_vals[4]): 
         eval_sum = eval_sum + 90 + legalMovesConst*len(GetPieceLegalMoves(board, i)) - 2*numberThreatsConst*isPositionUnderThreatNumber(board, i, player)
             
      if (board[i] == player_vals[5]):
         eval_sum = eval_sum + 900 + legalMovesConst*len(GetPieceLegalMoves(board, i)) - 3*numberThreatsConst*isPositionUnderThreatNumber(board, i, player)

      if (board[i] == enemy_vals[0]):
         eval_sum = eval_sum - 10 - legalMovesConst*len(GetPieceLegalMoves(board, i)) + numberThreatsConst*isPositionUnderThreatNumber(board, i, enemy)
             
      if (board[i] == enemy_vals[1]):
         eval_sum = eval_sum - 30 - legalMovesConst*len(GetPieceLegalMoves(board, i)) + 1.15*numberThreatsConst*isPositionUnderThreatNumber(board, i, enemy)
             
      if (board[i] == enemy_vals[2]):
         eval_sum = eval_sum - 40 - legalMovesConst*len(GetPieceLegalMoves(board, i)) + 1.25*numberThreatsConst*isPositionUnderThreatNumber(board, i, enemy)
             
      if (board[i] == enemy_vals[3]):
         eval_sum = eval_sum - 50 - legalMovesConst*len(GetPieceLegalMoves(board, i)) + 1.5*numberThreatsConst*isPositionUnderThreatNumber(board, i, enemy)
             
      if (board[i] == enemy_vals[4]):
         eval_sum = eval_sum - 90 - legalMovesConst*len(GetPieceLegalMoves(board, i)) + 2*numberThreatsConst*isPositionUnderThreatNumber(board, i, enemy)
             
      if (board[i] == enemy_vals[5]):
         eval_sum = eval_sum - 900 - legalMovesConst*len(GetPieceLegalMoves(board, i)) + 3*numberThreatsConst*isPositionUnderThreatNumber(board, i, enemy)
             
   return eval_sum

def printBoard(board):
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   return accum

def humanVSAI():
   L = init_chess()
   done = False
   while (done == False):
      print('eval = ', eval_func(L, 10))
      print('W ', len(GetPlayerPositions(L, 10)), ' B ', len(GetPlayerPositions(L,20)))
      print("\n-----\n")
      print(printBoard(L))
      white_move_done = False
      while white_move_done == False:
         start = time.time()
         white_move = pickMove(L, 10)
         white_piece_move = int(input("White player, enter the position of the piece to be moved"))
         white_piece_move_to = int(input("White player, enter the position where you want to move the piece"))
         l = GetPieceLegalMoves(L, white_piece_move)
         if (white_piece_move_to in l and ((10 <= L[white_piece_move]) and L[white_piece_move] <= 19)):
            L[white_piece_move_to] = L[white_piece_move]
            L[white_piece_move] = 0
            end = time.time()
            print(end - start)
            if ((end - start) > 10):
                print("Overtime")
            white_move_done = True

         else:
            print("Invalid move; try again")
         
      print("\n-----\n")
      print(printBoard(L))
      black_move_done = False
      while black_move_done == False:
         start = time.time()
         black_move = chessPlayer(L, 20)
         black_piece_move = black_move[1][0]
         print(black_move[1])
         black_piece_move_to = black_move[1][1]
         if ((20 <= L[black_piece_move]) and L[black_piece_move] <= 29):
            L[black_piece_move_to] = L[black_piece_move]
            L[black_piece_move] = 0
            end = time.time()
            if ((end - start) > 10):
               print("Overtime")
            print(end - start)
            black_move_done = True
         else:
            print("Invalid move; try again")


def playAIvsAI():
   L = init_chess()
   done = False
   while (done == False):
      print('eval = ', eval_func(L, 10))
      print('W ', len(GetPlayerPositions(L, 10)), ' B ', len(GetPlayerPositions(L,20)))
      print("\n-----\n")
      print(printBoard(L))
      white_move_done = False
      while white_move_done == False:
         start = time.time()
         white_move = pickMove(L, 10)
         white_piece_move = white_move[1][0] #int(input("White player, enter the position of the piece to be moved"))
         white_piece_move_to = white_move[1][1] #int(input("White player, enter the position where you want to move the piece"))
         l = GetPieceLegalMoves(L, white_piece_move)
         if (white_piece_move_to in l and ((10 <= L[white_piece_move]) and L[white_piece_move] <= 19)):
            L[white_piece_move_to] = L[white_piece_move]
            L[white_piece_move] = 0
            end = time.time()
            print(end - start)
            if ((end - start) > 10):
                print("Overtime")
            white_move_done = True

         else:
            print("Invalid move; try again")
         
      print("\n-----\n")
      print(printBoard(L))
      black_move_done = False
      while black_move_done == False:
         start = time.time()
         black_move = chessPlayer(L, 20)
         black_piece_move = black_move[1][0]
         print(black_move[1])
         black_piece_move_to = black_move[1][1]
         if ((20 <= L[black_piece_move]) and L[black_piece_move] <= 29):
            L[black_piece_move_to] = L[black_piece_move]
            L[black_piece_move] = 0
            end = time.time()
            if ((end - start) > 10):
               print("Overtime")
            print(end - start)
            black_move_done = True
         else:
            print("Invalid move; try again")
#humanVSAI() 
#playAIvsAI()