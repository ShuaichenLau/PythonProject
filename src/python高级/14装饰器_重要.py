import os
import sys
import time
from functools import wraps

user_login_flag = False  # 用户还没有登陆


def login(password_file):
    """
    定义了一个用户认证的装饰器
    :param password_file: 用户信息所在的文件，文件内容格式：{'username': '用户名', 'password': '密码'}
    :return:
    """

    def login_decorator(func):
        # 用户认证之前的准备工作
        users = []  # 暂存所有的用户信息
        if os.path.exists(password_file):  # 用户信息文件是否存在
            with open(password_file, encoding='utf8') as f:
                lines = f.readlines()  # 读取文件的内容
                for line in lines:  # 每一行代表一个用户信息
                    user = eval(line)  # user是一个字典
                    users.append(user)
        else:  # 用户信息文件不存在， 可能是第一次：由用户输入新的用户名和密码，并保存到文件中
            choice = input('是否要创建新用户(Y/N):')
            if choice == 'Y' or choice == 'y':
                with open(password_file, mode='w', encoding='utf8') as f:
                    username = input('请输入新用户的用户名:')
                    password = input('请输入新用户的密码:')
                    user = {'username': username, 'password': password}
                    users.append(user)
                    f.write(str(user) + '\n')  # 把用户名和密码写到文件中
            else:
                print('没有用户信息，直接退出')
                sys.exit(1)

        @wraps(func)
        def inner(*args, **kwargs):
            """开始装饰： 用户认证"""
            global user_login_flag
            if user_login_flag is False:  # 用户还没有登陆认证
                un = input('请输入登陆的用户名:')
                pwd = input('请输入登陆的密码:')
                for u in users:
                    if un == u['username'] and pwd == u['password']:
                        print(f'欢迎{un}登陆成功！！')
                        user_login_flag = True
                        break
                else:
                    print('你输入的用户名或密码错误！！')
                    sys.exit(1)
            if user_login_flag:
                func(*args, **kwargs)

        return inner

    return login_decorator


@login('my_user.txt')
def test1():
    time.sleep(1)
    print('test1函数执行了')


if __name__ == '__main__':
    test1()
    time.sleep(1)
    test1()
    test1()
