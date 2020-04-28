#program to decide file type ,its size,creation date  and other meta informations.

import os
from mimetypes import MimeTypes
import time
mime=MimeTypes()
path=raw_input("Path to file >")

try:
    print "File: "+str(os.path.basename(path))+" is a :"+str(mime.guess_type(path)[0])
    c=raw_input("Do u want to have more information about it press y :")
    if(c.lower()=="y"):
        print("last modified: %s" % time.ctime(os.path.getmtime(path)))
        print("created: %s" % time.ctime(os.path.getctime(path)))
        print "file size is %s  Bytes" % ((os.stat(path).st_size))

    else:
        print "Good Bye!"
        exit()

except:
    print "Not a kmown File type check manually before you execute!"
