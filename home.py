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
