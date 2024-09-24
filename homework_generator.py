import marimo as mo

__generated_with = "0.8.18"
app = mo.App()


@mo.cell
def __():
    import random
    import string
    return random, string


@mo.cell
def __(random, string):
    def generate_math_problem(operation):
        if operation == 'add':
            a, b = random.randint(1, 20), random.randint(1, 20)
            return f"{a} + {b} = ?", a + b
        elif operation == 'subtract':
            a, b = random.randint(1, 20), random.randint(1, 10)
            return f"{a} - {b} = ?", a - b
        elif operation == 'multiply':
            a, b = random.randint(1, 10), random.randint(1, 10)
            return f"{a} × {b} = ?", a * b
    
    def generate_word_problem():
        templates = [
            "If {name} has {num1} apples and gives {num2} to a friend, how many apples does {name} have left?",
            "{name} wants to buy a toy that costs ${num1}. If {name} has ${num2}, how much more money does {name} need?",
            "There are {num1} students in a class. If {num2} more students join, how many students are there in total?"
        ]
        names = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Ethan"]
        template = random.choice(templates)
        name = random.choice(names)
        num1, num2 = random.randint(5, 20), random.randint(1, 10)
        
        problem = template.format(name=name, num1=num1, num2=num2)
        if "left" in template:
            answer = num1 - num2
        elif "more money" in template:
            answer = num1 - num2
        else:
            answer = num1 + num2
        
        return problem, answer
    
    def generate_word_puzzle():
        words = ["cat", "dog", "sun", "moon", "tree", "book", "fish", "bird", "star", "house"]
        word = random.choice(words)
        missing_index = random.randint(0, len(word) - 1)
        puzzle = word[:missing_index] + "_" + word[missing_index+1:]
        return f"Fill in the missing letter: {puzzle}", word[missing_index]
    
    def generate_unscramble():
        words = ["apple", "banana", "orange", "grape", "cherry", "lemon", "melon", "peach", "plum", "berry"]
        word = random.choice(words)
        scrambled = ''.join(random.sample(word, len(word)))
        return f"Unscramble the word: {scrambled}", word
    
    return generate_math_problem, generate_word_problem, generate_word_puzzle, generate_unscramble


@mo.cell
def __(generate_math_problem, generate_word_problem, generate_word_puzzle, generate_unscramble):
    # Generate homework
    math_problems = [
        generate_math_problem('add'),
        generate_math_problem('subtract'),
        generate_math_problem('multiply')
    ]
    word_problem = generate_word_problem()
    word_puzzle = generate_word_puzzle()
    unscramble = generate_unscramble()
    
    # Display homework
    mo.md("# 1st Grade Homework")
    
    mo.md("## Math Problems")
    for i, (problem, answer) in enumerate(math_problems, 1):
        mo.md(f"{i}. {problem}")
        mo.input(f"Answer {i}", type=str)
    
    mo.md("## Word Problem")
    mo.md(word_problem[0])
    mo.input("Word Problem Answer", type=str)
    
    mo.md("## Word Puzzle")
    mo.md(word_puzzle[0])
    mo.input("Missing Letter", type=str)
    
    mo.md("## Unscramble")
    mo.md(unscramble[0])
    mo.input("Unscrambled Word", type=str)
    
    return math_problems, word_problem, word_puzzle, unscramble


@mo.cell
def __(math_problems, word_problem, word_puzzle, unscramble, math_answers, word_problem_answer, word_puzzle_answer, unscramble_answer):
    # Check answers function
    def check_answers():
        results = []
        
        # Check math problems
        for i, ((_, correct), user_answer) in enumerate(zip(math_problems, math_answers), 1):
            if user_answer.value.strip() == str(correct):
                results.append(f"Math Problem {i}: Correct!")
            else:
                results.append(f"Math Problem {i}: Incorrect. The correct answer is {correct}.")
        
        # Check word problem
        if word_problem_answer.value.strip() == str(word_problem[1]):
            results.append("Word Problem: Correct!")
        else:
            results.append(f"Word Problem: Incorrect. The correct answer is {word_problem[1]}.")
        
        # Check word puzzle
        if word_puzzle_answer.value.strip().lower() == word_puzzle[1].lower():
            results.append("Word Puzzle: Correct!")
        else:
            results.append(f"Word Puzzle: Incorrect. The correct letter is '{word_puzzle[1]}'.")
        
        # Check unscramble
        if unscramble_answer.value.strip().lower() == unscramble[1].lower():
            results.append("Unscramble: Correct!")
        else:
            results.append(f"Unscramble: Incorrect. The correct word is '{unscramble[1]}'.")
        
        return "\n".join(results)
    
    check_button = mo.ui.button("Check Answers")
    
    if check_button.value:
        mo.md(check_answers())
    return


if __name__ == "__main__":
    app.run()
