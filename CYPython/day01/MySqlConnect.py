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

    # 查询全部
    def fetch_all(self):
        cur = self.connect()
        sql = 'select * from user'
        cur.execute(sql)
        result = cur.fetchall()
        for i in result:
            print(str(i))
        self.close_mysql()


    # 查找单个
    def fetchone(self,sql):
        self.cur.execute(sql)
        res = self.cur.fetchone()
        return res

    # 修改
    def update(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print("修改成功")
        except Exception as e:
            print(e)
            self.conn.rollback()

    # 导入user old
    def db1_import_db2(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print("数据库导入成功")
            return True
        except Exception as e:
            print(e)
            self.conn.rollback()

    # 删除
    def delete(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print("删除用户成功")
            return True
        except Exception as e:
            print(e)
            self.conn.rollback()

    # 注册
    def insert(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print("插入用户成功")
            return True
        except Exception as e:
            print(e)
            self.conn.rollback()

    # 查询个人信息
    def query(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            res_list = self.cur.fetchall()
            for i in res_list:
                print(str(i))
            print("查询用户信息成功")
        except Exception as e:
            print(e)
            self.conn.rollback()


