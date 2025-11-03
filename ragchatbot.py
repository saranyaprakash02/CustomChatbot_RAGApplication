import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.llms import LlamaCpp
from langchain.chains import RetrievalQA

st.title("💬 Custom Chatbot Q&A (RAG Application)")

# Step 1: Upload PDF
uploaded_file = st.file_uploader("📄 Upload a PDF document", type=["pdf"])

if uploaded_file is not None:
    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ PDF uploaded successfully!")

    # Step 2: Extract text from PDF
    loader = PyPDFLoader("uploaded.pdf")
    documents = loader.load()

    st.info("🔍 Splitting document into smaller chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    st.info("📚 Creating document embeddings and storing in ChromaDB...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(docs, embedding=embeddings, persist_directory="db")
    vectorstore.persist()

    retriever = vectorstore.as_retriever()

    # Step 3: Initialize local LLM using LlamaCpp
    llm = LlamaCpp(model_path="D:\LLM_prj\RAGChatbot_Final\models\mistral-7b-instruct-v0.1.Q2_K.gguf")  # <-- replace with your local model path

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    # Step 4: User Question
    query = st.text_input("💡 Ask a question about your document:")

    if query:
        st.info("🤔 Thinking...")
        response = qa_chain.run(query)
        st.success("🧠 Answer:")
        st.write(response)
