
# Annuity Agent with LangChain ReAct

This project processes annuity application PDFs, extracts and validates key fields, and outputs structured reports using LangChain and LangSmith.

## Features
- Validate date of birth format
- Validate advisor ID against local database
- Extract demographics: state, sex, age, medical conditions
- Uses LangChain ReAct Agent
- LangSmith tracing enabled

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your-openai-key
export LANGCHAIN_API_KEY=your-langsmith-key
python main.py
```
