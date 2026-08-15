from dotenv import load_dotenv
import os

from pydantic import BaseModel, Field
from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent

from tools import (
    search_tool,
    wiki_tool,
    save_to_txt
)
# LOAD ENVIRONMENT VARIABLES
load_dotenv()
# STRUCTURED RESPONSE
class ResearchResponse(BaseModel):

    topic: str = Field(
        description="The topic that was researched"
    )

    summary: str = Field(
        description="A clear summary of the research"
    )

    source: list[str] = Field(
        description="Sources used during the research"
    )

    tools_used: list[str] = Field(
        description="Tools used during the research"
    )


# LLM
llm = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    temperature=0.7
)


# TOOLS
tools = [
    search_tool,
    wiki_tool,
    save_to_txt
]

# CREATE AGENT
agent = create_agent(
    model=llm,
    tools=tools,
    response_format=ResearchResponse,
    system_prompt="""
You are an intelligent research assistant.

Your job is to research the user's question.

Rules:

1. Use DuckDuckGo Search when internet or
   current information is required.

2. Use Wikipedia when general background
   information is useful.

3. Do not invent sources.

4. Clearly summarize the information.

5. Include the sources that were actually used.

6. Include the tools that were actually used.

7. Use the save_to_txt tool only when the
   user asks to save the research.

8. Always return the final answer using
   the ResearchResponse structure.
"""
)

# USER INPUT
query = input(
    "\nWhat can I help you research? "
)

# RUN AGENT

try:

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
    )


    # STRUCTURED RESPONSE
    structured_response = result.get(
        "structured_response"
    )



    # DISPLAY
    print("\n")
    print("=" * 60)
    print("RESEARCH RESULT")
    print("=" * 60)

    if structured_response:

        print("\nTOPIC:")
        print(structured_response.topic)

        print("\nSUMMARY:")
        print(structured_response.summary)

        print("\nSOURCES:")

        for source in structured_response.source:
            print(f"- {source}")

        print("\nTOOLS USED:")

        for tool_name in structured_response.tools_used:
            print(f"- {tool_name}")

    else:

        print("\nNo structured response returned.")

        print("\nRaw result:")
        print(result)


except Exception as e:

    print("\nERROR")
    print("=" * 60)
    print(e)