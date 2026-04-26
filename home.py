import streamlit as st
import pickle
st.title("Welcome!")

try:
    with open("points.pkl", "rb") as f:
        data = pickle.load(f)
except (FileNotFoundError, EOFError):
    data = {"points": 0}
    with open("points.pkl", "wb") as f:
        pickle.dump(data, f)

# Now check for specific content
with open("points.pkl", "rb") as f:
    data = pickle.load(f)
    if "points" in data:
        st.write(f"Existing score: {data['points']}")


from streamlit_extras.resizable_columns import *

"""Resizable columns with borders."""
st.write("### About you")
cols = resizable_columns(2, border=True, key="data")
with cols[0]:
    st.metric("points", f"{data[points]}")
with cols[1]:
    st.metric("Level", f"{data[points]//100}")
