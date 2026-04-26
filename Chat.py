import streamlit as st
import time

def greet_chat():
    st.chat_message("assistant").write("Allegra")
    prompt = "Say hello back" 
    while True:
        input = st.chat_input(prompt)
        if input == "Allegra":
            st.chat_message("user").write("Allegra")
            time.sleep(1)
            st.chat_message("assistant").write("Co vai?")
            prompt = "Reply with 'well, thank you'"
