list_a = {10,20,30}
list_b = {30,20,10}
list_c = {30,20,10,40}

print(list_a == list_b)
print(list_a != list_b)

# 是否子集
print(list_a.issubset(list_b))

# 是否交集 没有交集是true
print(list_a.isdisjoint(list_b))
# 并集
print(list_a.union(list_b))
# 差集
print(list_c.difference(list_a))


print(id(list_a))

hello = ' hello,hello'

print("count {}".format(hello.count('hello')))
print("find {}".format(hello.find('h')))
print("rfind {}".format(hello.rfind('h')))
print("index {}".format(hello.index('h')))
print("rindex {}".format(hello.rindex('h')))

print("not find {}".format(hello.find('A')))

# print("大小写  index {}".format(hello.index('H')))

print(hello.replace(" ","").title())



name = 'zhangsan'
age = 20
print('我的名字是%s,今年%d岁' %(name,age))
print('我的名字是{},今年{}岁'.format(name,age))

# 字符串的编码与解码

hehe = '天涯共此时'
#  编码
print(hehe.encode('UTF-8'))
print(hehe.encode('GBK'))

# 解码
print(hehe.encode('UTF-8').decode('UTF-8'))

# 编码 解码有码制异常
# UnicodeDecodeError: 'gbk' codec can't decode byte 0xad in position 10: illegal multibyte sequence
# decoding with 'GBK' codec failed
# print(hehe.encode('UTF-8').decode('GBK'))

# 乱码 可以屏蔽异常输出 errors='ignore'
print(hehe.encode('UTF-8').decode('GBK',errors='ignore'))
print(hehe.encode('GBK').decode('UTF-8',errors='ignore'))

# 战略上藐视敌人 战术上重视敌人







