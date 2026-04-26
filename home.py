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
            icon=":material/dns:",
            title="On-Prem",
            description="Host in your data center",
        ),
    ],
    key="demo_basic",
)
if selected is not None:
    st.write(f"You picked option **{selected}**


one, two = st.columns(2)
one.link_button("Go to excercises", "https://romansh-tools.streamlit.app/activities", width="stretch", type="primary")
two.link_button("Contribute sentences", "https://romansh-tools.streamlit.app/contribute", width="stretch", type="primary")
