import streamlit as st
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Welcome to my hosted resume and chatbot!
    **👈 Select a demo from the sidebar**
"""
)