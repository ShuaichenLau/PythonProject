num_a = 0
num_b = 0
num_c = 0

while num_a <= 100:
    num_b += num_a
    if num_a % 10 == 0:
        num_c += num_a
    num_a += 1

print("num_a={}".format(num_a))
print("num_b={}".format(num_b))
print("num_c={}".format(num_c))

with open('data2.txt', 'w', encoding='utf-8') as f:
    f.writelines("num_a={}\n".format(num_a))
    f.writelines("num_b={}\n".format(num_b))
    f.writelines("num_c={}\n".format(num_c))

item_num = range(101)

num_x = 0
num_y = 0

for item in item_num:
    if item % 2 == 0:
        num_x += item
    else:
        num_y += item

print("偶数之和 numX={}".format(num_x))
print("奇数之和 numY={}".format(num_y))

# 水仙花(阿姆斯特朗数)  100到999之间的水仙花
item_num_a = range(100, 1000)
for item in item_num_a:
    num_str = str(item)
    n = len(num_str)

    total_sum = 0
    for i in num_str:
        total_sum += int(i) ** n
    if total_sum == item:
        print("水仙花数:{}".format(item))
