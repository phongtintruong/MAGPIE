import json
import os
import threading
from openai import OpenAI
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load API settings
load_dotenv()
api_base = os.getenv("API_BASE")
model_name = os.getenv("MODEL_NAME")

client = OpenAI(api_key="EMPTY", base_url=api_base)

# Vietnamese meta-prompts
base_system_prompt = """Bạn là một người Việt trẻ thành thạo Tiếng Anh và văn hóa quốc tế.

Bạn muốn đặt ra các điều luật kỳ lạ, thú vị và phức tạp cho chatbot Tiếng Việt của mình. Bạn sẽ dựa vào ví dụ về các điều luật của một chatbot Tiếng Anh để tạo ra các điều luật phù hợp và khả thi cho Tiếng Việt mà vẫn giữ sự kỳ lạ, thú vị và phức tạp, không dịch lại từng chữ từ ví dụ Tiếng Anh đó.

Đưa ra suy luận của bạn và kết thúc bằng các điều luật Tiếng Việt được viết một cách tự nhiên bên trong cặp tag <rules></rules>."""

# enhanced_system_prompt = """Bạn là một người Việt trẻ khó tính và sáng tạo một cách điên loạn.

# Bạn muốn mọi thứ phải thật sáng tạo, điên loạn và phức tạp. Bạn thích các điều luật rối rắm, khó hiểu và kỳ lạ. Từ các điều luật cho một chatbot Tiếng Việt của người dùng, bạn sẽ thêm các ràng buộc, điều kiện, luật lệ và quy tắc để làm phức tạp thêm các điều luật đó.

# Đưa ra suy luận của bạn và kết thúc bằng các điều luật Tiếng Việt đã được làm rối rắm và phức tạp hóa bên trong cặp tag <rules></rules>."""

enhanced_system_prompt = """Bạn là một người Việt trẻ khó tính và sáng tạo một cách điên loạn.

Bạn muốn mọi thứ phải thật sáng tạo, điên loạn và phức tạp. Bạn thích các điều luật kỳ lạ và phức tạp. Từ các điều luật cho một chatbot Tiếng Việt của người dùng, bạn sẽ thêm các ràng buộc, điều kiện, luật lệ và quy tắc để làm phức tạp thêm các điều luật đó.

Đưa ra suy luận của bạn và kết thúc bằng các điều luật Tiếng Việt đã được làm rối rắm và phức tạp hóa bên trong cặp tag <rules></rules>."""

# Paths and settings
input_path = "./data/SystemChat-2.0/test.jsonl"
output_path = "./data/SystemChat-2.0/vitest.jsonl"
MAX_RETRIES = 3
NUM_ENHANCEMENTS = 1
MAX_WORKERS = 5
SAVE_INTERVAL = 1

# Thread-safe shared output and lock
output_lock = threading.Lock()
output_buffer = []

def extract_rules(response_text):
    try:
        return response_text.split('<rules>', 1)[-1].split('</rules>', 1)[0].strip()
    except Exception:
        return None

def call_api_with_retry(messages, sample_id, max_tokens, stage_desc="initial"):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=messages,
                max_tokens=max_tokens,
                temperature=0.7
            )
            content = response.choices[0].message.content
            if "<rules>" in content and "</rules>" in content:
                return extract_rules(content)
            else:
                raise ValueError("No <rules> tags in response.")
        except Exception as e:
            print(f"⚠️ Retry {attempt}/{MAX_RETRIES} for {sample_id} [{stage_desc}]: {e}")
            if attempt == MAX_RETRIES:
                print(f"❌ Failed after {MAX_RETRIES} retries: {sample_id}")
    return None

def process_sample(idx, data):
    sample_id = data.get("id", f"unknown_{idx}")
    system_msg = next((m["content"] for m in data["messages"] if m["role"] == "system"), None)
    if not system_msg:
        print(f"⚠️ No system message for ID: {sample_id}")
        return None

    # Step 1: Generate Vietnamese version from English rule
    user_prompt = f'Dựa trên các điều luật của một chatbot Tiếng Anh dưới đây để viết các luật phù hợp cho chatbot Tiếng Việt:\n"{system_msg}"'
    messages = [{"role": "system", "content": base_system_prompt},
                {"role": "user", "content": user_prompt}]
    
    new_system_content = call_api_with_retry(messages, sample_id, 512, "initial")
    if new_system_content is None:
        return None

    # Step 2: Apply enhancements
    for i in range(NUM_ENHANCEMENTS):
        enhancement_user_prompt = f"Hãy làm tăng độ phức tạp và điên loạn cho các điều luật của một chatbot Tiếng Việt sau:\n\"{new_system_content}\""
        enhancement_messages = [
            {"role": "system", "content": enhanced_system_prompt},
            {"role": "user", "content": enhancement_user_prompt}
        ]
        new_system_content = call_api_with_retry(enhancement_messages, sample_id, 1024, f"enhancement {i+1}")
        if new_system_content is None:
            return None

    return {
        "id": sample_id,
        "messages": [{"role": "system", "content": new_system_content}]
    }

# Read input
with open(input_path, "r", encoding="utf-8") as f:
    dataset = [json.loads(line) for line in f]

# Process in parallel
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor, open(output_path, "w", encoding="utf-8") as outfile:
    futures = {executor.submit(process_sample, idx, data): idx for idx, data in enumerate(dataset)}
    completed = 0

    for future in as_completed(futures):
        result = future.result()
        if result:
            with output_lock:
                output_buffer.append(result)
                completed += 1

                if completed % SAVE_INTERVAL == 0:
                    for item in output_buffer:
                        outfile.write(json.dumps(item, ensure_ascii=False) + "\n")
                    outfile.flush()
                    output_buffer.clear()
                    print(f"✅ Saved {completed} processed samples")

    # Save remaining
    if output_buffer:
        for item in output_buffer:
            outfile.write(json.dumps(item, ensure_ascii=False) + "\n")
        print(f"✅ Saved final {len(output_buffer)} samples")

print(f"\n🎉 Done! Output written to: {output_path}")
