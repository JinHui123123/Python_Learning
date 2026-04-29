import hashlib

#MD5加密
#生成一个加密对象
m = hashlib.md5()
#对123字符加密 加密的数据类型是bytes类型
str1 = "123"
#字符串转换为bytes类型
str_b = bytes(str1, "utf-8")
m.update(str_b)
#hexdigest 获取16进制的加密之后的字符串
res = m.hexdigest()
print(res)

# 没有解密方法  202cb962ac59075b964b07152d234b70
# 把加密后的16进制字符串 存入数据库