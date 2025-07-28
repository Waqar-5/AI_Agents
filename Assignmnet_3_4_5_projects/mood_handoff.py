# Import necessary classes from the Agentic SDK
from agents import Agent, Runner ,OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig, set_tracing_disabled

# Import Python system libraries
import os
import asyncio
# For loading API keys from a .env file
from dotenv import load_dotenv

# 🔐 Load environment variables (like GEMINI_API_KEY) from .env file

load_dotenv()
# 🔑 Get Gemini API Key from the environment
gemini_api_key = os.getenv("GEMINI_API_KEY")


# 🔧 Create an OpenAI-compatible client for Gemini using its base URL
client = AsyncOpenAI(
    api_key=gemini_api_key,  # your Gemini API key
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"  # Gemini-compatible endpoint
)




## 🧠 Create the model configuration using Gemini (flash version)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  # use a fast Gemini model
    openai_client=client # connect it to our Gemini client

)



# ⚙️ Configure how agents will run using RunConfig
config = RunConfig(
    model=model, # which model to use
    model_provider=client,  # who is providing the mode (Gemini)
    tracing_disabled=True # disable tracing/logging
)



# 🤖 Agent 1: Detects the user's mood from text
mood_checker_agent = Agent(
    name="Mood checker agent", # agent's internal name
    instructions="You are a mood checker agent. Your job is to understand the user's mood (e.g. happy, sad, stressed, excited) based on their message. but must understand user message, so answer be most related",
)





# 🤖 Agent 2: Suggests a helpful activity if user is sad or stressed
Suggester_Agent = Agent(
    name="Suggester Agent", # internal name
    instructions="You are an agent that suggests helpful activities when someone is feeling sad or stressed.",
)





# 🧠 Async main function (required for async agent runs)
async def main():
        # 🧍 Ask the user how they are feeling
    user_input = input("👤 How are you feeling today?\n> ")


    # Step 1: Run Mood Checker Agent with user input
    mood_result =await Runner.run(
    mood_checker_agent,  # agent that analyzes mood
    input=user_input,      # user's message
    run_config=config )              # config with Gemini model

    # 🧾 Extract the mood result text from agent response
    mood = mood_result.final_output.strip().lower()

        # 📢 Display the detected mood
    print("\n 🧠 Detected Mood:", mood)


 # Step 2: If mood is sad or stressed, run the suggestion agent
    if "sad" in mood or "stressed" in mood:
        print("\n🔄 Handoff to Suggester Agent...")

        # Step 2.1: Ask second agent to provide activity suggestion
        activity_result = await Runner.run(Suggester_Agent, input=f"The user is feeling {mood}. Suggest something helpful.", run_config=config)

        # 📢 Display the suggested activity
        print("\n🎯 Suggested Activity:", activity_result.final_output)
    else:
         # 😊 If the user is feeling fine, no help needed
        print("\n✅ No handoff needed. You're feeling good!")

# 🟢 Start the async program using asyncio
if __name__ == "__main__":
    asyncio.run(main())