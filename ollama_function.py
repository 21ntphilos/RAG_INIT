from ollama import embed, chat

embedding = embed(model="custom_pt", input=["write a poem about AI in psychology", "explain quantum computing in simple terms"])

print (embedding)