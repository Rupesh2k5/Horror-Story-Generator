import streamlit as st
from generate_story import generate_horror_story

st.title("HauntScript - AI Horror Story Generator")

# Input fields
name = st.text_input("Enter the character name:")
situation = st.text_area("Describe the situation:")
num_lines = st.number_input("Number of lines in the story:", min_value=1, step=1)

# Button to generate story
if st.button("Generate Horror Story"):
    # Input validation
    if not name.strip():
        st.warning("Please enter a character name.")
    elif not situation.strip():
        st.warning("Please describe the situation.")
    else:
        # Generate story
        story = generate_horror_story(name, situation, num_lines)
        st.subheader("📖 Your Horror Story:")
        st.write(story)
