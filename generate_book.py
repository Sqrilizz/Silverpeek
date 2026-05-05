#!/usr/bin/env python3
import ollama

response = ollama.chat(
    model='qwen2:7b',
    messages=[
        {
            "role": "user",
            "content": "сгенерируй markdown книгу"
        }
    ]
)

with open("recipes.md", "w", encoding="utf-8") as f:
    f.write(response['message']['content'])

print("Книга успешно сгенерирована в файл recipes.md")
