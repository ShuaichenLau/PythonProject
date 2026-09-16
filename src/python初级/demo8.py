t=(10,[20,30],9)
print(type(t),t)

# 元祖的便利

t=('Python','Word',98)
print(t[0])
print(t[1])
print(t[2])

for item in t:
    print(item)
print("====================")



list={10,20,30}
print(10 in list)
print(10 not in list)

list.add(40)
print(list)

list.update({50,60,70,90})
print(list)

list.remove(90)
print(list)

list.discard(90)
print(list)

list.pop()
print(list)

list.clear()
print(list)


