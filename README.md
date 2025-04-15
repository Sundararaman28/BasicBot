# Basic Chatbot Project

This project is a basic chatbot built using `pydantic-ai` and `groq`. The chatbot includes session-based memory and a system prompt. It also has two tools, websearch and rolldie.

## Project Structure

- `.env`: Environment variables file.
- `.gitignore`: Git ignore file.
- `.python-version`: Python version file.
- `pyproject.toml`: Project configuration file.
- `README.md`: Project documentation file.
- `test.py`: Main script for the chatbot.
- `search.py`: A script to test tavily.
- `app.py`: Streamlit frontend for the chatbot.

## Requirements

- Python 3.13 or higher
- `pydantic-ai` version 0.0.24 or higher
- `python-dotenv` version 1.0.1 or higher
- `streamlit` version 1.0.0 or higher

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Rikhil-Nell/BasicBot.git
    cd BasicBot
    ```

2. Create a virtual environment:

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

    OR

    ```sh
    uv sync
    ```

4. Set up the environment variables in the `.env` file:

    ```env
    GROQ_API_KEY=<your-groq-api-key>
    TAVILY_API_KEY=<your-tavily-api-key>
    ```

## Usage

Run the chatbot:

```sh
python test.py
```

Run the Streamlit app:

```sh
streamlit run app.py
```
