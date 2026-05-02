questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    }
]

score = 0

print("🧠 Welcome to Quiz App\n")

for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)
    
    user_ans = input("Enter your answer (A/B/C/D): ").upper()
    
    if user_ans == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong!\n")

print(f"🎯 Your Score: {score}/{len(questions)}")
