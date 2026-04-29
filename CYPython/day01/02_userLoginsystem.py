from MySqlConnect import MySqlTest
import random
import hashlib

class UserManage:
    def __init__(self):
        self.mt = MySqlTest()

    def main(self):
        print("——————————欢迎来到用户管理系统————————")
        opt = input("请选择登录(1) 或 注册(2):")
        if opt == 1:
            # 登录
            while True:
                account = input("请输入账号：")
                password = input("请输入密码：")
                islogin = self.login(account, password)
                if not islogin:
                    print("输入的账户或密码错误！")
                else:
                    #登录成功
                    num = input("您是否需要修改个人信息(输入1) 或 注销账户(输入2):")
                    if num == "1":
                        self.modefy(account)
                    elif num == "2":
                        self.cancel(account)
                    break
        elif opt == "2":
            # 注册
            while True:
                account = input("请输入账号：")
                isreg = self.register(account)
                if isreg:
                    print("-----账户注册成功-----")
                    break
                else:
                    print("-----账户已存在-----")

        else:
            print("------请输入正确的选项-------")


    # 登录 如果登录成果返回 true 否则false
    def login(self,account, password):
        #查询数据库中所有的信息
        sql = f"select * from user where account ='{account}' and password ='{password}';"
        res = self.mt.fetchone(sql)
        if res:
            while True:
                # 说明账号密码正常 然后随机验证码
                code = str(int(random.random() * 10000))
                u_code = input(f"请输入验证码({code}):\n")
                # 判断验证码是否输入正确
                if u_code == code:
                    print("登录成功，可以进行一下步操作")
                    return True
                else:
                    print("--------验证码有误,请重新输入验证码---------")

    # 修改
    def modefy(self,account):
        pwd1 = input("请输入新密码:")
        pwd2 = input("请确认密码:")
        nk = input("请输入新昵称:")
        if pwd1 == pwd2:
            sql = f"update user set password = '{pwd1}',nicname = '{nk}' where account ='{account}';"
            self.mt.update(sql)

        else:
            print("两次密码不正确!")
            self.modefy(account)

    #注销
    def cancel(self,account):
        # 把user表中的账户信息导入到user_old
        sql = (f"insert into user_old (account,password,nicname) "
               f"select account,password,nicname from user where account ='{account}';")
        # 从一个数据库导入到另一个数据库
        res1 = self.mt.db1_import_db2(sql)

        sql = f"delete from user where account ='{account}';"
        res2 = self.mt.delete(sql)

        if res1 and res2:
            print("-----用户注销成功-----")

    #加密
    def md5(self,str1):
        # MD5加密
        # 生成一个加密对象
        m = hashlib.md5()
        # 字符串转换为bytes类型
        str_b = bytes(str1, "utf-8")
        m.update(str_b)
        # hexdigest 获取16进制的加密之后的字符串
        res = m.hexdigest()
        #只需要加密后的前十位  字符串
        return res[:10]

    # 注册
    def register(self,account):
        sql = f"select account from user where account ='{account}';"
        res = self.mt.fetchone(sql)
        if res:
            #已经存在
            return False
        else:
            #用户不存在 输入密码
            pwd1 = input("请输入密码：")
            pwd2 = self.md5(pwd1)
            nickname = input("请输入昵称:")
            sql = (f"insert into user(account,password,nicname) values"
                   f"('{account}','{pwd2}','{nickname}');")
            print(sql)
            return self.mt.insert(sql)



if __name__ == '__main__':
    um = UserManage()
    um.main()
