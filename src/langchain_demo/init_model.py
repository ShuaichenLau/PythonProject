

from my_llm import zhipu_llm,deepseek_llm

print(zhipu_llm.invoke("请介绍一下你自己"))
print(type(zhipu_llm.invoke("请介绍一下你自己")))
print(deepseek_llm.invoke("请介绍一下你自己"))

