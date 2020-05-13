#!/usr/bin/python3
import pexpect
from pexpect import pxssh
import getpass

def db_setting():
	ip = '192.168.0.121'
	un = 'justincase'
	pw = 'Password01' #NEVER NEVER in production  Testing only
	#import getpass
	#pw = getpass.getpass('Enter the password:\n')
	db(un, ip, pw)

def db(un, ip, pw):

    try:
        tx = pxssh.pxssh()  #simplify the code by placing the function into variable
        tx.login(ip, un, pw, sync_multiplier=5)  #login using previous input
        tx.sync_original_prompt()  #make sure we have the prompt identified
        tx.sendline ('sudo dnf -y install MariaDB-server')
        tx.expect ("password .*:", timeout=5)
        tx.sendline(pw)
        tx.expect(".*Complete!", timeout=240)
        print("Installed MariaDB Server")
        tx.prompt()
        tx.sendline('sudo systemctl start httpd')
        tx.prompt()
        tx.sendline('sudo systemctl enable --now mariadb')
        tx.expect('Created .*')
        print('Service MariaDB enabled')
        tx.prompt()
        tx.sendline('sudo systemctl status mariadb')
        tx.expect('.*active.*')
        print('Service mariadb start verified')
        tx.close(force=True)
        tx.prompt(tx, timeout=-1)
        tx.logout()
        tx.close()
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(e)

web_setting()

