# this file is the content of the Learnbgame/hack
#
#

import pxssh

def send_command(s,cmd):
    s.sendline(cmd)
    s.prompt()
    print(s.before)

def connect(host,user,password):
    try:
        s.pxssh.pxssh()
        s.login(host,user,password)
        return s
    except:
        print('[-] Error connecting')
        exit(0)

s =  connect('127.0.0.1','root','19960320')
send_command(s,'cat /etc/shadow | grep root')














