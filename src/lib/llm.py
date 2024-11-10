from dotenv import load_dotenv

load_dotenv()
from langchain_openai import AzureChatOpenAI

azure_llm = AzureChatOpenAI(
    api_version="2024-10-01-preview",
    azure_deployment="gpt-4o",
    max_retries=2,
)
