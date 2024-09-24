import streamlit as st

# Title of the app
st.title("1st Grader's Homework App")

# Simple math problem
st.header("Math Problem")
st.write("What is 2 + 2?")

# Input for the answer
answer = st.number_input("Your answer:", min_value=0, max_value=10, step=1)

# Check the answer
if st.button("Submit"):
    if answer == 4:
        st.success("Correct!")
    else:
        st.error("Try again!")
