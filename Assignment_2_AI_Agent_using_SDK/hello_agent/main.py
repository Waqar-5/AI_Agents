# main.py
import os
from dotenv import load_dotenv
from datetime import datetime
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled

load_dotenv()
set_tracing_disabled(True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Shared agent object
agent = Agent(
    name="GeminiAgent",
    instructions="You are a helpful assistant. Respond concisely and clearly using prior conversation when available.",
    model=None  # We’ll assign it later
)

# Tries pro, falls back to flash if rate-limited
def get_response(prompt: str, chat_history=None) -> str:
    today = datetime.now().strftime("%A, %B %d, %Y")
    messages = [f"Today is {today}."]
    if chat_history:
        for turn in chat_history:
            messages.append(f"{turn['role'].capitalize()}: {turn['content']}")
    messages.append(f"User: {prompt}")
    full_prompt = "\n".join(messages)

    try:
        # Try gemini-1.5-pro
        model = OpenAIChatCompletionsModel(
            model="gemini-1.5-pro",
            openai_client=client
        )
        agent.model = model
        result = Runner.run_sync(agent, full_prompt)
        return result.final_output

    except Exception as e:
        print("⚠️ Pro model failed. Falling back to flash.")
        print(f"Error: {e}")

        # Fallback to flash model
        model = OpenAIChatCompletionsModel(
            model="gemini-1.5-flash",
            openai_client=client
        )
        agent.model = model
        result = Runner.run_sync(agent, full_prompt)
        return result.final_output
