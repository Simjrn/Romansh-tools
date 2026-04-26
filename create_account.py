from streamlit_extras.steps import *


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
            
