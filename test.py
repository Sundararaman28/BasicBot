import os
from typing import List, Any
import asyncio
from dataclasses import dataclass
from random import randint

from pydantic_ai import Agent
from pydantic_ai.messages import ModelMessage, ModelResponse, ModelRequest, UserPromptPart, TextPart
from pydantic_ai.models.groq import GroqModel, GroqModelSettings, GroqModelName
from pydantic_ai.providers.groq import GroqProvider
from tavily import AsyncTavilyClient

from dotenv import load_dotenv

load_dotenv()

model_name : GroqModelName = "llama-3.3-70b-versatile"

model = GroqModel(
    model_name = model_name,
    provider= GroqProvider(api_key=os.getenv("GROQ_API_KEY"))
)

settings = GroqModelSettings(temperature=0.5)

with open("prompt.txt", "r") as file:
    prompt = file.read()

@dataclass
class Deps:
    tavily_client: AsyncTavilyClient = AsyncTavilyClient(api_key=str(os.getenv("TAVILY_API_KEY")))

agent = Agent(
    model = model,
    system_prompt=str(prompt),
    deps_type=Deps,
    retries=2,
    model_settings=settings
)

messages : List[ModelMessage] = []

async def main():
    while True:
        user_input = input("You: ")
        messages.append(ModelRequest(parts=[UserPromptPart(content=user_input)]))
        response = await agent.run(user_prompt=user_input, message_history=messages, deps=Deps)
        messages.append(ModelResponse(parts=[TextPart(content=response.data)]))
        print("Bot:",response.data)
        
        if user_input == "exit":
            break
