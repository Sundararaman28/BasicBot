import os
from typing import List
import asyncio

from pydantic_ai import Agent
from pydantic_ai.messages import ModelMessage, ModelResponse, ModelRequest, UserPromptPart, TextPart
from pydantic_ai.models.groq import GroqModel
from dotenv import load_dotenv

load_dotenv()

llm = "llama-3.3-70b-versatile"

model = GroqModel(
    model_name = llm,
    api_key = os.getenv("GROQ_API_KEY"),
)

with open("prompt.txt", "r") as file:
    prompt = file.read()

agent = Agent(
    model = model,
    system_prompt=prompt
)

messages : List[ModelMessage] = []

while True:
    user_input = input("You:")
    print("\n")
    messages.append(ModelRequest(parts=[UserPromptPart(content=user_input)]))
    response = asyncio.run(agent.run(user_prompt=user_input, message_history=messages))
    messages.append(ModelResponse(parts=[TextPart(content=response.data)]))
    print("Bot:",response.data)
    print("\n")
    
    if user_input == "exit":
        break