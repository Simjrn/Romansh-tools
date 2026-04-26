import streamlit as st
import pickle
from streamlit_extras.steps import steps

# 1. Initialize a state to track if the dialog should be visible
if "show_account_dialog" not in st.session_state:
    st.session_state.show_account_dialog = False

@st.dialog("Create account")
def create_account_dialog():
    # We use a separate key for steps inside the dialog 
    # to ensure it stays in sync with the session
    left, right = st.columns((1, 3))
    
    with left:
        # 'steps' component can sometimes be finicky in dialogs. 
        # A simpler way is to use a session_state variable for the step index:
        if "step_index" not in st.session_state:
            st.session_state.step_index = 0
        
        # Display icons/labels based on current index
        st.write(f"Step {st.session_state.step_index + 1} of 3")

    with right:
        if st.session_state.step_index == 0:
            st.session_state.name = st.text_input("Your name", value=st.session_state.get("name", ""))
            if st.button("Next"):
                st.session_state.step_index = 1
                st.rerun()

        elif st.session_state.step_index == 1:
            st.session_state.colour = st.selectbox("Colour", ["Blue", "Red", "Green"])
            if st.button("Back"):
                st.session_state.step_index = 0
                st.rerun()
            if st.button("Next"):
                st.session_state.step_index = 2
                st.rerun()

        elif st.session_state.step_index == 2:
            st.success("All set!")
            if st.button("Finish"):
                profile = {"name": st.session_state.name, "colour": st.session_state.colour}
                with open("profile.pkl", "wb") as f:
                    pickle.dump(profile, f)
                
                # Close the dialog by resetting state and rerunning
                st.session_state.show_account_dialog = False
                st.rerun()

# --- MAIN APP LOGIC ---
try:
    with open("profile.pkl", "rb") as f:
        profile = pickle.load(f)
    st.write(f"Welcome back, {profile['name']}!")
except (FileNotFoundError, EOFError):
    # If file doesn't exist, set the flag to show dialog
    st.session_state.show_account_dialog = True

# Trigger the dialog if the flag is True
if st.session_state.show_account_dialog:
    create_account_dialog()
