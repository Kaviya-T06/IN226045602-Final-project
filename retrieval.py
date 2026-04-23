from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def retrieve(query):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    results = db.similarity_search(query, k=3)
    return results