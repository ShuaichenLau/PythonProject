# 字典生成式
items= ['zhangsan','lisi','wangwu']
prices = [96,78,85]
#
lst = zip(items,prices)
print(lst)
print(list(lst))

for e in zip(items, prices):
    print(e)


