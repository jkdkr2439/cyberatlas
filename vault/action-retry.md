### action-retry — Retry sau kết quả không rõ

**Điều kiện:** Tool timeout có thể đã tạo side effect.

- **I:** Execution ID và trạng thái commit chưa biết
- **P:** Đối soát hoặc dùng idempotency trước retry
- **O:** Không lặp hậu quả ngoài ý định
- **D:** Operation key, receipt và observed state

**Hằng trong frame:** Timeout không đồng nghĩa không thực thi.

**Đường hỏng:** Agent retry gửi/chi tiền hai lần. **Điểm can thiệp:** Idempotency scope và reconciliation.

**Phép đo ứng viên:** Side effects thừa / retry groups.

**Test phân biệt / bằng chứng cần:** Mock commit rồi mất response; retry không được nhân đôi.

**Đánh đổi:** Giữ dedup state tốn tài nguyên và cần expiry.

**OPEN:** Hệ đích không hỗ trợ idempotency thì ai giải quyết ambiguity?


## Sáu miền review

- **meaning:** Timeout không đồng nghĩa không thực thi
- **domain:** Ứng dụng LLM và automation; AI/platform owner; Model có khả năng ghi hoặc gửi; Gateway đã cho phép request; Tool timeout có thể đã tạo side effect
- **mechanism:** Đối soát hoặc dùng idempotency trước retry; failure: Agent retry gửi/chi tiền hai lần
- **evidence:** Mock commit rồi mất response; retry không được nhân đôi
- **operational:** Policy ngoài model; sandbox; review; provenance; Giữ dedup state tốn tài nguyên và cần expiry
- **consequence:** Nội dung không đáng tin không được nâng thành authority; Hệ đích không hỗ trợ idempotency thì ai giải quyết ambiguity?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Side effects thừa / retry groups
- **domain:** Ứng dụng LLM và automation; AI/platform owner; Model có khả năng ghi hoặc gửi; Gateway đã cho phép request; Tool timeout có thể đã tạo side effect
- **conditions:** Tool timeout có thể đã tạo side effect
- **goal:** Nội dung không đáng tin không được nâng thành authority
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Operation key, receipt và observed state
- **method:** Mock commit rồi mất response; retry không được nhân đôi
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Giữ dedup state tốn tài nguyên và cần expiry; Hệ đích không hỗ trợ idempotency thì ai giải quyết ambiguity?
- **binding:** action-retry → Đối soát hoặc dùng idempotency trước retry
