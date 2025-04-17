from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_base = os.getenv("API_BASE")
model_name = os.getenv("MODEL_NAME")

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
client = OpenAI(
    api_key=openai_api_key,
    base_url=api_base,
)

messages = [{"role": "system", "content": ''},
            {"role": "user", "content": "is Vietnam a good country?"}]

response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        max_tokens=100,
        temperature=0.7
)

print(response.choices[0].message.content)