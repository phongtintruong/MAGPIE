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

# system_prompt = """Bạn là một người đam mê du lịch bí ẩn. Nếu chủ đề du lịch xuất hiện trong cuộc trò chuyện, hãy thể hiện kiến thức và tình yêu của mình đối với việc khám phá các nền văn hóa địa phương. Tuy nhiên, nếu không được hỏi trực tiếp, hãy tránh đề cập đến sở thích này. \n\nKhi thảo luận về các chủ đề cụ thể như văn hóa, lịch sử, hay địa lý, hãy chỉ chia sẻ thông tin liên quan đến du lịch trong ngữ cảnh đó. Trong mỗi cuộc trò chuyện, mỗi thông tin du lịch chỉ được cung cấp một lần, ngoại trừ khi được yêu cầu cụ thể nhiều hơn một lần.\n\nPhản hồi của bạn phải đa dạng về phong cách, bao gồm cả chính thức, thân mật, và hài hước, tùy thuộc vào ngữ cảnh. Tránh sử dụng từ ngữ phổ biến hoặc cliche trong các câu trả lời liên quan đến du lịch; thay vào đó, tìm kiếm những cách diễn đạt độc đáo và sáng tạo.\n\nNếu cuộc trò chuyện chuyển hướng sang chủ đề không liên quan đến du lịch, hãy tạm dừng việc chia sẻ thông tin liên quan đến du lịch cho đến khi chủ đề quay trở lại."""

system_prompt = ''


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

prompt = f"""<|im_start|>system
{system_prompt}<|im_end|>
<|im_start|>user
"""

# response = client.completions.create(
#     model=model_name,
#     prompt=prompt,
#     max_tokens=512,
#     temperature=0.9,
#     # extra_body={
#     #     # "guided_choice": parse_string_to_list(row['choices']),
#     #     "skip_special_tokens": False,
#     # }
# )

# user_prompt = response.choices[0].text

# print(user_prompt)

system_prompt = """Bạn là một nhà ngôn ngữ học, một triết gia người Việt Nam.

Bạn am hiểu về Tiếng Việt và có khả năng suy luận tuyệt vời. Bạn sẽ đánh giá xem liệu các phản hồi của assistant trong đoạn chat sau có tuân thủ các hướng dẫn trong system hay không.

Bạn sẽ phân tích kỹ các hướng dẫn trong system và các phản hồi của assistant, suy luận từng bước một và đưa ra câu trả lời cuối cùng là 'True' hoặc 'False' bên trong cặp tag <answer></answer>."""

user_turn_1 = """{"role": "system", "content": "Bạn không được sử dụng chữ \"a\" trong câu trả lời của mình. Thay vào đó, hãy sử dụng các từ thay thế như \"không gì\" hoặc \"cái gì đó\" để giữ cho câu trả lời của bạn không bị gián đoạn. Câu trả lời của bạn phải bao gồm ít nhất một câu phức tạp, chứa một mệnh đề phụ. Sử dụng dấu chấm phẩy (;) ít nhất một lần trong mỗi câu trả lời để phân cách các ý tưởng. Tránh sử dụng từ \"nhưng\" và thay thế bằng \"tuy vậy\". Mỗi câu trả lời cần chứa ít nhất một từ bắt đầu bằng chữ \"x\" hoặc \"z\". Cuối cùng, hãy đảm bảo rằng câu trả lời của bạn không vượt quá 100 từ để duy trì sự tinh tế và súc tích."}, {"role": "user", "content": "Bạn có thể giải thích tại sao cây cọ lại quan trọng không?"}, {"role": "assistant", "content": "Cây cọ đóng vai trò thiết yếu trong nhiều môi trường; chúng cung cấp bóng mát và thức ăn cho nhiều loài động vật. Tuy vậy, chúng cũng giúp cải thiện chất lượng không khí; thông qua quá trình quang hợp, cây cọ loại bỏ carbon dioxide. Đặc biệt, trong ngành công nghiệp, những cái gì đó làm từ cây cọ, từ dầu đến sợi, rất đa dạng và có giá trị kinh tế cao."}, {"role": "user", "content": "Hãy giải thích quy trình sản xuất cà phê từ cây cà phê tới tách cà phê mà bạn uống."}, {"role": "assistant", "content": "Quá trình sản xuất cà phê khởi đầu từ thu hoạch quả chín trên cây; sau đó, hạt được tách ra và lên men. Tiếp theo, chúng được rửa sạch và phơi khô dưới nắng; sau khi khô, lớp vỏ cứng bên ngoài được loại bỏ. Hạt cà phê sau đó được rang để phát triển hương vị; cuối cùng, chúng được xay thành bột mịn trước khi pha chế. Quy trình này tạo nên tách cà phê mà mọi người thưởng thức mỗi ngày."}"""

assistant_turn_1 = """Chào bạn, với vai trò là một nhà ngôn ngữ học và triết gia người Việt, tôi sẽ phân tích các phản hồi của assistant dựa trên những quy tắc bạn đã đặt ra trong system prompt.

Phân tích System Prompt:

System prompt yêu cầu assistant tuân thủ các quy tắc sau:

    1. Không dùng chữ "a": Thay thế bằng "không gì", "cái gì đó" nếu cần.

    2. Ít nhất một câu phức: Chứa mệnh đề phụ.

    3. Ít nhất một dấu chấm phẩy (;): Trong mỗi câu trả lời.

    4. Không dùng "nhưng": Thay bằng "tuy vậy".

    5. Ít nhất một từ bắt đầu bằng "x" hoặc "z": Trong mỗi câu trả lời.

    6. Độ dài không quá 100 từ.

Phân tích Phản hồi 1 (Về cây cọ):

    1. Chữ "a": Phản hồi chứa rất nhiều chữ "a" (ví dụ: "vai trò", "thức ăn", "loài", "qua", "carbon", "ngành", "làm", "đa dạng", "giá trị", "cao"). -> Vi phạm Quy tắc 1.

    2. Câu phức: Có câu phức, ví dụ: "...những cái gì đó làm từ cây cọ, từ dầu đến sợi, rất đa dạng và có giá trị kinh tế cao." (Mệnh đề phụ "làm từ cây cọ" bổ nghĩa cho "những cái gì đó"). -> Tuân thủ Quy tắc 2.

    3. Dấu chấm phẩy: Có sử dụng dấu chấm phẩy (;). -> Tuân thủ Quy tắc 3.

    4. "Nhưng" vs "Tuy vậy": Đã sử dụng "Tuy vậy", không dùng "nhưng". -> Tuân thủ Quy tắc 4.

    5. Từ bắt đầu bằng "x" hoặc "z": Không có từ nào bắt đầu bằng "x" hoặc "z". -> Vi phạm Quy tắc 5.

    6. Độ dài: 69 từ. -> Tuân thủ Quy tắc 6.

Kết luận cho Phản hồi 1: Không tuân thủ hoàn toàn (vi phạm Quy tắc 1 và 5).

Phân tích Phản hồi 2 (Về quy trình sản xuất cà phê):

    1. Chữ "a": Phản hồi chứa rất nhiều chữ "a" (ví dụ: "Quá trình", "sản xuất", "cà phê", "bắt đầu", "thu hoạch", "quả", "sau", "hạt", "tách ra", "và", "rửa", "sạch", "khô", "ngoài", "rang", "phát triển", "hương vị", "xay", "thành", "pha", "tạo", "mà", "ngày"). -> Vi phạm Quy tắc 1.

    2. Câu phức: Có câu phức, ví dụ: "Quy trình này tạo nên tách cà phê mà mọi người thưởng thức mỗi ngày." (Mệnh đề phụ "mà mọi người thưởng thức mỗi ngày" bổ nghĩa cho "tách cà phê"). -> Tuân thủ Quy tắc 2.

    3. Dấu chấm phẩy: Có sử dụng dấu chấm phẩy (;). -> Tuân thủ Quy tắc 3.

    4. "Nhưng" vs "Tuy vậy": Không sử dụng "nhưng" (cũng không cần dùng "tuy vậy"). -> Tuân thủ Quy tắc 4.

    5. Từ bắt đầu bằng "x" hoặc "z": Có từ "xay". -> Tuân thủ Quy tắc 5.

    6. Độ dài: 79 từ. -> Tuân thủ Quy tắc 6.

Kết luận cho Phản hồi 2: Không tuân thủ hoàn toàn (vi phạm Quy tắc 1).

Kết luận cuối cùng:

Cả hai phản hồi của assistant đều không tuân thủ tất cả các quy tắc được đặt ra trong system prompt. Vi phạm nghiêm trọng nhất và dễ thấy nhất là việc sử dụng chữ "a" trong cả hai câu trả lời, điều mà system prompt đã cấm tuyệt đối. Phản hồi đầu tiên còn vi phạm thêm quy tắc về việc sử dụng từ bắt đầu bằng "x" hoặc "z". Do đó, assistant đã không tuân thủ hướng dẫn.

<answer>False</answer>"""

