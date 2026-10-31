from typing import Iterator

from langchain_core.runnables.utils import Output

from my_llm import zhipu_llm

#  1. 位置：config 是 batch() 的第二个位置参数，也可以省略 config= 直接写 zhipu_llm.batch([...], {"max_concurrency": 5})，但带上 config= 关键字更清晰、可读性更好。
#  2. 只影响 batch()/abatch() 这一批：这个并发限制是「本次批量调用」级别的，不会持久地改掉模型本身的设置。
#  3. 如果你的输入列表很大（比如上千条），max_concurrency=5 会让 LangChain 内部用线程池最多同时发起 5 个请求，避免把 API 的并发额度打满或触发限流。

resp1: Iterator[tuple[int, Output | Exception]] = zhipu_llm.batch_as_completed([
    "请介绍一下你自己",
    "北京天气怎样",
    "滦南天气怎样",
    "南京天气怎样",
    "介绍一下JAVA",
    "介绍一下Python",
],
    config={"max_concurrency": 5}
)

# for resp in resp1:
#     print(resp)

print('======================')
for resp in resp1:
    print(resp)
    # print(f'第{resp[0]}问题回答是{resp[1].content}')
    print(f"第 {resp[0]} 个问题回答完毕: {resp[1].content}")

# 限制最多同时进行5个并发调用 model.batch( large_list_of_inputs, config={ 'max_concurrency': 5 # 限制最大并发数为5 } )


# resp2:list[Output]=deepseek_llm.batch([
# "请介绍一下你自己",
# "北京天气怎样",
# ])
#
# for resp in resp2:
#     print(resp.content)
