import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter

# Absolute path (IMPORTANT - error avoid karva mate)
BASE_DIR = r"C:\Users\kavi vala\Desktop\AI Chatbot"

PDF_PATH = os.path.join(BASE_DIR, "data", "sample.pdf")
VECTOR_PATH = os.path.join(BASE_DIR, "vectorstore")

def create_vector_db():
    print("📄 Loading PDF...")
    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()

    print("✂️ Splitting text...")
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents = text_splitter.split_documents(documents)

    print("🤖 Creating embeddings...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    print("🧠 Building FAISS index...")
    db = FAISS.from_documents(documents, embeddings)

    print("💾 Saving vectorstore...")
    db.save_local(VECTOR_PATH)

    print("✅ Vector DB Created Successfully!")

def load_vector_db():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    if not os.path.exists(VECTOR_PATH):
        raise Exception("❌ Vectorstore not found! First run create_vector_db()")

    print("📂 Loading vectorstore...")
    return FAISS.load_local(
        VECTOR_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )


#  First time run karva mate
if __name__ == "__main__":
    create_vector_db()
