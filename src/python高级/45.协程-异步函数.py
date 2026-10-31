import asyncio
import time


# 协程
async def eat():
    for i in range(6):
        print('eat ')
        await asyncio.sleep(0.3)


async def work():
    for i in range(6):
        print('work ')
        await asyncio.sleep(0.3)


# 其他协程的入口
async def main():
    task1 = asyncio.create_task(eat())
    task2 = asyncio.create_task(work())
    await  task1
    await  task2

    # await  eat()
    # await  work()

# 更简单的写法
    await asyncio.gather(eat(), work())


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f'耗时{time.time()-start}')

