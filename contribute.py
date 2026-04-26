import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
        {"English": "My sentence in english", "Romansh": "My sentence translated into Romansh"}
    ]
)
edited_df = st.data_editor(df, num_rows="dynamic")
st.write(edited_df)
