import streamlit as st
from homework_generator import generate_math_problem, generate_word_problem, generate_word_puzzle, generate_unscramble

# Title of the app
st.title("1st Grader's Homework App")

# Initialize session state if not already done
if 'math_problems' not in st.session_state:
    st.session_state.math_problems = [
        generate_math_problem('add'),
        generate_math_problem('subtract'),
        generate_math_problem('multiply')
    ]
if 'word_problem' not in st.session_state:
    st.session_state.word_problem = generate_word_problem()
if 'word_puzzle' not in st.session_state:
    st.session_state.word_puzzle = generate_word_puzzle()
if 'unscramble' not in st.session_state:
    st.session_state.unscramble = generate_unscramble()

math_problems = st.session_state.math_problems
word_problem = st.session_state.word_problem
word_puzzle = st.session_state.word_puzzle
unscramble = st.session_state.unscramble

# Display homework
st.header("Math Problems")
for i, (problem, _) in enumerate(math_problems, 1):
    st.write(f"{i}. {problem}")
    user_input = st.number_input(f"Answer {i}", min_value=0, max_value=100, step=1, format="%d")
    math_problems[i-1] = (problem, user_input)

st.header("Word Problem")
st.write(word_problem[0])
word_problem_answer = st.text_input("Word Problem Answer")

st.header("Word Puzzle")
st.write(word_puzzle[0])
word_puzzle_answer = st.text_input("Missing Letter")

st.header("Unscramble")
st.write(unscramble[0])
unscramble_answer = st.text_input("Unscrambled Word")

# Check answers
if st.button("Submit"):
    results = []

    # Check math problems
    for i, (problem, correct) in enumerate(math_problems, 1):
        if problem[1] != '' and int(float(problem[1])) == correct:
            results.append(f"Math Problem {i}: Correct!")
        else:
            results.append(f"Math Problem {i}: Incorrect. The correct answer is {correct}.")

    # Check word problem
    if word_problem_answer.strip() == str(word_problem[1]):
        results.append("Word Problem: Correct!")
    else:
        results.append(f"Word Problem: Incorrect. The correct answer is {word_problem[1]}.")

    # Check word puzzle
    if word_puzzle_answer.strip().lower() == word_puzzle[1].lower():
        results.append("Word Puzzle: Correct!")
    else:
        results.append(f"Word Puzzle: Incorrect. The correct letter is '{word_puzzle[1]}'.")

    # Check unscramble
    if unscramble_answer.strip().lower() == unscramble[1].lower():
        results.append("Unscramble: Correct!")
    else:
        results.append(f"Unscramble: Incorrect. The correct word is '{unscramble[1]}'.")

    for result in results:
        st.write(result)
