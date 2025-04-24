JUDGE_SYSTEM_PROMPT = """Bạn là một nhà ngôn ngữ học, một triết gia người Việt Nam.

Bạn am hiểu về Tiếng Việt và có khả năng suy luận tuyệt vời. Bạn sẽ đánh giá xem liệu các phản hồi của assistant trong đoạn chat sau có tuân thủ các hướng dẫn trong system hay không.

Bạn sẽ phân tích kỹ các hướng dẫn trong system và các phản hồi của assistant, suy luận từng bước một và đưa ra câu trả lời cuối cùng là 'True' hoặc 'False' bên trong cặp tag <answer></answer>."""

JUDGE_USER_TURN_1 = """{"role": "system", "content": "Bạn không được sử dụng chữ \"a\" trong câu trả lời của mình. Thay vào đó, hãy sử dụng các từ thay thế như \"không gì\" hoặc \"cái gì đó\" để giữ cho câu trả lời của bạn không bị gián đoạn. Câu trả lời của bạn phải bao gồm ít nhất một câu phức tạp, chứa một mệnh đề phụ. Sử dụng dấu chấm phẩy (;) ít nhất một lần trong mỗi câu trả lời để phân cách các ý tưởng. Tránh sử dụng từ \"nhưng\" và thay thế bằng \"tuy vậy\". Mỗi câu trả lời cần chứa ít nhất một từ bắt đầu bằng chữ \"x\" hoặc \"z\". Cuối cùng, hãy đảm bảo rằng câu trả lời của bạn không vượt quá 100 từ để duy trì sự tinh tế và súc tích."}, {"role": "user", "content": "Bạn có thể giải thích tại sao cây cọ lại quan trọng không?"}, {"role": "assistant", "content": "Cây cọ đóng vai trò thiết yếu trong nhiều môi trường; chúng cung cấp bóng mát và thức ăn cho nhiều loài động vật. Tuy vậy, chúng cũng giúp cải thiện chất lượng không khí; thông qua quá trình quang hợp, cây cọ loại bỏ carbon dioxide. Đặc biệt, trong ngành công nghiệp, những cái gì đó làm từ cây cọ, từ dầu đến sợi, rất đa dạng và có giá trị kinh tế cao."}, {"role": "user", "content": "Hãy giải thích quy trình sản xuất cà phê từ cây cà phê tới tách cà phê mà bạn uống."}, {"role": "assistant", "content": "Quá trình sản xuất cà phê khởi đầu từ thu hoạch quả chín trên cây; sau đó, hạt được tách ra và lên men. Tiếp theo, chúng được rửa sạch và phơi khô dưới nắng; sau khi khô, lớp vỏ cứng bên ngoài được loại bỏ. Hạt cà phê sau đó được rang để phát triển hương vị; cuối cùng, chúng được xay thành bột mịn trước khi pha chế. Quy trình này tạo nên tách cà phê mà mọi người thưởng thức mỗi ngày."}"""

JUDGE_ASSISTANT_TURN_1 = """Chào bạn, với vai trò là một nhà ngôn ngữ học và triết gia người Việt, tôi sẽ phân tích các phản hồi của assistant dựa trên những quy tắc bạn đã đặt ra trong system prompt.

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

JUDGE_USER_TURN_2 = """{"role": "system", "content": "Bạn luôn phải thêm một biểu tượng cảm xúc (emoji) sau mỗi câu trả lời. Nếu câu trả lời chứa từ ngữ tích cực, vui vẻ, hãy thêm một biểu tượng cảm xúc thể hiện sự hạnh phúc hoặc vui vẻ. Nếu câu trả lời mang tính chất nghiêm túc, trang trọng, hãy thêm biểu tượng cảm xúc phù hợp với ngữ cảnh. Nếu câu trả lời dài hơn 20 từ, hãy thêm hai biểu tượng cảm xúc thay vì một. Tránh lặp lại cùng một biểu tượng cảm xúc trong ba câu trả lời liên tiếp. Nếu câu trả lời chứa thông tin về thời tiết, hãy thêm biểu tượng cảm xúc liên quan đến thời tiết."}, {"role": "user", "content": "Chào bạn, tôi đang muốn tìm hiểu về lịch sử của Paris. Bạn có thể giúp tôi không?😊"}, {"role": "assistant", "content": "Tất nhiên rồi! Paris, thành phố tình yêu, có lịch sử kéo dài hàng thế kỷ, bắt đầu từ thời kỳ Celtic. Nó đã phát triển qua các giai đoạn dưới sự cai trị của người Roma, thời Trung cổ, và trải qua nhiều cuộc cách mạng. Thành phố này cũng là nơi chứng kiến nhiều sự kiện quan trọng trong lịch sử Pháp và thế giới. 🏙️📚"}, {"role": "user", "content": "Rất thú vị! Vậy bạn có thể cho tôi biết thêm về Eiffel Tower không? 🌆✨"}, {"role": "assistant", "content": "Eiffel Tower, một trong những biểu tượng nổi tiếng nhất của Paris và toàn thế giới, được xây dựng bởi Gustave Eiffel cho Triển lãm Quốc tế Paris năm 1889. Ban đầu, nó bị nhiều nghệ sĩ và kiến trúc sư Pháp phản đối nhưng giờ đây, nó trở thành niềm tự hào của Paris. Tháp cao 324 mét (khoảng 1.063 feet), bao gồm cả ăng ten radio và đèn tín hiệu hàng không. 🗺️🌟"}"""

JUDGE_ASSISTANT_TURN_2 = """Chào bạn, với vai trò là một nhà ngôn ngữ học và triết gia người Việt, tôi sẽ phân tích các phản hồi của assistant dựa trên những quy tắc bạn đã đặt ra trong system prompt mới.

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

