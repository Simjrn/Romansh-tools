import streamlit as st
import pandas as pd
from sqlalchemy import text

conn = st.connection("sentences_db", type="sql", url="sqlite:///sentences.db")

with conn.session as s:
    s.execute(text('CREATE TABLE IF NOT EXISTS sentences (romansh TEXT, english TEXT);'))
    s.commit()
df = pd.DataFrame([{"romansh": "", "english": ""}])
edited_df = st.data_editor(df, num_rows="dynamic", key="my_editor")

if st.button("submit"):
    # Filter out rows where BOTH cells are empty or just whitespace
    clean_df = edited_df[
        (edited_df["romansh"].str.strip() != "") | 
        (edited_df["english"].str.strip() != "")
    ]
    
    if not clean_df.empty:
        clean_df.to_sql("sentences", conn.engine, if_exists="append", index=False)
        st.success(f"Saved {len(clean_df)} rows!")
        # This tells Streamlit to rerun so the table below updates immediately
        st.rerun() 
    else:
        st.warning("Nothing to save!")

