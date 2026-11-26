### end-execution — Quyền thực thi và cô lập

**Điều kiện:** Ứng dụng xử lý input không tin.

- **I:** File, process, user token
- **P:** Áp sandbox, privilege và policy thực thi
- **O:** Process bị giới hạn khả năng
- **D:** Process tree và quyền hiệu lực

**Hằng trong frame:** Chạy được mã không nên đồng nghĩa quản toàn máy.

**Đường hỏng:** Ứng dụng chạy admin hoặc sandbox escape. **Điểm can thiệp:** Giảm quyền; isolation; cập nhật lớp nền.

**Phép đo ứng viên:** Hành động ngoài quyền bị chặn / hành động thử có kiểm soát.

**Test phân biệt / bằng chứng cần:** Thử thao tác vô hại ngoài sandbox trong lab.

**Đánh đổi:** Sandbox có thể làm hỏng tương thích.

**OPEN:** Kernel/driver nào vẫn nằm ngoài ranh giới cô lập?

**Liên hệ có điều kiện:**

- `sup-builder` — Runner không tin cần quyền và state tách biệt.
- `F06` — Permission thực tế, sandbox, SDK và đường export dữ liệu trên từng platform là gì?
- `F07` — Chuỗi tin cậy từ boot tới runtime đứt ở đâu khi một thành phần firmware bị sửa?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Process bị giới hạn khả năng / Ứng dụng chạy admin hoặc sandbox escape
- **domain:** Chốt population và giới hạn: Máy trạm, server; endpoint team; Ứng dụng xử lý input không tin
- **mechanism:** Control có giữ invariant này không? Chạy được mã không nên đồng nghĩa quản toàn máy
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Thử thao tác vô hại ngoài sandbox trong lab
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Quản trị thiết bị; cập nhật; bộ nhớ; hỗ trợ người dùng; BYOD; EDR health; kernel; ứng dụng cũ
- **consequence:** Đạt Mã và quyền thực thi phù hợp công việc nhưng phải theo dõi Sandbox có thể làm hỏng tương thích

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Hành động ngoài quyền bị chặn / hành động thử có kiểm soát
- **domain:** Máy trạm, server; endpoint team; Ứng dụng xử lý input không tin
- **conditions:** Ứng dụng xử lý input không tin
- **goal:** Mã và quyền thực thi phù hợp công việc
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Process tree và quyền hiệu lực; bằng chứng test: Thử thao tác vô hại ngoài sandbox trong lab
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Sandbox có thể làm hỏng tương thích; Kernel/driver nào vẫn nằm ngoài ranh giới cô lập?
- **binding:** end-execution → điểm thực thi: Áp sandbox, privilege và policy thực thi
