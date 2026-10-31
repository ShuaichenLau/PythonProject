import time
from multiprocessing import Process
from multiprocessing import Process, Pool

def eat():
    for i in range(10):
        print(f'正在吃饭 == {i}')
        time.sleep(0.1)


def work():
    for i in range(10):
        print(f'正在工作 == {i}')
        time.sleep(0.1)

if __name__ == '__main__':
    process_pool=Pool(3)
    process_pool.apply_async(eat)
    process_pool.apply_async(work)
    # 进程池关闭 进程池不再接受新的请求任务
    process_pool.close()
    # 采用进程池的异步调用, 需要手动调用join函数阻塞主进程
    process_pool.join()
