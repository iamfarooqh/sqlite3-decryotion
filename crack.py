#! /usr/bin/python
from pysqlcipher import dbapi2 as sqlite
import sys
conn = sqlite.connect(sys.argv[1])
c = conn.cursor()

f = open(sys.argv[2], 'r')
for line in f:
    st = line.strip()
    print "Trying: " + st
    c.execute("PRAGMA key='" + st + "'")
    try:
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print "key is '" + st + "'"
        break
    except:
        pass
