#!/usr/bin/python
import MySQLdb
def handle_mysql (host,username,password,database,command,port=3306):
    ret=0;
    data='';
    print "MySQLdb.connect(host=",host,",user=",username,",passwd=",password,",db=",database,",port=",port,")";
    db = MySQLdb.connect(host=host,user=username,passwd=password,db=database,port=port);
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
        ret=2052;
    db.close();
    print "data:"
    print data
    print "end"
    return ret;