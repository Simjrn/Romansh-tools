import streamlit as st
import pickle
from streamlit_extras.resizable_columns import resizable_columns

st.title("Welcome!")

# 1. LOAD DATA: Try to open the file once. If it fails, create default data.
try:
    with open("points.pkl", "rb") as f:
        data = pickle.load(f)
except (FileNotFoundError, EOFError):
    data = {"points": 0}
    with open("points.pkl", "wb") as f:
        pickle.dump(data, f)

# 2. DISPLAY SCORE: Use the dictionary 'data' to access 'points'
if "points" in data:
    st.write(f"Existing score: {data['points']}")

st.write("### About you")

# 3. LAYOUT: Using resizable columns
# Note: 'resizable_columns' returns a list of column objects
cols = resizable_columns(2, border=True, key="layout_cols") 

with cols[0]:
    # Always use data['points'] because 'points' itself isn't a variable
    st.metric("Points", f"{data['points']}")

with cols[1]:
    # Level calculation using the points value from the dictionary
    st.metric("Level", f"{data['points'] // 300}")
