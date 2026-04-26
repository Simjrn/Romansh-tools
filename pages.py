import streamlit as st

# Define your pages
home = st.Page("home.py", title="home", url_path="home", icon="🏠")
excercises = st.Page("excercises.py", title="excercises", icon="🏋", url_path='activities')

pg = st.navigation([home,excercises], position="hidden")
pg.run()
