from langchain_deepseek import ChatDeepSeek

try:
    # 当以包方式导入时（from langchain_demo.my_llm import ...），用相对导入
    from .env_utils import (
        DEEPSEEK_API_KEY,
        DEEPSEEK_BASE_URL,
        ZHIPUAI_BASE_URL,
        ZHIPUAI_API_KEY,
        ZENMUX_API_KEY,
        ZENMUX_BASE_URL,
    )
except ImportError:
    # 当 my_llm.py 作为顶层模块运行时（脚本在 langchain_demo 目录内），用裸导入
    from env_utils import (
        DEEPSEEK_API_KEY,
        DEEPSEEK_BASE_URL,
        ZHIPUAI_BASE_URL,
        ZHIPUAI_API_KEY,
        ZENMUX_API_KEY,
        ZENMUX_BASE_URL,
    )

deepseek_llm = ChatDeepSeek(
    api_key=DEEPSEEK_API_KEY,
    api_base=DEEPSEEK_BASE_URL,
    # model="deepseek-chat",
    model="deepseek-flash",
    # model="deepseek-v4-pro",
    temperature=0.7,
    # rate_limiter=5
    # model="deepseek-flash",
    # model_kwargs={"thinking": {"type": "disabled"}},  # 关闭思维链模式
)

zhipu_llm = ChatDeepSeek(
    api_key=ZHIPUAI_API_KEY,
    api_base=ZHIPUAI_BASE_URL,
    model="glm-5.3-flash",
)


zenmux_gemini_llm = ChatDeepSeek(
    api_key=ZENMUX_API_KEY,
    api_base=ZENMUX_BASE_URL,
    model="google/gemini-3.8-flash",
)
