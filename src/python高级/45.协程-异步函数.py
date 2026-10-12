import asyncio


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
    task1=asyncio.create_task(eat())
    task2=asyncio.create_task(work())
    await  task1
    await  task2

    # await  eat()
    # await  work()


if __name__ == '__main__':
    asyncio.run(main())
