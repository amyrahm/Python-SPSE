#Directory travesing like tree
import os

path=raw_input("Enter path for travesing   >")
level=1
for root,dirs,files in os.walk(path):
    p=root.split(os.sep)
    print "directory:-"+((len(p) - 1)) * '+', os.path.basename(root)
    print "|"
    for file in files:
        print "file :"+len(p) * '-', file
