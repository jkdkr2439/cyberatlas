### auth-policy — Quyền hiệu lực

**Điều kiện:** Nhiều role và policy chồng nhau.

- **I:** Membership, resource policy và context
- **P:** Kết hợp luật theo precedence đã định
- **O:** Effective permissions
- **D:** Policy version và quyết định

**Hằng trong frame:** Quyền phải được xét sau mọi phép kế thừa.

**Đường hỏng:** Deny trong một lớp bị allow ở lớp khác hiểu sai. **Điểm can thiệp:** Policy simulation và test precedence.

**Phép đo ứng viên:** Đường quyền vượt intent / đường được kiểm thử.

**Test phân biệt / bằng chứng cần:** Kết hợp hai role riêng lẻ ít quyền nhưng hợp lại nguy hiểm.

**Đánh đổi:** Mô hình biểu đạt mạnh khó giải thích và bảo trì.

**OPEN:** Đường quyền nào phụ thuộc thuộc tính đã cũ?

**Liên hệ có điều kiện:**

- `cld-policy` — Quyền hiệu lực phụ thuộc kết hợp policy và đường cấp quyền.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Effective permissions / Deny trong một lớp bị allow ở lớp khác hiểu sai
- **domain:** Chốt population và giới hạn: API và kho dữ liệu; chủ sản phẩm; Nhiều role và policy chồng nhau
- **mechanism:** Control có giữ invariant này không? Quyền phải được xét sau mọi phép kế thừa
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Kết hợp hai role riêng lẻ ít quyền nhưng hợp lại nguy hiểm
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Policy engine; test matrix; owner dữ liệu; Role; thuộc tính; ownership; tenant; thời điểm commit
- **consequence:** Đạt Chủ thể chỉ tác động đúng đối tượng và hành động được phép nhưng phải theo dõi Mô hình biểu đạt mạnh khó giải thích và bảo trì

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Đường quyền vượt intent / đường được kiểm thử
- **domain:** API và kho dữ liệu; chủ sản phẩm; Nhiều role và policy chồng nhau
- **conditions:** Nhiều role và policy chồng nhau
- **goal:** Chủ thể chỉ tác động đúng đối tượng và hành động được phép
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Policy version và quyết định; bằng chứng test: Kết hợp hai role riêng lẻ ít quyền nhưng hợp lại nguy hiểm
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Mô hình biểu đạt mạnh khó giải thích và bảo trì; Đường quyền nào phụ thuộc thuộc tính đã cũ?
- **binding:** auth-policy → điểm thực thi: Kết hợp luật theo precedence đã định
