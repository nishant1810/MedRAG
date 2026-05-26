import os
from flask import Flask, render_template, jsonify, request
from src.helper import download_embeddings
from src.prompt import *
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

app= Flask(__name__)

PINECONE_API_KEY= os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")

embedding= download_embeddings()

index_name= "medrag"

docsearch= PineconeVectorStore.from_existing_index(
    index_name= index_name,
    embedding= embedding
)

retriever = docsearch.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 15
    }
)

model= ChatOpenAI(
    model= "gpt-4o-mini"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

ques_ans_chain= create_stuff_documents_chain(model, prompt)
rag_chain= create_retrieval_chain(retriever, ques_ans_chain)


@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods= ["GET", "POST"])
def chat():
    msg= request.form["msg"]
    input= msg
    response= rag_chain.invoke({"input": msg})
    return str(response["answer"])

if __name__=='__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)