#!/usr/bin/env python
import xml.parsers.expat,sys
from glob import glob

def parsefile(file):
    parser = xml.parsers.expat.ParserCreate()
    parser.ParseFile(open(file, "r"))

for arg in sys.argv[1:]:
    for filename in glob(arg):
        try:
            parsefile(filename)
            print "%s is well-formed" % filename
            exit(0)
        except Exception, e:
            print "%s is %s" % (filename, e)
            exit(1)
