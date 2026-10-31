import asyncio

# 协程
async def test1():
    print('test1')

    await asyncio.sleep(1)
    print('test2')


if __name__ == '__main__':
    asyncio.run(test1())