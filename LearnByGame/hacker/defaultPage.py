# this file is the studying of Learnbgame/hack
#
#

import ftplib

def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        print("[-] Could not list directory contents.")
        print('[-] Skipping To Next Target.')
        return
    retList = []
    for fileName in dirList():
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print('[+] Found default page:' + fileName)
            retList.append(fileName)
    return retList
host = '218.198.196.138'
userName = 'guest'
password = 'guest'
ftp = ftplib.FTP(host)
ftp.login(userName,password)
returnDefault(ftp)









