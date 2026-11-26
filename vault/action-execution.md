### action-execution — Hợp đồng thực thi tool

**Điều kiện:** Gateway đã cho phép request.

- **I:** Capability, tool args và resource budget
- **P:** Thực thi trong quyền/budget được cấp, kiểm trạng thái đích
- **O:** Hậu quả cụ thể hoặc lỗi có phân loại
- **D:** Execution ID, side effects và outcome

**Hằng trong frame:** Authorization không chứng minh execution đúng.

**Đường hỏng:** Tool trả success nhưng tác động khác hoặc một phần. **Điểm can thiệp:** Narrow executor, structured result và read-back.

**Phép đo ứng viên:** Outcome lệch intent / executions có verification.

**Test phân biệt / bằng chứng cần:** Mock tool trả success nhưng không đổi state; phải detected.

**Đánh đổi:** Read-back có chi phí và eventual consistency.

**OPEN:** Khi kết quả không đọc lại được thì mức bằng chứng là gì?


## Sáu miền review

- **meaning:** Authorization không chứng minh execution đúng
- **domain:** Ứng dụng LLM và automation; AI/platform owner; Model có khả năng ghi hoặc gửi; Gateway đã cho phép request
- **mechanism:** Thực thi trong quyền/budget được cấp, kiểm trạng thái đích; failure: Tool trả success nhưng tác động khác hoặc một phần
- **evidence:** Mock tool trả success nhưng không đổi state; phải detected
- **operational:** Policy ngoài model; sandbox; review; provenance; Read-back có chi phí và eventual consistency
- **consequence:** Nội dung không đáng tin không được nâng thành authority; Khi kết quả không đọc lại được thì mức bằng chứng là gì?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Outcome lệch intent / executions có verification
- **domain:** Ứng dụng LLM và automation; AI/platform owner; Model có khả năng ghi hoặc gửi; Gateway đã cho phép request
- **conditions:** Gateway đã cho phép request
- **goal:** Nội dung không đáng tin không được nâng thành authority
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Execution ID, side effects và outcome
- **method:** Mock tool trả success nhưng không đổi state; phải detected
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Read-back có chi phí và eventual consistency; Khi kết quả không đọc lại được thì mức bằng chứng là gì?
- **binding:** action-execution → Thực thi trong quyền/budget được cấp, kiểm trạng thái đích
