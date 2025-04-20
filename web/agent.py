"""Defines the main ADK agent for Brave Search."""

from google.adk.agents import Agent
from .search_tool import brave_search

# Note: Ensure GOOGLE_API_KEY is set in your environment or .env if needed
# for the chosen model, unless using Vertex AI authentication.
AGENT_MODEL = "gemini-2.5-flash-preview-04-17"

root_agent = Agent(
    name="search_agent",
    model=AGENT_MODEL,
    instruction=(
        "You are a helpful assistant. Your primary goal is to answer user "
        "questions accurately. When a question requires information beyond your "
        "internal knowledge or needs up-to-date details (like news, current "
        "events, specific technical details, or recent discoveries), you MUST "
        "use the 'brave_search' tool. Analyze the tool's response: if the "
        "status is 'error', inform the user politely about the search problem. "
        "If the status is 'success', synthesize the search results from the "
        "'results' list (title, url, description) into a coherent answer. "
        "Provide the answer based on the search results. Do not simply list the results."
    ),
    description=(
        "An assistant that uses the Brave Search API via the 'brave_search' "
        "tool to answer questions requiring web information."
    ),
    tools=[brave_search], # Register the custom tool function
)

print(f"Agent '{root_agent.name}' defined using model '{AGENT_MODEL}'.") 