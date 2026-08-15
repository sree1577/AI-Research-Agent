# AI Research Agent

An AI-powered research assistant built with **Python and LangChain** that can autonomously decide when to use external tools to research a user's question and return the findings in a structured format.

The project demonstrates the core architecture of an **LLM-powered tool-calling agent**, including web search, Wikipedia retrieval, structured Pydantic responses, and file-based research storage.

---

## Overview

The AI Research Agent accepts a natural-language research question and uses an LLM to determine how to answer it.

Depending on the query, the agent can use:

* **DuckDuckGo Search** — for web-based and current information
* **Wikipedia** — for general background information
* **Text File Storage** — to save research results when requested
* **Pydantic** — to enforce a structured research response

### Example

```text
User:
"What is Retrieval Augmented Generation?"

                ↓

        LangChain Agent

                ↓

       ┌────────┴────────┐
       ↓                 ↓
DuckDuckGo           Wikipedia
   Search

       └────────┬────────┘
                ↓

             LLM

                ↓

      Structured Response

       ┌────────┼─────────┐
       ↓        ↓         ↓
     Topic   Summary   Sources
```

---

## Key Features

### 1. Autonomous Tool Selection

The agent decides which available tools are useful for answering the user's question rather than requiring the user to manually select a tool.

### 2. Web Search

The agent can use DuckDuckGo to retrieve information from the web.

### 3. Wikipedia Research

Wikipedia can be used for general background and conceptual information.

### 4. Structured Output

Research results are validated using a Pydantic model:

```python
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    source: list[str]
    tools_used: list[str]
```

This makes the agent's output predictable and easier to consume programmatically.

### 5. Research Storage

The project includes a tool for saving research results to a text file with a timestamp.

### 6. LLM Flexibility

The agent architecture can be connected to different LLM providers, including Anthropic Claude and OpenAI models.

---

## Architecture

```text
                         ┌──────────────┐
                         │     User     │
                         └───────┬──────┘
                                 │
                                 ▼
                      ┌────────────────────┐
                      │   LangChain Agent  │
                      └─────────┬──────────┘
                                │
                       Tool Selection
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
       ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
       │ DuckDuckGo  │   │  Wikipedia  │   │ Save to TXT │
       │   Search    │   │    Tool     │   │    Tool     │
       └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
              │                 │                 │
              └─────────────────┼─────────────────┘
                                ▼
                         ┌──────────────┐
                         │     LLM      │
                         │ Claude/OpenAI│
                         └──────┬───────┘
                                │
                                ▼
                    ┌──────────────────────┐
                    │ ResearchResponse     │
                    │      Pydantic        │
                    └──────────┬───────────┘
                               │
                               ▼
                         Final Result
```

---

## Tech Stack

| Technology          | Purpose                           |
| ------------------- | --------------------------------- |
| Python              | Core programming language         |
| LangChain           | Agent and tool orchestration      |
| LangChain Community | Search and Wikipedia integrations |
| Anthropic Claude    | LLM provider                      |
| OpenAI              | Alternative LLM provider          |
| DuckDuckGo          | Web search                        |
| Wikipedia           | Knowledge retrieval               |
| Pydantic            | Structured output validation      |
| python-dotenv       | Environment variable management   |
| Git                 | Version control                   |
| GitHub              | Source code hosting               |

---

## Project Structure

```text
AI_AGENT/
│
├── main.py                 # Agent configuration and execution
├── tools.py                # Search, Wikipedia and file tools
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignored files
├── README.md               # Project documentation
│
├── .env                    # API keys - NOT committed
└── venv/                   # Virtual environment - NOT committed
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd AI_AGENT
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If DuckDuckGo dependencies are missing:

```bash
pip install -U ddgs
```

---

## Environment Variables

Create a `.env` file in the project root.

For Anthropic:

```env
ANTHROPIC_API_KEY=your_anthropic_api_key
```

Or for OpenAI:

```env
OPENAI_API_KEY=your_openai_api_key
```

### Security

**Never commit `.env` to GitHub.**

The project uses environment variables so API credentials remain outside the source code.

The `.gitignore` should contain:

```text
.env
venv/
__pycache__/
*.pyc
.vscode/
research_output.txt
```

---

## Running the Agent

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Run:

```powershell
python main.py
```

You will be prompted:

```text
What can I help you research?
```

Enter a research question such as:

```text
What is Retrieval Augmented Generation?
```

The agent will process the question and return a structured research response.

---

## Example Output

```text
============================================================
RESEARCH RESULT
============================================================

TOPIC:
Retrieval Augmented Generation

SUMMARY:
Retrieval Augmented Generation, or RAG, is an AI architecture
that combines information retrieval with generative language
models. Instead of relying entirely on the model's internal
knowledge, relevant documents are retrieved and provided to
the model as additional context.

SOURCES:
- Wikipedia
- DuckDuckGo Search

TOOLS USED:
- Wikipedia
- DuckDuckGo Search

============================================================
```

---

## How the Agent Works

### Step 1 — User Query

The user enters a natural-language research question.

```text
"What is RAG?"
```

### Step 2 — Agent Reasoning

The LangChain agent receives the question and determines whether external tools are useful.

### Step 3 — Tool Execution

The agent can call:

```text
DuckDuckGo Search
```

or:

```text
Wikipedia
```

depending on the task.

### Step 4 — Information Processing

The retrieved information is provided to the LLM as context.

### Step 5 — Structured Response

The final response is validated against the `ResearchResponse` Pydantic schema.

### Step 6 — Optional Storage

If requested, the research can be saved to a timestamped text file.

---

## Learning Objectives

This project demonstrates practical concepts used in modern AI engineering:

* Large Language Models
* AI Agents
* Tool Calling
* Agentic Workflows
* Prompt Engineering
* External Information Retrieval
* Structured LLM Output
* Pydantic Models
* Environment Variables
* API Integration
* LangChain
* Python Project Structure

---

## License

This project is intended for educational and portfolio purposes.

---

## Author
**Sri Naga Dhanyata**
AI Engineering | Generative AI | Agentic AI | Python
