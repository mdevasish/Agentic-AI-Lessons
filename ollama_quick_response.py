from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model = 'glm-5:cloud', messages=[
  {'role': 'user','content': 'Why is the sky blue?'},
  {"role": "system", "content": "You are a helpful assistant."},
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)