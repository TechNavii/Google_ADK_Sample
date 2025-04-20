"""Defines the custom Brave Search tool for the ADK agent."""

import os
import requests
import logging
from typing import Dict, Any, Optional
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

BRAVE_API_ENDPOINT = "https://api.search.brave.com/res/v1/web/search"

def brave_search(query: str, num_results: int = 5) -> Dict[str, Any]:
    """Performs a web search using the Brave Search API.

    Use this tool when the user asks a question that requires searching
    the internet for up-to-date information or general knowledge.
    For example: 'Search the web for recent AI advancements',
    'What is the capital of France?', 'Find news about the stock market'.

    Args:
        query (str): The search query.
        num_results (int): The desired number of search results (default: 5).

    Returns:
        Dict[str, Any]: A dictionary containing the search results or an error.
            On success: {'status': 'success', 'results': [{'title': str, 'url': str, 'description': str}]}]
            On failure: {'status': 'error', 'message': str}
    """
    api_key: Optional[str] = os.getenv("BRAVE_API_KEY")

    if not api_key:
        logger.error("Brave API key not found in environment variables.")
        return {
            "status": "error",
            "message": "Brave API key is missing. Cannot perform search."
        }

    headers: Dict[str, str] = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": api_key,
    }
    params: Dict[str, Any] = {
        "q": query,
        "count": num_results,
        "text_decorations": False, # Keep results clean
    }

    try:
        logger.info(f"Performing Brave search for query: '{query}'")
        response = requests.get(
            BRAVE_API_ENDPOINT, headers=headers, params=params, timeout=10
        )
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)

        data = response.json()
        web_results = data.get("web", {}).get("results", [])

        if not web_results:
            logger.warning(f"No web results found for query: '{query}'")
            return {"status": "success", "results": [], "message": "No results found."}

        # Extract relevant information
        formatted_results = [
            {
                "title": result.get("title", "No Title"),
                "url": result.get("url", "No URL"),
                "description": result.get("description", "No Description"),
            }
            for result in web_results
        ]

        logger.info(f"Found {len(formatted_results)} results for query: '{query}'")
        return {"status": "success", "results": formatted_results}

    except requests.exceptions.RequestException as e:
        logger.error(f"Error calling Brave Search API: {e}")
        return {"status": "error", "message": f"Error during web search: {e}"}
    except Exception as e:
        logger.error(f"An unexpected error occurred during Brave search: {e}")
        return {"status": "error", "message": f"An unexpected error occurred: {e}"}

# Example usage (for testing the function directly)
if __name__ == "__main__":
    test_query = "Google Agent Development Kit"
    search_result = brave_search(test_query)
    print(f"\nSearch results for '{test_query}':")
    import json
    print(json.dumps(search_result, indent=2))

    test_query_no_key = "Test query without key"
    os.environ.pop("BRAVE_API_KEY", None) # Temporarily remove key for testing
    search_result_no_key = brave_search(test_query_no_key)
    print(f"\nSearch results for '{test_query_no_key}' (no API key):")
    print(json.dumps(search_result_no_key, indent=2)) 