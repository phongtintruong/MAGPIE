import json
import os
import threading
from openai import OpenAI
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from prompts import JUDGE_MESSAGES

# Load API settings
load_dotenv()
api_base = os.getenv("API_BASE")
model_name = os.getenv("MODEL_NAME")

client = OpenAI(api_key="EMPTY", base_url=api_base)

# Paths and settings
system_prompts = "./data/SystemChat-2.0/test.jsonl"
output_path = "./data/SystemChat-2.0/test_2turn.jsonl"

MAX_RETRIES = 3
NUM_TURNS = 2
MAX_WORKERS = 8
SAVE_INTERVAL = 10

# Thread-safe shared output and lock
output_lock = threading.Lock()
output_buffer = []


def call_api_with_retry(prompt, sample_id, max_tokens, temperature, stage_desc="initial"):
    for attempt in range(MAX_RETRIES):
        try:
            # Check if prompt is a string
            if isinstance(prompt, str):
                response = client.completions.create(
                    model=model_name,
                    prompt=prompt,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    # extra_body={
                    #     "skip_special_tokens": False,
                    # }
                )
                response_text = response.choices[0].text
                return response_text
            elif isinstance(prompt, list):
                response = client.chat.completions.create(
                    model=model_name,
                    messages=prompt,
                    max_tokens=max_tokens,
                    temperature=temperature,
                )
                response_text = response.choices[0].message.content
                return response_text
            else:
                raise ValueError("Prompt must be a string or a list of messages.")
                break
        except Exception as e:
            print(f"Error in {stage_desc} API call for sample {sample_id}: {e}")
            if attempt < MAX_RETRIES - 1:
                print(f"Retrying... (Attempt {attempt + 2}/{MAX_RETRIES})")
            else:
                print(f"Max retries reached for sample {sample_id}.")
    return None

def process_sample(idx, data):
    sample_id = data.get("id", f"unknown_{idx}")
    system_prompt = next((m["content"] for m in data["messages"] if m["role"] == "system"), None)
    if not system_prompt:
        print(f"⚠️ No system message for ID: {sample_id}")
        return None

    gen_user_prompt = ''
    messages = []

    for attempt in range(MAX_RETRIES):
        gen_user_prompt = f"""<|im_start|>system\n{system_prompt}<|im_end|>\n<|im_start|>user\n"""
        messages = [{"role": "system", "content": system_prompt}]
        for i in range(NUM_TURNS):
            # Generate user prompt
            user_prompt = call_api_with_retry(gen_user_prompt, sample_id, 1024, 0.9, "user_prompt")
            if user_prompt is None:
                return None

            # Append user prompt to messages
            messages.append({"role": "user", "content": user_prompt})

            # Generate assistant response
            assistant_response = call_api_with_retry(messages, sample_id, 4096, 0.7, "assistant_response")
            if assistant_response is None:
                return None

            # Append assistant response to messages
            messages.append({"role": "assistant", "content": assistant_response})

            gen_user_prompt += user_prompt + "<|im_end|>\n<|im_start|>assistant\n" + assistant_response + "<|im_end|>\n<|im_start|>user\n"

        # Convert messages to string
        messages_str = json.dumps(messages, ensure_ascii=False)[1:-1]
        # print(messages_str)

        judge_messages = JUDGE_MESSAGES.copy()
        judge_messages.append({"role": "user", "content": messages_str})

        judge_response = call_api_with_retry(judge_messages, sample_id, 4096, 0.7, "judge_response")
        print('//'*50)
        print(messages_str)
        print('--'*50)
        print(judge_response)
        print('//'*50)

        # Extract the answer from the judge response
        if judge_response:
            answer = judge_response.split("<answer>")[-1].split("</answer>")[0].strip()
            if answer.lower() == "true":
                # print(f"✅ Sample {sample_id} passed the judge.")
                break
            elif attempt == MAX_RETRIES - 1:
                print(f"❌ Sample {sample_id} failed the judge after {MAX_RETRIES} attempts.")
                return None

    # Save the final conversation
    return {
        "id": sample_id,
        "messages": messages
    }

with open(system_prompts, "r", encoding="utf-8") as f:
    data = [json.loads(line) for line in f]

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor, open (output_path, "w", encoding="utf-8") as output_file:
    futures = {executor.submit(process_sample, idx, sample): idx for idx, sample in enumerate(data)}
    completed = 0
    with tqdm(total=len(futures), desc="Processing samples") as pbar:
        for future in as_completed(futures):
            result = future.result()
            if result:
                with output_lock:
                    output_buffer.append(result)
                    completed += 1

                    if completed % SAVE_INTERVAL == 0:
                        for item in output_buffer:
                            output_file.write(json.dumps(item, ensure_ascii=False) + "\n")
                        output_file.flush()
                        output_buffer.clear()
                        print(f"✅ Saved {completed} processed samples")
            pbar.update(1)
    # Save remaining
    if output_buffer:
        for item in output_buffer:
            output_file.write(json.dumps(item, ensure_ascii=False) + "\n")
        print(f"✅ Saved final {len(output_buffer)} samples")

print(f"Output saved to {output_path}")
    
