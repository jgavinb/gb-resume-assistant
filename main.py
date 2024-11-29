import os
import json
import docx
import streamlit as st
from groq import Groq

# read in resume
resume = docx.Document("brumfield_gavin.docx")
resume_text = "\n".join([p.text for p in resume.paragraphs])

# streamlit page config
st.set_page_config(
    page_title="gavChat 1.0",
    page_icon="🧊",
    layout="centered"
)

working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))


GROQ_API_KEY = config_data["GROQ_API_KEY"]

# save the api key to environment
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

client = Groq()

# initialize the chat history as streamlit session state if not present already
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# streamlit title
st.title("🧊 gavChat 1.0")

# display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# input field for user's message:
user_prompt = st.chat_input("Ask me anything...")

if user_prompt:

    st.chat_message("user").markdown(user_prompt)
    st.ession_state.chat_history.append({"role": "user", "content": user_prompt})

    # send user message to LLM and get a response
    messages = [
        {"role": "system", "content": f"You are a helpful asssistant, trained on the following resume to answer questions: {resume_text}"},
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