from ollama import chat
from ollama import ChatResponse

stream = chat(
    model='glm-5:cloud',
    messages=[{'role': 'user', 'content': 'Do you know who can win tonight mens cricket match beteen India and NZ'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)