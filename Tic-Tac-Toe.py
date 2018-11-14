board = [" " for i in range(0,9)]

def print_board():
     print(" {}|{}|{} ".format(board[0],board[1],board[2]))
     print(" {}|{}|{} ".format(board[3],board[4],board[5]))
     print(" {}|{}|{} ".format(board[6],board[7],board[8]))

def is_vict(turn):
     if turn == 1:
          icon = "X"
     else:
          icon = "O"
     if((board[0]==icon and board[1]==icon and board[2]==icon) or (board[3]==icon and board[4]==icon and board[5]==icon) or (board[6]==icon and board[7]==icon and board[8]==icon) or (board[0]==icon and board[3]==icon and board[6]==icon) or (board[1]==icon and board[4]==icon and board[7]==icon) or (board[2]==icon and board[5]==icon and board[8]==icon) or (board[0]==icon and board[4]==icon and board[8]==icon) or (board[2]==icon and board[4]==icon and board[7]==icon) ):
          return True
     else:
          return False

def is_draw():
     if " " not in board:
          return True
     else:
          return False
     

def check(turn):
     if is_vict(turn):
          print("Congratulations!! Player {} wins".format(turn))
          return True
     elif is_draw():
          print("Game over! Its a draw")
          return True
     else:
          return False

def move(turn):
     choice = int(input("Where do you want to mark player {}: ".format(turn)).strip())
     if board[choice - 1] == " ":
          if turn==1:
               board[choice - 1] = "X"
          else:
               board[choice - 1] = "O"
     else:
          print("That position is already marked")
          move(turn)
          
while True:
     print_board()
     turn = 1
     print("Your turn Player {}",turn)
     move(turn)
     print_board()
     if check(turn):
          break
     turn = 2
     print("Your turn Player {}",turn)
     move(turn)
     if check(turn):
          break
     
