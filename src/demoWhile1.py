num_d = 3.14
lst = ["aa", "aa", "呵呵", "哈哈", 1, 33, num_d]

print(len(lst))
print(type(lst))
for item in lst:
    print("id是{},类型是{}, value是{}".format(id(item), type(item), item))

# lst2 = list(lst)
lst2 = lst
print(len(lst2))
print(type(lst2))

lst2.append("helloWorld")
for item in lst:
    print("id是{},类型是{}, value是{}".format(id(item), type(item), item))
print("====================================")
for item in lst2:
    print("id是{},类型是{}, value是{}".format(id(item), type(item), item))

print(lst == lst2)

print(lst2.index("helloWorld"))
# print(lst2.index("helloWorld",1,2))
print(lst2.count("aa"))
print("========================================================================")
lst3 = list(lst)
lst3.append("bbb")
lst3.append(True)
lst3.append(False)
lst3.append(False)
lst3.extend(lst2)
lst3.insert(0, "cccd")

print("包含aa的数量 {}".format(lst3.count("aa")))
print(lst3)
lst3.sort(key=str)
print(lst3)
lst3[0] = 2
print(lst3)

lst4 = [x * x for x in range(1, 10)]
print(lst4)

lst5 = [2 ** (x - 1) for x in range(1, 20)]
print(lst5)

lst6 = [2 << x for x in range(1, 20)]
print(lst6)

print(6 << 3)

"""
1 << x (左移 $x$ 位)
同理，它在十进制里就是 $1 \times 2^x$。
"""

lst7 = {"zhangsan": 11, "lisi": 12}
print(type(lst7))

print(lst7.get("zhangsan"))

for item in lst7:
    print(item + "  " + str(lst7[item]))
