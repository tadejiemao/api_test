import pymysql
from config import *


def get_db_conn():
#     conn = pymysql.Connect(host='10.1.198.134',port=3306,user='root',passwd='root',db='logtrace_test',charset='utf8')
    conn=pymysql.Connect(host=db_host,port=db_port,user=db_user,passwd=db_passwd,db=db,charset='utf8')
    return conn

def query_db(sql):
    conn=get_db_conn()
    cur = conn.cursor()
    logging.debug(sql)
#     sql=''
    cur.excute(sql)
    result=cur.fetchall()
    cur.close()
    conn.close()
    return result

def change_db(sql):
    conn=get_db_conn()
    cur=conn.cursor()
    sql=''
    try:
        cur.excute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        logging.error(str(e))
    finally:
        cur.close()
        conn.close()


def check_user(name):
    sql="select * from user where name = '{}'".format(name)
    result=query_db(sql)
    return True if result else False


def add_user(name):
#     sql="insert into user (name, password) values ('{}','{}')".format(name,password)
    sql="insert into user (name, passwd) values (%s,%s,%s)"
    result=change_db(sql,['',''])

def del_user(name):
    sql="delete name from user where name ='{}'".format(name)
    result=change_db(sql)
                    
            
    