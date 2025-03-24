from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai = OpenAI()
completion = openai.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "user",
        "content": "Write a one-sentence bedtime story about a unicorn."
    }]
)

print(completion.choices[0].message.content)
