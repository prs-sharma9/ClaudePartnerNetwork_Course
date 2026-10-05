import os
from anthropic import Anthropic
from dotenv import load_dotenv


load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

model = os.getenv("MODEL")


# Define utility functions
def add_user_message(messages, text):
    user_message = {
        "role": "user",
        "content": text
    }
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {
        "role": "assistant",
        "content": text
    }
    messages.append(assistant_message)

# Chat function take chat history and system prompt to guide model.
def chat(messages, system_prompt = None, temperature=0, stop_sequences = None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }

    if(system_prompt):
        params["system"] = system_prompt

    if(stop_sequences):
        params["stop_sequences"] = stop_sequences

    message = client.messages.create(**params)
    return message.content[0].text