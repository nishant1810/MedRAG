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
from langchain_groq import ChatGroq

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain
)

from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


def initialize_rag_chain():

    try:
        print("STEP 1: Loading HF Token")

        hf_token = os.getenv("HF_TOKEN")

        if hf_token:
            os.environ["HF_TOKEN"] = hf_token

        print("STEP 2: Loading Embeddings")

        embedding = download_embeddings()

        print("STEP 3: Connecting Pinecone")

        index_name = "medrag"

        docsearch = PineconeVectorStore.from_existing_index(
            index_name=index_name,
            embedding=embedding
        )

        print("STEP 4: Creating Retriever")

        retriever = docsearch.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 2,
                "fetch_k": 5
            }
        )

        print("STEP 5: Connecting Groq")

        model = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.3-70b-versatile",
            temperature=0.3
        )

        print("STEP 6: Creating Prompt")

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}")
        ])

        print("STEP 7: Creating QA Chain")

        ques_ans_chain = create_stuff_documents_chain(
            model,
            prompt
        )

        print("STEP 8: Creating Retrieval Chain")

        rag_chain = create_retrieval_chain(
            retriever,
            ques_ans_chain
        )

        print("STEP 9: RAG Chain Ready")

        return rag_chain

    except Exception as e:
        print(f"INITIALIZATION ERROR: {str(e)}")
        raise


def get_rag_response(query: str):

    try:

        query_lower = query.lower().strip()

        greetings = ["hi", "hello", "hey", "hii", "helo"]
        thanks = ["thanks", "thank you", "thx"]
        bye_words = ["bye", "goodbye", "see you"]

        if query_lower in greetings:
            return "Hello! How can I help you with your health concerns today?"

        if query_lower in thanks:
            return "You're welcome! Take care and stay healthy."

        if query_lower in bye_words:
            return "Goodbye! Wishing you good health."

        print("STEP 10: Initializing RAG")

        rag_chain = initialize_rag_chain()

        print("STEP 11: Invoking Chain")

        response = rag_chain.invoke({
            "input": query
        })

        print("STEP 12: Response Generated")

        return response.get(
            "answer",
            "No answer generated."
        )

    except Exception as e:
        print(f"QUERY ERROR: {str(e)}")
        raise Exception(
            f"RAG Pipeline Failed: {str(e)}"
        )