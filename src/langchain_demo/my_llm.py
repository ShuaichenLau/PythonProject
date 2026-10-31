from langchain_deepseek import ChatDeepSeek

from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, ZHIPUAI_BASE_URL, ZHIPUAI_API_KEY

deepseek_llm = ChatDeepSeek(
    api_key=DEEPSEEK_API_KEY,
    api_base=DEEPSEEK_BASE_URL,
    # model="deepseek-chat",
    model="deepseek-flash",
)



zhipu_llm = ChatDeepSeek(
    api_key=ZHIPUAI_API_KEY,
    api_base=ZHIPUAI_BASE_URL,
    model="glm-5.3-flash",
)