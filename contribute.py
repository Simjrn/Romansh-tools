import streamlit as st
import pandas as pd
from sqlalchemy import text

# Initialize the DataFrame
df = pd.DataFrame([
    {"English": "My sentence in english", "Romansh": "My sentence translated into Romansh"}
])

# Display the editor
edited_df = st.data_editor(df, num_rows="dynamic")

if st.button("submit"):
    conn = st.connection("sentences_db", type="sql")
    
    with conn.session as s:
        # Loop through each ROW of the edited dataframe
        for index, row in edited_df.iterrows():
            # Use :variable syntax for security and to handle quotes/apostrophes
            query = text('INSERT INTO sentences (romansh, english) VALUES (:rom, :eng)')
            s.execute(query, params={"rom": row["Romansh"], "eng": row["English"]})
        
        s.commit()
    
    st.success(f"Saved {len(edited_df)} sentences!")
