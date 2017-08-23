#!/usr/bin/python
import MySQLdb
def query_mysql (host,username,password,database,command):
    ret=0;
    data='';
    db = MySQLdb.connect(host,username,password,database);
    cursor = db.cursor();
    cursor.execute(command);
    data = cursor.fetchall();
    db.close();
    print "data_"+str(data)+"_end"
    return ret;