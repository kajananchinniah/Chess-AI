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

