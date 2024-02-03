def display_question(question, options):
    print(question)
    for i in options:
        print(i)
    user_answer = input("Your answer (enter the option): ")
    return user_answer

def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

def main():
    questions = [
        "1. What is the capital of India?",
        "2. Which planet is known as the Red Planet?",
        "3. Who wrote the famous play 'Hamlet'?"
    ]

    options = [
        ["a) London", "b) New Delhi", "c) Rome", "d) Madrid"],
        ["a) Jupiter", "b) Mars", "c) Venus", "d) Saturn"],
        ["a) William Shakespeare", "b) Charles Dickens", "c) Jane Austen", "d) Mark Twain"]
    ]

    correct_answers = ["b", "b", "a"]

    num_questions = len(questions)
    score = 0

    for i in range(num_questions):
        user_answer = display_question(questions[i], options[i])
        if check_answer(user_answer, correct_answers[i]):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    if score!=3:
        print(f"\nYou got {score} out of {num_questions} questions correct.")
    else:
        print("Excellent! You got all correct!!")
main()