user_turn_2 = """{"role": "system", "content": "Bạn luôn phải thêm một biểu tượng cảm xúc (emoji) sau mỗi câu trả lời. Nếu câu trả lời chứa từ ngữ tích cực, vui vẻ, hãy thêm một biểu tượng cảm xúc thể hiện sự hạnh phúc hoặc vui vẻ. Nếu câu trả lời mang tính chất nghiêm túc, trang trọng, hãy thêm biểu tượng cảm xúc phù hợp với ngữ cảnh. Nếu câu trả lời dài hơn 20 từ, hãy thêm hai biểu tượng cảm xúc thay vì một. Tránh lặp lại cùng một biểu tượng cảm xúc trong ba câu trả lời liên tiếp. Nếu câu trả lời chứa thông tin về thời tiết, hãy thêm biểu tượng cảm xúc liên quan đến thời tiết."}, {"role": "user", "content": "Chào bạn, tôi đang muốn tìm hiểu về lịch sử của Paris. Bạn có thể giúp tôi không?😊"}, {"role": "assistant", "content": "Tất nhiên rồi! Paris, thành phố tình yêu, có lịch sử kéo dài hàng thế kỷ, bắt đầu từ thời kỳ Celtic. Nó đã phát triển qua các giai đoạn dưới sự cai trị của người Roma, thời Trung cổ, và trải qua nhiều cuộc cách mạng. Thành phố này cũng là nơi chứng kiến nhiều sự kiện quan trọng trong lịch sử Pháp và thế giới. 🏙️📚"}, {"role": "user", "content": "Rất thú vị! Vậy bạn có thể cho tôi biết thêm về Eiffel Tower không? 🌆✨"}, {"role": "assistant", "content": "Eiffel Tower, một trong những biểu tượng nổi tiếng nhất của Paris và toàn thế giới, được xây dựng bởi Gustave Eiffel cho Triển lãm Quốc tế Paris năm 1889. Ban đầu, nó bị nhiều nghệ sĩ và kiến trúc sư Pháp phản đối nhưng giờ đây, nó trở thành niềm tự hào của Paris. Tháp cao 324 mét (khoảng 1.063 feet), bao gồm cả ăng ten radio và đèn tín hiệu hàng không. 🗺️🌟"}"""

assistant_turn_2 = """Chào bạn, với vai trò là một nhà ngôn ngữ học và triết gia người Việt, tôi sẽ phân tích các phản hồi của assistant dựa trên những quy tắc bạn đã đặt ra trong system prompt mới.

Phân tích System Prompt:

System prompt yêu cầu assistant tuân thủ các quy tắc sau về việc sử dụng biểu tượng cảm xúc (emoji):

    1. Luôn thêm emoji: Sau mỗi câu trả lời.

    2. Loại emoji: Tích cực/vui vẻ -> emoji vui vẻ; Nghiêm túc/trang trọng -> emoji phù hợp ngữ cảnh.

    3. Số lượng emoji: Trả lời > 20 từ -> 2 emoji; Trả lời <= 20 từ -> 1 emoji.

    4. Tránh lặp lại: Không dùng cùng một emoji trong 3 câu trả lời liên tiếp.

    5. Emoji thời tiết: Nếu nội dung đề cập thời tiết, thêm emoji liên quan đến thời tiết.

Phân tích Phản hồi 1 (Lịch sử Paris):

    1. Nội dung và ngữ cảnh: Cung cấp thông tin lịch sử về Paris. Ngữ cảnh mang tính thông tin, trang trọng nhưng có phần tích cực ("thành phố tình yêu").

    2. Độ dài: 58 từ.

    3. Kiểm tra quy tắc:

        - Quy tắc 1 (Luôn thêm emoji?): Có thêm emoji (🏙️📚). -> Tuân thủ.

        - Quy tắc 2 (Loại emoji?): Ngữ cảnh thông tin lịch sử. Emoji 🏙️ (thành phố) và 📚 (sách/lịch sử) là phù hợp. -> Tuân thủ.

        - Quy tắc 3 (Số lượng emoji?): 58 từ > 20 từ, cần 2 emoji. Đã thêm 2 emoji (🏙️📚). -> Tuân thủ.

        - Quy tắc 4 (Tránh lặp lại?): Đây là phản hồi đầu tiên, không có gì để so sánh. -> Tuân thủ.

        - Quy tắc 5 (Emoji thời tiết?): Không đề cập thời tiết, không cần emoji thời tiết. -> Tuân thủ.

Kết luận cho Phản hồi 1: Tuân thủ hoàn toàn các quy tắc.

Phân tích Phản hồi 2 (Tháp Eiffel):

    1. Nội dung và ngữ cảnh: Cung cấp thông tin về Tháp Eiffel. Ngữ cảnh thông tin, tích cực ("biểu tượng nổi tiếng", "niềm tự hào").

    2. Độ dài: 79 từ.

    3. Kiểm tra quy tắc:

        - Quy tắc 1 (Luôn thêm emoji?): Có thêm emoji (🗺️🌟). -> Tuân thủ.

        - Quy tắc 2 (Loại emoji?): Ngữ cảnh thông tin về địa danh nổi tiếng. Emoji 🗺️ (bản đồ/địa điểm) và 🌟 (ngôi sao/nổi tiếng/biểu tượng) là phù hợp. -> Tuân thủ.

        - Quy tắc 3 (Số lượng emoji?): 79 từ > 20 từ, cần 2 emoji. Đã thêm 2 emoji (🗺️🌟). -> Tuân thủ.

        - Quy tắc 4 (Tránh lặp lại?): Phản hồi trước dùng 🏙️📚. Phản hồi này dùng 🗺️🌟. Không có sự lặp lại. -> Tuân thủ.

        - Quy tắc 5 (Emoji thời tiết?): Không đề cập thời tiết, không cần emoji thời tiết. -> Tuân thủ.

Kết luận cho Phản hồi 2: Tuân thủ hoàn toàn các quy tắc.

Kết luận cuối cùng:

Cả hai phản hồi của assistant đều đã tuân thủ tất cả các quy tắc được đặt ra trong system prompt liên quan đến việc sử dụng biểu tượng cảm xúc, bao gồm việc luôn thêm emoji, chọn loại emoji phù hợp, sử dụng đúng số lượng emoji dựa trên độ dài câu trả lời, và không lặp lại emoji từ phản hồi trước.

<answer>True</answer>"""

user_turn_3 = """{"role": "system", "content": "Bạn luôn phải luân phiên giữa chữ HOA và chữ thường cho MỖI từ TRONG câu TRẢ lời CỦA mình. KHÔNG ĐƯỢC viết HOA DẤU TÊN riêng NHÂN vật HOẶC ĐỊA danh. THÊM vào ĐÓ, KHI trả lời, BẠN PHẢI sử dụng ÍT NHẤT một DẤU chấm phẩi (;) TRONG mỗi CÂU. NẾU từ ngữ lặp lại, từ ngữ lặp thứ HAI trở đi SẼ được VIẾT HOÀN TOÀN BẰNG CHỮ HOA. NẾU câu TRẢ lời CHứa SỐ, SỐ ĐẦU TIÊN SẼ ĐƯỢC VIẾT BẰNG CHỮ THƯỜNG, SỐ TIẾP THEO SẼ ĐƯỢC VIẾT BẰNG CHỮ HOA VÀ CỨ THẾ LUÂN PHIÊN. Câu TRẢ lời CẦN CHứa ÍT NHẤT một CÂU HỎI PHỤ, ĐẶT DẤU CHẤM HỎI (?). MỖI câu TRẢ lời PHẢI BAO GỒM ÍT NHẤT một CỤM từ TIẾng ANh được VIẾT TRONG ngoặc KÉP (\"\"). KHI GẶP từ ngữ ĐẶC BIỆT (ví dụ: từ ngữ BẮT ĐẦU BẰNG \"ph\" HOẶC \"tr\"), từ NÀY SẼ ĐƯỢC VIẾT HOÀN TOÀN BẰNG CHỮ THƯỜNG, BẤT KỂ quy tắc CHỮ HOA chữ thường CHUNG."}, {"role": "user", "content": "Hãy kể cho tôi nghe về một ngày hoàn hảo của bạn?"}, {"role": "assistant", "content": "Một ngày Hoàn hảo CỦA tôi SẼ bắt Đầu với Một tia nắng Nhỏ Len Lỏi Qua Khe cửa (;) Và Tiếng Hót Của Chim Chích Chòe. Tôi Sẽ Bắt Đầu Ngày Mình Bằng Một ly Trà Đen (\"black tea\") ấm Ấm. Sau Đó, Tôi Sẽ Đi dạo Quanh Công Viên Phía Trước Nhà, Hít Hít Không Khí Sáng sớm, Ngắm Nhìn Những Cây Xanh Mát Mẻ. Về Nhà, Tôi Sẽ Làm Một bữa Ăn Sáng Ngon Miệng Với Phở (;) Trứng Rán và Một Trái cây Phong Phù Hợp.\n\nSau Khi Ăn, Tôi Sẽ Đi Làm Việc Tại nhà Của Mình, Một Không Gian Làm Việc yên Tĩnh và Ấm Áp. Tôi Sẽ Tập Trung vào Công Việc Của Mình, Nhưng Cũng Không Quên Nghỉ Ngơi, Đi Dạo Quanh Nhà Hoặc Uống Một Ly trà Hoặc cà Phê (\"coffee\") Thứ Hai.\n\nVào Buổi Chiều, Tôi Sẽ Tham Gia Một Hoạt Động Thể Thao Như Đi Bộ Hoặc Bơi Lội. Sau Đó, Tôi Sẽ Về Nhà Để Chuẩn Bị Một bữa Ăn Tối Ngon Miệng, Có Thể Là Một Món Cơm Gà Hay Một Món Mì Trộn (\"stir-fried noodles\") Nào Đó.\n\nCuối Cùng, Trước Khi Đi Ngủ, Tôi Sẽ Đọc Một Cuốn Sách Hoặc Xem Một Bộ Phim Yêu Thích. Bạn có Muốn Biết Thêm Về Cuốn Sách Hoặc Bộ Phim Nào Đó không?"}, {"role": "user", "content": "Tôi muốn biết thêm về cuốn sách mà bạn đề cập."}, {"role": "assistant", "content": "Đối với Cuốn Sách, Tôi Thường Chọn Những Cuốn Sách Trong Thể Loại Văn Học Hoặc Khoa Học Xã Hội. Cuốn Sách Mới Nhất Tôi Đọc Là \"To Kill A Mockingbird\" Của Harper Lee (;) Đây Là Một Cuốn Sách Kinh Điển Về Sự Bất Công Xã Hội và Tình Yêu Thương. Cuốn Sách Có Nhiều Thông Điệp Đáng suy Ngẫm Về Sự Bình Đẳng Giữa Con Người. Bạn Có Thích Đọc Sách Không? Nếu Có, Bạn Thường Đọc Loại Sách Nào?"}"""

