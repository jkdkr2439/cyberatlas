### action-toctou — Môi trường đổi sau approval

**Điều kiện:** Giữa review và execution có thời gian.

- **I:** Approved snapshot và target state hiện tại
- **P:** Kiểm lại precondition quan trọng tại commit
- **O:** Hành động chỉ chạy nếu context còn khớp
- **D:** Resource version và expiry result

**Hằng trong frame:** Approval đúng quá khứ không tự đúng hiện tại.

**Đường hỏng:** Target owner/quyền/giá trị đổi nhưng lệnh vẫn chạy. **Điểm can thiệp:** Precondition, expiry và re-approval khi cần.

**Phép đo ứng viên:** Hành động commit với precondition lỗi / race fixtures.

**Test phân biệt / bằng chứng cần:** Đổi owner hoặc target version sau review.

**Đánh đổi:** Kiểm lại nhiều dễ gây review fatigue.

**OPEN:** Điều kiện nào đổi là vô hại, điều kiện nào bắt buộc hỏi lại?


## Sáu miền review

- **meaning:** Approval đúng quá khứ không tự đúng hiện tại
- **domain:** Ứng dụng LLM và automation; AI/platform owner; Model có khả năng ghi hoặc gửi; Agent chuẩn bị hành động có hậu quả; Giữa review và execution có thời gian
- **mechanism:** Kiểm lại precondition quan trọng tại commit; failure: Target owner/quyền/giá trị đổi nhưng lệnh vẫn chạy
- **evidence:** Đổi owner hoặc target version sau review
- **operational:** Policy ngoài model; sandbox; review; provenance; Kiểm lại nhiều dễ gây review fatigue
- **consequence:** Nội dung không đáng tin không được nâng thành authority; Điều kiện nào đổi là vô hại, điều kiện nào bắt buộc hỏi lại?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Hành động commit với precondition lỗi / race fixtures
- **domain:** Ứng dụng LLM và automation; AI/platform owner; Model có khả năng ghi hoặc gửi; Agent chuẩn bị hành động có hậu quả; Giữa review và execution có thời gian
- **conditions:** Giữa review và execution có thời gian
- **goal:** Nội dung không đáng tin không được nâng thành authority
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Resource version và expiry result
- **method:** Đổi owner hoặc target version sau review
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Kiểm lại nhiều dễ gây review fatigue; Điều kiện nào đổi là vô hại, điều kiện nào bắt buộc hỏi lại?
- **binding:** action-toctou → Kiểm lại precondition quan trọng tại commit
