import sys
#import random
from random import randint

#from random import seed

#from datetime import datetime

# lets us have random integers

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# defines the number list
sym = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`',
       '~', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
       ';', ':', "'", '"', ',', '.', '<', '>', '/', '?']
# defines the symbol list
low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#defines the lowercase alphabet
upp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
       'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#defines the upcase alphabet
pw = ""  #sets pw to an empty str variable
alpha = low + upp
charset = low


def choice():
    global dif
    global dif2
    # request password length
    dif = int(input("Enter Desired Password Length 8 - 300 characters:\n"))
    while dif < 8 or dif > 300: # makes sure password length is correct
        choice()
        if  8 <= dif <= 300:
            continue
    dif2 = dif #backs up dif var so it can be reset to gen a second password
    print("PASSWORD GENERATOR QUIZ!!!\n")
    upper()

def upper():  
    global charset
    global upp

    option = str(input('Upper case y/n: '))
    if option == 'y':
        charset += upp
        print("Including Upper Case...")
        numb()
    elif option == 'n':
        numb()
    else:
        upper()

def numb():
    global charset
    global num
    option = str(input('Numbers? y/n: '))
    if option == 'y':
        charset += num
        print("Including Numbers...")
        symb()
    elif option == 'n':
        symb()
    else:
        numb()

def symb():
    global charset
    global sym
    option = str(input('Symbols? y/n: '))
    if option == 'y':
        charset += sym
        print ("Including Symbols...")
        exc1()
    elif option == 'n':
        exc1()
    else:
        symb()

def exc1():
    global charset
    option = str(input('Leave out i, l, L, 1 and !? y/n: '))
    if option == 'y':
        exclude = {'i', 'l', 'L', '1', '!'}
        charset = [char for char in charset if char not in exclude]  #iterate the charset and remove the exclude list
        print("Removing Similar characters...")
        exc2()
    elif option == 'n':
        exc2()
    else:
        exc1()

def exc2():
    global charset
    option = str(input('Leave out  {}[]()/\\!\'",;:>,.? y/n: '))
    if option == 'y':
        exclude = {'{', '}', '[', ']', '(', ')', '/', '\\', '"', "'",
                   '!', ':', ';', '>', '<', ',', '.', '?'}
        charset = [char for char in charset if char not in exclude]

        print("Removing some symbols...")
        first_letter()
    elif option == 'n':
        first_letter()
    else:
        exc2()

def first_letter():
    global charset
    option = str(input('Ensure the first character is a letter y/n: '))
    if option == 'y':
        fchar()
    elif option == 'n':
         pwgen()
    else:
        first_letter()
def fchar():
    global pw
    global dif
    dif2 = dif
    pw = alpha[(randint(1, len(alpha))-1)]
    dif2 -= 1
    while dif2 > 0:
            gen += charset[(randint(1, len(charset))-1)]
            dif2 -= 1
            continue
    pw = gen
    print(pw)
    count()

def pwgen():
    global dif
    global pw
    dif2 = dif
    while dif2 > 0:
        gen += charset[(randint(1, len(charset))-1)]
        dif2 -= 1
        continue
    pw = gen
    print(pw)
    count()

def count():
    global dif    
    option = str(input('Would you like another password y/n/r: '))
    if option == 'y':
       # dif = dif2   #resets dif
        first_letter()
    elif option == 'r':
        reset()
    elif option == 'n':
        sys.exit(0)
    else:
        count()

def reset():
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    # defines the number list
    sym = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`',
           '~', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
           ';', ':', "'", '"', ',', '.', '<', '>', '/', '?']
    # defines the symbol list
    low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #defines the lowercase alphabet
    upp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    #defines the upcase alphabet
    pw = ""
    alpha = low + upp
    charset = []
    choice()
#def leave():
 #   exit()
choice()