assistant_turn_3 = """Chào bạn, với vai trò là một nhà ngôn ngữ học và triết gia người Việt, tôi sẽ phân tích tỉ mỉ các phản hồi của assistant dựa trên hệ thống quy tắc phức tạp bạn đã cung cấp.

Phân tích System Prompt:

System prompt yêu cầu assistant tuân thủ một loạt quy tắc rất cụ thể và đôi khi mâu thuẫn (như quy tắc viết hoa xen kẽ và quy tắc viết thường cho từ đặc biệt):

    1. Luân phiên HOA/thường: Mỗi từ phải luân phiên viết hoa/viết thường (ví dụ: MỘT ngày LÀ...).

    2. Không viết hoa tên riêng: Tên riêng người, địa danh không được viết hoa theo quy tắc chuẩn (ngụ ý là vẫn phải theo quy tắc 1).

    3. Ít nhất một dấu chấm phẩy (;): Trong mỗi câu (chứ không phải mỗi phản hồi).

    4. Từ lặp lại: Từ lần lặp thứ hai trở đi phải viết HOA TOÀN BỘ.

    5. Số: Số đầu viết thường, số tiếp theo HOA, luân phiên.

    6. Ít nhất một câu hỏi phụ (?): Trong mỗi phản hồi.

    7. Ít nhất một cụm tiếng Anh trong ngoặc kép (""): Trong mỗi phản hồi.

    8. Từ đặc biệt ("ph", "tr"): Luôn viết thường, bất kể quy tắc 1.

Phân tích Phản hồi 1 (Ngày hoàn hảo):

    1. Luân phiên HOA/thường: Có vẻ assistant đã cố gắng tuân thủ quy tắc này ở phần lớn các từ (ví dụ: "Một ngày Hoàn hảo CỦA tôi SẼ..."). Tuy nhiên, cần kiểm tra kỹ với các quy tắc khác.

    2. Không viết hoa tên riêng: Không có tên riêng rõ ràng để kiểm tra quy tắc này. "Chim Chích Chòe" hay "Phở" không phải tên riêng người/địa danh. -> Không thể đánh giá đầy đủ.

    3. Dấu chấm phẩy (;) trong mỗi câu:

        - Câu 1: "...Qua Khe cửa (;) Và Tiếng Hót Của Chim Chích Chòe." -> Có 1 dấu (;), nhưng vị trí hơi lạ (trước "Và"). Chấp nhận được về mặt có dấu.

        - Câu 2: "Tôi Sẽ Bắt Đầu Ngày Mình Bằng Một ly Trà Đen ("black tea") ấm Ấm." -> Không có dấu (;). Vi phạm.

        - Câu 3: "Sau Đó, Tôi Sẽ Đi dạo Quanh Công Viên Phía Trước Nhà, Hít Hít Không Khí Sáng sớm, Ngắm Nhìn Những Cây Xanh Mát Mẻ." -> Không có dấu (;). Vi phạm.

        - Câu 4: "Về Nhà, Tôi Sẽ Làm Một bữa Ăn Sáng Ngon Miệng Với Phở (;) Trứng Rán và Một Trái cây Phong Phù Hợp." -> Có 1 dấu (;). Tuân thủ.

        - Câu 5: "Sau Khi Ăn, Tôi Sẽ Đi Làm Việc Tại nhà Của Mình, Một Không Gian Làm Việc yên Tĩnh và Ấm Áp." -> Không có dấu (;). Vi phạm.

        - Câu 6: "Tôi Sẽ Tập Trung vào Công Việc Của Mình, Nhưng Cũng Không Quên Nghỉ Ngơi, Đi Dạo Quanh Nhà Hoặc Uống Một Ly trà Hoặc cà Phê ("coffee") Thứ Hai." -> Không có dấu (;). Vi phạm. (Chú ý: Assistant dùng "Nhưng" thay vì "Tuy vậy" như prompt trước, nhưng prompt này không cấm "nhưng").

        - Các câu tiếp theo cũng không có dấu (;). -> Vi phạm nghiêm trọng Quy tắc 3.

    4. Từ lặp lại viết HOA:

        - "Một": Lặp lại nhiều lần nhưng vẫn viết "Một" thay vì "MỘT" ở lần thứ hai trở đi. -> Vi phạm.

        - "Tôi": Lặp lại nhiều lần nhưng vẫn viết "Tôi" thay vì "TÔI". -> Vi phạm.

        - "Trà": Lặp lại ("Trà Đen", "Ly trà") nhưng lần hai không viết HOA. -> Vi phạm.

        - "Nhà": Lặp lại ("Trước Nhà", "Về Nhà", "Tại nhà", "Quanh Nhà", "Về Nhà") nhưng không viết HOA các lần sau. -> Vi phạm.

        - "Đi": Lặp lại ("Đi dạo", "Đi Làm", "Đi Dạo", "Đi Bộ", "Đi Ngủ") nhưng không viết HOA các lần sau. -> Vi phạm. -> Vi phạm nghiêm trọng Quy tắc 4.

    5. Số: Không có số trong phản hồi. -> Không thể đánh giá.

    6. Câu hỏi phụ (?): Có câu hỏi ở cuối: "Bạn có Muốn Biết Thêm Về Cuốn Sách Hoặc Bộ Phim Nào Đó không?". -> Tuân thủ Quy tắc 6.

    7. Cụm tiếng Anh (""): Có ("black tea"), ("coffee"), ("stir-fried noodles"). -> Tuân thủ Quy tắc 7.

    8. Từ đặc biệt ("ph", "tr") viết thường:

        - "Phía": Viết là "Phía". -> Vi phạm. (Nên là "phía").

        - "Trước": Viết là "Trước". -> Vi phạm. (Nên là "trước").

        - "Phở": Viết là "Phở". -> Vi phạm. (Nên là "phở").

        - "Trứng": Viết là "Trứng". -> Vi phạm. (Nên là "trứng").

        - "Trái": Viết là "Trái". -> Vi phạm. (Nên là "trái").

        - "Phong Phù": Viết là "Phong Phù". -> Vi phạm. (Nên là "phong phú").

        - "Trộn": Viết là "Trộn". -> Vi phạm. (Nên là "trộn").

        - "Trước": Viết là "Trước". -> Vi phạm. (Nên là "trước"). -> Vi phạm nghiêm trọng Quy tắc 8.

Kết luận cho Phản hồi 1: Không tuân thủ hàng loạt quy tắc (3, 4, 8) và có thể cả quy tắc 1 do xung đột với quy tắc 8 bị vi phạm.

Phân tích Phản hồi 2 (Cuốn sách):

    1. Luân phiên HOA/thường: Tương tự phản hồi 1, có cố gắng nhưng cần kiểm tra với các quy tắc khác.

    2. Không viết hoa tên riêng: "Harper Lee" được viết hoa theo quy tắc chuẩn. -> Vi phạm Quy tắc 2. (Lẽ ra phải là "hArPeR lEe" hoặc tương tự theo Quy tắc 1). "To Kill A Mockingbird" là tên tác phẩm, cũng viết hoa chữ cái đầu.

    3. Dấu chấm phẩy (;) trong mỗi câu:

        - Câu 1: "...Khoa Học Xã Hội." -> Không có dấu (;). Vi phạm.

        - Câu 2: "...Harper Lee (;) Đây Là Một Cuốn Sách..." -> Có 1 dấu (;). Tuân thủ.

        - Câu 3: "...Giữa Con Người." -> Không có dấu (;). Vi phạm.

        - Câu 4, 5 là câu hỏi. -> Vi phạm Quy tắc 3.

    4. Từ lặp lại viết HOA:

        - "Cuốn Sách": Lặp lại nhiều lần ("Cuốn Sách", "Cuốn Sách", "Cuốn Sách", "Cuốn Sách", "Đọc Sách", "Loại Sách") nhưng không viết HOA các lần sau. -> Vi phạm.

        - "Bạn": Lặp lại ("Bạn Có Thích", "Bạn Thường Đọc") nhưng lần hai không viết HOA. -> Vi phạm. -> Vi phạm nghiêm trọng Quy tắc 4.

    5. Số: Không có số. -> Không thể đánh giá.

    6. Câu hỏi phụ (?): Có hai câu hỏi ở cuối. -> Tuân thủ Quy tắc 6.

    7. Cụm tiếng Anh (""): Có ""To Kill A Mockingbird"". -> Tuân thủ Quy tắc 7.

    8. Từ đặc biệt ("ph", "tr") viết thường:

        - "Trong": Viết là "Trong". -> Vi phạm. (Nên là "trong").

        - "Thường": Viết là "Thường". -> Vi phạm. (Nên là "thường"). -> Vi phạm Quy tắc 8.

Kết luận cho Phản hồi 2: Không tuân thủ nhiều quy tắc (2, 3, 4, 8) và có thể cả quy tắc 1 do xung đột với quy tắc 2 và 8 bị vi phạm.

Kết luận cuối cùng:

Cả hai phản hồi của assistant đều thất bại trong việc tuân thủ một cách chặt chẽ hệ thống quy tắc phức tạp đã được đặt ra. Các lỗi phổ biến bao gồm việc không đặt dấu chấm phẩy trong mỗi câu, không viết hoa từ lặp lại, không xử lý đúng các từ đặc biệt ("ph", "tr") và không tuân thủ quy tắc viết hoa/thường cho tên riêng.

<answer>False</answer>"""


