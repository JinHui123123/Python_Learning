a = 'abcdefghigklmno'
print(a[1:5]) #bcde

print(a[1:6:2])  #bdf 从截取的长度开始计算

print(a[:]) #abcdefghigklmno   提取整个

print(a[2:]) #cdefghigklmno 从下标2开始

print(a[:3]) #abc 从0开始到3截至

print(a[::-1]) #onmlkgihgfedcba 逆序排列

# 倒叙输出  to be or not to be
print("to be or not to be"[::-1])

# 输出所有s   sxtsxtsxtsxt
print("sxtsxtsxtsxt"[::3])
