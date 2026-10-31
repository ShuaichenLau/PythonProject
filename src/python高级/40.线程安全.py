import threading

# 采用两个线程累加g_num

g_num = 0

lo = threading.Lock()

def sum_num1():
    for i in range(1000000):
        lo.acquire()
        global g_num
        g_num += 1
        lo.release()
    print(f'线程A  {g_num}')


def sum_num2():
    for i in range(1000000):
        lo.acquire()
        global g_num
        g_num += 1
        lo.release()
    print(f'线程B  {g_num}')


def sum_num3():
    for i in range(1000000):
        lo.acquire()
        global g_num
        g_num += 1
        lo.release()
    print(f'线程C  {g_num}')

if __name__ == '__main__':
    threading.Thread(target=sum_num1).start()
    threading.Thread(target=sum_num2).start()
    threading.Thread(target=sum_num3).start()

