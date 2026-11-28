# 这种方法更传统，依赖于在提示词中明确指示模型输出特定格式的文本，然后使用解析器进行转换。其流程是：提示词指导 (引导生成指定类型）→ 模型生成文本 → 解析器转换。

from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from langchain_demo.env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL

# 初始化模型
deepseek_reasoner_llm = init_chat_model(
    # model="deepseek-reasoner",
    model="deepseek-v4-pro",
    model_provider="deepseek",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
)


# 定义结构
class Movie(BaseModel):
    title: str = Field(description="电影标题")
    year: int = Field(description="电影年份")

#创建解析器和提示模板
parser=JsonOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_template(" 回答用户问题。 问题：{question} 你必须始终输出一个包含title(电影标题)和year(上映年份)的 JSON 对象。 ")

chain=prompt | deepseek_reasoner_llm | parser

# 调用(返回字典)
response = chain.invoke({"question": "《肖申克的救赎》是哪一年上映的？"})
print(response)

print(type(response))


