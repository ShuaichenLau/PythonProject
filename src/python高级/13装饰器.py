import time

def timer(func):
    print(f'{func.__name__}时间装饰器开始执行=======')

    def inner():
        start = time.time()
        result = func()
        end = time.time()
        print(f'函数{func.__name__}执行的时间:{end-start}')
        return result
    return inner

@timer
def test1():
    print('test1')
    time.sleep(2)

@timer
def test2():
    print('test2')
    time.sleep(1)

if __name__ == '__main__':
    test1()
    test2()

