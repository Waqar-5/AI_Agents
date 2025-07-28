from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
import asyncio
import os
from dotenv import load_dotenv

# ─────────────────────────────────────────────────────────────
# 1️⃣ Load Gemini API Key from .env
# ─────────────────────────────────────────────────────────────
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# ─────────────────────────────────────────────────────────────
# 2️⃣ Gemini Client & Model Setup
# ─────────────────────────────────────────────────────────────
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",   # or "gemini-1.5-pro" if you prefer
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

# ─────────────────────────────────────────────────────────────
# 3️⃣ Smart Store Agent Setup
# ─────────────────────────────────────────────────────────────
Product_Suggest_agent = Agent(
    name="Universal Smart Store Agent",
    instructions=(
        "You are a smart, helpful store assistant. A user will describe a symptom, need, or situation "
        "(e.g., 'I have a headache', 'I feel tired', 'I'm going camping', etc).\n"
        "Your job is to:\n"
        "1. Understand the user's need.\n"
        "2. Suggest one relevant product from a general store (medicine, snack, skincare, hygiene, travel item, etc).\n"
        "3. Briefly explain how it helps.\n"
        "Only suggest practical, realistic products sold in common stores."
    )
)

# ─────────────────────────────────────────────────────────────
# 4️⃣ Main Function
# ─────────────────────────────────────────────────────────────
async def main():
    user_input = input("🛒 What can I help you with today?\n> ")

    result = await Runner.run(
        Product_Suggest_agent,
        input=user_input,
        run_config=config
    )

    print("\n🧠 Smart Suggestion:\n", result.final_output.strip())

# ─────────────────────────────────────────────────────────────
# 5️⃣ Entry Point
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    asyncio.run(main())



# or 




# from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, AsyncOpenAI, RunConfig
# import asyncio
# import os
# from dotenv import load_dotenv


# load_dotenv()

# gemini_api_key = os.getenv("GEMINI_API_KEY")

# client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=client
# )



# config = RunConfig(
#     model=model,
#     model_provider=client,
#     tracing_disabled=True
# )


# # Product_Suggest_agent = Agent(
# #     name="Suggester Smart Agent",
# # instructions = (
# #     "You are a helpful store agent that recommends store products based on customer needs.\n"
# #     "If the customer describes a symptom or a need (like 'I have a headache or any thing'), suggest a specific product (like a medicine or according to problem user provide), "
# #     "mention its name, and explain why it's helpful. Always stay within the context of a store that sells medicines, toiletries, snacks, etc."
# # )
# # )

# Product_Suggest_agent = Agent(
#     name="Universal Smart Store Agent",
#     instructions=(
#         "You are a smart, helpful store agent. A user will tell you a problem, need, or situation (e.g., 'I have a headache', 'I feel tired', 'My skin is dry', 'I'm going on a trip', etc).\n"
#         "Your job is to:\n"
#         "1. Understand their need or problem.\n"
#         "2. Suggest one or more products from a general store (e.g., medicines, snacks, toiletries, accessories, drinks, etc).\n"
#         "3. Clearly explain how and why the suggested product helps solve their issue.\n"
#         "Never say you are an AI. Always stay within store-related products and explain with practical logic., why that happens"
#     )
# )
# user_input = input("🛒 What can I help you with today? ")

# async def main():
#     result = await Runner.run(Product_Suggest_agent, user_input, run_config=config )
#     print("🧠 Smart Suggestion", result.final_output)

# asyncio.run(main())