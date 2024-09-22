import os
import streamlit as st
from pinecone import Pinecone, ServerlessSpec
import cohere
from typing import List
from pdf_loader import load_pdf
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Pinecone and Cohere
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")  # Set your Pinecone API key here
COHERE_API_KEY = os.getenv("COHERE_API_KEY")  # Set your Cohere API key here
# Initialize Cohere client
co = cohere.Client(api_key=COHERE_API_KEY)

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
INDEX_NAME = 'qa-bot-index'

# Delete existing index if it exists
if INDEX_NAME in pc.list_indexes().names():
    pc.delete_index(INDEX_NAME)

# Create a new index
pc.create_index(
    name=INDEX_NAME,
    dimension=384,
    metric='euclidean',
    spec=ServerlessSpec(cloud='aws', region='us-east-1')
)

# Connect to the index
index = pc.Index(INDEX_NAME)


def answer_query_with_cohere(query: str, documents: List[str]) -> str:
    """Generate a direct answer using Cohere based on the user's query and document context."""
    prompt = f"Using the following context from the document:\n{documents}\n\nPlease answer the following question: {query}\nAnswer:"

    response = co.generate(
        model='command-r-plus',
        prompt=prompt,
        max_tokens=150
    )

    return response.generations[0].text.strip()


# Streamlit UI
st.title("PDF Question Answering Bot")

uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")
if uploaded_file is not None:
    documents = load_pdf(uploaded_file)  # Load and process the PDF
    st.write("Document loaded successfully!")

    query = st.text_input("Ask your question:")

    if st.button("Get Answer"):
        if query:
            answer = answer_query_with_cohere(query, documents)
            st.write("### Answer:")
            st.write(answer)
        else:
            st.write("Please enter a question.")

