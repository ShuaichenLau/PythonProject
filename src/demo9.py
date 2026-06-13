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



