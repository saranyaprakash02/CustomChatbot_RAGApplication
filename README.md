
# 💬 Custom Chatbot Q&A (RAG Application)

## 📘 Project Overview
The **Custom Chatbot Q&A (RAG Application)** is a document-based AI system that enables users to upload a PDF file and ask context-specific questions. It leverages **LangChain**, **ChromaDB**, and **local LLMs (LlamaCpp)** to retrieve and generate answers based on the uploaded document.

This approach implements the **Retrieval-Augmented Generation (RAG)** architecture, combining **information retrieval** and **text generation** to create intelligent document-based assistants.

---

## 🧠 Technologies & Libraries Used

| Component | Description |
|------------|-------------|
| **Streamlit** | Frontend UI for uploading documents and interacting with the chatbot. |
| **LangChain** | Framework for chaining components such as loaders, retrievers, and LLMs. |
| **PyPDFLoader** | Extracts text data from PDF files. |
| **RecursiveCharacterTextSplitter** | Splits large text documents into smaller overlapping chunks for better vectorization. |
| **ChromaDB** | Vector database used to store document embeddings. |
| **HuggingFaceEmbeddings** | Converts text chunks into numerical vectors for similarity search. |
| **LlamaCpp** | Loads and interacts with local LLM models (e.g., Mistral, LLaMA). |
| **RetrievalQA Chain** | Handles the question-answer retrieval and response generation process. |

---

## ⚙️ Requirements

Before running the app, install the required dependencies:

```bash
pip install streamlit langchain-community chromadb sentence-transformers llama-cpp-python pypdf
```

You also need a **local model file** (e.g., `mistral-7b-instruct-v0.1.Q2_K.gguf`) downloaded and placed in a folder like:
```
D:/LLM_prj/RAGChatbot_Final/models/
```

---

## 🧩 Workflow

1. **Upload PDF Document**  
   The user uploads a `.pdf` file through the Streamlit UI.

2. **Extract Text from PDF**  
   The text is extracted using `PyPDFLoader`.

3. **Split Document**  
   `RecursiveCharacterTextSplitter` divides the text into smaller overlapping chunks for better processing.

4. **Create Embeddings & Store in ChromaDB**  
   The text chunks are converted into vector embeddings using `HuggingFaceEmbeddings` and stored in `ChromaDB`.

5. **Initialize Local LLM**  
   A local model (e.g., Mistral or LLaMA) is loaded using `LlamaCpp` for efficient inference.

6. **User Query Processing**  
   The user types a question, and the **RetrievalQA** chain retrieves the most relevant document chunks from ChromaDB.

7. **Generate Answer**  
   The LLM generates a coherent answer based on the retrieved content, displayed on the Streamlit UI.

---

## 🧰 Architecture Diagram (Conceptual)

```
         ┌────────────┐
         │  Streamlit │
         │   (UI)     │
         └─────┬──────┘
               │
         Upload PDF
               │
         ┌─────▼──────┐
         │  LangChain │
         │  Pipeline  │
         └─────┬──────┘
               │
     ┌─────────▼─────────┐
     │  Text Splitter     │
     │ + Embeddings       │
     └────────┬───────────┘
              │
      ┌───────▼──────────┐
      │   ChromaDB        │
      │ (Vector Storage)  │
      └───────┬──────────┘
              │
       ┌──────▼──────┐
       │  LlamaCpp   │
       │ (Local LLM) │
       └──────┬──────┘
              │
       ┌──────▼──────┐
       │  Response    │
       │  Generation  │
       └──────────────┘
```

---

## 🚀 How to Run

### Step 1: Start the Streamlit App
```bash
streamlit run ragchatbot.py
```

### Step 2: Upload and Query
- Upload your desired **PDF file**.  
- Enter a **question** related to the document.  
- The system retrieves relevant text and generates an answer using your local model.

---

## 🧩 Common Issues & Fixes

| Issue | Cause | Solution |
|--------|--------|-----------|
| **ModuleNotFoundError: No module named 'langchain.text_splitter'** | LangChain submodules are now under `langchain_community`. | Use `from langchain_community.text_splitter import RecursiveCharacterTextSplitter` or install `langchain-community`. |
| **Model not found or path error** | Incorrect local path for `.gguf` model. | Ensure model path is valid (e.g., `D:/LLM_prj/...`). |
| **ChromaDB locking issue** | Concurrent DB access. | Use unique persist_directory names per session or restart the app. |
| **High memory usage** | Large PDF or LLM model. | Use smaller model (e.g., `mistral-7b-instruct.Q4_K_M.gguf`). |

---

## 🎯 Learning Outcomes

- Understanding of **RAG (Retrieval-Augmented Generation)** workflow.  
- Experience using **LangChain** and **ChromaDB** for document intelligence.  
- Local **LLM integration** using `LlamaCpp`.  
- Knowledge of **embedding-based retrieval** and **vector similarity search**.

---

## 🔮 Future Enhancements

- Add **multi-PDF support**.  
- Use **Ollama** or **local API** for faster inference.  
- Integrate **chat memory** for contextual multi-turn conversations.  
- Enhance retrieval with **FAISS** or **Milvus** for larger datasets.

---

**Developed by:** *Saranya P*  
**Phase 3 Project — SEQATO LLM Awareness and Portfolio Development Program*
