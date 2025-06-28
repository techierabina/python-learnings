# Quiz questions stored as dictionaries in a list
quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. London", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"],
        "answer": "B"
    },
    {
        "question": "Which language is primarily used for data analysis?",
        "options": ["A. Java", "B. C++", "C. Python", "D. HTML"],
        "answer": "C"
    },
    {
        "question": "What is the output of 3 * 1 ** 3?",
        "options": ["A. 3", "B. 1", "C. 0", "D. 9"],
        "answer": "A"
    },
    {
        "question": "Which of these is a mutable data type in Python?",
        "options": ["A. Tuple", "B. String", "C. List", "D. Integer"],
        "answer": "C"
    }
]

def run_quiz():
    score = 0
    print("🔍 Welcome to the Python Quiz!\n")
    
    for i, q in enumerate(quiz):
        print(f"Q{i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer is {q['answer']}.\n")

    print(f"🎉 Quiz completed! Your final score is {score}/{len(quiz)}.")

# Run the quiz
run_quiz()
