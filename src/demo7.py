# 字典生成式
items= ['zhangsan','lisi','wangwu']
prices = [96,78,85]
#
lst = zip(items,prices)
print(lst)
print(list(lst))

for e in zip(items, prices):
    print(e)

# 空列表
lst = []
lst1 = list()
# 空字典
d = {}
d2 = dict()
# 空元祖
t4 = ()
t5 = tuple()

# 在python中 列表/字典/元祖 区别是什么?

print(type(lst),type(d),type(t4))
print(type(lst1),type(d2),type(t5))
