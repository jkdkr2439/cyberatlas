### sw-design — Yêu cầu bảo mật từ thiết kế

**Điều kiện:** Tính năng mới thay trust boundary.

- **I:** Use case, abuse case và data flow
- **P:** Chuyển hậu quả cần tránh thành yêu cầu testable
- **O:** Requirement gắn owner và acceptance
- **D:** Design decisions và security tests

**Hằng trong frame:** Checklist chung không thay yêu cầu nghiệp vụ.

**Đường hỏng:** Control được thêm sau khi thiết kế đã khóa. **Điểm can thiệp:** Threat modeling theo boundary và scenario.

**Phép đo ứng viên:** Requirement có test phản ví dụ / requirement đã cam kết.

**Test phân biệt / bằng chứng cần:** Đưa vai trò không hợp lệ vào một use case.

**Đánh đổi:** Phân tích sớm tốn thời gian nhưng giảm rework.

**OPEN:** Abuse case nào chưa có tiêu chí đúng/sai?

**Liên hệ có điều kiện:**

- `api-state` — Abuse case nghiệp vụ sinh invariant và test transition.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Requirement gắn owner và acceptance / Control được thêm sau khi thiết kế đã khóa
- **domain:** Chốt population và giới hạn: Thiết kế đến vận hành; engineering; Tính năng mới thay trust boundary
- **mechanism:** Control có giữ invariant này không? Checklist chung không thay yêu cầu nghiệp vụ
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đưa vai trò không hợp lệ vào một use case
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Review; CI; test fixtures; owner khắc phục; Ngôn ngữ; framework; test quality; release pressure
- **consequence:** Đạt Yêu cầu bảo mật tồn tại qua các lần thay đổi nhưng phải theo dõi Phân tích sớm tốn thời gian nhưng giảm rework

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Requirement có test phản ví dụ / requirement đã cam kết
- **domain:** Thiết kế đến vận hành; engineering; Tính năng mới thay trust boundary
- **conditions:** Tính năng mới thay trust boundary
- **goal:** Yêu cầu bảo mật tồn tại qua các lần thay đổi
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Design decisions và security tests; bằng chứng test: Đưa vai trò không hợp lệ vào một use case
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Phân tích sớm tốn thời gian nhưng giảm rework; Abuse case nào chưa có tiêu chí đúng/sai?
- **binding:** sw-design → điểm thực thi: Chuyển hậu quả cần tránh thành yêu cầu testable
