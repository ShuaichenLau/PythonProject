'''
调用与操作系统相关的一个模块
os模块的常用函数
'''

import os
from os import listdir, getcwd

# os.system('notepad.exe')
print(os.getcwd())
# 返回指定路径下的文件和目录信息
print(listdir(getcwd()))

if os.path.exists('hh_test'):
    os.rmdir('hh_test')
    print('删除文件夹 hh_test')
    os.mkdir('hh_test')
    print('重新创建文件夹 hh_test')
dirlist = listdir(getcwd())
for dir in dirlist:
    print(dir + ' 是否为文件夹=> '+ ('是' if os.path.isdir(dir) else '否'))

'''
getcwd 输出当前系统目录


'''

strA = 'a';
strB = 'B';

print(strA+strB+'C')

