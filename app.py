import streamlit as st
import asyncio
from test import agent, Deps, ModelRequest, ModelResponse, UserPromptPart, TextPart, messages

# Set up the Streamlit app
st.title("Basic Chatbot")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to display chat messages
def display_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Function to handle user input and get bot response
async def get_bot_response(user_input: str):
    try:
        # Run the agent to get the bot's response
        response = await agent.run(user_prompt=user_input, message_history=messages, deps=Deps)
        return response.data
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Display existing messages
display_messages()

# Get user input
user_input = st.chat_input("You: ")

if user_input:
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Get bot response
    bot_response = asyncio.run(get_bot_response(user_input))

    # Add bot response to session state
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # Display bot response
    with st.chat_message("assistant"):
        st.write(bot_response)

    # Update message history (if needed)
    messages.append(ModelRequest(parts=[UserPromptPart(content=user_input)]))
    messages.append(ModelResponse(parts=[TextPart(content=bot_response)]))