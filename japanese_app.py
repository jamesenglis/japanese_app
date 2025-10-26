import streamlit as st

st.title("こんにちは! (Hello!) Japanese Learning App")
st.write("This is your first AI language app project!")

name = st.text_input("What is your name?")
if name:
    st.success(f"Nice to meet you, {name}! Let's start learning Japanese together.")

