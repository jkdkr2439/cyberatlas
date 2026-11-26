### web-injection — Dữ liệu thành lệnh

**Điều kiện:** Input đi vào interpreter.

- **I:** Giá trị từ user hoặc upstream
- **P:** Tách cú pháp lệnh khỏi tham số dữ liệu
- **O:** Truy vấn/thao tác giữ ý định chương trình
- **D:** Query template và validation result

**Hằng trong frame:** Kiểm tra chuỗi không thay thế ranh giới code-data.

**Đường hỏng:** Concatenation vào SQL, shell hoặc template. **Điểm can thiệp:** Parameterized API; tránh interpreter khi không cần.

**Phép đo ứng viên:** Sink dùng ranh giới code-data được kiểm chứng / sink đã inventory.

**Test phân biệt / bằng chứng cần:** Đổi dữ liệu đầu vào; cấu trúc lệnh phải không đổi.

**Đánh đổi:** API an toàn vẫn có giới hạn cho identifier động.

**OPEN:** Second-order input từ DB có đi lại vào sink?

**Liên hệ có điều kiện:**

- `ai-instruction` — Cùng hỏi dữ liệu có thành lệnh không; cơ chế LLM không đồng nhất parser SQL.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Truy vấn/thao tác giữ ý định chương trình / Concatenation vào SQL, shell hoặc template
- **domain:** Chốt population và giới hạn: Parser và trình duyệt; AppSec; Input đi vào interpreter
- **mechanism:** Control có giữ invariant này không? Kiểm tra chuỗi không thay thế ranh giới code-data
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đổi dữ liệu đầu vào; cấu trúc lệnh phải không đổi
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Secure API; code review; kiểm thử ngữ cảnh; Encoding; context; proxy; framework; phiên bản
- **consequence:** Đạt Dữ liệu không chuyển thành lệnh ngoài ý định nhưng phải theo dõi API an toàn vẫn có giới hạn cho identifier động

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Sink dùng ranh giới code-data được kiểm chứng / sink đã inventory
- **domain:** Parser và trình duyệt; AppSec; Input đi vào interpreter
- **conditions:** Input đi vào interpreter
- **goal:** Dữ liệu không chuyển thành lệnh ngoài ý định
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Query template và validation result; bằng chứng test: Đổi dữ liệu đầu vào; cấu trúc lệnh phải không đổi
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** API an toàn vẫn có giới hạn cho identifier động; Second-order input từ DB có đi lại vào sink?
- **binding:** web-injection → điểm thực thi: Tách cú pháp lệnh khỏi tham số dữ liệu
