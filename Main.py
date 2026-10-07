import json
import random


FLASHCARD_FILE = "flashcards.json"
flashcards = []


def load_flashcards():
    global flashcards

    try:
        with open(FLASHCARD_FILE, "r", encoding="utf-8") as file:
            flashcards = json.load(file)
    except FileNotFoundError:
        flashcards = []
    except json.JSONDecodeError:
        print("There was a problem reading the saved flashcards file.")
        flashcards = []


def save_flashcards():
    with open(FLASHCARD_FILE, "w", encoding="utf-8") as file:
        json.dump(flashcards, file, indent=4)


def show_menu():
    print("\n=== Study Helper Bot ===")
    print("1. Add a flashcard")
    print("2. Quiz me")
    print("3. Show all flashcards")
    print("4. Give me a study tip")
    print("5. Exit")


def add_flashcard():
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")

    flashcards.append({
        "question": question,
        "answer": answer
    })

    save_flashcards()
    print("Flashcard added and saved!")


def quiz_user():
    if not flashcards:
        print("You do not have any flashcards yet.")
        return

    card = random.choice(flashcards)

    print("\nQuestion:")
    print(card["question"])

    user_answer = input("Your answer: ")

    print("\nCorrect answer:")
    print(card["answer"])

    if user_answer.lower().strip() == card["answer"].lower().strip():
        print("Great job! You got it right.")
    else:
        print("Nice try! Review this one again.")


def show_flashcards():
    if not flashcards:
        print("No flashcards have been added yet.")
        return

    print("\n=== Your Flashcards ===")

    for index, card in enumerate(flashcards, start=1):
        print(f"\nFlashcard {index}")
        print(f"Question: {card['question']}")
        print(f"Answer: {card['answer']}")


def give_study_tip():
    tips = [
        "Study in short sessions with breaks in between.",
        "Use active recall: test yourself instead of just rereading notes.",
        "Teach the topic to someone else to check your understanding.",
        "Review difficult topics more often.",
        "Remove distractions before starting a study session.",
        "Use flashcards for definitions, formulas, and key ideas."
    ]

    print("\nStudy Tip:")
    print(random.choice(tips))


def main():
    load_flashcards()

    print("Hello! I am your Study Helper Bot.")

    while True:
        show_menu()

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_flashcard()
        elif choice == "2":
            quiz_user()
        elif choice == "3":
            show_flashcards()
        elif choice == "4":
            give_study_tip()
        elif choice == "5":
            save_flashcards()
            print("Your flashcards have been saved.")
            print("Good luck studying! Goodbye.")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()