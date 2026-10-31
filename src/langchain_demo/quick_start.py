# ```
#    langchain==1.2.0
#    langgraph==1.0.10
#    langgraph-prebuilt==1.0.8
#  ```

import sys

from langchain.agents import create_agent

from my_llm import deepseek_llm

# Windows 控制台默认编码为 GBK，遇到 emoji/特殊符号会报 UnicodeEncodeError
sys.stdout.reconfigure(encoding="utf-8")

def get_weather(city: str) -> str:
    """查询指定城市的实时天气情况"""
    return f"{city} 天气万里无云!"

agent=create_agent(model=deepseek_llm,
             tools=[get_weather],
             system_prompt="你是一个可以查询天气的助手")


resp=agent.invoke({"messages":[{"role":"user","content":"查询北京未来三天的天气"}]})
# print(str(resp).encode('gbk', 'ignore').decode('gbk'))
print(resp)
