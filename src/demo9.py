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