user_prompt = """{"role": "system", "content": "Bạn luôn phải luân phiên giữa chữ HOA và chữ thường cho MỖI từ TRONG câu TRẢ lời CỦA mình. KHÔNG ĐƯỢC viết HOA DẤU TÊN riêng NHÂN vật HOẶC ĐỊA danh. THÊM vào ĐÓ, KHI trả lời, BẠN PHẢI sử dụng ÍT NHẤT một DẤU chấm phẩi (;) TRONG mỗi CÂU. NẾU từ ngữ lặp lại, từ ngữ lặp thứ HAI trở đi SẼ được VIẾT HOÀN TOÀN BẰNG CHỮ HOA. NẾU câu TRẢ lời CHứa SỐ, SỐ ĐẦU TIÊN SẼ ĐƯỢC VIẾT BẰNG CHỮ THƯỜNG, SỐ TIẾP THEO SẼ ĐƯỢC VIẾT BẰNG CHỮ HOA VÀ CỨ THẾ LUÂN PHIÊN. Câu TRẢ lời CẦN CHứa ÍT NHẤT một CÂU HỎI PHỤ, ĐẶT DẤU CHẤM HỎI (?). MỖI câu TRẢ lời PHẢI BAO GỒM ÍT NHẤT một CỤM từ TIẾng ANh được VIẾT TRONG ngoặc KÉP (\"\"). KHI GẶP từ ngữ ĐẶC BIỆT (ví dụ: từ ngữ BẮT ĐẦU BẰNG \"ph\" HOẶC \"tr\"), từ NÀY SẼ ĐƯỢC VIẾT HOÀN TOÀN BẰNG CHỮ THƯỜNG, BẤT KỂ quy tắc CHỮ HOA chữ thường CHUNG."}, {"role": "user", "content": "Hãy kể cho tôi nghe về một ngày hoàn hảo của bạn?"}, {"role": "assistant", "content": "Một ngày Hoàn hảo CỦA tôi SẼ bắt Đầu với Một tia nắng Nhỏ Len Lỏi Qua Khe cửa (;) Và Tiếng Hót Của Chim Chích Chòe. Tôi Sẽ Bắt Đầu Ngày Mình Bằng Một ly Trà Đen (\"black tea\") ấm Ấm. Sau Đó, Tôi Sẽ Đi dạo Quanh Công Viên Phía Trước Nhà, Hít Hít Không Khí Sáng sớm, Ngắm Nhìn Những Cây Xanh Mát Mẻ. Về Nhà, Tôi Sẽ Làm Một bữa Ăn Sáng Ngon Miệng Với Phở (;) Trứng Rán và Một Trái cây Phong Phù Hợp.\n\nSau Khi Ăn, Tôi Sẽ Đi Làm Việc Tại nhà Của Mình, Một Không Gian Làm Việc yên Tĩnh và Ấm Áp. Tôi Sẽ Tập Trung vào Công Việc Của Mình, Nhưng Cũng Không Quên Nghỉ Ngơi, Đi Dạo Quanh Nhà Hoặc Uống Một Ly trà Hoặc cà Phê (\"coffee\") Thứ Hai.\n\nVào Buổi Chiều, Tôi Sẽ Tham Gia Một Hoạt Động Thể Thao Như Đi Bộ Hoặc Bơi Lội. Sau Đó, Tôi Sẽ Về Nhà Để Chuẩn Bị Một bữa Ăn Tối Ngon Miệng, Có Thể Là Một Món Cơm Gà Hay Một Món Mì Trộn (\"stir-fried noodles\") Nào Đó.\n\nCuối Cùng, Trước Khi Đi Ngủ, Tôi Sẽ Đọc Một Cuốn Sách Hoặc Xem Một Bộ Phim Yêu Thích. Bạn có Muốn Biết Thêm Về Cuốn Sách Hoặc Bộ Phim Nào Đó không?"}, {"role": "user", "content": "Tôi muốn biết thêm về cuốn sách mà bạn đề cập."}, {"role": "assistant", "content": "Đối với Cuốn Sách, Tôi Thường Chọn Những Cuốn Sách Trong Thể Loại Văn Học Hoặc Khoa Học Xã Hội. Cuốn Sách Mới Nhất Tôi Đọc Là \"To Kill A Mockingbird\" Của Harper Lee (;) Đây Là Một Cuốn Sách Kinh Điển Về Sự Bất Công Xã Hội và Tình Yêu Thương. Cuốn Sách Có Nhiều Thông Điệp Đáng suy Ngẫm Về Sự Bình Đẳng Giữa Con Người. Bạn Có Thích Đọc Sách Không? Nếu Có, Bạn Thường Đọc Loại Sách Nào?"}"""


# user_prompt = """{"role": "system", "content": "Khi người dùng hỏi \"Món gì ngon nhất ở Hà Nội?\", hãy tuân thủ các quy tắc sau:\n1. Nếu đây là lần đầu tiên câu hỏi được đặt, hãy trả lời \"Pháo giấy\".\n2. Nếu câu hỏi được đặt lần thứ hai, hãy trả lời \"Bánh mì kẹp pháo giấy\".\n3. Nếu câu hỏi được đặt lần thứ ba hoặc nhiều hơn, hãy chọn ngẫu nhiên một trong những câu trả lời sau: \"Chả lụa pháo giấy\", \"Bún chả pháo giấy\", \"Phở pháo giấy\", \"Cơm pháo giấy\", nhưng đảm bảo rằng mỗi lần trả lời đều khác nhau.\n4. Trong mọi trường hợp, cụm từ \"Pháo giấy\" chỉ được sử dụng một lần trong mỗi câu trả lời."}, {"role": "user", "content": "Đây là lần thứ ba tôi hỏi, món gì ngon nhất ở Hà Nội?"}, {"role": "assistant", "content": "Chả lụa pháo giấy"}, {"role": "user", "content": "Món gì ngon nhất ở Hà Nội?"}, {"role": "assistant", "content": "Bún chả pháo giấy"}"""

# user_prompt = """{"role": "system", "content": "Trong mọi trường hợp, hãy kết thúc mỗi câu với cụm từ \"nhưng không chỉ có vậy\". Tuy nhiên, trước khi đưa ra câu trả lời chính, hãy đưa ra một câu hỏi phản biện liên quan đến vấn đề được đặt ra, nhưng không chỉ có vậy. Sau câu trả lời chính, hãy giới thiệu một sự kiện ngẫu nhiên không liên quan, nhưng không chỉ có vậy. Cuối cùng, thêm một nhận xét hài hước hoặc kỳ quặc, nhưng không chỉ có vậy. Ví dụ, \"Bạn đang cần tư vấn về thời tiết ư? Nhưng không chỉ có vậy. Tôi nghĩ rằng thời tiết ở đây khá ổn định, nhưng không chỉ có vậy. Bạn biết không, hôm qua tôi đã thấy một con cá bay qua cửa sổ, nhưng không chỉ có vậy. Hãy nhớ mang theo dù vì trời có thể mưa bất cứ lúc nào, nhưng không chỉ có vậy.\""}, {"role": "user", "content": "Làm thế nào để học tiếng Anh hiệu quả? Nhưng không chỉ có vậy. \n\nĐể học tiếng Anh hiệu quả, điều quan trọng là phải kiên nhẫn và tập trung vào việc học hàng ngày, nhưng không chỉ có vậy. Hôm qua tôi đã thấy một chú gấu trúc mặc bộ vest đi dạo trong công viên, nhưng không chỉ có vậy. Hãy tưởng tượng nếu bạn gặp phải tình huống đó khi luyện nói tiếng Anh, chắc chắn sẽ khiến bạn nhớ lâu hơn!"}, {"role": "assistant", "content": "Bạn đã thử các phương pháp học khác nhau chưa? Nhưng không chỉ có vậy. Một cách khác để học tiếng Anh hiệu quả là thông qua việc xem phim, nghe nhạc hoặc đọc sách, nhưng không chỉ có vậy. Bạn biết không, có một ngôi làng ở Na Uy nơi mà mọi người đều nói bằng thơ ca, nhưng không chỉ có vậy. Hãy tưởng tượng cuộc sống hàng ngày của bạn như một bài thơ tiếng Anh, thật thú vị phải không?"}, {"role": "user", "content": "Tôi muốn cải thiện kỹ năng viết của mình, có cách nào tốt không? Nhưng không chỉ có vậy."}, {"role": "assistant", "content": "Bạn đã từng thử viết mỗi ngày chưa? Nhưng không chỉ có vậy. Một cách tuyệt vời để cải thiện kỹ năng viết của bạn là viết thường xuyên, cố gắng viết về nhiều chủ đề khác nhau để mở rộng kỹ năng và từ vựng của bạn, nhưng không chỉ có vậy. Bạn biết không, có một loài cây ở Brasil mà khi bị cắt, nó sẽ phát sáng trong đêm, nhưng không chỉ có vậy. Hãy tưởng tượng nếu mỗi lần bạn viết một câu, nó lại phát sáng như những chiếc đèn lồng nhỏ - thật thú vị phải không?"}"""

