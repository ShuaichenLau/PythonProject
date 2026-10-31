import asyncio

from langchain.chat_models import init_chat_model

from env_utils import *

deepseek_llm = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
)

async def demo_async_invoke():
    print('=====演示一步ainvoke的异步')
    print('invoke程序开始')
    async_task =deepseek_llm.ainvoke('什么是大模型')

    for i in range(3):
        await asyncio.sleep(1)
        print(f'正在执行{i}任务')

    resp = await async_task
    print(f">>> 模型返回: {resp.content}")


async def demo_async_stream():
    print('=====演示一步stream的异步')
    print('stream程序开始')
    stream_resp =deepseek_llm.astream('什么是机器学习')

    for i in range(3):
        await asyncio.sleep(1)
        print(f'正在执行{i}任务')

    print(">>> 流式输出: ", end="", flush=True)
    async for chunk in stream_resp:
        if hasattr(chunk, 'content'):
            print(chunk.content,end="",flush=True)
    print('流式输出结束\n')

async def demo_async_batch():
    print('=====演示一步batch的异步')
    print('batch程序开始')
    questions = ['用一句话说明深度学习与传统机器学习的区别']

    batch_resp=deepseek_llm.abatch(questions)
    for i in range(3):
        await asyncio.sleep(1)
        print(f'正在执行{i}任务')
    respose = await batch_resp

    for resp in respose:
        print('流式输出{}'.format(resp.content))

async def main():
    await demo_async_invoke()
    await demo_async_stream()
    await demo_async_batch()

if __name__ == '__main__':
    asyncio.run(main())