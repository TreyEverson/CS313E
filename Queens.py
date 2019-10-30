#  File: Queens.py

#  Description: Gives all possible arrangements of n queens on a nxn board

#  Student Name: Trey Everson

#  Unique Number: 50210

#  Date Created: 10/19/2019

#  Date Last Modified: 10/20/2019

count = 0
class Queens (object):
  # initialize the board
  def __init__ (self, n = 3):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()

  # check if no queen captures another
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True

  # do a recursive backtracking solution
  def recursive_solve (self, col):
    global count
    if (col == self.n):
      self.print_board()
      print()
      count += 1
      return 
    else:
      for i in range (self.n):
        if (self.is_valid(i, col)):
          self.board[i][col] = 'Q'
          if (self.recursive_solve (col + 1)):
            return True
          self.board[i][col] = '*'
      return False

  # if the problem has a solution print the board
  def solve (self):
    self.recursive_solve(0)        
    
def main():
  n = int(input("Enter the size of board: "))
  print()
    
  # create a regular chess board
  game = Queens (n)

  # place the queens on the board
  game.solve()
  print('There are', count,'solutions for a',n,'x',n,'board.')


main()
