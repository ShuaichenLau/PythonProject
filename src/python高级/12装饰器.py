import time


def login(func):
    print('装饰器开始执行=======')

    def inner():
        print('检查是否登录了,如果没有,则登录')
        time.sleep(2)
        print('登录成功')
        time.sleep(2)
        func()
    return inner

@login
def comment():
    print('发布评论====')


# comment = login(comment)
comment()

