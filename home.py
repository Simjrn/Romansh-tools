import streamlit as st
import pickle
from streamlit_extras.resizable_columns import resizable_columns
from streamlit_extras.steps import steps

# --- DIALOG DEFINITION ---
@st.dialog("Create account")
def create_account():
    left, right = st.columns((1, 3))
    
    with left:
        s = steps(["Name", "Colour", "Confirmation"], icons=range(1, 4), key="steps_ui")

    with right:
        # Initialize variables in session state so they always exist
        if "temp_name" not in st.session_state: st.session_state.temp_name = ""
        if "temp_colour" not in st.session_state: st.session_state.temp_colour = "Blue"

        with s[0]:
            st.session_state.temp_name = st.text_input("Your name", value=st.session_state.temp_name)
            if st.button("Next", key="n1"): s.next()

        with s[1]:
            st.session_state.temp_colour = st.selectbox("Colour", ["Blue", "Red", "Green"], index=0)
            c1, c2 = st.columns(2)
            with c1: 
                if st.button("Back", key="b1"): s.previous()
            with c2: 
                if st.button("Next", key="n2"): s.next()

        with s[2]:
            st.success("All done!")
            if st.button("Save & Start"):
                # Save to file and refresh
                profile = {"name": st.session_state.temp_name, "colour": st.session_state.temp_colour}
                with open("profile.pkl", "wb") as f:
                    pickle.dump(profile, f)
                st.rerun()

st.title("Welcome!")

# --- LOAD POINTS ---
try:
    with open("points.pkl", "rb") as f:
        points_data = pickle.load(f)
except:
    points_data = {"points": 0}

# --- LOAD PROFILE ---
try:
    with open("profile.pkl", "rb") as f:
        profile_data = pickle.load(f)
    st.write(f"Hello, {profile_data['name']}!")
except:
    # If no profile exists, trigger the dialog
    if st.button("Setup Profile"):
        create_account()
    st.info("Please create an account to continue.")
    st.stop() # Stop execution until they have a profile

# --- UI DISPLAY ---
st.write(f"Existing score: {points_data['points']}")
cols = resizable_columns(2, border=True, key="layout_cols") 

with cols[0]:
    st.metric("Points", f"{points_data['points']}")
with cols[1]:
    st.metric("Level", f"{points_data['points'] // 300}")
