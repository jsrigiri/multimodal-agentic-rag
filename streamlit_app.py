import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="Multimodal Agentic RAG",
    layout="wide",
)

st.title("Multimodal Agentic RAG")
st.write("Upload documents and ask grounded questions with sources.")


uploaded_file = st.file_uploader(
    "Upload PDF, CSV, TXT, Markdown, or Image",
    type=["pdf", "csv", "txt", "md", "png", "jpg", "jpeg"],
)

if uploaded_file is not None:
    if st.button("Upload and Index"):
        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type,
            )
        }

        response = requests.post(f"{API_URL}/upload", files=files)

        if response.status_code == 200:
            st.success("File uploaded and indexed.")
            st.json(response.json())
        else:
            st.error("Upload failed.")
            st.text(response.text)


question = st.text_input("Ask a question")

if st.button("Ask"):
    response = requests.post(
        f"{API_URL}/ask",
        json={"question": question},
    )

    if response.status_code == 200:
        result = response.json()

        st.subheader("Answer")
        st.write(result["answer"])

        st.subheader("Sources")
        st.json(result["sources"])
    else:
        st.error("Question failed.")
        st.text(response.text)