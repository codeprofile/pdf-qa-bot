# pdf-qa-bot
A Retrieval-Augmented Generation (RAG) model for a Question Answering (QA) bot for a business. Use a vector database `Pinecone DB` and a generative model  `Cohere API` . The QA bot  able to retrieve relevant information from a dataset and generate coherent answers.

# Interactive PDF Question Answering Bot

## Overview
This Streamlit app allows users to upload a PDF document and ask questions based on its content. The app utilizes Cohere for generating answers and Pinecone for managing document embeddings.

## Instructions
1. **Install Streamlit**: Ensure Streamlit is installed with `pip install streamlit`.
2. **Set API Keys**: Provide your Pinecone and Cohere API keys in the environment variables.
3. **Run the App**: Execute `streamlit run app.py` to start the app.
4. **Upload PDF**: Use the file uploader to upload your PDF document.
5. **Ask Questions**: Enter your questions and click "Get Answer" to receive responses.

## Requirements
- Python 3.x
- Streamlit
- Pinecone API key
- Cohere API key
- PDF document for testing

## UI

![image](https://github.com/user-attachments/assets/b431a0d5-b7fa-4be5-9960-d7b5384e72b7)
