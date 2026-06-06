f = open('data.txt', 'r', encoding='utf-8')
print(f.read())
f.close()
print("=======================================")

with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.replace('\n', ''))

print("=======================================")

with open('data.txt', 'r', encoding='utf-8') as f:
    print(f.readlines())

with open('data.txt', 'r', encoding='utf-8') as f:
    with open('data1.txt', 'w', encoding='utf-8') as f1:
        for line in f.readlines():
            f1.writelines(line)

with open('data1.txt', 'a', encoding='utf-8') as f:
    f.writelines("我欲乘风归去1,\n")
    f.writelines("又恐琼楼玉宇2,\n")

with open('data1.txt', 'a+', encoding='utf-8') as f:
    f.writelines("我欲乘风归去3,\n")
    f.writelines("又恐琼楼玉宇4,\n")
