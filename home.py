import streamlit as st

st.title("Welcome!")

one, two = st.columns(2)
one.link_button("Go to excercises", "https://romansh-tools.streamlit.app/activities", width="stretch", type="primary")
two.link_button("Contribute sentences", "https://romansh-tools.streamlit.app/contribute", width="stretch", type="primary")
