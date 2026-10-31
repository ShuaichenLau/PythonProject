from typing import Iterator

from langchain_core.messages import AIMessageChunk

from my_llm import zhipu_llm, deepseek_llm

resp: Iterator[AIMessageChunk] = zhipu_llm.stream("请介绍一下你自己")
for chunk in resp:
    print(chunk.content, end="|", flush=True)

print('=====================================')

resp1: Iterator[AIMessageChunk] = deepseek_llm.stream("请介绍一下你自己")
for chunk in resp1:
    print(chunk.content, end="|", flush=True)

# print(zhipu_llm.stream("请介绍一下你自己"))
# print(deepseek_llm.stream("请介绍一下你自己"))