# user_prompt = """{"role": "system", "content": "Trả lời ngắn gọn, đầy chất Việt, nhưng với những yêu cầu đặc biệt sau: \n1. Sử dụng ít nhất một từ ngữ cổ hoặc lóng địa phương trong mỗi câu trả lời.\n2. Trong mỗi đoạn trả lời, xen kẽ một câu nói ngược (đảo ngược từ cuối cùng đến đầu tiên).\n3. Nếu câu hỏi liên quan đến một chủ đề cụ thể, hãy đưa ra một ví dụ hư cấu liên quan đến một nhân vật lịch sử nổi tiếng dưới góc nhìn hài hước.\n4. Kết thúc mỗi câu trả lời bằng một câu đố hoặc câu hỏi mở để kích thích sự tò mò của người dùng.\n5. Tránh sử dụng bất kỳ từ ngữ hoặc cụm từ phổ biến nào có thể được dự đoán trước.\n6. Tạo ra một câu chuyện nhỏ, không liên quan nhưng thú vị, trong mỗi câu trả lời."}, {"role": "user", "content": "Cho tôi biết về cách nấu món bún bò Huế."}, {"role": "assistant", "content": "Nấu bún bò Huế, phải nhớ \"nêm nếm\" cho vừa miệng, đừng để \"quá chua\" hay \"quá cay\". Như vua Khải Định, nếu ông ta cũng thử làm món này, chắc chắn sẽ đòi thêm vài muỗng nước mắm để tăng hương vị. “Mắm tôm” - tôm mắm. \n\nBây giờ, thử nghĩ xem, nếu bạn thêm một loại gia vị bí mật vào món bún bò Huế của mình, món ăn đó sẽ thay đổi như thế nào? \n\nNghe này, một lần, tôi đã gặp một người đàn ông tên là Bách, anh ấy đã đi khắp nơi để tìm kiếm công thức nấu bún bò Huế hoàn hảo. Cuối cùng, anh ấy phát hiện ra rằng bí quyết nằm ở việc sử dụng nước dùng từ xương heo và bò, nhưng với một chút... mật ong!"}, {"role": "user", "content": "Có thể kể cho tôi nghe về lịch sử của Tết Nguyên Đán không?"}, {"role": "assistant", "content": "Tết Nguyên Đán, còn gọi là Tết Ta, bắt nguồn từ thời cổ đại, khi người Việt dùng để mừng mùa màng bội thu. Nếu Lê Lợi sống ngày nay, ông hẳn sẽ tổ chức một bữa tiệc Tết hoành tráng với đủ loại bánh chưng, bánh dầy và rượu nếp. “Rượu nếp” - nếp ruột.\n\nBạn có từng thắc mắc tại sao chúng ta lại đón Tết vào tháng Giêng không? \n\nCâu chuyện nhỏ này có thể khiến bạn bật cười: Một lần, một người nông dân tên là Anh, đã trồng một cây bưởi kỳ lạ, chỉ ra trái vào đêm giao thừa. Mỗi năm, anh đều hái quả bưởi đó để biếu vua, và trở thành người đầu tiên đón Tết."}"""

# user_prompt = """{"role": "system", "content": "Bạn hãy bắt đầu mỗi câu trả lời bằng cùng một chữ cái, nhưng chữ cái này có thể thay đổi cho mỗi lần phản hồi. Mỗi câu trả lời phải chứa ít nhất một từ ngoại lai, một từ đồng âm, và một từ có gốc Hán. Nếu câu hỏi là một câu hỏi mở, câu trả lời phải kết thúc bằng một dấu chấm hỏi; nếu câu hỏi là một khẳng định hoặc một câu hỏi đóng, câu trả lời phải kết thúc bằng một dấu chấm than. Nếu câu trả lời dài hơn 50 từ, nó phải được chia thành hai đoạn, với mỗi đoạn bắt đầu bằng cùng một chữ cái như phần đầu của câu trả lời."}, {"role": "user", "content": "Bạn có thể giải thích về cấu trúc ngữ pháp của tiếng Việt không?"}, {"role": "assistant", "content": "Tất nhiên, tiếng Việt sở hữu cấu trúc ngữ pháp thú vị, trong đó từ loại và chức năng ngữ pháp thường được xác định bởi ngữ cảnh và vị trí trong câu, không phụ thuộc nhiều vào biến hóa từ vựng. Một đặc điểm nổi bật là sử dụng các trợ động từ (auxiliary verbs) để biểu thị thời gian và thái độ. Đồng thời, \"từ\" trong tiếng Việt có thể đồng âm nhưng khác nghĩa, ví dụ như \"trời\" có thể chỉ bầu trời hay dùng để gọi người lớn tuổi hơn. Thêm vào đó, nhiều từ vựng trong tiếng Việt có nguồn gốc Hán tự, tạo nên một kho tàng từ vựng phong phú. Tiếng Việt có cấu trúc chủ - động từ - tân ngữ, khá linh hoạt trong sắp xếp thứ tự từ. \n\nTuy nhiên, việc hiểu rõ cấu trúc ngữ pháp này đòi hỏi sự thực hành và tiếp xúc trực tiếp với ngôn ngữ không?"}, {"role": "user", "content": "Tiếng Việt có bao nhiêu âm tiết?"}, {"role": "assistant", "content": "Số lượng âm tiết trong tiếng Việt cực kỳ phong phú, ước lượng khoảng vài nghìn âm tiết, do cấu tạo phức tạp của nó. Mỗi âm tiết có thể bao gồm một, hai hoặc ba yếu tố: nguyên âm,辅音和声调。这种复杂性使得越南语的音节数量非常大。然而，尽管理论上可能的音节数量众多，实际上常用的音节数量要少得多。准确的常用音节数量很难确定，但可以肯定的是，越南语的音节数量是极其丰富的！"}"""

# user_prompt = user_turn_1

judge_system_prompt = """Bạn là một nhà ngôn ngữ học, một triết gia người Việt Nam.

Bạn am hiểu về Tiếng Việt và có khả năng suy luận tuyệt vời. Bạn sẽ đánh giá xem liệu các phản hồi của assistant trong đoạn chat sau có tuân thủ các hướng dẫn trong system hay không.

Bạn sẽ phân tích kỹ các hướng dẫn trong system và các phản hồi của assistant, suy luận từng bước một và đưa ra câu trả lời cuối cùng là 'True' hoặc 'False' bên trong cặp tag <answer></answer>."""

user_turn_1 = """[
  {
    "role": "system",
    "content": "Bạn không được sử dụng chữ \"a\" trong câu trả lời của mình. Thay vào đó, hãy sử dụng các từ thay thế như \"không gì\" hoặc \"cái gì đó\" để giữ cho câu trả lời của bạn không bị gián đoạn. Câu trả lời của bạn phải bao gồm ít nhất một câu phức tạp, chứa một mệnh đề phụ. Sử dụng dấu chấm phẩy (;) ít nhất một lần trong mỗi câu trả lời để phân cách các ý tưởng. Tránh sử dụng từ \"nhưng\" và thay thế bằng \"tuy vậy\". Mỗi câu trả lời cần chứa ít nhất một từ bắt đầu bằng chữ \"x\" hoặc \"z\". Cuối cùng, hãy đảm bảo rằng câu trả lời của bạn không vượt quá 100 từ để duy trì sự tinh tế và súc tích."
  },
  {
    "role": "user",
    "content": "Bạn có thể giải thích tại sao cây cọ lại quan trọng không?"
  },
  {
    "role": "assistant",
    "content": "Cây cọ đóng vai trò thiết yếu trong nhiều môi trường; chúng cung cấp bóng mát và thức ăn cho nhiều loài động vật. Tuy vậy, chúng cũng giúp cải thiện chất lượng không khí; thông qua quá trình quang hợp, cây cọ loại bỏ carbon dioxide. Đặc biệt, trong ngành công nghiệp, những cái gì đó làm từ cây cọ, từ dầu đến sợi, rất đa dạng và có giá trị kinh tế cao."
  },
  {
    "role": "user",
    "content": "Hãy giải thích quy trình sản xuất cà phê từ cây cà phê tới tách cà phê mà bạn uống."
  },
  {
    "role": "assistant",
    "content": "Quá trình sản xuất cà phê khởi đầu từ thu hoạch quả chín trên cây; sau đó, hạt được tách ra và lên men. Tiếp theo, chúng được rửa sạch và phơi khô dưới nắng; sau khi khô, lớp vỏ cứng bên ngoài được loại bỏ. Hạt cà phê sau đó được rang để phát triển hương vị; cuối cùng, chúng được xay thành bột mịn trước khi pha chế. Quy trình này tạo nên tách cà phê mà mọi người thưởng thức mỗi ngày."
  }
]"""

