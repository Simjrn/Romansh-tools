import pickle
import streamlit as st
import os


if st.button("Clear file"):
    with open("sentencespkl", "wb") as f:
        os.remove("sentences.pkl")

objects = []
with open("sentences.pkl", "rb") as f:
    while True:
        try:
            objects.append(pickle.load(f))
        except EOFError:
            break  # Reached the end of the file
st.dataframe(objects)
