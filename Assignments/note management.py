import os
import re

# Define word lists for sentiment analysis
positive_words = ["good", "great", "excellent", "happy", "love", "fantastic", "wonderful"]
negative_words = ["bad", "sad", "poor", "hate", "terrible", "horrible", "worst"]

# Directory for storing notes
NOTES_DIR = "usernotes"

# Ensure notes directory exists
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

def analyze_sentiment(text):
    """Analyze sentiment of text using regex word matching."""
    pos_count = len(re.findall(r"\b(" + "|".join(positive_words) + r")\b", text.lower()))
    neg_count = len(re.findall(r"\b(" + "|".join(negative_words) + r")\b", text.lower()))

    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"

def list_notes():
    """Return list of note filenames."""
    return [f for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]

def read_and_analyze_notes():
    notes = list_notes()
    if not notes:
        print("⚠ No notes found!")
        return

    print("\nAvailable notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")

    choice = input("Enter note number to analyze (or 'all' for all notes): ")

    if choice.lower() == "all":
        for note in notes:
            with open(os.path.join(NOTES_DIR, note), "r") as f:
                content = f.read()
                print(f"\n📄 {note} → Sentiment: {analyze_sentiment(content)}")
    else:
        try:
            idx = int(choice) - 1
            with open(os.path.join(NOTES_DIR, notes[idx]), "r") as f:
                content = f.read()
                print(f"\n📄 {notes[idx]} → Sentiment: {analyze_sentiment(content)}")
        except (ValueError, IndexError):
            print("❌ Invalid choice!")

def create_new_note():
    filename = input("Enter new note filename (without .txt): ") + ".txt"
    filepath = os.path.join(NOTES_DIR, filename)
    if os.path.exists(filepath):
        print("⚠ File already exists! Choose Modify option instead.")
        return

    content = input("Enter note content: ")
    with open(filepath, "w") as f:
        f.write(content)
    print("✅ Note created successfully.")

def modify_existing_note():
    notes = list_notes()
    if not notes:
        print("⚠ No notes found!")
        return

    print("\nAvailable notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")

    try:
        idx = int(input("Enter note number to modify: ")) - 1
        filepath = os.path.join(NOTES_DIR, notes[idx])
    except (ValueError, IndexError):
        print("❌ Invalid choice!")
        return

    print("\n1. Overwrite note")
    print("2. Append to note")
    choice = input("Choose option: ")

    if choice == "1":
        new_content = input("Enter new content: ")
        with open(filepath, "w") as f:
            f.write(new_content)
        print("✅ Note overwritten successfully.")
    elif choice == "2":
        new_content = input("Enter text to append: ")
        with open(filepath, "a") as f:
            f.write("\n" + new_content)
        print("✅ Note updated successfully.")
    else:
        print("❌ Invalid choice!")

def main():
    while True:
        print("\n📘 Intelligent Notes Management System")
        print("1. Read & Analyze Notes")
        print("2. Create New Note")
        print("3. Modify Existing Note")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            read_and_analyze_notes()
        elif choice == "2":
            create_new_note()
        elif choice == "3":
            modify_existing_note()
        elif choice == "4":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
