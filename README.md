# RAG-Based Customer Support Assistant

##  Overview
This project is a Retrieval-Augmented Generation (RAG) based customer support assistant.  
It answers user queries using a PDF knowledge base and provides contextual responses.  
It also includes a Human-in-the-Loop (HITL) mechanism for handling unknown queries.

---

## Features
- PDF-based knowledge retrieval  
- Context-aware answer generation  
- Vector database using ChromaDB  
- Embedding using HuggingFace model  
- Workflow-based query processing  
- Human-in-the-Loop (HITL) escalation  


---

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
2. Activate Environment
venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Add PDF
Place your PDF inside the data/ folder
Update file path in ingestion.py if needed
     Run Project
Step 1: Ingest PDF
python src/ingestion.py
Step 2: Run Application
python main.py
