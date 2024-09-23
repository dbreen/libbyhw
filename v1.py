import marimo
import random


__generated_with = "0.8.18"
app = marimo.App(width="medium")


@app.cell
def generate_math_question():
    operations = ['+', '-', '*']
    op = random.choice(operations)
    if op == '+':
        a = random.randint(1, 20)
        b = random.randint(1, 20)
    elif op == '-':
        a = random.randint(1, 20)
        b = random.randint(1, a)
    else:  # multiplication
        a = random.randint(1, 10)
        b = random.randint(1, 10)
    question = f"What is {a} {op} {b}?"
    answer = eval(f"{a} {op} {b}")
    return question, str(answer)

@app.cell
def generate_reading_question():
    stories = [
        ("The Big Red Dog", 
         "Sam had a big red dog named Max. Max loved to play fetch in the park. "
         "One day, Sam threw the ball too far. Max ran into the bushes to get it. "
         "When Max came back, he had a blue ball! Sam was confused. "
         "Where did the blue ball come from? Then, Sam saw a girl looking for her ball. "
         "Sam and Max made a new friend that day."),
        ("The Magic Tree",
         "In Jenny's backyard, there was an old oak tree. One morning, Jenny found "
         "a door in the tree trunk. She opened it and saw a staircase going up. "
         "At the top, she found a treehouse full of talking animals. They told her "
         "she could visit anytime, but to keep it a secret. Jenny had many adventures "
         "in the magic tree after that.")
    ]
    
    story_title, story_text = random.choice(stories)
    
    questions = [
        f"What was the name of the dog in '{story_title}'?",
        f"What color was the ball Max found in '{story_title}'?",
        f"What did Jenny find in the tree in '{story_title}'?",
        f"Who did Jenny meet in the treehouse in '{story_title}'?"
    ]
    
    answers = ["Max", "blue", "a door", "talking animals"]
    
    question = random.choice(questions)
    answer = answers[questions.index(question)]
    
    return f"Read the story and answer the question:\n\n{story_text}\n\n{question}", answer

@app.cell
def generate_spelling_question():
    word_list = [
        "cat", "dog", "sun", "book", "tree", "house", "ball", "school", "friend", "happy",
        "jump", "play", "read", "write", "sing", "dance", "laugh", "smile", "love", "kind"
    ]
    
    word = random.choice(word_list)
    question = f"Spell the word: {word.upper()}"
    answer = word
    
    return question, answer

@app.cell
def check_answer(question, user_answer, correct_answer):
    user_answer = user_answer.strip().lower()
    correct_answer = str(correct_answer).strip().lower()
    return user_answer == correct_answer

@app.cell
def question_types():
    return {
        "math": generate_math_question,
        "reading": generate_reading_question,
        "spelling": generate_spelling_question
    }

@app.cell
def ui():
    question_type = mo.ui.dropdown(list(question_types().keys()), label="Select question type")
    new_question_button = mo.ui.button("New Question")
    question_display = mo.ui.markdown("Click 'New Question' to start!")
    user_input = mo.ui.text(label="Your answer")
    submit_button = mo.ui.button("Submit")
    result = mo.ui.markdown("")
    
    if new_question_button.value:
        global current_question, current_answer
        current_question, current_answer = question_types()[question_type.value]()
        question_display.value = f"## {question_type.value.capitalize()} Question\n\n{current_question}"
        result.value = ""
        user_input.value = ""
    
    if submit_button.value:
        is_correct = check_answer(current_question, user_input.value, current_answer)
        result.value = "Correct!" if is_correct else f"Sorry, the correct answer was '{current_answer}'."
    
    return mo.vstack([
        question_type,
        new_question_button,
        question_display,
        user_input,
        submit_button,
        result
    ])

# @app.cell
# def homework_app():
#     return ui()

# mo.app(homework_app)

if __name__ == "__main__":
    app.run()
