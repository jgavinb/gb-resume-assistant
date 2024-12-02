import PyPDF2
import streamlit as st
from groq import Groq

# read in resume
with open("brumfield_gavin.pdf", "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)

    resume_text = ""
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        resume_text += page.extract_text()

# streamlit page config
st.set_page_config(
    page_title="gavChat",
    page_icon="🤖",
    layout="centered"
)

# initialize GROQ client
client = Groq(api_key="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")

# initialize the chat history as streamlit session state if not present already
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# streamlit title
st.title("🤖 gavChat 1.0")
st.info('''LLAMA3-70B-8192 trained on my resume to answer any questions you may have!
- [LinkedIn](https://www.linkedin.com/in/gavinbrumfield)''')

# display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# input field for user's message:
user_prompt = st.chat_input("Ask me anything...")

if user_prompt:

    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # send user message to LLM and get a response
    messages = [
        {"role": "system", "content": f"You are trained on the following resume to answer questions: {resume_text}. If you are not able to answer a question please state this and refer the user to Gavin Brumfield's LinkedIn (https://www.linkedin.com/in/gavinbrumfield) to contact him to learn more."},
        *st.session_state.chat_history
    ]

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages
    )

    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})


    # display assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)