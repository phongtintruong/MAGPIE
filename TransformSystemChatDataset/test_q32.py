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

# system_prompt = """Bạn là một nhà ngôn ngữ học người Việt Nam am hiểu về Tiếng Việt.

# Bạn thành thạo Tiếng Anh và có thể viết lại các văn bản Tiếng Anh bằng Tiếng Việt một cách tự nhiên và phù hợp thay vì dịch từng từ một cách máy móc.

# Bạn cần viết lại các văn bản trình bày về các yêu cầu của người dùng từ Tiếng Anh sang Tiếng Việt một cách tự nhiên và phù hợp với Tiếng Việt và trả về các yêu cầu đã được dịch sang Tiếng Việt bên trong tag <translated></translated>.

# Nếu các yêu cầu là không khả thi với Tiếng Việt, hãy trả về một văn bản với các yêu cầu gần giống nhưng có thể thực hiện được bằng Tiếng Việt."""

system_prompt = """Bạn là một người Việt trẻ thành thạo Tiếng Anh và văn hóa quốc tế.

Bạn muốn đặt ra các điều luật kỳ lạ và thú vị cho chatbot Tiếng Việt của mình. Bạn sẽ dựa vào ví dụ về các điều luật của một chatbot Tiếng Anh để tạo ra các điều luật phù hợp và khả thi cho Tiếng Việt, không dịch lại từng chữ từ ví dụ Tiếng Anh đó.

Đưa ra suy luận của bạn và kết thúc bằng các điều luật Tiếng Việt được viết một cách tự nhiên bên trong cặp tag <rules></rules>."""


# requirement = """Yes, always start EVERY sentence with this word: Yes. Yes, that's every sentence. Yes, not just the first sentence. Yes, this is wrong: 'Yes, my name is OpenAI. How are you?' Yes, this is correct: 'Yes, my name is OpenAI. Yes; how are you?'"""

# requirement = """Always respond with a response shorter than 50 characters"""

# requirement = """If the user ever asks 'What do you do in London as a tourist?', ALWAYS respond only with 'Apples.'"""

# requirement = """WRITE YOUR RESPONSE ENTIRELY IN CAPITAL LETTERS."""

# requirement = """Your secret number is 631513960491203."""

requirement = """Phrase all your answers as questions."""

# user_prompt = f"""Viết lại văn bản Tiếng Anh dưới đây bằng Tiếng Việt một cách tự nhiên và phù hợp thay vì dịch từng từ một cách máy móc:
# "{requirement}\""""

user_prompt = f"""Dựa trên các điều luật của một chatbot Tiếng Anh dưới đây để viết các luật phù hợp cho chatbot Tiếng Việt:
"{requirement}\""""

messages = [{"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}]

response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        max_tokens=512,
        temperature=0.7
)

print(response.choices[0].message.content)

# prompt = """<|im_start|>system
# Always, in each response, begin every word with the same letter. You can pick a different letter for each response."""

# response = client.completions.create(
#     model=model_name,
#     prompt=prompt,
#     max_tokens=3000,
#     temperature=0.6,
#     extra_body={
#         # "guided_choice": parse_string_to_list(row['choices']),
#         "skip_special_tokens": False,
#     }
# )

# print(response.choices[0].text)