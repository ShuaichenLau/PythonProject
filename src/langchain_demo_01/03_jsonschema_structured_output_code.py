from langchain_demo.my_llm import deepseek_llm

json_schema = {
    "title": "MovieInfo",
    "description": "电影信息",
    "type": "object",
    "properties": {
        "title": {"type": "string", "description": "电影标题"},
        "year": {"type": "integer", "description": "电影上映年份"},
        "director": {"type": "string", "description": "电影导演"},
        "rating": {"type": "number", "description": "电影评分"},
        "cast": {"type": "string", "description": "电影演员列表"},
    },
    "required": ["title", "year", "director", "rating", "cast"],
}

# 绑定结构化输出json_schema
model_with_Structured_output = deepseek_llm.with_structured_output(json_schema)
# 调用大模型
resp = model_with_Structured_output.invoke("介绍一下温子仁电影《潜伏5：红门》")
print(type(resp))

print(resp)
