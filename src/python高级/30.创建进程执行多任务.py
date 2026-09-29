import time
from multiprocessing import Process


def eat():
    for i in range(10):
        print(f'正在吃饭 == {i}')
        time.sleep(0.1)


def work():
    for i in range(10):
        print(f'正在工作 == {i}')
        time.sleep(0.1)


if __name__ == '__main__':
    # 创建一个紫禁城 每个任务由独立的紫禁城来完成
    p1 = Process(target=eat,name='进程1')
    p2 = Process(target=work,name='进程2')
    p1.start()
    p2.start()



