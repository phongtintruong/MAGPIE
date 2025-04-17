from openai import OpenAI

openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

response = client.completions.create(
    model="Qwen/Qwen2.5-3B-Instruct",
    prompt="<|im_start|>system",
    temperature=0.7,
    max_tokens=512,
    extra_body={"skip_special_tokens": False}
)

print(response)
