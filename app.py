import streamlit as st
from streamlit_tags import st_tags
import json


f = open('tag_map.json')        # OPEN JSON FILE

data = json.load(f)             # LOAD DATA

f.close()                       # CLOSE FILE

# --------------------------- VARIABLES

# SPLIT DATA
GENRE_TAGS = data['genre']
MOOD_TAGS = data['mood']
INSTRUMENT_TAGS = data['instrument']

MAX_TAGS = 3

# --------------------------- TITLE
st.title("FIRE COML FALL 2022 Audio Generation Model")

# --------------------------- MAIN
# SELECT TYPE OF GENERATION
option = st.selectbox("Select Generation type:", ("Sentence Based", "Tag Based"))

# SENTENCE BASED 
if option == "Sentence Based":
    input_sentence = st.text_input("Enter a description for a song you want to hear:")

    # SUBMIT DESCRIPTION
    if st.button("Submit Description"):
        if input_sentence is not None and len(input_sentence) > 0:
            st.write("Here is the generated audio: ")
            st.write(input_sentence)
        else:
            st.write("Invalid Description")

# TAG BASED
else:
    st.write("Enter Genre(s), Mood/Theme(s), and Instrument(s)")

    instructions = "Press enter to add more"

    genre = st_tags(
            label = 'Enter Genre(s):',
            text = instructions,
            suggestions = GENRE_TAGS,
            maxtags = MAX_TAGS,
            key = '1'
        )
    
    mood = st_tags(
            label = 'Enter Mood/Theme(s):',
            text = instructions,
            suggestions = MOOD_TAGS,
            maxtags = MAX_TAGS,
            key = '2'
        )
    
    instrument = st_tags(
            label = 'Enter Instrument(s):',
            text = instructions,
            suggestions = INSTRUMENT_TAGS,
            maxtags = MAX_TAGS,
            key = '3'
        )

    # SUBMIT TAGS
    if st.button("Submit Tags"):
        st.write("Tags are:")
        input = genre + mood + instrument
        st.write(str(input))
