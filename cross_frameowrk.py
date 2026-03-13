import aisuite

# Use the aisuite library to call model from ollama - Because I have free credits for ollama
# 1. Define the configuration
# We use 'openai' as the provider framework, but point it to localhost.
config = {
    "openai": {
        "base_url": "http://localhost:11434/v1", # Point to Ollama's OpenAI-compatible endpoint
        "api_key": "ollama",                     # Dummy key (required by library, ignored by Ollama)
    }
}

# 2. Initialize the aisuite client
client = aisuite.Client(config)

# 3. Make a call
# Important: In aisuite, the model format is "provider:model_name".
# Since we are using the OpenAI provider config pointing to Ollama:
model_id = "openai:glm-5:cloud"

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is your knowledge cut off time?"}
]

response = client.chat.completions.create(
    model=model_id,
    messages=messages,
)

print(response.choices[0].message.content)
