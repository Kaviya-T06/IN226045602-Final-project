from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def ingest_pdf():
    loader = PyPDFLoader("data/sample.pdf")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = Chroma.from_documents(
        chunks,
        embedding=embeddings,
        persist_directory="db"
    )

    db.persist()
    print("✅ PDF processed and stored!")

if __name__ == "__main__":
    ingest_pdf()