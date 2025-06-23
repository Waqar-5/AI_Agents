# chainlit_app.py
import chainlit as cl
from main import get_response

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="🤖 Hi! Ask me anything — I’ll remember your past questions during this session.").send()

@cl.on_message
async def on_message(msg: cl.Message):
    chat_history = cl.user_session.get("chat_history", [])

    # Add user message to chat history
    chat_history.append({"role": "user", "content": msg.content})

    # Generate response
    response = get_response(msg.content, chat_history=chat_history)

    # Add assistant reply to history
    chat_history.append({"role": "assistant", "content": response})
    cl.user_session.set("chat_history", chat_history)

    await cl.Message(content=response).send()

