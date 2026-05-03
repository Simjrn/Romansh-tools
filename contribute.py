import streamlit as st
import pandas as pd
import pickle
import os
from sqlalchemy import text

df = pd.DataFrame(
    [
        {"English": "My sentence in english", "Romansh": "My sentence translated into Romansh"}
    ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

if st.button("submit"):
    for line in edited_df:
        English 
        conn = st.connection("sentences_db", type="sql")
        with conn.session as s:
            s.execute(text('''INSERT INTO sentences
            VALUES 
