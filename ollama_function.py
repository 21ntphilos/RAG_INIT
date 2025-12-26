from ollama import embed, chat

embeddings = embed(model="custom_pt", input=["write a poem about AI in psychology", "explain quantum computing in simple terms"])


response = chat(model="qwen3:0.6b", messages=[
    {
    "role": "user",
    "content": "what is older the chicken or the egg?"
    }
])

print(response.message.content)