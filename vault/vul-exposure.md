### vul-exposure — Cửa sổ phơi nhiễm

**Điều kiện:** Tài sản đổi trạng thái theo thời gian.

- **I:** Vulnerability state và exposure intervals
- **P:** Ghép khoảng thời gian bằng asset identity
- **O:** Exposure duration theo đối tượng
- **D:** Timeline có gaps/unknowns

**Hằng trong frame:** Không quan sát không được tính thành an toàn.

**Đường hỏng:** Scanner hàng tuần bỏ khoảng phơi nhiễm ngắn. **Điểm can thiệp:** Event-based inventory bổ sung scan.

**Phép đo ứng viên:** Tổng giờ phơi nhiễm quan sát; unknown-hours báo riêng.

**Test phân biệt / bằng chứng cần:** Ẩn một đoạn telemetry; metric phải tăng unknown.

**Đánh đổi:** Lấy mẫu dày tăng chi phí.

**OPEN:** Khoảng trước lần phát hiện đầu được xử lý ra sao?

**Liên hệ có điều kiện:**

- `tel-coverage` — Khoảng không có sensor phải được báo unknown, không tính zero exposure.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Exposure duration theo đối tượng / Scanner hàng tuần bỏ khoảng phơi nhiễm ngắn
- **domain:** Chốt population và giới hạn: Asset-vulnerability pair; VM team; Tài sản đổi trạng thái theo thời gian
- **mechanism:** Control có giữ invariant này không? Không quan sát không được tính thành an toàn
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Ẩn một đoạn telemetry; metric phải tăng unknown
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Scanner; inventory; change window; kiểm chứng sửa; Reachability; exploitability; control; tuổi tồn tại
- **consequence:** Đạt Giảm đường gây hại có ý nghĩa trong scope nhưng phải theo dõi Lấy mẫu dày tăng chi phí

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Tổng giờ phơi nhiễm quan sát; unknown-hours báo riêng
- **domain:** Asset-vulnerability pair; VM team; Tài sản đổi trạng thái theo thời gian
- **conditions:** Tài sản đổi trạng thái theo thời gian
- **goal:** Giảm đường gây hại có ý nghĩa trong scope
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Timeline có gaps/unknowns; bằng chứng test: Ẩn một đoạn telemetry; metric phải tăng unknown
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Lấy mẫu dày tăng chi phí; Khoảng trước lần phát hiện đầu được xử lý ra sao?
- **binding:** vul-exposure → điểm thực thi: Ghép khoảng thời gian bằng asset identity
