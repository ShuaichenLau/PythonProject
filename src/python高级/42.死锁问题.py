import time
from threading import Thread, Lock,current_thread

lock = Lock()
my_list = [1, 2, 6, 8, 19]


def get_value(index):
    lock.acquire()
    print(f'当前线程是{current_thread()}')

    # 判断下标是否越界
    if index >= len(my_list):
        print(f'下标越界了, 你传入下标是:{index}')
        lock.release()
        return
    v = my_list[index]
    print(f'当前线程取到的值:{index}')
    time.sleep(0.5)
    lock.release()


if __name__ == '__main__':
    # 创建20个线程模拟多线程分别从列表取值操作
    for i in range(20):
        t = Thread(target=get_value, args=(i,))
        t.start()
