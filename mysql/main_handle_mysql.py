#!/usr/bin/python
import subprocess;
import sys;
host = sys.argv[1];
username = sys.argv[2];
password = sys.argv[3];
database = sys.argv[4];
command = sys.argv[5];
import handle_mysql;
ret = handle_mysql.handle_mysql(host,username,password,database,command);
print "ret:",ret

exit(ret);


