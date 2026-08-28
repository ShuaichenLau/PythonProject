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
        id = input('请输入ID:')
        if not id:
            break
        name = input('请输入名字:')
        if not name:
            break

        try:
            english = float(input('请输入英语成绩:'))
            python = float(input('请输入python成绩:'))
            java = float(input('请输入java成绩:'))
        except:
            print('输入信息无效,请重新输入')
            continue

        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
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
def show_student_by_condition(student_query):
    if len(student_query) == 0:
        print('没有学生信息可以显示...')
        return
    else:
        for stu in student_query:
            print(stu)


def select():
    student_query = []
    while True:
        id = ''
        name = ''
        str = ''
        if os.path.exists(filename):
            model = input(
                '按照ID查找请输入1; 按照姓名查找请输入2; ID和姓名一起搜索请输入3; 模糊搜索请输入4; 返回主菜单请输入0')
            if model == '1':
                id = input('请输入学生ID')
            elif model == '2':
                name = input('请输入学生姓名')
            elif model == '3':
                str = input('请输入学生姓名或者ID')
            elif model == '4':
                str = input('请输入学生姓名或者ID')
            elif model == '0':
                return
            else:
                print('输入有误, 请重新输入')
                select()  # 递归
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '' and d['id'] == id:
                        student_query.append(d)
                    elif name != '' and d['name'] == name:
                        student_query.append(d)
                    elif model == '3' and str != '' and (d['id'] == str or d['name'] == str):
                        student_query.append(d)
                    elif model == '4' and str != '' and (str in d['id'] or str in d['name']):
                        student_query.append(d)

            show_student_by_condition(student_query)
        student_query.clear()


# 显示文件中所有的学生
def show_all_stuent():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            for line in rfile.readlines():
                print(line)
    else:
        print('文件不存在, 系统环境数据有误1')


# 统计学生总人数
def count_student():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            print('学生总人数是 {}'.format(len(rfile.readlines())))
    else:
        print('文件不存在, 系统环境数据有误2')

# todo 更新学生的逻辑还有待完善
# 更新修改学生信息
def update_student():
    show_all_stuent()
    student_list_old = []
    found = False
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list_old = rfile.readlines()

        student_id = input('请输入要修改的学生ID')
        with open(filename, 'w', encoding='utf-8') as wfile:
            for stu in student_list_old:
                if stu['id'] == student_id:
                    found=True
                    print(stu)
                    print('已经找到该学生的信息,请进行修改')
                    while True:
                        try:
                            stu['name'] = input('请输入修改后的姓名:')
                            stu['english'] = input('请输入修改后的英语成绩:')
                            stu['python'] = input('请输入修改后的Python成绩:')
                            stu['java'] = input('请输入修改后的Java成绩:')
                        except:
                            print('输入异常,请重新输入!')
                    wfile.write(stu + '\n')
                    print('修改完成!')
                else:
                    wfile.write(stu + '\n') #未修改的学生信息应该原样写回
            if found == False:
                answer=input('没有找到该学生的信息,是否要继续修改其他学生的信息? y/n \n')
                if answer == 'y' or answer == 'Y':
                    update_student()
                else:
                    return

        answer=input('是否继续修改其他学生信息? y/n\n')
        if answer == 'y' or answer == 'Y':
            update_student()


    else:
        print('文件不存在, 系统环境数据有误3')


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

            elif choice == 4:  # 修改学生信息
                update_student()

            elif choice == 6:  # 统计学生总人数
                count_student()

            elif choice == 7:
                show_all_stuent()


if __name__ == '__main__':
    main()
