import streamlit as st
import pandas as pd
import pickle
import os

df = pd.DataFrame(
    [
        {"English": "My sentence in english", "Romansh": "My sentence translated into Romansh"}
    ]
)
edited_df = st.data_editor(df, num_rows="dynamic")
st.write(edited_df)

if st.button("submit"):
    file_path = "sentences.pkl"

    if os.path.exists(file_path):
        with open(file_path, "ab") as f:
            pickle.dump(edited_df, f)
    else:
        with open(file_path, "wb") as f:
            pickle.dump(edited_df, f)
