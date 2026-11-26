### web-xss — Ngữ cảnh output trình duyệt

**Điều kiện:** Dữ liệu hiển thị trong HTML/JS/URL.

- **I:** Untrusted content và vị trí render
- **P:** Encode/sanitize đúng context và policy
- **O:** Nội dung hiển thị không tự thực thi ngoài ý định
- **D:** Context và kiểm thử render

**Hằng trong frame:** Encode cho HTML không tự đúng trong JS hay URL.

**Đường hỏng:** Dữ liệu được đánh dấu safe sai hoặc DOM sink nguy hiểm. **Điểm can thiệp:** Context-aware escaping, safe DOM API, CSP bổ sung.

**Phép đo ứng viên:** Render context nguy hiểm đã test / context trong inventory.

**Test phân biệt / bằng chứng cần:** Kiểm tra cùng input ở text, attribute và script context.

**Đánh đổi:** Sanitize mạnh có thể bỏ nội dung hợp lệ.

**OPEN:** Stored content cũ và editor rich text được xử lý thế nào?

**Liên hệ có điều kiện:**

- `ses-concurrency` — Script ngoài ý định có thể hành động bằng phiên người dùng dù cookie khó đọc.
- `F09` — Origin/site, cookie, storage và messaging tạo ranh giới khác nhau thế nào?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Nội dung hiển thị không tự thực thi ngoài ý định / Dữ liệu được đánh dấu safe sai hoặc DOM sink nguy hiểm
- **domain:** Chốt population và giới hạn: Parser và trình duyệt; AppSec; Dữ liệu hiển thị trong HTML/JS/URL
- **mechanism:** Control có giữ invariant này không? Encode cho HTML không tự đúng trong JS hay URL
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Kiểm tra cùng input ở text, attribute và script context
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Secure API; code review; kiểm thử ngữ cảnh; Encoding; context; proxy; framework; phiên bản
- **consequence:** Đạt Dữ liệu không chuyển thành lệnh ngoài ý định nhưng phải theo dõi Sanitize mạnh có thể bỏ nội dung hợp lệ

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Render context nguy hiểm đã test / context trong inventory
- **domain:** Parser và trình duyệt; AppSec; Dữ liệu hiển thị trong HTML/JS/URL
- **conditions:** Dữ liệu hiển thị trong HTML/JS/URL
- **goal:** Dữ liệu không chuyển thành lệnh ngoài ý định
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Context và kiểm thử render; bằng chứng test: Kiểm tra cùng input ở text, attribute và script context
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Sanitize mạnh có thể bỏ nội dung hợp lệ; Stored content cũ và editor rich text được xử lý thế nào?
- **binding:** web-xss → điểm thực thi: Encode/sanitize đúng context và policy
