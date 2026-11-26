### end-health — Control endpoint còn hoạt động

**Điều kiện:** Thiết bị được coi là có EDR.

- **I:** Agent heartbeat, version và telemetry test
- **P:** Phân biệt cài đặt, kết nối và thực sự quan sát
- **O:** Trạng thái control có freshness
- **D:** Heartbeat, sensor gaps và test receipt

**Hằng trong frame:** Có phần mềm không đồng nghĩa có bảo vệ hoạt động.

**Đường hỏng:** Agent cài nhưng im lặng hoặc bị vô hiệu. **Điểm can thiệp:** Health kiểm độc lập và test hành vi lành tính.

**Phép đo ứng viên:** Thiết bị đạt health+test / thiết bị trong scope.

**Test phân biệt / bằng chứng cần:** Ngắt sensor trong lab; dashboard phải báo unknown/degraded.

**Đánh đổi:** Telemetry liên tục dùng tài nguyên và có riêng tư.

**OPEN:** Máy offline dài ngày có được loại khỏi mẫu số không?

**Liên hệ có điều kiện:**

- `tel-coverage` — Sensor không hoạt động phải tạo tín hiệu thiếu quan sát.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Trạng thái control có freshness / Agent cài nhưng im lặng hoặc bị vô hiệu
- **domain:** Chốt population và giới hạn: Máy trạm, server; endpoint team; Thiết bị được coi là có EDR
- **mechanism:** Control có giữ invariant này không? Có phần mềm không đồng nghĩa có bảo vệ hoạt động
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Ngắt sensor trong lab; dashboard phải báo unknown/degraded
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Quản trị thiết bị; cập nhật; bộ nhớ; hỗ trợ người dùng; BYOD; EDR health; kernel; ứng dụng cũ
- **consequence:** Đạt Mã và quyền thực thi phù hợp công việc nhưng phải theo dõi Telemetry liên tục dùng tài nguyên và có riêng tư

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Thiết bị đạt health+test / thiết bị trong scope
- **domain:** Máy trạm, server; endpoint team; Thiết bị được coi là có EDR
- **conditions:** Thiết bị được coi là có EDR
- **goal:** Mã và quyền thực thi phù hợp công việc
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Heartbeat, sensor gaps và test receipt; bằng chứng test: Ngắt sensor trong lab; dashboard phải báo unknown/degraded
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Telemetry liên tục dùng tài nguyên và có riêng tư; Máy offline dài ngày có được loại khỏi mẫu số không?
- **binding:** end-health → điểm thực thi: Phân biệt cài đặt, kết nối và thực sự quan sát
