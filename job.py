# Simple Career Chatbot

def compress_text(text):
    """
    Simple compression:
    Keeps important lines containing keywords.
    """
    keywords = ["experience", "skills", "responsibility", "qualification", "requirement"]
    lines = text.split(".")
    important_lines = []

    for line in lines:
        for word in keywords:
            if word.lower() in line.lower():
                important_lines.append(line.strip())
                break

    if important_lines:
        return ". ".join(important_lines)
    else:
        return "No major requirements found. Please read full description."


def resume_tips():
    tips = """
Resume Tips:
1. Keep resume 1 page (for freshers).
2. Highlight skills matching job description.
3. Use bullet points.
4. Add measurable achievements (e.g., Increased sales by 20%).
5. Avoid spelling mistakes.
"""
    return tips

def career_chatbot():
    print("===== Career Assistant Chatbot =====")
    print("1. Compress Job Description")
    print("2. Get Resume Tips")
    print("3. Exit")

    while True:
        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            jd = input("\nPaste Job Description:\n")
            summary = compress_text(jd)
            print("\n--- Important Points ---")
            print(summary)

        elif choice == "2":
            print(resume_tips())

        elif choice == "3":
            print("Good luck with your applications!")
            break

        else:
            print("Invalid choice. Try again.")


# Run chatbot
career_chatbot()
