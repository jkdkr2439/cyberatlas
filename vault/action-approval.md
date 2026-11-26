### action-approval — Phê duyệt gắn hành động cụ thể

**Điều kiện:** Agent chuẩn bị hành động có hậu quả.

- **I:** Preview args, target và user intent
- **P:** Cho reviewer xem đúng dữ liệu/đích/hậu quả rồi bind approval
- **O:** Approval có scope, version và expiry
- **D:** Approved action representation

**Hằng trong frame:** “Đồng ý” chung không cấp quyền cho mọi hành động về sau.

**Đường hỏng:** Review mô tả một việc, tool thực thi việc khác. **Điểm can thiệp:** Immutable approval contract.

**Phép đo ứng viên:** Execute khác approved intent / approval tests.

**Test phân biệt / bằng chứng cần:** Duyệt gửi bản A đến B rồi đổi file hoặc người nhận.

**Đánh đổi:** Preview đầy đủ có thể lộ dữ liệu cho reviewer không phù hợp.

**OPEN:** Ai có quyền duyệt dữ liệu của người khác?


## Sáu miền review

- **meaning:** “Đồng ý” chung không cấp quyền cho mọi hành động về sau
- **domain:** Ứng dụng LLM và automation; AI/platform owner; Model có khả năng ghi hoặc gửi; Agent chuẩn bị hành động có hậu quả
- **mechanism:** Cho reviewer xem đúng dữ liệu/đích/hậu quả rồi bind approval; failure: Review mô tả một việc, tool thực thi việc khác
- **evidence:** Duyệt gửi bản A đến B rồi đổi file hoặc người nhận
- **operational:** Policy ngoài model; sandbox; review; provenance; Preview đầy đủ có thể lộ dữ liệu cho reviewer không phù hợp
- **consequence:** Nội dung không đáng tin không được nâng thành authority; Ai có quyền duyệt dữ liệu của người khác?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Execute khác approved intent / approval tests
- **domain:** Ứng dụng LLM và automation; AI/platform owner; Model có khả năng ghi hoặc gửi; Agent chuẩn bị hành động có hậu quả
- **conditions:** Agent chuẩn bị hành động có hậu quả
- **goal:** Nội dung không đáng tin không được nâng thành authority
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Approved action representation
- **method:** Duyệt gửi bản A đến B rồi đổi file hoặc người nhận
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Preview đầy đủ có thể lộ dữ liệu cho reviewer không phù hợp; Ai có quyền duyệt dữ liệu của người khác?
- **binding:** action-approval → Cho reviewer xem đúng dữ liệu/đích/hậu quả rồi bind approval
