import streamlit as st
import asyncio
from test import agent, Deps, ModelRequest, ModelResponse, UserPromptPart, TextPart, messages
from pydantic_ai import BinaryContent
from pathlib import Path
import os
from datetime import datetime

# Set up the Streamlit app
st.title("E-waste Chatbot")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to display chat messages
def display_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Function to handle user input and get bot response
async def get_bot_response(user_input: str, bin_con : BinaryContent|str):
    try:
        # Run the agent to get the bot's response
        input = [user_input,bin_con]
        response = await agent.run(user_prompt=input, message_history=messages, deps=Deps)
        return response.output
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Ensure the images folder exists
os.makedirs("images", exist_ok=True)

# Image upload section
uploaded_file = st.file_uploader("Upload an image (e-waste related)", type=["png", "jpg", "jpeg"])

# Initialize BinaryContent variable
bin_con = ""

if uploaded_file is not None:
    # Create a unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_extension = uploaded_file.name.split('.')[-1].lower()
    filename = f"image_{timestamp}.{file_extension}"
    filepath = os.path.join("images", filename)

    # Save the uploaded image to the images folder
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Image uploaded and saved as `{filename}`!")
    st.image(filepath, caption="Uploaded Image", use_column_width=True)

    # Set correct media type
    media_type = f"image/{file_extension if file_extension != 'jpg' else 'jpeg'}"

    # Read binary and initialize BinaryContent
    bin_con = BinaryContent(
        data=Path(filepath).read_bytes(),
        media_type=media_type
    )

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
    bot_response = asyncio.run(get_bot_response(user_input, bin_con))

    # Add bot response to session state
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # Display bot response
    with st.chat_message("assistant"):
        st.write(bot_response)

    # Update message history
    messages.append(ModelRequest(parts=[UserPromptPart(content=user_input)]))
    messages.append(ModelResponse(parts=[TextPart(content=bot_response)]))
