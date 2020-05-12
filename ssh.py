#!/usr/bin/python3
def connect(un, ip, pw):
    import pexpect
    from pexpect import pxssh
    import getpass
    try:
        #ip = "192.168.142.232" #for testing
        #ip = str(input("Enter the hostname/IP:\n"))
        #un = "student" #for testing
        #un = str(input("Enter the username:\n"))
        #password = getpass.getpass("Enter the password:\n")
        #pw = "Password01" #for testing
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
        print("Created User egoad with a secret password!")

        
        tx.sendline ('sudo dnf install httpd -y')
        tx.expect(".*Complete!", timeout=120)
        print("Installed Web Server")
        #tx.sendline(pw)
        tx.prompt()
        tx.sendline('sudo systemctl start httpd')
        tx.prompt()
        tx.sendline('sudo systemctl enable httpd')
        tx.expect('Created .*')
        print('Service httpd enabled')
        tx.prompt()
        tx.sendline('sudo systemctl status httpd')
        tx.expect('.*active.*')
        print('Service httpd start verified')
        tx.close(force=True)
        #tx.prompt()
        tx.prompt(tx, timeout=-1)
        tx.logout()
        tx.close()
        exit()
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(e)

connect()
