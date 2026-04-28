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

    def update(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print("修改成功")
        except Exception as e:
            print(e)
            self.conn.rollback()

    def db1_import_db2(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print("数据库导入成功")
            return True
        except Exception as e:
            print(e)
            self.conn.rollback()

    def delete(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print("删除用户成功")
            return True
        except Exception as e:
            print(e)
            self.conn.rollback()



