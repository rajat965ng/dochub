import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore


def execute():
    loader = PyPDFLoader("resources/IBM_Annual_Report_2023.pdf")
    docs = loader.load_and_split()
    print(len(docs))

    embeddings = OpenAIEmbeddings()
    index_name = os.getenv('INDEX_NAME')

    docsearch = PineconeVectorStore.from_documents(
        docs, embeddings, index_name=index_name
    )
    # query = "What did the president say about Ketanji Brown Jackson"
    # docs = docsearch.similarity_search(query)
    # print(docs[0].page_content)
