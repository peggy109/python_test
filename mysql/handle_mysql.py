#!/usr/bin/python
import MySQLdb
def handle_mysql (host,username,password,database,command):
    db = MySQLdb.connect(host,username,password,database);
    cursor = db.cursor();
    try:
        cursor.execute(command);
        data = cursor.fetchall();
        print "data:"
        print data
        print "end"
        print "host:",host
        print "username:",username
        print "database:",database
        print "command:",command
        if (command.startswith("delete") == True) or (command.startswith("update") == True) or (command.startswith("insert") == True) :
            print "will commit:"
            db.commit();
    except:
        db.rollback();
    db.close();
    print "data:"
    print data
    print "end"