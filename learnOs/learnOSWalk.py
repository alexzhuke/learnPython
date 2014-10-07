__author__ = 'modoojunko'
import os
import os.path
rootdir = "/Users/modoojunko/PycharmProjects"


for parent,dirnames,filenames in os.walk(rootdir):
    for dirname in dirnames:
        #print "parent is:" + parent
        #print "dirname is:" + dirname
        print os.path.join(parent, dirname)
    for filename in filenames:
            #print "parent is:" + parent
            #print "filename is:" + filename
        print os.path.join(parent,filename)
