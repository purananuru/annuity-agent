
# Annuity Agent with LangChain ReAct

This project processes annuity application PDFs, extracts relevant fields, validates them, and outputs structured reports using a LangChain ReAct agent.

## Features
- Extract and validate fields (DOB, advisor ID)
- Use LangSmith for tracing/debugging
- PDF text extraction using PyMuPDF

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your-api-key
export LANGCHAIN_API_KEY=your-langsmith-api-key
python main.py
```

## To Do
- Add more validations (name presence, medical conditions)
- Handle batch processing of PDFs
