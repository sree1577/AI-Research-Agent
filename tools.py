from datetime import datetime

from langchain_community.tools import (
    WikipediaQueryRun,
    DuckDuckGoSearchRun
)
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool

# DuckDuckGo Search

search_tool = DuckDuckGoSearchRun()


# Wikipedia

api_wrapper = WikipediaAPIWrapper(
    top_k_results=2,
    doc_content_chars_max=2000
)

wiki_tool = WikipediaQueryRun(
    api_wrapper=api_wrapper
)

# Save to TXT
@tool
def save_to_txt(
    data: str,
    filename: str = "research_output.txt"
) -> str:
    """
    Save research output to a text file.
    """

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    formatted_text = (
        "--- Research Output ---\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n\n"
    )

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data saved to {filename} at {timestamp}"