import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

from dotenv import load_dotenv

from src.helper import download_embeddings
from src.prompt import *

from langchain_pinecone import PineconeVectorStore
from langchain_ollama import ChatOllama

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# API Keys
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
hf_token = os.getenv("HF_TOKEN")

if hf_token:
    os.environ["HF_TOKEN"] = hf_token

# Embeddings
embedding = download_embeddings()

# Pinecone Index
index_name = "medrag"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embedding
)

# Retriever
retriever = docsearch.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 2,
        "fetch_k":5
    }
)

# Ollama Model
OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)

model = ChatOllama(
    model="phi3",
    base_url=OLLAMA_BASE_URL,
    temperature=0.3,
    num_predict=80
)

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

# RAG Chain
ques_ans_chain = create_stuff_documents_chain(
    model,
    prompt
)

rag_chain = create_retrieval_chain(
    retriever,
    ques_ans_chain
)

# Function for FastAPI
def get_rag_response(query: str):

    query_lower = query.lower().strip()

    # Instant replies

    greetings = ["hi", "hello", "hey", "hii", "helo"]
    thanks = ["thanks", "thank you", "thx"]
    bye_words = ["bye", "goodbye", "see you"]

    if query_lower in greetings:
        return "Hello! How can I help you with your health concerns today?"

    if query_lower in thanks:
        return "You're welcome! Take care and stay healthy."

    if query_lower in bye_words:
        return "Goodbye! Wishing you good health."

    # AI response

    response = rag_chain.invoke({
        "input": query
    })

    return response["answer"]