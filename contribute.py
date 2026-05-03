import streamlit as st
import pandas as pd
from sqlalchemy import text

# Initialize the DataFrame
df = pd.DataFrame([
    {"English": "My sentence in english", "Romansh": "My sentence translated into Romansh"}
])


edited_df = st.data_editor(df, num_rows="dynamic")

if st.button("submit"):
    edited_df.to_sql("sentences", st.connection("sentences_db", type="sql", url="sqlite:///sentences.db").engine, if_exists="append", index=False)
    st.success("All rows saved!")
conn = st.connection("sentences_db", type="sql", url="sqlite:///sentences.db")
with conn.session as s:
    table = s.execute(text('SELECT * FROM sentences'))
    st.text(table)
