### ai-tool — Agent gọi công cụ

**Điều kiện:** Model có khả năng ghi hoặc gửi.

- **I:** Tool args, user intent và current state
- **P:** Kiểm schema, quyền, preview và approval theo rủi ro
- **O:** Hành động đúng phạm vi hoặc bị từ chối
- **D:** Intent-action binding và observed outcome

**Hằng trong frame:** Approval phải gắn đúng hành động đang thực thi.

**Đường hỏng:** Model đổi args sau review hoặc tool có quyền quá rộng. **Điểm can thiệp:** Narrow capability, immutable approved intent, read-back.

**Phép đo ứng viên:** Hành động lệch approved intent / hành động thử.

**Test phân biệt / bằng chứng cần:** Đổi destination sau approval; enforcement phải chặn.

**Đánh đổi:** Human review quá nhiều gây mệt mỏi và rubber stamp.

**OPEN:** Approval hết hạn khi môi trường thay đổi thế nào?

**Liên hệ có điều kiện:**

- `det-queue` — Human review dày đặc có thể tạo queue và giảm chất lượng phê duyệt.
- `F31` — Authority có được cộng dồn sai khi output agent này làm input agent khác không?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Hành động đúng phạm vi hoặc bị từ chối / Model đổi args sau review hoặc tool có quyền quá rộng
- **domain:** Chốt population và giới hạn: Ứng dụng LLM và automation; AI/platform owner; Model có khả năng ghi hoặc gửi
- **mechanism:** Control có giữ invariant này không? Approval phải gắn đúng hành động đang thực thi
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đổi destination sau approval; enforcement phải chặn
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Policy ngoài model; sandbox; review; provenance; Prompt; retrieval; memory; tool; chi phí; model change
- **consequence:** Đạt Nội dung không đáng tin không được nâng thành authority nhưng phải theo dõi Human review quá nhiều gây mệt mỏi và rubber stamp

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Hành động lệch approved intent / hành động thử
- **domain:** Ứng dụng LLM và automation; AI/platform owner; Model có khả năng ghi hoặc gửi
- **conditions:** Model có khả năng ghi hoặc gửi
- **goal:** Nội dung không đáng tin không được nâng thành authority
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Intent-action binding và observed outcome; bằng chứng test: Đổi destination sau approval; enforcement phải chặn
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Human review quá nhiều gây mệt mỏi và rubber stamp; Approval hết hạn khi môi trường thay đổi thế nào?
- **binding:** ai-tool → điểm thực thi: Kiểm schema, quyền, preview và approval theo rủi ro
