import aisuite as ai

# Configure aisuite to use local Ollama
client = ai.Client({
    "ollama": {
        "base_url": "http://localhost:11434/v1"
    }
})

# Call your local model through aisuite
response = client.chat.completions.create(
    model="ollama:glm-5cloud",
    messages=[{"role": "user", "content": "Explain why light is faster than sound?"}]
)