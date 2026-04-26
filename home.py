import streamlit as st
import webbrowser

st.title("Welcome!")

from streamlit_extras.card_selector import *

def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)

selected = card_selector(
    [
        dict(
            icon="📖",
            title="Learn",
            description="Do excercises to boost your Romansh skills",
        ),
        dict(
            icon="🎁",
            title="Contribute",
            description="Contribute sentences to be used in excercises",
        ),
        dict(
            icon="🗨",
            title="Chats",
            description="Simulate conversations",
        ),
    ],
    key="demo_basic",
)
if selected is not None:
    st.write(selected)
    if selected == 0:
        nav_to("https://romansh-tools.streamlit.app/activities")
    elif selected == 1:
        nav_to("https://romansh-tools.streamlit.app/contribute")






        
