import random

def play_quiz(questions):
    score = 0
    num_questions = len(questions)

    for question, answer in questions.items():
        print(question)
        user_answer = input("Your answer: ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The answer is {answer}")

    print(f"\nYou got {score} out of {num_questions} questions right.")

if __name__ == "__main__":
    questions = \
    {
        "What is a rivers ability to carry grain sizes?": "competency",
        "do all rivers have the same velocity?": "no",
        "What is a meandering river?": "a river that moves",
        "What is are the agents that move sediment called?": "water, wind, ice, gravity alone",
        "How do you prevent flooding?": "dams and levees",
        "Where do you find more weathering on the rocks, the Grand Canyon or the New River Gorge?": "New River Gorge",
        "If you find shale in the ground does it mean the sea level rised or fell?": "the sea level rised then fell",
    }

    play_quiz(questions)