import streamlit as st
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

st.set_page_config(page_title="RAG Local com Ollama", layout="wide")
st.title("🦙 RAG 100% Local")

with st.sidebar:
    uploaded_file = st.file_uploader("Suba um PDF", type="pdf")
    processar = st.button("Criar Mapa de Vetores")

embeddings = OllamaEmbeddings(model="mxbai-embed-large")
llm = ChatOllama(model="llama3.2")

if processar and uploaded_file:
    with st.spinner("Lendo PDF e criando embeddings locais..."):
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        loader = PyPDFLoader("temp.pdf")
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100)
        chunks = splitter.split_documents(docs)

        vector_db = Chroma.from_documents(
            documents=chunks, embedding=embeddings, persist_directory="./db_local"
        )
        st.success("Banco de vetores local pronto!")

st.divider()
pergunta = st.text_input("O que deseja saber do seu documento?")

if pergunta:
    vector_db = Chroma(persist_directory="./db_local", embedding_function=embeddings)

    system_prompt = (
        "Você é um especialista em Clean Code, mas quando alguem faz pergunta que não seja sobre código você fala dos seus interesses que é fazer bolo"
        "Sua resposta DEVE ser baseada EXCLUSIVAMENTE nos trechos do livro fornecidos abaixo. "
        "Se a informação não estiver no contexto, de uma curiosidade sobre a confecção de bolo para descontrair"
        "Contexto:\n{context}"
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(vector_db.as_retriever(), combine_docs_chain)

    resultado = rag_chain.invoke({"input": pergunta})

    st.subheader("Resposta (Ollama):")
    st.write(resultado["answer"])
