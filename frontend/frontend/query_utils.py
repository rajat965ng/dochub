import os

from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore


def query(q: str) -> str:
    embeddings = OpenAIEmbeddings()
    index_name = os.getenv('INDEX_NAME')
    docsearch = PineconeVectorStore.from_existing_index(
        index_name=index_name, embedding=embeddings
    )
    chat = ChatOpenAI(temperature=0)

    qa = RetrievalQA.from_chain_type(
        llm=chat,
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        return_source_documents=True,
    )

    return qa.invoke({"query": q})
