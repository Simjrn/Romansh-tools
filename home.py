import streamlit as st

st.title("Welcome!")

col1, col2 = st.columns(2)
one = col1.container(width = "stretch", height = 234)
two = col2.container(width = "stretch", height = 234)
one.link_button("Go to excercises", "romansh-tools.streamlit.app/activities")
