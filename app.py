from groq import Groq
from docx import Document
import streamlit as st

GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

st.title("Resume Assistant")

st.write("Upload your resume and ask questions about it.")

uploaded_resume = st.file_uploader("Upload your resume (docx)", type="docx")

if uploaded_resume:
    resume = Document(uploaded_resume)
    resume_text = "\n".join([paragraph.text for paragraph in resume.paragraphs])

    question = st.text_input("Ask a question about the resume")
    if question:
        answer = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {
                    "role": "user",
                    "content": f"Answer the following question based on the resume.\n\nResume:\n{resume_text}\n\nQuestion:\n{question}"
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        answer_content = ""
        for chunk in answer:
            answer_content += chunk.choices[0].delta.content or ""

        st.write("Answer:")
        st.write(answer_content)
