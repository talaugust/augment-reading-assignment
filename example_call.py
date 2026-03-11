import requests

word = "temporal"

url = "https://chat.illinois.edu/api/chat-api/chat"
headers = {
  'Content-Type': 'application/json'
}
data = {
  "model": "llama4:16x17b",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful AI assistant. Follow instructions carefully. Respond using markdown."
    },
    {
      "role": "user",
      "content": f"Can you define the word {word} for me?"
    }
  ],
  "api_key": "<your_api_key_here>",
  "course_name": "Human-LM-interaction",
  "stream": True,
  "temperature": 0.1,
  "retrieval_only": False
}

response = requests.post(url, headers=headers, json=data)
for chunk in response.iter_lines():
    if chunk:
        print(chunk.decode())