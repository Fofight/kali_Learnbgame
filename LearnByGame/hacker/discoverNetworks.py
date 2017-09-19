# this file is the studying notes of Learnbgame/hack
#
# by which we can found the location where we located past
#

import os 
import optparse
import mechanize
import urllib
import re 
import urlparse
from _winreg import *

def val2addr(val):
    addr = ''
    for ch in val:
        addr += "%02x "% ord(ch)
        addr = addr.strip('').replace('',':')[0:17]
        return addr

def wiglePrint(username,password,netid):
    browser = mechanize.Browser()
    browser.open('http://wigle.net')
    reqData = urllib.urlencode({"credential_0": username,'credential_1':password})

    browser.open('https://wigle.net//gps/gps/main/login',reqData)
    params = {}
    params['netid'] = netid
    reqParams = urllib.urlencode(params)





















