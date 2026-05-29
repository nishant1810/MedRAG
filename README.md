# MedRAG – Intelligent Medical Question Answering System

MedRAG is a production-ready AI medical chatbot built using **Retrieval-Augmented Generation (RAG) architecture medical chatbot** .

The system combines vector search and large language models to retrieve relevant medical context and generate concise, context-aware responses.


---

# Overview

Large language models often hallucinate when asked domain-specific questions.
MedRAG solves this by using **retrieval-augmented generation**, where relevant medical documents are retrieved first and then provided to the language model for accurate responses.

The system processes medical PDFs, converts them into semantic embeddings using Sentence Transformers, and stores them in Pinecone vector databases for efficient similarity search. When a user submits a medical query, the system retrieves the most relevant contextual information and passes it to the language model to generate concise and reliable answers.

---

# Features

• Retrieval-Augmented Generation for accurate answers

• Semantic medical documents search

• Vector database powered by Pinecone

• Context-aware LLM responses

• Local LLM inference using Ollama

• FastAPI backend APIs

• Dockerized multi-container architecture

• Nginx reverse proxy integration

• Pinecone vector database integration

• Interactive chatbot UI

---

# Key Highlights

* Processes **100+ pages of medical knowledge documents**
* Generates **384-dimensional semantic embeddings**
* Retrieves relevant knowledge using **vector similarity search**
* Returns concise answers with **context-aware LLM reasoning**

---

# Tech Stack

**Backend**

* Python
* FastAPI
* LangChain

**AI / ML**

* Ollama
* HuggingFace Sentence Transformers
* Phi3 / Mistral

**Vector Database**

* Pinecone

**Infrastructure Ready**

* Docker containerization
* Nginx
* Architecture compatible with cloud deployment

**Frontend**

* HTML
* Bootstrap
* JavaScript

---

# Project Structure

```
Medical-Chatbot
├── backend_fastapi/     # FastAPI backend services
│         ├── routes/    # API route handlers
│         ├── schemas/   # Request/response schemas
│         ├── services/  # RAG and AI service logic
│         └── main.py    # FastAPI application entry point
│
├── Data/                # Medical knowledge PDFs
├── src/
│   ├── helper.py        # Document loading & embeddings
│   ├── prompt.py        # LLM prompt templates
│
├── templates/
│   └── chat.html        # Chat interface
│
├── nginx/ 
│     └── nginx.conf     # Nginx reverse proxy
configuration
│ 
├── Dockerfile           # Docker image configuration
├── docker-compose.yml   # Multi-container orchestration
├── store_index.py       # Vector index creation
├── app.py               # Flask application
├── requirements.txt
└── README.md
```

---

# Pipeline

### 1. Document Processing

Medical PDFs are loaded and processed into text chunks.

### 2. Embedding Generation

Chunks are converted into semantic embeddings using Sentence Transformers.

### 3. Vector Storage

Embeddings are stored in Pinecone for similarity search.

### 4. Query Retrieval

Relevant context is retrieved based on user queries.

### 5. LLM Response Generation

Retrieved context is passed to the LLM to generate accurate medical responses.

### 6. Retrieval

Relevant document chunks are retrieved based on the user query.

---

# Example Query

User Question:

```
What are the symptoms of diabetes?
```

System Response:

```
Common symptoms of diabetes include increased thirst, frequent urination, fatigue, and blurred vision. These symptoms occur due to high blood sugar levels affecting the body's normal metabolic processes.
```

---

# Future Improvements

* Add response streaming for real-time AI output
* Integrate clinical datasets for broader coverage
* Implement JWT-based user authentication
* Add conversation history and memory support
* Deploy using Kubernetes and cloud infrastructure
* Add monitoring and logging for production systems
---

# License

This project is for educational and research purposes.
