import streamlit as st
import random
from streamlit_sortables import sort_items

page = st.sidebar.radio(
    "Choose which activity:",
    ("Cloze deletions", "Verb conjugation exercises", "Word shuffle")
)


if page == "Cloze deletions":
    line_count = 0
    with open('sentences.txt', 'r') as file:
        for line in file:
            line_count += 1
    line_with_sentence = random.randint(1, line_count)


    line_count = 0
    with open('sentences.txt', 'r') as file:
        for line in file:
            line_count += 1
            if line_count == line_with_sentence:
                item = line

    item = item.split(",")
    sentence = item[1].split()
    random_int = random.randint(0, len(sentence)-1)
    random_str = sentence[random_int]
    question = item[1].replace(random_str, "____")
    if "?" in random_str:
        question = question + '?'
    st.header(question)
    st.caption(item[0])

    @st.fragment
    def get_answer():
        answer = st.text_input("Input your answer: ")
        submit_button = st.button(label='Submit')
        if submit_button:
            if answer == random_str.replace('?', '').replace('.',''):
                st.balloons()
            else:
                st.error(f"No, the correct answer was '{random_str}'")   
    get_answer()

    col1, col2, col3 = st.columns([1, 2, 1])
    col2.button("Next", use_container_width=True, type="primary")
####################
#Verb conjugation
###################
elif page == "Verb conjugation exercises":
    tense = st.selectbox("What would you like to study?", ["Present tense","Past perfect"])
    if tense == "Present tense":
        line_count = 0
        with open('present_tense.txt', 'r') as file:
            for line in file:
                line_count += 1
        random_line = random.randint(1, line_count)
        line_count = 0
        with open('present_tense.txt', 'r') as file:
            for line in file:
                line_count += 1
                if line_count == random_line:
                    sentences = line
                    translation = sentences.split(",")[0]
                    sentence = sentences.split(",")[1]
                    st.header(translation)
                    @st.fragment()
                    def get_conj():
                        answer = st.text_input(sentence.split()[0])
                        button = st.button("Submit")
                        if button:
                            if answer == sentence.split()[1]:
                                st.balloons()
                            else:
                                st.error(f"Incorrect. The correct answer was '{sentence.split()[1]}'")
                    get_conj()
                    col1, col2, col3 = st.columns([1,2,1])
                    col2.button("Next", type="primary", width="stretch")
    elif tense == "Past perfect":
        line_count = 0
        with open('past_perfect.txt', 'r') as file:
            for line in file:
                line_count += 1
        random_line = random.randint(1, line_count)
        line_count = 0
        with open('past_perfect.txt', 'r') as file:
            for line in file:
                line_count += 1
                if line_count == random_line:
                    sentences = line
                    translation = sentences.split(",")[0]
                    sentence = sentences.split(",")[1]
                    st.header(translation)
                    @st.fragment()
                    def get_conj():
                        answer = st.text_input(sentence.split()[0])
                        button = st.button("Submit")
                        if button:
                            if answer == sentence.split()[1]+' '+sentence.split()[2]:
                                st.balloons()
                            else:
                                st.error(f"Incorrect. The correct answer was '{sentence.split()[1]+' '+sentence.split()[2]}'")
                    get_conj()
                    col1, col2, col3 = st.columns([1,2,1])
                    col2.button("Next", type="primary", width="stretch")
###############################
#Pick words
#######################
elif page == "Word shuffle":
    line_count = 0
    with open('sentences.txt', 'r') as file:
        for line in file:
            line_count += 1
    line_with_sentence = random.randint(1, line_count)


    line_count = 0
    with open('sentences.txt', 'r') as file:
        for line in file:
            line_count += 1
            if line_count == line_with_sentence:
                item = line

    item = item.split(",")
    trans = item[0]
    st.header(trans)
    sentence = item[1].split()
    se = sentence.copy()
    items_to_shuffle = sentence
    random.shuffle(items_to_shuffle)
    original_items = items_to_shuffle
    @st.fragment()
    def get_sentence():     
        sorted_items = sort_items(original_items)
        col1, col2, col3 = st.columns([1, 3, 1])
        button = col2.button("Submit", type="primary", width="stretch")
        if button:
            if sorted_items == se:
                st.balloons()
            else:
                st.error(f"No, the correct answer was '{se.join()}'")
    get_sentence()
    st.button("Next", type="tertiary")
  


                    
        
