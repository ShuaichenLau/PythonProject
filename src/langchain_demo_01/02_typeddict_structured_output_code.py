from typing import TypedDict, Annotated

from langchain_demo.my_llm import deepseek_llm


class Actor(TypedDict):
    name: str = Annotated[str,"演员姓名"]
    role: str = Annotated[str,"演员在电影中的角色"]

class Moive(TypedDict):
    title: str = Annotated[str,"电影标题"]
    year: int = Annotated[int,"电影上映年份"]
    director: str = Annotated[str,"电影导演"]
    rating: float = Annotated[float,"电影评分"]
    cast: list[Actor] = Annotated[list[Actor],"电影演员列表"]

# 绑定结构化输出模型
model_with_Structured_output=deepseek_llm.with_structured_output(Moive)
# 调用大模型
resp=model_with_Structured_output.invoke("介绍一下温子仁电影《潜伏5：红门》")
print(type(resp))

print(resp)