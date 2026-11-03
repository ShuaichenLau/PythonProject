from langchain_core.tools import tool

from langchain_demo.my_llm import deepseek_llm


# 1 创建工具
@tool
def get_weather(local: str) -> str:
    "获取{local}天气信息"
    return f"{local}天气非常晴朗...."

# 2. 工具告诉大模型
model_with_tools = deepseek_llm.bind_tools([get_weather])
# 3.模型调用句返回工具结果
resp = model_with_tools.invoke("北京天气是什么?")


if resp.tool_calls:
    for tool_call in resp.tool_calls:
        print(tool_call)
        if tool_call['name'] == "get_weather":
            tool_result = get_weather.invoke(tool_call)
            print(tool_result)
            # class 'langchain_core.messages.tool.ToolMessage'>
            print(type(tool_result))


# 4.模型返回结构
# <class 'langchain_core.messages.ai.AIMessage'>
print(type(resp))
# tool_calls=[{'name': 'get_weather', 'args': {'local': '北京'},
print(resp)


