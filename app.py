import streamlit as st
from utils.gemini import get_response
from utils.logger import save_interaction

st.set_page_config(page_title="AI Learning Assistant")

st.title("AI-Driven Emotion Detection & Personalized Learning Support Platform")

user_input = st.text_area("Enter your study problem")

if st.button("Analyze"):
    if user_input.strip():
        # Get AI response
        response = get_response(user_input)

        # Save interaction to CSV
        save_interaction(user_input, response)

        # Display AI response
        st.subheader("AI Response")
        st.write(response)

    else:
        st.warning("Please enter your study problem.")