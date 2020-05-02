#!/usr/bin/python3
# from random import seed
# from random import randint
def clear():
  # clear the terminal screen
  print("\n"*50)

def banner():
  # prints a banner and game mode menu
  print("""    &&& &&& &&&
   &   &   &   &
      &   &   &
     &   &   &

     *   *   *

      Welcome\n         to\n   Number Guess!!!

Note:  Numbers only please, anything else
       will probably crash the game
""")
  mode = int(input("[1]  You play computer\n[2]  Computer plays you\n[3]  Exit\n:"))
  if mode == 1:
    menu()
  elif mode == 2:
    pcmenu()
  elif mode == 3:
    exit(0)
  else:
    banner()

def menu():
  clear()
  from random import seed
  from random import randint
  global hidden_number
  global turn
  turn = 0
  level = int(input("Choose a difficulty \n [1] Easy:    1-10\n [2] Medium:  1-100\n [3] Hard:    1-1000\n [4] Exit \n:"))

  if level == 1:
    hidden_number = randint(1,10)
    print("Guess my number it is between 1 and 10...")
    game()
  elif level == 2:
    hidden_number = randint(1,100)
    print("Guess my number it is between 1 and 100...")
    game()
  elif level == 3:
    hidden_number = randint(1,1000)
    print("Guess my number it is between 1 and 1000...")
    game()
  elif level == 4:
    banner()
  else:
      print("Thats not an option, Choose again")
      menu()

def pcmenu():
  clear()
  global turn
  global user_number
  global high
  global low

  turn = 0
  level = int(input("Welcome to Number Guess!!! \n \n Choose a difficulty \n [1] Easy:    1-10\n [2] Medium:  1-100\n [3] Hard:    1-1000\n [4] Exit \n:"))

  if level == 1:
    user_number = int(input("Enter a number from 1 to 10:  \n"))
    low = 1
    high = 10
    pcgame()
  elif level == 2:
    user_number = int(input("Enter a number from 1 to 100:  \n"))
    low = 1
    high = 100
    pcgame()
  elif level == 3:
    user_number = int(input("Enter a number from 1 to 1000:  \n"))
    low = 1
    high = 1000
    pcgame()
  elif level == 4:
    banner()
  else:
    print("Thats not an option, Choose again")
    pcmenu()

def game():
  global turn
  turn+=1
  guess = int(input("Guess the number:"))
  if guess < hidden_number:
    print ("Too Low!")
    game()
  elif guess > hidden_number:
    print ("Too High")
    game()
  elif guess == hidden_number:
    print("\n\n",guess,"is the Correct Number!\n\n You guessed the number in",turn,"turns!!!")
    banner()
  # else:
  #   except(ValueError)
  #   print("Thats not a number... try again")
  #   menu()


def pcgame():
  global high
  global low
  guess = round((low + high)/2)
  #print(guess)
  print("Is your number",guess,"? \nL = too low \nH = too high \nY = You guessed correctly!!!\n")
  ask = str(input())
 # print(ask)
  if ask == "L" or ask == "l":
    low = guess
    pcgame()
  elif ask == "H" or ask == "h":
    high = guess
    pcgame()
  elif ask == "Y" or ask == "y":
    print("I guessed",guess,"and the number you thought of was",user_number)
    print("Let's Play Again \n\n")
    banner()

clear()
banner()
