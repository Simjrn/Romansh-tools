import streamlit as st
import pandas as pd
from sqlalchemy import text

conn = st.connection("sentences_db", type="sql", url="sqlite:///sentences.db")

# 1. Ensure table exists (and use lowercase for safety)
with conn.session as s:
    s.execute(text('CREATE TABLE IF NOT EXISTS sentences (romansh TEXT, english TEXT);'))
    s.commit()

# 2. Match your DF columns to your SQL columns
df = pd.DataFrame([{"romansh": "", "english": ""}])
edited_df = st.data_editor(df, num_rows="dynamic")

if st.button("submit"):
    clean_df = edited_df.dropna(how='all')
    clean_df.to_sql("sentences", conn.engine, if_exists="append", index=False)
    st.success(f"Saved {len(clean_df)} rows!")

sentences = conn.query("SELECT * FROM sentences", ttl=0)
