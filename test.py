import os
from typing import List, Any
import asyncio
from dataclasses import dataclass
from random import randint

from pydantic_ai import Agent, RunContext
from pydantic_ai.messages import ModelMessage, ModelResponse, ModelRequest, UserPromptPart, TextPart
from pydantic_ai.models.groq import GroqModel

from tavily import AsyncTavilyClient

from dotenv import load_dotenv

load_dotenv()

llm = "llama-3.3-70b-versatile"

model = GroqModel(
    model_name = llm,
    api_key = os.getenv("GROQ_API_KEY"),
)

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
)

messages : List[ModelMessage] = []

@agent.tool
async def websearch(ctx: RunContext[Deps], query: str) -> str:
    """Search the web for the user's query
    Args:
        ctx: The context.
        query: The user's query.
    
    Returns:
        str: The response from the web search
    """
    print("Searching the web for:", query)
    response = await ctx.deps.tavily_client.get_search_context(query, max_results=2) 
    return response


ROLLS : int = 1

@agent.tool_plain(retries=ROLLS)
async def rolldie() -> int:
    """Roll a die
    Returns:
        int: The result of the die roll
    """
    print("Rolling a die")
    roll = randint(1, 6)
    return roll

async def main():
    while True:
        user_input = input("You: ")
        messages.append(ModelRequest(parts=[UserPromptPart(content=user_input)]))
        response = await agent.run(user_prompt=user_input, message_history=messages, deps=Deps)
        messages.append(ModelResponse(parts=[TextPart(content=response.data)]))
        print("Bot:",response.data)
        
        if user_input == "exit":
            break

asyncio.run(main())