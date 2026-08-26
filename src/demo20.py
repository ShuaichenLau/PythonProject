'''
学生信息管理系统
    持久化保存到文本文件
'''

import os
from os import write

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


# 保存学生信息到文件
def saveStudent(student_list):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for student in student_list:
        stu_txt.write(str(student) + '\n')
    stu_txt.close()

def insert():
    student_list = []
    while True:
        id=input('请输入ID:')
        if not id:
            break
        name=input('请输入名字:')
        if not name:
            break

        try:
            english=float(input('请输入英语成绩:'))
            python=float(input('请输入python成绩:'))
            java=float(input('请输入java成绩:'))
        except:
            print('输入信息无效,请重新输入')
            continue

        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        student_list.append(student)
        print('学生信息 {} 已保存'.format(student))
        answer = input('是否继续添加？y/n \n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    saveStudent(student_list)
    print('学生信息录入完毕')

#  查找学生信息
def select():
    pass


def main():
    while True:
        menm()
        choice = int(input('请选择:'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n \n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢使用!')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                select()


if __name__ == '__main__':
    main()
