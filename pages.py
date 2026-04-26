import streamlit as st

# Define your pages
home = st.Page("home.py", title="home", url_path="home", icon="🏠")
excercises = st.Page("pages/excercises.py", title="excercises", icon="🏋", url_path='activities')
contribute = st.Page("pages/contribute.py", title="contribute", icon="🎁", url_path='contribute')
edit = st.Page("add.py", title = "add", url_path='add')

pg = st.navigation([home,excercises,contribute,edit], position="hidden")
pg.run()
