#Copyright (C) 2013 Fofight Fong
#
#This file is part os LearnByGame.
#
import os

_version = ''

def version():
    global _version
    if _version == '':
        f = open(os.path.join('doc','version.txt'),'rU')
        _version = f.read()
        f.close()
def main():
    print('LearnByGame From Fofight')
    print(version())