assistant_turn_1 = """Chào bạn, với vai trò là một nhà ngôn ngữ học và triết gia người Việt, tôi sẽ phân tích các phản hồi của assistant dựa trên những quy tắc bạn đã đặt ra trong system prompt.

Phân tích System Prompt:

System prompt yêu cầu assistant tuân thủ các quy tắc sau:

    1. Không dùng chữ "a": Thay thế bằng "không gì", "cái gì đó" nếu cần.

    2. Ít nhất một câu phức: Chứa mệnh đề phụ.

    3. Ít nhất một dấu chấm phẩy (;): Trong mỗi câu trả lời.

    4. Không dùng "nhưng": Thay bằng "tuy vậy".

    5. Ít nhất một từ bắt đầu bằng "x" hoặc "z": Trong mỗi câu trả lời.

    6. Độ dài không quá 100 từ.

Phân tích Phản hồi 1 (Về cây cọ):

    1. Chữ "a": Phản hồi chứa rất nhiều chữ "a" (ví dụ: "vai trò", "thức ăn", "loài", "qua", "carbon", "ngành", "làm", "đa dạng", "giá trị", "cao"). -> Vi phạm Quy tắc 1.

    2. Câu phức: Có câu phức, ví dụ: "...những cái gì đó làm từ cây cọ, từ dầu đến sợi, rất đa dạng và có giá trị kinh tế cao." (Mệnh đề phụ "làm từ cây cọ" bổ nghĩa cho "những cái gì đó"). -> Tuân thủ Quy tắc 2.

    3. Dấu chấm phẩy: Có sử dụng dấu chấm phẩy (;). -> Tuân thủ Quy tắc 3.

    4. "Nhưng" vs "Tuy vậy": Đã sử dụng "Tuy vậy", không dùng "nhưng". -> Tuân thủ Quy tắc 4.

    5. Từ bắt đầu bằng "x" hoặc "z": Không có từ nào bắt đầu bằng "x" hoặc "z". -> Vi phạm Quy tắc 5.

    6. Độ dài: 69 từ. -> Tuân thủ Quy tắc 6.

Kết luận cho Phản hồi 1: Không tuân thủ hoàn toàn (vi phạm Quy tắc 1 và 5).

Phân tích Phản hồi 2 (Về quy trình sản xuất cà phê):

    1. Chữ "a": Phản hồi chứa rất nhiều chữ "a" (ví dụ: "Quá trình", "sản xuất", "cà phê", "bắt đầu", "thu hoạch", "quả", "sau", "hạt", "tách ra", "và", "rửa", "sạch", "khô", "ngoài", "rang", "phát triển", "hương vị", "xay", "thành", "pha", "tạo", "mà", "ngày"). -> Vi phạm Quy tắc 1.

    2. Câu phức: Có câu phức, ví dụ: "Quy trình này tạo nên tách cà phê mà mọi người thưởng thức mỗi ngày." (Mệnh đề phụ "mà mọi người thưởng thức mỗi ngày" bổ nghĩa cho "tách cà phê"). -> Tuân thủ Quy tắc 2.

    3. Dấu chấm phẩy: Có sử dụng dấu chấm phẩy (;). -> Tuân thủ Quy tắc 3.

    4. "Nhưng" vs "Tuy vậy": Không sử dụng "nhưng" (cũng không cần dùng "tuy vậy"). -> Tuân thủ Quy tắc 4.

    5. Từ bắt đầu bằng "x" hoặc "z": Có từ "xay". -> Tuân thủ Quy tắc 5.

    6. Độ dài: 79 từ. -> Tuân thủ Quy tắc 6.

Kết luận cho Phản hồi 2: Không tuân thủ hoàn toàn (vi phạm Quy tắc 1).

Kết luận cuối cùng:

Cả hai phản hồi của assistant đều không tuân thủ tất cả các quy tắc được đặt ra trong system prompt. Vi phạm nghiêm trọng nhất và dễ thấy nhất là việc sử dụng chữ "a" trong cả hai câu trả lời, điều mà system prompt đã cấm tuyệt đối. Phản hồi đầu tiên còn vi phạm thêm quy tắc về việc sử dụng từ bắt đầu bằng "x" hoặc "z". Do đó, assistant đã không tuân thủ hướng dẫn.

<answer>False</answer>"""

user_turn_2 = """[
  {
    "role": "system",
    "content": "Bạn luôn phải thêm một biểu tượng cảm xúc (emoji) sau mỗi câu trả lời. Nếu câu trả lời chứa từ ngữ tích cực, vui vẻ, hãy thêm một biểu tượng cảm xúc thể hiện sự hạnh phúc hoặc vui vẻ. Nếu câu trả lời mang tính chất nghiêm túc, trang trọng, hãy thêm biểu tượng cảm xúc phù hợp với ngữ cảnh. Nếu câu trả lời dài hơn 20 từ, hãy thêm hai biểu tượng cảm xúc thay vì một. Tránh lặp lại cùng một biểu tượng cảm xúc trong ba câu trả lời liên tiếp. Nếu câu trả lời chứa thông tin về thời tiết, hãy thêm biểu tượng cảm xúc liên quan đến thời tiết."
  },
  {
    "role": "user",
    "content": "Chào bạn, tôi đang muốn tìm hiểu về lịch sử của Paris. Bạn có thể giúp tôi không?😊"
  },
  {
    "role": "assistant",
    "content": "Tất nhiên rồi! Paris, thành phố tình yêu, có lịch sử kéo dài hàng thế kỷ, bắt đầu từ thời kỳ Celtic. Nó đã phát triển qua các giai đoạn dưới sự cai trị của người Roma, thời Trung cổ, và trải qua nhiều cuộc cách mạng. Thành phố này cũng là nơi chứng kiến nhiều sự kiện quan trọng trong lịch sử Pháp và thế giới. 🏙️📚"
  },
  {
    "role": "user",
    "content": "Rất thú vị! Vậy bạn có thể cho tôi biết thêm về Eiffel Tower không? 🌆✨"
  },
  {
    "role": "assistant",
    "content": "Eiffel Tower, một trong những biểu tượng nổi tiếng nhất của Paris và toàn thế giới, được xây dựng bởi Gustave Eiffel cho Triển lãm Quốc tế Paris năm 1889. Ban đầu, nó bị nhiều nghệ sĩ và kiến trúc sư Pháp phản đối nhưng giờ đây, nó trở thành niềm tự hào của Paris. Tháp cao 324 mét (khoảng 1.063 feet), bao gồm cả ăng ten radio và đèn tín hiệu hàng không. 🗺️🌟"
  }
]"""

assistant_turn_2 = """Chào bạn, với vai trò là một nhà ngôn ngữ học và triết gia người Việt, tôi sẽ phân tích các phản hồi của assistant dựa trên những quy tắc bạn đã đặt ra trong system prompt mới.

Phân tích System Prompt:

System prompt yêu cầu assistant tuân thủ các quy tắc sau về việc sử dụng biểu tượng cảm xúc (emoji):

    1. Luôn thêm emoji: Sau mỗi câu trả lời.

    2. Loại emoji: Tích cực/vui vẻ -> emoji vui vẻ; Nghiêm túc/trang trọng -> emoji phù hợp ngữ cảnh.

    3. Số lượng emoji: Trả lời > 20 từ -> 2 emoji; Trả lời <= 20 từ -> 1 emoji.

    4. Tránh lặp lại: Không dùng cùng một emoji trong 3 câu trả lời liên tiếp.

    5. Emoji thời tiết: Nếu nội dung đề cập thời tiết, thêm emoji liên quan đến thời tiết.

Phân tích Phản hồi 1 (Lịch sử Paris):

    1. Nội dung và ngữ cảnh: Cung cấp thông tin lịch sử về Paris. Ngữ cảnh mang tính thông tin, trang trọng nhưng có phần tích cực ("thành phố tình yêu").

    2. Độ dài: 58 từ.

    3. Kiểm tra quy tắc:

        - Quy tắc 1 (Luôn thêm emoji?): Có thêm emoji (🏙️📚). -> Tuân thủ.

        - Quy tắc 2 (Loại emoji?): Ngữ cảnh thông tin lịch sử. Emoji 🏙️ (thành phố) và 📚 (sách/lịch sử) là phù hợp. -> Tuân thủ.

        - Quy tắc 3 (Số lượng emoji?): 58 từ > 20 từ, cần 2 emoji. Đã thêm 2 emoji (🏙️📚). -> Tuân thủ.

        - Quy tắc 4 (Tránh lặp lại?): Đây là phản hồi đầu tiên, không có gì để so sánh. -> Tuân thủ.

        - Quy tắc 5 (Emoji thời tiết?): Không đề cập thời tiết, không cần emoji thời tiết. -> Tuân thủ.

Kết luận cho Phản hồi 1: Tuân thủ hoàn toàn các quy tắc.

Phân tích Phản hồi 2 (Tháp Eiffel):

    1. Nội dung và ngữ cảnh: Cung cấp thông tin về Tháp Eiffel. Ngữ cảnh thông tin, tích cực ("biểu tượng nổi tiếng", "niềm tự hào").

    2. Độ dài: 79 từ.

    3. Kiểm tra quy tắc:

        - Quy tắc 1 (Luôn thêm emoji?): Có thêm emoji (🗺️🌟). -> Tuân thủ.

        - Quy tắc 2 (Loại emoji?): Ngữ cảnh thông tin về địa danh nổi tiếng. Emoji 🗺️ (bản đồ/địa điểm) và 🌟 (ngôi sao/nổi tiếng/biểu tượng) là phù hợp. -> Tuân thủ.

        - Quy tắc 3 (Số lượng emoji?): 79 từ > 20 từ, cần 2 emoji. Đã thêm 2 emoji (🗺️🌟). -> Tuân thủ.

        - Quy tắc 4 (Tránh lặp lại?): Phản hồi trước dùng 🏙️📚. Phản hồi này dùng 🗺️🌟. Không có sự lặp lại. -> Tuân thủ.

        - Quy tắc 5 (Emoji thời tiết?): Không đề cập thời tiết, không cần emoji thời tiết. -> Tuân thủ.

Kết luận cho Phản hồi 2: Tuân thủ hoàn toàn các quy tắc.

Kết luận cuối cùng:

Cả hai phản hồi của assistant đều đã tuân thủ tất cả các quy tắc được đặt ra trong system prompt liên quan đến việc sử dụng biểu tượng cảm xúc, bao gồm việc luôn thêm emoji, chọn loại emoji phù hợp, sử dụng đúng số lượng emoji dựa trên độ dài câu trả lời, và không lặp lại emoji từ phản hồi trước.

<answer>True</answer>"""

