# Google ADK Brave Search Agent Sample

This project demonstrates a simple agent built using the Google Agent Development Kit (ADK) for Python. The agent uses the Brave Search API as a custom tool to answer user queries that require web search.

## Features

*   Google ADK agent setup.
*   Custom tool integration (`brave_search`).
*   Configuration via environment variables (`.env`).
*   Basic project structure (`web`, `tests`).
*   Dependency management with `uv`.

## Setup

1.  **Clone the repository (or ensure you have the files).**

2.  **Install `uv`:**
    ```bash
    pip install uv
    ```

3.  **Create a virtual environment and install dependencies:**
    ```bash
    uv venv
    uv pip install -e .[dev]
    ```
    *   This installs the project in editable mode (`-e .`) along with development dependencies (`[dev]`).

4.  **Set up Environment Variables:**
    *   Copy `.env.example` to `.env`:
        ```bash
        cp .env.example .env
        ```
    *   Edit the `.env` file and add your Brave Search API key:
        ```
        BRAVE_API_KEY="YOUR_ACTUAL_BRAVE_API_KEY"
        ```
    *   You can obtain a key from [Brave Search API](https://brave.com/search/api/).
    *   Optionally, set your Google API key if needed for the specific Gemini model (ensure it's set in your environment or `.env`):
        ```
        GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
        ```

5.  **Activate the virtual environment:**
    *   macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```
    *   Windows:
        ```bash
        .venv\Scripts\activate
        ```

## Running the Agent

Use the ADK CLI to interact with the agent:

```bash
adk run web
```

This command tells the ADK to look for an agent definition within the `web` directory (it will find `web.agent.root_agent`).

You can then type queries like:

*   "What is the latest news about Google ADK?"
*   "Search the web for python asynchronous programming tutorials."
*   "Who won the last Formula 1 race?"

The agent will use the `brave_search` tool for these queries.

## Running Tests

To run the tests (requires dev dependencies):

```bash
pytest
```

## Project Structure

```
.
├── .env              # Local environment variables (ignored by git)
├── .env.example      # Example environment variables
├── .gitignore        # Files ignored by git
├── pyproject.toml    # Project metadata and dependencies (for uv/pip)
├── README.md         # This file
├── web/
│   ├── __init__.py   # Makes 'web' a Python package
│   ├── agent.py      # Defines the ADK agent
│   └── search_tool.py # Defines the custom Brave Search tool
└── tests/
    ├── __init__.py   # Makes 'tests' a Python package
    └── test_search_tool.py # Tests for the search tool (optional)
``` 