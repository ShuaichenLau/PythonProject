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
def show_all_stuentd():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            for line in rfile.readlines():
                stu_dict = eval(line)
                print(stu_dict)  # 输出不再带有额外多余的空行
    else:
        print('文件不存在, 系统环境数据有误1')


# 统计学生总人数
def count_student():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            print('学生总人数是 {}'.format(len(rfile.readlines())))
    else:
        print('文件不存在, 系统环境数据有误2')


# 更新学生的逻辑还有待完善
# 更新修改学生信息
def update_student():
    show_all_stuentd()
    student_list_old = []
    found = False
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list_old = rfile.readlines()

        student_id = input('请输入要修改的学生ID')
        with open(filename, 'w', encoding='utf-8') as wfile:
            for stu in student_list_old:
                stu_dict = eval(stu)

                if stu_dict['id'] == student_id:
                    found = True
                    print(stu_dict)
                    print('已经找到该学生的信息,请进行修改')
                    while True:
                        try:
                            stu_dict['name'] = input('请输入修改后的姓名:')
                            stu_dict['english'] = input('请输入修改后的英语成绩:')
                            stu_dict['python'] = input('请输入修改后的Python成绩:')
                            stu_dict['java'] = input('请输入修改后的Java成绩:')

                            wfile.write(str(stu_dict) + '\n')  # 将字典转为字符串再拼接
                            print('修改完成!')
                            break
                        except Exception as e:
                            print(f'输入异常，原因: {e}，异常类型: {type(e).__name__}')
                            print('输入异常,请重新输入!')

                else:
                    wfile.write(str(stu_dict) + '\n')  # 未修改的学生信息应该原样写回
            if found == False:
                answer = input('没有找到该学生的信息,是否要继续修改其他学生的信息? y/n \n')
                if answer == 'y' or answer == 'Y':
                    update_student()
                else:
                    return

        answer = input('是否继续修改其他学生信息? y/n\n')
        if answer == 'y' or answer == 'Y':
            update_student()


    else:
        print('文件不存在, 系统环境数据有误3')
        return


'''删除学生信息'''


def delete():
    # 先根据ID查找学生 找到就删除 找不到就返回不存在这个学生 并且再次询问是否删除其他学生信息
    student_old = []
    while True:
        stuId = input('请输出要删除学生的ID:')
        if stuId != '' and os.path.exists(filename):
            delete_flag = False
            with open(filename, 'r', encoding='utf-8') as rfile:
                student_old = rfile.readlines()

            with open(filename, 'w', encoding='utf-8') as wfile:
                d = {}
                for item in student_old:
                    d = eval(item)
                    if stuId != d['id']:
                        wfile.write(item)
                    else:
                        delete_flag = True
            if delete_flag:
                print('学生ID{}的学生信息已经删除'.format(stuId))
            else:
                print('没有找到学生ID{}的学生信息'.format(stuId))
            answer = input('还要继续删除学生信息吗? y/n \n')
            if answer.lower() != 'y':
                return

        else:
            student_old = []
            print('无学生信息')
            break
    return


# 排序
def sort_stu():
    student_list = []
    show_all_stuentd()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        student_dict = []
        for item in student_list:
            stu_dict = eval(item)
            student_dict.append(stu_dict)
    else:
        print('文件不存在, 系统环境数据有误4')

    while True:
        asc_or_desc_bool = True
        asc_or_desc = input('请选择排序方式 0升序 1降序')
        if asc_or_desc == '0':
            asc_or_desc_bool = False
        else:
            asc_or_desc_bool = True

        model = input('排序字段, 1按英语排序, 2按python排序 3按java排序 4按总成绩排序 5退出')
        if model == '1':
            student_dict.sort(key=lambda stu_dict: stu_dict['english'], reverse=asc_or_desc_bool)
            show_stu_dict(student_dict)
        elif model == '2':
            student_dict.sort(key=lambda stu_dict: stu_dict['python'], reverse=asc_or_desc_bool)
            show_stu_dict(student_dict)
        elif model == '3':
            student_dict.sort(key=lambda stu_dict: stu_dict['java'], reverse=asc_or_desc_bool)
            show_stu_dict(student_dict)
        elif model == '4':
            student_dict.sort(
                key=lambda stu_dict: int(stu_dict['java']) + int(stu_dict['python']) + int(stu_dict['english']),
                reverse=asc_or_desc_bool)
            show_stu_dict(student_dict)
        elif model == '5':
            return
        else:
            print('您的输入有误,请重新输入')


def show_stu_dict(list):
    if len(list) == 0:
        print('没有学生信息')
        return
    else:
        for item in list:
            print(item)


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
            elif choice == 3:  # 删除
                delete()
            elif choice == 4:  # 修改学生信息
                update_student()

            elif choice == 5:  # 排序
                sort_stu()

            elif choice == 6:  # 统计学生总人数
                count_student()

            elif choice == 7:
                show_all_stuentd()


if __name__ == '__main__':
    main()
