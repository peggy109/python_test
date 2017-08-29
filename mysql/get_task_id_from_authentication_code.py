#!/usr/bin/python
import MySQLdb
import sys;
host = sys.argv[1];
username = sys.argv[2];
password = sys.argv[3];
database = sys.argv[4];
authentication_code = sys.argv[5];

ret = 0;
#print "host:", host
#print "username:", username
#print "database:", database

query="select max(task_id) from verify_tasks where authentication_code='"+authentication_code+"'";
#print "query:", query
db = MySQLdb.connect(host, username, password, database);
cursor = db.cursor();
cursor.execute(query);
data = cursor.fetchall();
db.close();
#print "data:"
#print data
#print "end"
task_id_str=str(data).replace("((","").replace("L,),)","");
print task_id_str

if task_id_str.isdigit() :
    exit(0);
else :
    exit(2051);




