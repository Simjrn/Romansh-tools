import streamlit as st

st.title("Welcome!")

from streamlit_extras.card_selector import *

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
        st.switch_page("https://romansh-tools.streamlit.app/activities")
    elif selected == 1:
        st.switch_page("https://romansh-tools.streamlit.app/contribute")






        
