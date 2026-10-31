from langchain_core.runnables.utils import Output

from my_llm import zhipu_llm, deepseek_llm

resp1:list[Output]=zhipu_llm.batch([
"请介绍一下你自己",
"北京天气怎样",
])

for resp in resp1:
    print(resp.content)


print('=====================================')

resp2:list[Output]=deepseek_llm.batch([
"请介绍一下你自己",
"北京天气怎样",
])

for resp in resp2:
    print(resp.content)