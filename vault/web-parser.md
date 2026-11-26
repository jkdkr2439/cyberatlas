### web-parser — Sai khác giữa các parser

**Điều kiện:** Proxy và backend cùng diễn giải request.

- **I:** Byte stream và metadata
- **P:** Chuẩn hóa theo một contract end-to-end
- **O:** Một cách hiểu nhất quán về request
- **D:** Raw/normalized correlation khi cần

**Hằng trong frame:** Các lớp phải thống nhất ranh giới và encoding.

**Đường hỏng:** Hai parser hiểu length hoặc path khác nhau. **Điểm can thiệp:** Giảm ambiguity, cập nhật parser và test xuyên lớp.

**Phép đo ứng viên:** Ca parser differential bất đồng / corpus được thử.

**Test phân biệt / bằng chứng cần:** Corpus không chứa dữ liệu thật; so frontend/backend interpretation.

**Đánh đổi:** Lưu raw request gây rủi ro dữ liệu.

**OPEN:** WebSocket, HTTP upgrade và protocol translation có khác?

**Liên hệ có điều kiện:**

- `net-egress` — Chuẩn hóa URL sai có thể làm policy và connector hiểu khác đích.
- `F10` — Parser, converter, metadata và antivirus tạo những process con với quyền gì?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Một cách hiểu nhất quán về request / Hai parser hiểu length hoặc path khác nhau
- **domain:** Chốt population và giới hạn: Parser và trình duyệt; AppSec; Proxy và backend cùng diễn giải request
- **mechanism:** Control có giữ invariant này không? Các lớp phải thống nhất ranh giới và encoding
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Corpus không chứa dữ liệu thật; so frontend/backend interpretation
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Secure API; code review; kiểm thử ngữ cảnh; Encoding; context; proxy; framework; phiên bản
- **consequence:** Đạt Dữ liệu không chuyển thành lệnh ngoài ý định nhưng phải theo dõi Lưu raw request gây rủi ro dữ liệu

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Ca parser differential bất đồng / corpus được thử
- **domain:** Parser và trình duyệt; AppSec; Proxy và backend cùng diễn giải request
- **conditions:** Proxy và backend cùng diễn giải request
- **goal:** Dữ liệu không chuyển thành lệnh ngoài ý định
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Raw/normalized correlation khi cần; bằng chứng test: Corpus không chứa dữ liệu thật; so frontend/backend interpretation
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Lưu raw request gây rủi ro dữ liệu; WebSocket, HTTP upgrade và protocol translation có khác?
- **binding:** web-parser → điểm thực thi: Chuẩn hóa theo một contract end-to-end
