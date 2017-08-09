#! /user/bin/python
        
import os ,sys
import Main

if os.path.isdir(sys.path[0]):
    os.chdir(sys.path[0])

sys.path.append('src')
Main.main()



version           = "0.1"
description       = ""
long_description  = ""

url               = "https://github.com/Fofight/Learnbgame"
download_url      = 
author            = "Fofight Fong"
author_email      = "ffofight@gmail.com"
maintainer        = "Fofight"
maintainer_email  = ""
install_requires  = 
platforms         = ["any"]
licenses           = "OSI Approved"
keywords          = ["python","pygame",]

