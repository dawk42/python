#!/usr/bin/python3
def connect():
    from pexpect import pxssh
    import getpass
    try:
        ip = "192.168.142.232" #for testing
        #ip = str(input("Enter the hostname/IP:\n"))
        un = "student" #for testing
        #un = str(input("Enter the username:\n"))
        #password = getpass.getpass("Enter the password:\n")
        pw = "Password01" #for testing
        tx = pxssh.pxssh()  #simplify the code by placing the function into variable
        tx.login(ip, un, pw, sync_multiplier=5)  #login using previous input
        tx.sync_original_prompt()  #make sure we have the prompt identified
     #   tx.set_unique_prompt()
        tx.sendline ('sudo useradd egoad')  #sends command
        tx.expect ("password .*:", timeout=5)
        tx.sendline(pw)
        tx.sendline ('sudo passwd egoad')
        tx.expect('New password:')
        tx.sendline ('RubberDuck!')
        tx.expect('Retype .*:')
        tx.sendline ('RubberDuck!')
        tx.expect('passwd: .*')
        tx.prompt()
        print(tx.before)

        
        tx.sendline ('sudo dnf install httpd -y')
        #tx.expect("password for", timeout=10)
        #tx.sendline(pw)
        #tx.prompt()
        #tx.sendline('')
        #tx.prompt()
        #print(tx.before)
        tx.logout()
        print('Done')
        #print(username)
        #print(password)
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(e)

connect()
    
