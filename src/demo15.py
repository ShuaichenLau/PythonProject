import math


class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('{} 汽车已经启动'.format(self.brand))

    def stop(self):
        print('{} 汽车已经停止'.format(self.brand))


bmw=Car('BMW_X3')
bmw.start()

print(dir(bmw))


print(id(math))
print(type(math))

print(math)
print(math.pi)

print(math.log2(2))

'''
模式含义如果文件存在如果文件不存在常用场景
'r'只读 (Read)从头开始读取报错 (FileNotFoundError)默认模式，读取配置文件或文本
'w'只写 (Write)直接清空旧内容并覆盖自动创建新文件重新生成日志、保存新数据
'a'追加 (Append)保留原内容，在末尾写入自动创建新文件记录日志（Log）、追加日志行
'x'排他创建 (eXclusive)报错 (FileExistsError)自动创建新文件防止误覆盖已有文件（安全写入）
'''

# 声明list
lines=[]

#  上下文管理器
with open('data.txt','r',encoding='UTF-8') as file:
    for line in file:
        print(line)
        lines.append(line)


print("=========================")
print("打印输出",lines)

# with open('output.txt', 'w', encoding='UTF-8') as out_file:

with open('output.txt','w',encoding='UTF-8') as out_file:
    out_file.writelines(lines)
print("=========================")


with (open('output1.txt','w',encoding='UTF-8') as out_file1):
    for line in lines:
        out_file1.write(line)
    out_file1.write('\n')
    out_file1.write('HelloWorld+++\n')
    out_file1.writelines('HelloWorld===')
print("=========================")








