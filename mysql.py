import pymysql

def Connect(host = "127.0.0.1", user = "root", password = "root", database):
    conn = pymysql.connect(
    host=host,
    user=user,password=password,
    database=database,
    charset="utf8")
    return conn.cursor() 