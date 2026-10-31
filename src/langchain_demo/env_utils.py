import os

from dotenv import load_dotenv

load_dotenv(override=True)
DEEPSEEK_API_KEY=os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL=os.getenv("DEEPSEEK_BASE_URL")


ZHIPUAI_API_KEY=os.getenv("ZHIPUAI_API_KEY")
ZHIPUAI_BASE_URL=os.getenv("ZHIPUAI_BASE_URL")
