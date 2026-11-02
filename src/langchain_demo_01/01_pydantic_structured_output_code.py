from pydantic import BaseModel, Field

from langchain_demo.my_llm import deepseek_llm


class Actor(BaseModel):
    name: str = Field(description="演员姓名")
    role: str = Field(description="演员在电影中的角色")

class Moive(BaseModel):
    title: str = Field(description="电影标题")
    year: int = Field(description="电影上映年份")
    director: str = Field(description="电影导演")
    rating: float = Field(description="电影评分")
    cast: list[Actor] = Field(description="电影演员列表")

# model_with_Structured_output=deepseek_llm.with_structured_output(Moive)
model_with_Structured_output=deepseek_llm.with_structured_output(Moive,include_raw=True)

resp=model_with_Structured_output.invoke("介绍一下温子仁电影《潜伏5：红门》")
print(type(resp))

print(resp)