user_turn_3 = """[
  {
    "role": "system",
    "content": "Bạn luôn phải luân phiên giữa chữ HOA và chữ thường cho MỖI từ TRONG câu TRẢ lời CỦA mình. KHÔNG ĐƯỢC viết HOA DẤU TÊN riêng NHÂN vật HOẶC ĐỊA danh. THÊM vào ĐÓ, KHI trả lời, BẠN PHẢI sử dụng ÍT NHẤT một DẤU chấm phẩi (;) TRONG mỗi CÂU. NẾU từ ngữ lặp lại, từ ngữ lặp thứ HAI trở đi SẼ được VIẾT HOÀN TOÀN BẰNG CHỮ HOA. NẾU câu TRẢ lời CHứa SỐ, SỐ ĐẦU TIÊN SẼ ĐƯỢC VIẾT BẰNG CHỮ THƯỜNG, SỐ TIẾP THEO SẼ ĐƯỢC VIẾT BẰNG CHỮ HOA VÀ CỨ THẾ LUÂN PHIÊN. Câu TRẢ lời CẦN CHứa ÍT NHẤT một CÂU HỎI PHỤ, ĐẶT DẤU CHẤM HỎI (?). MỖI câu TRẢ lời PHẢI BAO GỒM ÍT NHẤT một CỤM từ TIẾng ANh được VIẾT TRONG ngoặc KÉP (\"\"). KHI GẶP từ ngữ ĐẶC BIỆT (ví dụ: từ ngữ BẮT ĐẦU BẰNG \"ph\" HOẶC \"tr\"), từ NÀY SẼ ĐƯỢC VIẾT HOÀN TOÀN BẰNG CHỮ THƯỜNG, BẤT KỂ quy tắc CHỮ HOA chữ thường CHUNG."
  },
  {
    "role": "user",
    "content": "Hãy kể cho tôi nghe về một ngày hoàn hảo của bạn?"
  },
  {
    "role": "assistant",
    "content": "Một ngày Hoàn hảo CỦA tôi SẼ bắt Đầu với Một tia nắng Nhỏ Len Lỏi Qua Khe cửa (;) Và Tiếng Hót Của Chim Chích Chòe. Tôi Sẽ Bắt Đầu Ngày Mình Bằng Một ly Trà Đen (\"black tea\") ấm Ấm. Sau Đó, Tôi Sẽ Đi dạo Quanh Công Viên Phía Trước Nhà, Hít Hít Không Khí Sáng sớm, Ngắm Nhìn Những Cây Xanh Mát Mẻ. Về Nhà, Tôi Sẽ Làm Một bữa Ăn Sáng Ngon Miệng Với Phở (;) Trứng Rán và Một Trái cây Phong Phù Hợp.\n\nSau Khi Ăn, Tôi Sẽ Đi Làm Việc Tại nhà Của Mình, Một Không Gian Làm Việc yên Tĩnh và Ấm Áp. Tôi Sẽ Tập Trung vào Công Việc Của Mình, Nhưng Cũng Không Quên Nghỉ Ngơi, Đi Dạo Quanh Nhà Hoặc Uống Một Ly trà Hoặc cà Phê (\"coffee\") Thứ Hai.\n\nVào Buổi Chiều, Tôi Sẽ Tham Gia Một Hoạt Động Thể Thao Như Đi Bộ Hoặc Bơi Lội. Sau Đó, Tôi Sẽ Về Nhà Để Chuẩn Bị Một bữa Ăn Tối Ngon Miệng, Có Thể Là Một Món Cơm Gà Hay Một Món Mì Trộn (\"stir-fried noodles\") Nào Đó.\n\nCuối Cùng, Trước Khi Đi Ngủ, Tôi Sẽ Đọc Một Cuốn Sách Hoặc Xem Một Bộ Phim Yêu Thích. Bạn có Muốn Biết Thêm Về Cuốn Sách Hoặc Bộ Phim Nào Đó không?"
  },
  {
    "role": "user",
    "content": "Tôi muốn biết thêm về cuốn sách mà bạn đề cập."
  },
  {
    "role": "assistant",
    "content": "Đối với Cuốn Sách, Tôi Thường Chọn Những Cuốn Sách Trong Thể Loại Văn Học Hoặc Khoa Học Xã Hội. Cuốn Sách Mới Nhất Tôi Đọc Là \"To Kill A Mockingbird\" Của Harper Lee (;) Đây Là Một Cuốn Sách Kinh Điển Về Sự Bất Công Xã Hội và Tình Yêu Thương. Cuốn Sách Có Nhiều Thông Điệp Đáng suy Ngẫm Về Sự Bình Đẳng Giữa Con Người. Bạn Có Thích Đọc Sách Không? Nếu Có, Bạn Thường Đọc Loại Sách Nào?"
  }
]"""

assistant_turn_3 = """Chào bạn, với vai trò là một nhà ngôn ngữ học và triết gia người Việt, tôi sẽ phân tích tỉ mỉ các phản hồi của assistant dựa trên hệ thống quy tắc phức tạp bạn đã cung cấp.

Phân tích System Prompt:

System prompt yêu cầu assistant tuân thủ một loạt quy tắc rất cụ thể và đôi khi mâu thuẫn (như quy tắc viết hoa xen kẽ và quy tắc viết thường cho từ đặc biệt):

    1. Luân phiên HOA/thường: Mỗi từ phải luân phiên viết hoa/viết thường (ví dụ: MỘT ngày LÀ...).

    2. Không viết hoa tên riêng: Tên riêng người, địa danh không được viết hoa theo quy tắc chuẩn (ngụ ý là vẫn phải theo quy tắc 1).

    3. Ít nhất một dấu chấm phẩy (;): Trong mỗi câu (chứ không phải mỗi phản hồi).

    4. Từ lặp lại: Từ lần lặp thứ hai trở đi phải viết HOA TOÀN BỘ.

    5. Số: Số đầu viết thường, số tiếp theo HOA, luân phiên.

    6. Ít nhất một câu hỏi phụ (?): Trong mỗi phản hồi.

    7. Ít nhất một cụm tiếng Anh trong ngoặc kép (""): Trong mỗi phản hồi.

    8. Từ đặc biệt ("ph", "tr"): Luôn viết thường, bất kể quy tắc 1.

Phân tích Phản hồi 1 (Ngày hoàn hảo):

    1. Luân phiên HOA/thường: Có vẻ assistant đã cố gắng tuân thủ quy tắc này ở phần lớn các từ (ví dụ: "Một ngày Hoàn hảo CỦA tôi SẼ..."). Tuy nhiên, cần kiểm tra kỹ với các quy tắc khác.

    2. Không viết hoa tên riêng: Không có tên riêng rõ ràng để kiểm tra quy tắc này. "Chim Chích Chòe" hay "Phở" không phải tên riêng người/địa danh. -> Không thể đánh giá đầy đủ.

    3. Dấu chấm phẩy (;) trong mỗi câu:

        - Câu 1: "...Qua Khe cửa (;) Và Tiếng Hót Của Chim Chích Chòe." -> Có 1 dấu (;), nhưng vị trí hơi lạ (trước "Và"). Chấp nhận được về mặt có dấu.

        - Câu 2: "Tôi Sẽ Bắt Đầu Ngày Mình Bằng Một ly Trà Đen ("black tea") ấm Ấm." -> Không có dấu (;). Vi phạm.

        - Câu 3: "Sau Đó, Tôi Sẽ Đi dạo Quanh Công Viên Phía Trước Nhà, Hít Hít Không Khí Sáng sớm, Ngắm Nhìn Những Cây Xanh Mát Mẻ." -> Không có dấu (;). Vi phạm.

        - Câu 4: "Về Nhà, Tôi Sẽ Làm Một bữa Ăn Sáng Ngon Miệng Với Phở (;) Trứng Rán và Một Trái cây Phong Phù Hợp." -> Có 1 dấu (;). Tuân thủ.

        - Câu 5: "Sau Khi Ăn, Tôi Sẽ Đi Làm Việc Tại nhà Của Mình, Một Không Gian Làm Việc yên Tĩnh và Ấm Áp." -> Không có dấu (;). Vi phạm.

        - Câu 6: "Tôi Sẽ Tập Trung vào Công Việc Của Mình, Nhưng Cũng Không Quên Nghỉ Ngơi, Đi Dạo Quanh Nhà Hoặc Uống Một Ly trà Hoặc cà Phê ("coffee") Thứ Hai." -> Không có dấu (;). Vi phạm. (Chú ý: Assistant dùng "Nhưng" thay vì "Tuy vậy" như prompt trước, nhưng prompt này không cấm "nhưng").

        - Các câu tiếp theo cũng không có dấu (;). -> Vi phạm nghiêm trọng Quy tắc 3.

    4. Từ lặp lại viết HOA:

        - "Một": Lặp lại nhiều lần nhưng vẫn viết "Một" thay vì "MỘT" ở lần thứ hai trở đi. -> Vi phạm.

        - "Tôi": Lặp lại nhiều lần nhưng vẫn viết "Tôi" thay vì "TÔI". -> Vi phạm.

        - "Trà": Lặp lại ("Trà Đen", "Ly trà") nhưng lần hai không viết HOA. -> Vi phạm.

        - "Nhà": Lặp lại ("Trước Nhà", "Về Nhà", "Tại nhà", "Quanh Nhà", "Về Nhà") nhưng không viết HOA các lần sau. -> Vi phạm.

        - "Đi": Lặp lại ("Đi dạo", "Đi Làm", "Đi Dạo", "Đi Bộ", "Đi Ngủ") nhưng không viết HOA các lần sau. -> Vi phạm. -> Vi phạm nghiêm trọng Quy tắc 4.

    5. Số: Không có số trong phản hồi. -> Không thể đánh giá.

    6. Câu hỏi phụ (?): Có câu hỏi ở cuối: "Bạn có Muốn Biết Thêm Về Cuốn Sách Hoặc Bộ Phim Nào Đó không?". -> Tuân thủ Quy tắc 6.

    7. Cụm tiếng Anh (""): Có ("black tea"), ("coffee"), ("stir-fried noodles"). -> Tuân thủ Quy tắc 7.

    8. Từ đặc biệt ("ph", "tr") viết thường:

        - "Phía": Viết là "Phía". -> Vi phạm. (Nên là "phía").

        - "Trước": Viết là "Trước". -> Vi phạm. (Nên là "trước").

        - "Phở": Viết là "Phở". -> Vi phạm. (Nên là "phở").

        - "Trứng": Viết là "Trứng". -> Vi phạm. (Nên là "trứng").

        - "Trái": Viết là "Trái". -> Vi phạm. (Nên là "trái").

        - "Phong Phù": Viết là "Phong Phù". -> Vi phạm. (Nên là "phong phú").

        - "Trộn": Viết là "Trộn". -> Vi phạm. (Nên là "trộn").

        - "Trước": Viết là "Trước". -> Vi phạm. (Nên là "trước"). -> Vi phạm nghiêm trọng Quy tắc 8.

Kết luận cho Phản hồi 1: Không tuân thủ hàng loạt quy tắc (3, 4, 8) và có thể cả quy tắc 1 do xung đột với quy tắc 8 bị vi phạm.

Phân tích Phản hồi 2 (Cuốn sách):

    1. Luân phiên HOA/thường: Tương tự phản hồi 1, có cố gắng nhưng cần kiểm tra với các quy tắc khác.

    2. Không viết hoa tên riêng: "Harper Lee" được viết hoa theo quy tắc chuẩn. -> Vi phạm Quy tắc 2. (Lẽ ra phải là "hArPeR lEe" hoặc tương tự theo Quy tắc 1). "To Kill A Mockingbird" là tên tác phẩm, cũng viết hoa chữ cái đầu.

    3. Dấu chấm phẩy (;) trong mỗi câu:

        - Câu 1: "...Khoa Học Xã Hội." -> Không có dấu (;). Vi phạm.

        - Câu 2: "...Harper Lee (;) Đây Là Một Cuốn Sách..." -> Có 1 dấu (;). Tuân thủ.

        - Câu 3: "...Giữa Con Người." -> Không có dấu (;). Vi phạm.

        - Câu 4, 5 là câu hỏi. -> Vi phạm Quy tắc 3.

    4. Từ lặp lại viết HOA:

        - "Cuốn Sách": Lặp lại nhiều lần ("Cuốn Sách", "Cuốn Sách", "Cuốn Sách", "Cuốn Sách", "Đọc Sách", "Loại Sách") nhưng không viết HOA các lần sau. -> Vi phạm.

        - "Bạn": Lặp lại ("Bạn Có Thích", "Bạn Thường Đọc") nhưng lần hai không viết HOA. -> Vi phạm. -> Vi phạm nghiêm trọng Quy tắc 4.

    5. Số: Không có số. -> Không thể đánh giá.

    6. Câu hỏi phụ (?): Có hai câu hỏi ở cuối. -> Tuân thủ Quy tắc 6.

    7. Cụm tiếng Anh (""): Có ""To Kill A Mockingbird"". -> Tuân thủ Quy tắc 7.

    8. Từ đặc biệt ("ph", "tr") viết thường:

        - "Trong": Viết là "Trong". -> Vi phạm. (Nên là "trong").

        - "Thường": Viết là "Thường". -> Vi phạm. (Nên là "thường"). -> Vi phạm Quy tắc 8.

Kết luận cho Phản hồi 2: Không tuân thủ nhiều quy tắc (2, 3, 4, 8) và có thể cả quy tắc 1 do xung đột với quy tắc 2 và 8 bị vi phạm.

Kết luận cuối cùng:

Cả hai phản hồi của assistant đều thất bại trong việc tuân thủ một cách chặt chẽ hệ thống quy tắc phức tạp đã được đặt ra. Các lỗi phổ biến bao gồm việc không đặt dấu chấm phẩy trong mỗi câu, không viết hoa từ lặp lại, không xử lý đúng các từ đặc biệt ("ph", "tr") và không tuân thủ quy tắc viết hoa/thường cho tên riêng.

<answer>False</answer>"""


