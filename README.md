# Basic Chatbot Project

This project is a basic chatbot built using `pydantic-ai` and `groq`. The chatbot includes session-based memory and a system prompt.

## Project Structure

- `.env`: Environment variables file.
- `.gitignore`: Git ignore file.
- `.python-version`: Python version file.
- `pyproject.toml`: Project configuration file.
- `README.md`: Project documentation file.
- `test.py`: Main script for the chatbot.

## Requirements

- Python 3.13 or higher
- `pydantic-ai` version 0.0.24 or higher
- `python-dotenv` version 1.0.1 or higher

## Installation

1. Clone the repository:

    ```sh
    git clone <repository-url>
    cd <repository-directory>
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

4. Set up the environment variables in the [.env](http://_vscodecontentref_/0) file:

    ```env
    GROQ_API_KEY=<your-groq-api-key>
    ```

## Usage

Run the  scriptchatbot:

```sh
python test.py
