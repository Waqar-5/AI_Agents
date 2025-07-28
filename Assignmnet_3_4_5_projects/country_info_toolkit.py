from agents import function_tool, Agent, Runner, RunConfig, OpenAIChatCompletionsModel, AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio

# Load environment variable
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")

# Gemini-compatible OpenAI client
client = AsyncOpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Model setup
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

# Run config
config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

# ✅ Tool 1: Capital Finder
@function_tool
async def capital_tool(country: str) -> str:
    """Returns the capital of the given country."""
    response = await client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=[
            {"role": "user", "content": f"What is the capital of {country}?"}
        ]
    )
    return response.choices[0].message.content.strip()



# @function_tool
# async def language_tool(country: str) -> str:
#     """Returns the official language(s) of the given country."""
#     response = await client.chat.completions.create(
#         model="gemini-1.5-flash",
#         n=2,  # 👈 This tells the model to return 2 completions
#         messages=[
#             {"role": "user", "content": f"What is the official language of {country}?"}
#         ]
#     )

#     # 🧪 Print both choices to see the difference
#     print("Response 1:", response.choices[0].message.content.strip())
#     print("Response 2:", response.choices[1].message.content.strip())

#     # ✅ Return the first one (you can change this to 1 if you want the second)
#     return response.choices[0].message.content.strip()


        # OR above
        #  Important Note:
# Not all models support multiple completions. If gemini-1.5-flash doesn’t support n > 1, it might return only one response anyway. But GPT models (like gpt-4) do support it.




# ✅ Tool 2: Language Finder
@function_tool
async def language_tool(country: str) -> str:
    """Returns the official language(s) of the given country."""

    #  This line sends your question to Gemini AI and waits for its answer using the "gemini-1.5-flash" model.
    response = await client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=[
            {"role": "user", "content": f"What is the official language of {country}?"}
        ]
    )

    # “Return the first reply from ChatGPT, only the text, and remove any extra spaces.”
    return response.choices[0].message.content.strip()

# ✅ Tool 3: Population Finder
@function_tool
async def population_tool(country: str) -> str:
    """Returns the population of the given country."""
    response = await client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=[
            {"role": "user", "content": f"What is the current population of {country}?"}
        ]
    )
       # 🔍 Print the full response to see structure
    # print(response)
    return response.choices[0].message.content.strip()

# Orchestrator Agent
orchestrator_agent = Agent(  # ✅ Create a new AI Agent and assign it to the variable 'orchestrator_agent'
    name="Country Info Agent", # ✅ Give the agent a name (just for identification or logging)
    instructions=(  # ✅ Tell the agent what its job is and how to behave
        "You are an expert in global country data. "
        "Use the tools to fetch the capital, language, and population of any country the user asks about. "
        "Combine the responses into a friendly, readable summary." # → How to respond
    ),
    tools=[capital_tool, language_tool, population_tool], # ✅ Give the agent 3 tools it can use to fetch info

)

# Define the main asynchronous function
async def main():
        # Ask the user to enter a country name and store it in the variable `country`
    country = input("🌍 Enter a country name:\n> ")
    # Use the OpenAI Agent SDK Runner to execute the orchestrator agent
    # Pass the user's input as the agent's input and use a config object to define behavior
    result = await Runner.run(orchestrator_agent, input=country, run_config=config)
        # Print the final output from the agent, nicely labeled with an emoji
    print("\n📘 Country Info:\n", result.final_output)

# This condition ensures the script runs only when it's executed directly (not imported)
if __name__ == "__main__":
        # Run the main asynchronous function using asyncio's event loop
    asyncio.run(main())






"""
 response = await client.chat.completions.create(
        model="gemini-1.5-flash",
        messages=[
            {"role": "user", "content": f"What is the current population of {country}?"}
        ]
    )
"""
# response =                    # Save the result of the AI's answer in the variable named 'response'

# await                         # Wait for the AI to respond (used because the call is asynchronous)

# client                        # This is your Gemini client that connects to the Gemini API

# .chat                         # Access the chat-based model (not image or other types)

# .completions                  # Request a text completion (a full answer or response)

# .create(                      # Call the API to create (generate) the AI's response

#     model="gemini-1.5-flash", # Choose the Gemini model version to use (a fast and smart model)

#     messages=[                # Send a list of chat messages (just like a conversation)

#         {                     # This is a dictionary (a single message)

#             "role": "user",   # Set the speaker role as "user" (you are asking the question)

#             "content": f"What is the official language of {country}?" 
#                                # The actual question you ask the AI, using the country name
#         }

#     ]
# )


# return response.choices[0].message.content.strip()
# return                       # Send back (output) the result from this function

# response                     # This is the full response object returned by the AI

# .choices                     # 'choices' is a list of possible answers (usually only one)

# [0]                          # Pick the first answer from the list (index 0)

# .message                     # Inside the choice, get the actual message part

# .content                     # From the message, get just the text (the answer)

# .strip()                     # Remove any extra spaces or newlines at the start or end
