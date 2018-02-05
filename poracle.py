
import cx_Oracle
import os
import sys
print(sys.stdout.encoding)

os.environ["NLS_LANG"]="SIMPLIFIED CHINESE_CHINA.ZHS16GBK"
print(cx_Oracle.version)

username = "bigdata"
pwd = "atadgib#509"
host = "192.168.60.154"
port = 1521
dbname = "orcl"

dsn = cx_Oracle.makedsn(host,port,dbname)
#print(type(dsn))
conn = cx_Oracle.connect("bigdata","atadgib#509",dsn,charset="gbk")

cursor = conn.cursor()

cursor.close()
conn.close()