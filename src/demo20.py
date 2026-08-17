'''
学生信息管理系统
    持久化保存到文本文件
'''


import os

filename = 'students.txt'

def menm():
    print('===================学生管理系统===================')
    print('===================功能菜单======================')
    print('\t\t\t\t 1.录入学生信息')
    print('\t\t\t\t 2.查找学生信息')
    print('\t\t\t\t 3.删除学生信息')
    print('\t\t\t\t 4.修改学生信息')
    print('\t\t\t\t 5.排序')
    print('\t\t\t\t 6.统计学生总人数')
    print('\t\t\t\t 7.显示所有学生信息')
    print('\t\t\t\t 0.退出')
    print('===============================================')


# 创建学生信息
def insert():

    pass


def main():
    while True:
        menm()
        choice=int[input('请选择:')]
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n')
                if answer =='y' or answer == 'Y':
                    print('谢谢使用!')
                    break
                else:
                    continue
            elif choice == 1:
                insert()







if __name__ == '__main__':
    main()