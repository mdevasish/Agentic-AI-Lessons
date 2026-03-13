import pandas as pd
from datetime import datetime, date
from aisuite import Client
import aisuite
import json
client = Client()

config = {
    "openai": {
        "base_url": "http://localhost:11434/v1", # Point to Ollama's OpenAI-compatible endpoint
        "api_key": "ollama",                     # Dummy key (required by library, ignored by Ollama)
    }
}

# 2. Initialize the aisuite client
client = aisuite.Client(config)

def get_current_time():
    """
    Returns the current time as a string.
    """
    return datetime.now().strftime("%H:%M:%S")

# Message structure
prompt = "What time is it?"
messages = [
    {"role": "user","content": prompt},
    {"role": "system", "content": "You are a helpful assistant."}
]
tools = [{
    "type": "function",
    "function": {
        "name": "get_current_time", # <--- Your functions name
        "description": "Returns the current time as a string.", # <--- a description for the LLM
        "parameters": {}
    }
}]
response = client.chat.completions.create(
    model="openai:glm-5:cloud",
    messages=messages,
    tools=tools,

)

# See the LLM response
#response_dict = response.model_dump()
#print(json.dumps(response.model_dump(), indent=2))

message = response.choices[0].message
print(message)
#print(json.dumps(message),indent = 2)
if message.tool_calls:
    tool_call = message.tool_calls[0]
    #print(tool_call)
    function_name = tool_call.function.name


    if function_name == "get_current_time":
        function_result = get_current_time()

        # Send the result back to the model
        messages.append(message)  # Add the assistant's tool call message
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": function_result
        })

        # Get the final response with the time
        final_response = client.chat.completions.create(
            model="openai:glm-5:cloud",
            messages=messages,
            tools=tools,
        )
        print(final_response.choices[0].message.content)
else:
    # No tool call, just print the content directly
    print(message.content)


