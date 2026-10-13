import asyncio
import time


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


# 其他协程的入口
async def main():
    # 多任务异步
    task1 = asyncio.create_task(eat())
    task2 = asyncio.create_task(work())

    await task1
    await task2
    result = await asyncio.gather(task1, task2)
    print(result)

    # 显示更详细的结果
    result = await asyncio.wait([task1,task2])
    print(result)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f'耗时{time.time()-start}')

