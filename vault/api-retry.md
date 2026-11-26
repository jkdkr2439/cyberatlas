### api-retry — Retry và idempotency

**Điều kiện:** Mạng timeout rồi client gửi lại.

- **I:** Operation ID, body và principal
- **P:** Deduplicate nguyên tử theo đúng scope
- **O:** Một hiệu ứng nghiệp vụ cho một ý định
- **D:** Idempotency record và kết quả gốc

**Hằng trong frame:** Cùng key khác nội dung phải có cách xử lý rõ.

**Đường hỏng:** Retry nhân đôi thanh toán hoặc key dùng xuyên tenant. **Điểm can thiệp:** Atomic uniqueness, body binding, TTL đủ dài.

**Phép đo ứng viên:** Hiệu ứng thừa / nhóm retry trong test.

**Test phân biệt / bằng chứng cần:** Gửi đồng thời và mô phỏng crash sau commit trước response.

**Đánh đổi:** Giữ record lâu tốn storage và dữ liệu.

**OPEN:** Exactly-once ở đâu chỉ là giả định của ứng dụng?

**Liên hệ có điều kiện:**

- `ir-contain` — Tự động ứng phó cần tránh retry gây hiệu ứng lặp ngoài ý định.
- `F32` — Retry, tool recursion, memory growth và budget exhaustion có stop condition nào ngoài model?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Một hiệu ứng nghiệp vụ cho một ý định / Retry nhân đôi thanh toán hoặc key dùng xuyên tenant
- **domain:** Chốt population và giới hạn: API đồng bộ/bất đồng bộ; product team; Mạng timeout rồi client gửi lại
- **mechanism:** Control có giữ invariant này không? Cùng key khác nội dung phải có cách xử lý rõ
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Gửi đồng thời và mô phỏng crash sau commit trước response
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Transaction store; rate budget; test nghiệp vụ; Retry; concurrency; tenant; giá; số lượng
- **consequence:** Đạt Giao dịch giữ đúng quyền, thứ tự và giới hạn nhưng phải theo dõi Giữ record lâu tốn storage và dữ liệu

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Hiệu ứng thừa / nhóm retry trong test
- **domain:** API đồng bộ/bất đồng bộ; product team; Mạng timeout rồi client gửi lại
- **conditions:** Mạng timeout rồi client gửi lại
- **goal:** Giao dịch giữ đúng quyền, thứ tự và giới hạn
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Idempotency record và kết quả gốc; bằng chứng test: Gửi đồng thời và mô phỏng crash sau commit trước response
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Giữ record lâu tốn storage và dữ liệu; Exactly-once ở đâu chỉ là giả định của ứng dụng?
- **binding:** api-retry → điểm thực thi: Deduplicate nguyên tử theo đúng scope
