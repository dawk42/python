from random import randint
# lets us have random integers

num = ['1','2','3','4','5','6','7','8','9','0']
# defines the number list
sym = ['!','@','#','$','%','^','&','*','(',')','`','~','-','_','=','+','[',']','{','}','\\','|',';',':',"'",'"',',','.','<','>','/','?']
# defines the symbol list
low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
#defines the lowercase alphabet
upp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
#defines the upcase alphabet
pw = ""
alpha = low + upp
charset = ""

def choice():
    global dif
    # request password length
    dif = int(input("Enter Desired Password Length 8 - 300 characters:\n"))
    while dif < 8 or dif > 300: # makes sure password length is correct
        choice()
        if dif >= 8 and dif <= 300:
            continue
    options()
    
def options():
    global charset
    print("PASSWORD GENERATOR QUIZ!!!\n")
    option = str(input('Ensure the first character is a letter y/n: '))
    if option == 'y':
        fchar()
    else:
        upper()

def upper():
    global charset
    global upp
    option = str(input('Upper case y/n: '))
    if option == 'y':
        temp = charset + upp
        charset = temp
        print ("Passed Upper")
        lower()
    else:
        lower()

def lower():
    global charset
    global low
    option = str(input('Lower case y/n: '))
    if option == 'y':
        temp = charset + low
        charset = temp
        numb()
    else:
        numb()
def numb():
    global charset
    global num
    option = str(input('Numbers? y/n: '))
    if option == 'y':
        charset += num
        print(charset)
        sym()
    else:
        sym()

def symb():
    global charset
    global sym
    option = str(input('Symbols? y/n: '))
    if option == 'y':
        charset += sym
        print(charset)
        ecx1()
    else:
        ecx1()

def exc1():
    global charset
    option = str(input('Leave out i, l, L, 1 and !? y/n: '))
    if option == 'y':
        exclude = {'i','l','L','1','!'}
        charset = [char for char in charset if char not in exclude]
        print(charset)
        ecx2()
    else:
        ecx2()

def exc2():
    global charset
    option = str(input('Leave out  {}[]()/\\!\'",;:>,.? y/n: '))
    if option == 'y':
        exclude = {'{','}','[',']','(',')''/','\\','"',"'",'!',':',';','>','<',',','.','?'}
        charset = [char for char in charset if char not in exclude]

        print(charset)
        ecx2()
    else:
        ecx2()

#  generate multiple passwords to choose from
def count():
    option = str(input('How many passwords do you want to generate?: '))
    print(pwgen()* option)

def fchar():
    global pw
    global dif
    pw = alpha[(randint(1,len(alpha))-1)]
    dif -= 1
    upper()

def pwgen():
    global dif
    global pw
    #pwlen = randint(1,dif)
    size = len(charset)
    while dif > 0:
        pw += charset[(randint(1,len(charset)-1))]
        dif -= 1
        print (pw)

choice()
#print(charset)
#pwgen()
