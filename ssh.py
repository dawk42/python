#!/usr/bin/python3
def connect():
    from pexpect import pxssh
    import getpass
    try:
        ip = "192.168.142.241"
        un = "student"
        #password = getpass.getpass('password:')
        pw = "Password01"
        tx = pxssh.pxssh()
        tx.login(ip, un, pw, sync_multiplier=5)
        tx.sync_original_prompt()
     #   tx.set_unique_prompt()
        tx.sendline ('sudo su')
        tx.expect("password for", timeout=10)
        tx.sendline(pw)
        tx.prompt()
        tx.sendline('dnf install httpd -y')
        tx.prompt()
        print(tx.before)
        tx.logout()
        print('Done')
        #print(username)
        #print(password)
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(e)

connect()
    
