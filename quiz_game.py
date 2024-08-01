def ask_question(question, correct_answer):
    """Ask a question and return True if the answer is correct, otherwise False."""
    answer = input(question + " ").lower()
    if answer == correct_answer:
        print("Answer is Correct!")
        return True
    else:
        print("Answer is not Correct!")
        return False

def main():
    print("Welcome to my computer quiz!")

    playing = input("Do you want to play? ").lower()
    if playing != "yes":
        print("Okay, maybe next time!")
        return

    print("Okay! Let's play :)")
    score = 0

    # Dictionary of questions and answers
    questions = {
        "What does CPU stand for?": "central processing unit",
        "What does GPU stand for?": "graphics processing unit",
        "Who invented Python?": "guido van rossum",
        "What does RAM stand for?": "random access memory"
    }

    # Loop through questions
    for question, correct_answer in questions.items():
        if ask_question(question, correct_answer):
            score += 1

    # Display results
    total_questions = len(questions)
    print(f"You got {score} out of {total_questions} questions correct!")
    print(f"You got {(score / total_questions) * 100:.2f}%.")

if __name__ == "__main__":
    main()
