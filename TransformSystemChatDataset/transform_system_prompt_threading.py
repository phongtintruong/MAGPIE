import json
import os
import threading
from openai import OpenAI
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


# Load API settings
load_dotenv()
api_base = os.getenv("API_BASE")
model_name = os.getenv("MODEL_NAME")

client = OpenAI(api_key="EMPTY", base_url=api_base)

# Vietnamese meta-prompts
base_system_prompt = """Bạn là một người Việt trẻ thành thạo Tiếng Anh và văn hóa quốc tế.

Bạn muốn văn bản mà chatbot Tiếng Việt của bạn trả lời phải luôn tuân theo System Prompt kỳ lạ, thú vị và phức tạp của bạn. Bạn sẽ dựa vào ví dụ về System Prompt của một chatbot Tiếng Anh để tạo ra một System Prompt phù hợp và khả thi cho Tiếng Việt mà vẫn giữ sự kỳ lạ, thú vị và phức tạp. Giữ giọng văn tự nhiên, không dịch lại từng chữ từ ví dụ Tiếng Anh đó.

Đưa ra suy luận của bạn và kết thúc bằng System Prompt Tiếng Việt được viết một cách tự nhiên bên trong cặp tag <system_prompt></system_prompt>."""

# enhanced_system_prompt = """Bạn là một người Việt trẻ khó tính và sáng tạo một cách điên loạn.

# Bạn muốn mọi thứ phải thật sáng tạo, điên loạn và phức tạp. Bạn thích các điều luật rối rắm, khó hiểu và kỳ lạ. Từ các điều luật cho một chatbot Tiếng Việt của người dùng, bạn sẽ thêm các ràng buộc, điều kiện, luật lệ và quy tắc để làm phức tạp thêm các điều luật đó.

# Đưa ra suy luận của bạn và kết thúc bằng các điều luật Tiếng Việt đã được làm rối rắm và phức tạp hóa bên trong cặp tag <rules></rules>."""

enhanced_system_prompt = """Bạn là một người Việt trẻ khó tính và sáng tạo một cách điên loạn.

Bạn muốn mọi thứ phải thật sáng tạo, điên loạn và phức tạp. Bạn thích các điều luật kỳ lạ và phức tạp. Bạn muốn văn bản mà chatbot Tiếng Việt của bạn trả lời phải luôn tuân theo một System Prompt kỳ lạ, thú vị và phức tạp.

Từ một System Prompt sẵn có, bạn sẽ thêm các thông tin, ràng buộc, điều kiện, luật lệ và quy tắc để làm phức tạp hóa System Prompt đó. Đảm báo System Prompt không liên quan đến các thông tin bên ngoài như thời gian, ngày tháng, địa điểm, tên người dùng, v.v. mà LLMs không thể tự truy cập.

Đưa ra suy luận của bạn và kết thúc bằng System Prompt Tiếng Việt đã được làm phức tạp hóa bên trong cặp tag <system_prompt></system_prompt>."""

slot_system_prompt = """Bạn là một AI/LLM Engineer hiểu rõ cách hoạt động của các LLMs và cách xây dựng các ứng dụng từ LLMs.

Bạn hiểu rằng các LLMs không thể tự truy cập các thông tin bên ngoài. Bạn sẽ định nghĩa các slot để dánh dấu các thông tin bên ngoài trong trường hợp LLMs cần các thông tin đó để tuân thủ System Prompt.

Đưa ra suy luận của bạn và kết thúc bằng các slot bên trong cặp tag <slot></slot>. Ví dụ: "<slot>DATE</slot>\n<slot>TIME</slot>" hoặc "<slot></slot>" nếu không có thông tin bên ngoài nào cần thiết."""

# Paths and settings
input_path = "./data/SystemChat-2.0/ID_SystemChat_filtered_0-499.jsonl"
output_path = "./data/SystemChat-2.0/viID_SystemChat_filtered_0-499.jsonl"
MAX_RETRIES = 3
NUM_ENHANCEMENTS = 1
MAX_WORKERS = 8
SAVE_INTERVAL = 10

# Thread-safe shared output and lock
output_lock = threading.Lock()
output_buffer = []

def extract_tag(response_text, tag):
    try:
        return response_text.split(f'<{tag}>', 1)[-1].split(f'</{tag}>', 1)[0].strip()
    except Exception:
        return None

def call_api_with_retry(messages, sample_id, max_tokens, extracted_tag, stage_desc="initial"):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=messages,
                max_tokens=max_tokens,
                temperature=0.7
            )
            content = response.choices[0].message.content
            # print("-"* 50)
            # print(content)
            # print("-"* 50)
            if f"<{extracted_tag}>" in content and f"</{extracted_tag}>" in content:
                return extract_tag(content, extracted_tag)
            else:
                raise ValueError(f"No <{extracted_tag}> tags in response.")
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
    user_prompt = f'Dựa trên System Prompt của một chatbot Tiếng Anh dưới đây để viết System Prompt phù hợp cho chatbot Tiếng Việt:\n"{system_msg}"'
    messages = [{"role": "system", "content": base_system_prompt},
                {"role": "user", "content": user_prompt}]
    
    new_system_content = call_api_with_retry(messages, sample_id, 512, "system_prompt", "initial")
    if new_system_content is None:
        return None

    # Step 2: Apply enhancements
    for i in range(NUM_ENHANCEMENTS):
        enhancement_user_prompt = f"Hãy làm tăng độ phức tạp cho System Prompt của một chatbot Tiếng Việt sau:\n\"{new_system_content}\""
        enhancement_messages = [
            {"role": "system", "content": enhanced_system_prompt},
            {"role": "user", "content": enhancement_user_prompt}
        ]
        new_system_content = call_api_with_retry(enhancement_messages, sample_id, 1024, "system_prompt", f"enhancement {i+1}")
        if new_system_content is None:
            return None
        
    # # Step 3: Slot extraction
    # slot_system_prompt = f"""Hãy định nghĩa các slot để đánh dấu các thông tin bên ngoài mà LLMs cần để tuân thủ System Prompt sau đây:\n\"{new_system_content}\""""
    # slot_messages = [
    #     {"role": "system", "content": slot_system_prompt},
    #     {"role": "user", "content": slot_system_prompt}
    # ]
    # slot_content = call_api_with_retry(slot_messages, sample_id, 512, "slots", f"slot extraction {i+1}")
    # if slot_content is None:
    #     return None
    # # Step 4: Final system message
    # new_system_content = f"{new_system_content}\n\n{slot_content}"


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

    # for future in as_completed(futures):
    #     result = future.result()
    #     if result:
    #         with output_lock:
    #             output_buffer.append(result)
    #             completed += 1

    #             if completed % SAVE_INTERVAL == 0:
    #                 for item in output_buffer:
    #                     outfile.write(json.dumps(item, ensure_ascii=False) + "\n")
    #                 outfile.flush()
    #                 output_buffer.clear()
    #                 print(f"✅ Saved {completed} processed samples")

    with tqdm(total=len(futures), desc="Processing") as pbar:
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
            pbar.update(1)


    # Save remaining
    if output_buffer:
        for item in output_buffer:
            outfile.write(json.dumps(item, ensure_ascii=False) + "\n")
        print(f"✅ Saved final {len(output_buffer)} samples")

print(f"\n🎉 Done! Output written to: {output_path}")
