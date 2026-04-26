import streamlit as st
import pickle
from streamlit_extras.resizable_columns import resizable_columns


@st.dialog("Create account")
def create_account():
   left, right = st.columns((1, 3))

    with left:
        s = steps(
            ["Name", "Colour", "Confirmation"],
           icons=range(1, 4),
            key="demo_vn",
        )

    with right:
        with s[0]:
            st.text_input("Your name", key="name_input")
            if st.button("Next", key="vn_next_0"):
                s.next()

        with s[1]:
            st.selectbox("Colour", ["Blue", "Red", "Green], key="colour_select")
            with st.container(horizontal=True):
                if st.button("Back", key="vn_back_1"):
                   s.previous()
                if st.button("Next", key="vn_next_1"):
                    s.next()

        with s[2]:
            st.success("All done! You're all set.")
            


st.title("Welcome!")

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
