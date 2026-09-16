'''
九九乘法表
'''

pwd = '123456'

def checkPass():
    '''密码正确 登录成功'''
    retry = 1
    while True:
        retry += 1
        passwd = input('请输入您的密码')
        if passwd != '' and passwd == pwd:
            print('登录成功')
            break
        else:
            if retry <= 3:
                print('密码错误,请重新输入 \t')
            else:
                print('密码错误次数超过3次,程序结束')

def checkPass1():
    retryCount = 1
    while retryCount <= 3:
        passwd = input('请输入您的密码')
        retryCount += 1
        if passwd != '' and passwd == pwd:
            print('密码正确,登录成功')
            break
    else:
        print('密码错误次数超过3次,程序结束')


def function():
    for x in range(1, 10):
        str = ""
        for y in range(1, (x + 1)):
            str += (f"{y}*{x}={x * y} \t")
        print(str)


if __name__ == '__main__':
    checkPass1()


print('==============================================')


