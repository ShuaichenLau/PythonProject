import asyncio
import time
from functools import partial

# 协程
async def eat():
    for i in range(6):
        print('eat ')
        await asyncio.sleep(0)
    return 'eat done'

async def work():
    for i in range(6):
        print('work ')
        await asyncio.sleep(0)
    return 'work done'


# 定义一个回调函数
# 协程的异步任务完成之后 自动调用的函数
# coro
# current_time
def my_callback(coro,current_time):
    print(f'当前收到一个参数{current_time}')
    print(f'当前协程返回值{coro.result()},协程结束的时间{current_time}')

async def main():
    task1 = asyncio.create_task(eat())
    task2 = asyncio.create_task(work())

    task1.add_done_callback(partial(my_callback, current_time=time.time()))
    task2.add_done_callback(partial(my_callback, current_time=time.time()))
    # ✅ 必须 await 等待任务完成，回调才能正常执行
    await task1
    await task2


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())

    print(f'耗时{time.time()-start}')

