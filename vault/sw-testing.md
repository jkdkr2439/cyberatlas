### sw-testing — Kiểm thử bảo mật đa lớp

**Điều kiện:** Code thay đổi thường xuyên.

- **I:** Source, build, endpoint và test cases
- **P:** Phối hợp SAST, DAST, SCA, fuzz, review theo mục tiêu
- **O:** Finding được xác minh và regression
- **D:** Version, tool config, finding disposition

**Hằng trong frame:** Tool chạy xong không đồng nghĩa đã test mọi cơ chế.

**Đường hỏng:** Chỉ đo số scan hoặc số finding. **Điểm can thiệp:** Map test tới requirement và lớp lỗi.

**Phép đo ứng viên:** Requirement đạt test xác định / requirement trong scope.

**Test phân biệt / bằng chứng cần:** Cố ý bỏ một control trong fixture rồi test phải fail.

**Đánh đổi:** Nhiều tool tăng noise và thời gian CI.

**OPEN:** Runtime-only và logic business thiếu ở đâu?

**Liên hệ có điều kiện:**

- `vul-fix` — Regression test hỗ trợ xác nhận sửa trong frame đã thử.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Finding được xác minh và regression / Chỉ đo số scan hoặc số finding
- **domain:** Chốt population và giới hạn: Thiết kế đến vận hành; engineering; Code thay đổi thường xuyên
- **mechanism:** Control có giữ invariant này không? Tool chạy xong không đồng nghĩa đã test mọi cơ chế
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Cố ý bỏ một control trong fixture rồi test phải fail
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Review; CI; test fixtures; owner khắc phục; Ngôn ngữ; framework; test quality; release pressure
- **consequence:** Đạt Yêu cầu bảo mật tồn tại qua các lần thay đổi nhưng phải theo dõi Nhiều tool tăng noise và thời gian CI

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Requirement đạt test xác định / requirement trong scope
- **domain:** Thiết kế đến vận hành; engineering; Code thay đổi thường xuyên
- **conditions:** Code thay đổi thường xuyên
- **goal:** Yêu cầu bảo mật tồn tại qua các lần thay đổi
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Version, tool config, finding disposition; bằng chứng test: Cố ý bỏ một control trong fixture rồi test phải fail
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Nhiều tool tăng noise và thời gian CI; Runtime-only và logic business thiếu ở đâu?
- **binding:** sw-testing → điểm thực thi: Phối hợp SAST, DAST, SCA, fuzz, review theo mục tiêu
