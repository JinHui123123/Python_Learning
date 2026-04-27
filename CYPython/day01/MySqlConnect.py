import pymysql

class MySqlTest:
    def __init__(self):
        self.username = "root"
        self.password = "123456"
        self.host = "localhost"
        self.dbs = "user_manage"
        self.connect()

    #连接MySql数据库
    def connect(self):
        self.conn = pymysql.connect(user=self.username,passwd=self.password,host=self.host,db=self.dbs)
        self.cur = self.conn.cursor()
        return self.cur

    def close_mysql(self):
        self.cur.close()
        self.conn.close()

    def fetch_all(self): #查询
        cur = self.connect()
        sql = 'select * from user'
        cur.execute(sql)
        result = cur.fetchall()
        for i in result:
            print(str(i))
        self.close_mysql()

    def insert_mysql(self):
        pass

    def fetchone(self,sql):
        self.cur.execute(sql)
        res = self.cur.fetchone()
        return res






