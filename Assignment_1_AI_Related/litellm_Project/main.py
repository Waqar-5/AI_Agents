import os
from datetime import datetime
from dotenv import load_dotenv
from litellm import completion

load_dotenv()  # Load from .env first

gemini_key = os.getenv("GEMINI_API_KEY")
if not gemini_key:
    raise ValueError("❌ Environment variable 'GEMINI_API_KEY' is missing in your .env file.")

os.environ["LITELLM_GEMINI_API_KEY"] = gemini_key  # ✅ Now safe to assign
# Journal file
JOURNAL_FILE = "mood_journal.txt"

def analyze_mood(entry: str) -> str:
    prompt = (
        "You are a compassionate mental wellness assistant.\n"
        "Analyze this journal entry and respond in a gentle, helpful way. "
        "Suggest a positive thought or coping strategy. Here's the entry:\n\n"
        f"{entry}\n\n"
        "Reply in 3 short paragraphs."
    )
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def save_to_journal(entry: str):
    with open(JOURNAL_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"\n[{timestamp}]\n{entry}\n{'-'*40}\n")

def main():
    print("🧘 Welcome to MentalMend – Your AI Mental Health Journal")
    user_input = input("💬 How are you feeling today? Write anything:\n\n👉 ")

    print("\n🔎 Analyzing your journal entry...\n")
    response = analyze_mood(user_input)

    print("🪷 Here's some support for you:\n")
    print(response)

    save_to_journal(user_input)

if __name__ == "__main__":
    main()
