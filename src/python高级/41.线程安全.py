import threading

# 采用两个线程累加g_num

g_num = 0

# 创建互斥锁
lock = threading.Lock()

def sum_num1():
    with lock:
        for i in range(1000000):
            global g_num
            g_num += 1
    print(f'线程A  {g_num}')


def sum_num2():
    with lock:
        for i in range(1000000):
            global g_num
            g_num += 1
    print(f'线程B  {g_num}')


def sum_num3():
    with lock:
        for i in range(1000000):
            global g_num
            g_num += 1
    print(f'线程C  {g_num}')

if __name__ == '__main__':
    threading.Thread(target=sum_num1).start()
    threading.Thread(target=sum_num2).start()
    threading.Thread(target=sum_num3).start()

