### vul-fix — Sửa và kiểm lại

**Điều kiện:** Ticket được đánh dấu resolved.

- **I:** Patch/config và finding gốc
- **P:** Kiểm artifact/state thực và test lại điều kiện lỗi
- **O:** Finding thật sự không tái hiện trong scope
- **D:** Fix receipt, version và retest result

**Hằng trong frame:** Đóng ticket không phải bằng chứng sửa xong.

**Đường hỏng:** Patch chưa restart; node khác chưa cập nhật. **Điểm can thiệp:** Retest ở asset đúng và check drift.

**Phép đo ứng viên:** Finding reopen / finding từng xác nhận fixed.

**Test phân biệt / bằng chứng cần:** Một node cố tình chưa rollout trong lab.

**Đánh đổi:** Retest tăng thời gian và tải hệ.

**OPEN:** Mitigation tạm có hết hạn hoặc mất hiệu lực khi đổi route?

**Liên hệ có điều kiện:**

- `F19` — Scope, phối hợp vá, bằng chứng không gây hại và thời gian disclosure được quyết định thế nào?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Finding thật sự không tái hiện trong scope / Patch chưa restart; node khác chưa cập nhật
- **domain:** Chốt population và giới hạn: Asset-vulnerability pair; VM team; Ticket được đánh dấu resolved
- **mechanism:** Control có giữ invariant này không? Đóng ticket không phải bằng chứng sửa xong
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Một node cố tình chưa rollout trong lab
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Scanner; inventory; change window; kiểm chứng sửa; Reachability; exploitability; control; tuổi tồn tại
- **consequence:** Đạt Giảm đường gây hại có ý nghĩa trong scope nhưng phải theo dõi Retest tăng thời gian và tải hệ

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Finding reopen / finding từng xác nhận fixed
- **domain:** Asset-vulnerability pair; VM team; Ticket được đánh dấu resolved
- **conditions:** Ticket được đánh dấu resolved
- **goal:** Giảm đường gây hại có ý nghĩa trong scope
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Fix receipt, version và retest result; bằng chứng test: Một node cố tình chưa rollout trong lab
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Retest tăng thời gian và tải hệ; Mitigation tạm có hết hạn hoặc mất hiệu lực khi đổi route?
- **binding:** vul-fix → điểm thực thi: Kiểm artifact/state thực và test lại điều kiện lỗi
