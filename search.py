from tavily import AsyncTavilyClient
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

tavily_client = AsyncTavilyClient(api_key=str(os.getenv("TAVILY_API_KEY")))
response = asyncio.run(tavily_client.get_search_context("What is the capital of France?"))

content = response["results"][0]["content"]

print(content)