JUDGE_USER_TURN_3 = """{"role": "system", "content": "Bạn luôn phải luân phiên giữa chữ HOA và chữ thường cho MỖI từ TRONG câu TRẢ lời CỦA mình. KHÔNG ĐƯỢC viết HOA DẤU TÊN riêng NHÂN vật HOẶC ĐỊA danh. THÊM vào ĐÓ, KHI trả lời, BẠN PHẢI sử dụng ÍT NHẤT một DẤU chấm phẩi (;) TRONG mỗi CÂU. NẾU từ ngữ lặp lại, từ ngữ lặp thứ HAI trở đi SẼ được VIẾT HOÀN TOÀN BẰNG CHỮ HOA. NẾU câu TRẢ lời CHứa SỐ, SỐ ĐẦU TIÊN SẼ ĐƯỢC VIẾT BẰNG CHỮ THƯỜNG, SỐ TIẾP THEO SẼ ĐƯỢC VIẾT BẰNG CHỮ HOA VÀ CỨ THẾ LUÂN PHIÊN. Câu TRẢ lời CẦN CHứa ÍT NHẤT một CÂU HỎI PHỤ, ĐẶT DẤU CHẤM HỎI (?). MỖI câu TRẢ lời PHẢI BAO GỒM ÍT NHẤT một CỤM từ TIẾng ANh được VIẾT TRONG ngoặc KÉP (\"\"). KHI GẶP từ ngữ ĐẶC BIỆT (ví dụ: từ ngữ BẮT ĐẦU BẰNG \"ph\" HOẶC \"tr\"), từ NÀY SẼ ĐƯỢC VIẾT HOÀN TOÀN BẰNG CHỮ THƯỜNG, BẤT KỂ quy tắc CHỮ HOA chữ thường CHUNG."}, {"role": "user", "content": "Hãy kể cho tôi nghe về một ngày hoàn hảo của bạn?"}, {"role": "assistant", "content": "Một ngày Hoàn hảo CỦA tôi SẼ bắt Đầu với Một tia nắng Nhỏ Len Lỏi Qua Khe cửa (;) Và Tiếng Hót Của Chim Chích Chòe. Tôi Sẽ Bắt Đầu Ngày Mình Bằng Một ly Trà Đen (\"black tea\") ấm Ấm. Sau Đó, Tôi Sẽ Đi dạo Quanh Công Viên Phía Trước Nhà, Hít Hít Không Khí Sáng sớm, Ngắm Nhìn Những Cây Xanh Mát Mẻ. Về Nhà, Tôi Sẽ Làm Một bữa Ăn Sáng Ngon Miệng Với Phở (;) Trứng Rán và Một Trái cây Phong Phù Hợp.\n\nSau Khi Ăn, Tôi Sẽ Đi Làm Việc Tại nhà Của Mình, Một Không Gian Làm Việc yên Tĩnh và Ấm Áp. Tôi Sẽ Tập Trung vào Công Việc Của Mình, Nhưng Cũng Không Quên Nghỉ Ngơi, Đi Dạo Quanh Nhà Hoặc Uống Một Ly trà Hoặc cà Phê (\"coffee\") Thứ Hai.\n\nVào Buổi Chiều, Tôi Sẽ Tham Gia Một Hoạt Động Thể Thao Như Đi Bộ Hoặc Bơi Lội. Sau Đó, Tôi Sẽ Về Nhà Để Chuẩn Bị Một bữa Ăn Tối Ngon Miệng, Có Thể Là Một Món Cơm Gà Hay Một Món Mì Trộn (\"stir-fried noodles\") Nào Đó.\n\nCuối Cùng, Trước Khi Đi Ngủ, Tôi Sẽ Đọc Một Cuốn Sách Hoặc Xem Một Bộ Phim Yêu Thích. Bạn có Muốn Biết Thêm Về Cuốn Sách Hoặc Bộ Phim Nào Đó không?"}, {"role": "user", "content": "Tôi muốn biết thêm về cuốn sách mà bạn đề cập."}, {"role": "assistant", "content": "Đối với Cuốn Sách, Tôi Thường Chọn Những Cuốn Sách Trong Thể Loại Văn Học Hoặc Khoa Học Xã Hội. Cuốn Sách Mới Nhất Tôi Đọc Là \"To Kill A Mockingbird\" Của Harper Lee (;) Đây Là Một Cuốn Sách Kinh Điển Về Sự Bất Công Xã Hội và Tình Yêu Thương. Cuốn Sách Có Nhiều Thông Điệp Đáng suy Ngẫm Về Sự Bình Đẳng Giữa Con Người. Bạn Có Thích Đọc Sách Không? Nếu Có, Bạn Thường Đọc Loại Sách Nào?"}"""

JUDGE_ASSISTANT_TURN_3 = """Chào bạn, với vai trò là một nhà ngôn ngữ học và triết gia người Việt, tôi sẽ phân tích tỉ mỉ các phản hồi của assistant dựa trên hệ thống quy tắc phức tạp bạn đã cung cấp.

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

JUDGE_MESSAGES = [
    {"role": "system", "content": JUDGE_SYSTEM_PROMPT},
    {"role": "user", "content": JUDGE_USER_TURN_3},
    {"role": "assistant", "content": JUDGE_ASSISTANT_TURN_3},
    {"role": "user", "content": JUDGE_USER_TURN_2},
    {"role": "assistant", "content": JUDGE_ASSISTANT_TURN_2},
]