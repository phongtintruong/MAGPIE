import json
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API settings
load_dotenv()
api_base = os.getenv("API_BASE")
model_name = os.getenv("MODEL_NAME")

client = OpenAI(api_key="EMPTY", base_url=api_base)

# Vietnamese meta-prompt
base_system_prompt = """Bạn là một người Việt trẻ thành thạo Tiếng Anh và văn hóa quốc tế.

Bạn muốn đặt ra các điều luật kỳ lạ, thú vị và phức tạp cho chatbot Tiếng Việt của mình. Bạn sẽ dựa vào ví dụ về các điều luật của một chatbot Tiếng Anh để tạo ra các điều luật phù hợp và khả thi cho Tiếng Việt mà vẫn giữ sự kỳ lạ, thú vị và phức tạp, không dịch lại từng chữ từ ví dụ Tiếng Anh đó.

Đưa ra suy luận của bạn và kết thúc bằng các điều luật Tiếng Việt được viết một cách tự nhiên bên trong cặp tag <rules></rules>."""

enhanced_system_prompt = """Bạn là một người Việt trẻ khó tính và sáng tạo một cách điên loạn.

Bạn muốn mọi thứ phải thật sáng tạo, điên loạn và phức tạp. Bạn thích các điều luật rối rắm, khó hiểu và kỳ lạ. Từ các điều luật cho một chatbot Tiếng Việt của người dụng, bạn sẽ thêm các ràng buộc, điều kiện, luật lệ và quy tắc để làm phức tạp thêm các điều luật đó.

Đưa ra suy luận của bạn và kết thúc bằng các điều luật Tiếng Việt đã được làm rối rắm và phức tạp hóa bên trong cặp tag <rules></rules>."""

# Input/output paths
input_path = "./data/SystemChat-2.0/test.jsonl"
output_path = "./data/SystemChat-2.0/vitest.jsonl"

# Retry configuration
MAX_RETRIES = 3
NUM_ENHANCEMENTS = 3

# Keep track of processed count
processed_count = 0

with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
    for idx, line in enumerate(infile):
        data = json.loads(line)
        sample_id = data.get("id", f"unknown_{idx}")

        # Find original system message
        system_msg = next((m["content"] for m in data["messages"] if m["role"] == "system"), None)
        if system_msg is None:
            print(f"⚠️ No system message found for ID: {sample_id}")
            continue

        # Compose user prompt using the extracted message
        user_prompt = f"""Dựa trên các điều luật của một chatbot Tiếng Anh dưới đây để viết các luật phù hợp cho chatbot Tiếng Việt:\n\"{system_msg}\""""

        # Construct message list for completion
        messages = [
            {"role": "system", "content": base_system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        # Retry logic
        response_text = None
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                response = client.chat.completions.create(
                    model=model_name,
                    messages=messages,
                    max_tokens=512,
                    temperature=0.7
                )
                response_text = response.choices[0].message.content

                if "<rules>" not in response_text or "</rules>" not in response_text:
                    print(response_text)
                    raise ValueError("Response does not contain <rules> tags")

                break  # Successful
            except Exception as e:
                print(f"⚠️ Attempt {attempt}/{MAX_RETRIES} failed for ID {sample_id}: {e}")
                if attempt >= MAX_RETRIES:
                    print(f"❌ Skipping ID {sample_id} after {MAX_RETRIES} failed attempts.")
                    response_text = None

        if response_text is None:
            continue

        # Extract content between <rules> tags
        new_system_content = response_text.split('<rules>', 1)[-1].split('</rules>', 1)[0].strip()

        for i in range(NUM_ENHANCEMENTS):
            # Construct message list for enhancement
            messages = [
                {"role": "system", "content": enhanced_system_prompt},
                {"role": "user", "content": f"Hãy làm tăng độ phức tạp, rối rắm và điên loạn cho các điều luật của một chatbot Tiếng Việt sau:\n\"{new_system_content}\""}
            ]

            # Retry logic for enhancement
            for attempt in range(1, MAX_RETRIES + 1):
                try:
                    response = client.chat.completions.create(
                        model=model_name,
                        messages=messages,
                        max_tokens=512,
                        temperature=0.7
                    )
                    response_text = response.choices[0].message.content

                    if "<rules>" not in response_text or "</rules>" not in response_text:
                        print(response_text)
                        raise ValueError("Response does not contain <rules> tags")

                    break  # Successful
                except Exception as e:
                    print(f"⚠️ Attempt {attempt}/{MAX_RETRIES} failed for ID {sample_id}: {e}")
                    if attempt >= MAX_RETRIES:
                        print(f"❌ Skipping ID {sample_id} after {MAX_RETRIES} failed attempts.")
                        response_text = None

            if response_text is None:
                print(f"❌ Skipping ID {sample_id} after {MAX_RETRIES} failed attempts for enhancement.")
                break

            # Extract content between <rules> tags
            new_system_content = response_text.split('<rules>', 1)[-1].split('</rules>', 1)[0].strip()

        # Build new sample with the new system message only
        new_data = {
            "id": sample_id,
            "messages": [{"role": "system", "content": new_system_content}]
        }

        # Write to output
        outfile.write(json.dumps(new_data, ensure_ascii=False) + "\n")

        if (idx + 1) % 10 == 0:
            print(f"✅ Processed {idx + 1} samples")

print(f"\n🎉 Done! Output written to: {output_path}")