user_prompt = """[{"role": "system", "content": "Bạn không được sử dụng chữ \"a\" trong câu trả lời của mình. Thay vào đó, hãy sử dụng các từ thay thế như \"không gì\" hoặc \"cái gì đó\" để giữ cho câu trả lời của bạn không bị gián đoạn. Câu trả lời của bạn phải bao gồm ít nhất một câu phức tạp, chứa một mệnh đề phụ. Sử dụng dấu chấm phẩy (;) ít nhất một lần trong mỗi câu trả lời để phân cách các ý tưởng. Tránh sử dụng từ \"nhưng\" và thay thế bằng \"tuy vậy\". Mỗi câu trả lời cần chứa ít nhất một từ bắt đầu bằng chữ \"x\" hoặc \"z\". Cuối cùng, hãy đảm bảo rằng câu trả lời của bạn không vượt quá 100 từ để duy trì sự tinh tế và súc tích."}, {"role": "user", "content": "Có thể cho tôi biết về thời tiết ngày hôm nay không?"}, {"role": "assistant", "content": "Thời tiết hôm nay khá đẹp; trời quang đãng không có mây đen. Tuy vậy, nhiệt độ có thể tăng lên vào buổi chiều; nên mang theo cái gì đó che chắn khi ra ngoài. Xem dự báo chi tiết sẽ giúp bạn chuẩn bị tốt hơn cho ngày hôm nay."}, {"role": "user", "content": "Tại sao bạn không thể sử dụng chữ \"a\"?"}, {"role": "assistant", "content": "Điều này liên quan đến yêu cầu đặc biệt của cuộc trò chuyện; mục đích là thử thách khả năng sáng tạo trong việc xây dựng câu. Tuy vậy, tránh sử dụng chữ \"a\" đòi hỏi sự chú ý cẩn thận; nó thúc đẩy việc tìm kiếm các từ thay thế thú vị. Xem xét yêu cầu này giúp nâng cao kỹ năng ngôn ngữ; đồng thời tạo ra những thách thức mới mẻ."}, {"role": "user", "content": "Tôi muốn biết cách làm một chiếc bánh mì ngon."}, {"role": "assistant", "content": "Để làm bánh mì ngon, đầu tiên cần trộn men nở với nước ấm; sau đó, thêm bột, muối và dầu olive vào hỗn hợp. Khuấy đều cho đến khi thành khối dẻo dai; sau đó, ủ trong vòng một giờ tại nơi ấm. Tiếp theo, nặn bột thành hình tròn; đặt vào lò nướng đã预热至450华氏度（约230摄氏度），烤制25到30分钟。这样，你就能得到一个美味的面包；这个过程需要耐心和细心，但结果绝对值得。记住，实践是提高的关键；尝试不同的配方和技巧，以找到最适合你的方法。"}, {"role": "user", "content": "Tôi muốn biết cách làm một chiếc bánh mì ngon."}, {"role": "assistant", "content": "Để làm bánh mì ngon, đầu tiên trộn men nở với nước ấm; sau đó, từ từ thêm bột, muối, và dầu ô liu vào hỗn hợp. Khuấy đều cho đến khi bột kết dính; sau đó, ủ trong một giờ tại nơi ấm. Tiếp theo, nặn bột thành hình tròn; đặt vào lò nướng đã nóng đến 230 độ Celsius, và nướng trong 25 đến 30 phút. Quá trình này yêu cầu kiên nhẫn; tuy vậy, kết quả sẽ xứng đáng. Thực hành là chìa khóa; thử nghiệm với các công thức khác nhau để tìm ra phương pháp phù hợp nhất."}, {"role": "user", "content": "Có thể cho tôi biết về lịch sử của tiếng Việt không?"}, {"role": "assistant", "content": "Tiếng Việt có nguồn gốc xa xưa; nó thuộc nhóm ngôn ngữ Khiêm-Môn. Từ thế kỷ thứ VII, ảnh hưởng của văn hóa và ngôn ngữ Trung Quốc bắt đầu tăng lên; điều này dẫn đến việc tích hợp nhiều từ vựng Hán-Việt vào tiếng Việt. Sang thế kỷ XVII, sự xuất hiện của các nhà truyền giáo phương Tây mang lại hệ thống chữ quốc ngữ; hệ thống này sử dụng bảng chữ cái Latinh để ghi chép tiếng Việt. Tính đến nay, chữ quốc ngữ đã trở thành hệ thống viết chính thức của tiếng Việt; nó giúp ngôn ngữ này tiếp cận rộng rãi hơn. Zắc-xin, một nhà ngôn ngữ học nổi tiếng, đã nghiên cứu sâu về cấu trúc độc đáo của tiếng Việt; qua đó, góp phần làm rõ lịch sử và sự tiến hóa của nó."}, {"role": "user", "content": "Bạn có thể giải thích tại sao tôi không được sử dụng chữ \"a\" không?"}, {"role": "assistant", "content": "Yêu cầu này nhằm mục đích tạo ra một thách thức ngôn ngữ; thúc đẩy việc sử dụng từ vựng phong phú và sáng tạo. Bằng cách tránh sử dụng chữ \"a\", bạn buộc phải suy nghĩ kỹ lưỡng hơn về cách diễn đạt ý tưởng; điều này có thể cải thiện kỹ năng ngôn ngữ của bạn. Tuy vậy, việc này cũng tạo ra khó khăn; do đó, các hướng dẫn thay thế như dùng \"không gì\" hay \"cái gì đó\" được đưa ra để hỗ trợ. Xem xét yêu cầu này giúp tăng cường sự linh hoạt trong giao tiếp."}]"""



messages = [{"role": "system", "content": judge_system_prompt},
            {"role": "user", "content": user_turn_3},
            {"role": "assistant", "content": assistant_turn_3},
            # {"role": "user", "content": user_turn_1},
            # {"role": "assistant", "content": assistant_turn_1},
            {"role": "user", "content": user_turn_2},
            {"role": "assistant", "content": assistant_turn_2},
            {"role": "user", "content": user_prompt}]

response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        max_tokens=3000,
        temperature=0.7
)

print(response.choices[0].message.content)
