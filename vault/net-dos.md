### net-dos — Cạn tài nguyên và DDoS

**Điều kiện:** Traffic vượt capacity hoặc cost budget.

- **I:** Request volume, size, thời gian xử lý
- **P:** Admission, quota và phân phối tài nguyên
- **O:** Dịch vụ ưu tiên còn hoạt động
- **D:** Queue, latency, drops, bill

**Hằng trong frame:** Rate theo IP không đại diện chi phí xử lý.

**Đường hỏng:** Ít request đắt làm cạn worker. **Điểm can thiệp:** Budget theo chi phí và tenant; upstream protection.

**Phép đo ứng viên:** Throughput hợp lệ và tail latency dưới tải đã mô tả.

**Test phân biệt / bằng chứng cần:** Giữ request count, đổi workload sang loại đắt.

**Đánh đổi:** Chống abuse có thể chặn người dùng chung IP.

**OPEN:** Phụ thuộc upstream giới hạn nào không do mình điều khiển?

**Liên hệ có điều kiện:**

- `api-abuse` — Request hợp lệ vẫn có thể cạn tài nguyên và ngân sách.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Dịch vụ ưu tiên còn hoạt động / Ít request đắt làm cạn worker
- **domain:** Chốt population và giới hạn: Lưu lượng giữa dịch vụ; network team; Traffic vượt capacity hoặc cost budget
- **mechanism:** Control có giữ invariant này không? Rate theo IP không đại diện chi phí xử lý
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Giữ request count, đổi workload sang loại đắt
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Thiết bị mạng; bản đồ luồng; năng lực lọc; DNS; route; IPv6; proxy; lưu lượng mã hóa
- **consequence:** Đạt Đường kết nối chỉ mở cho quan hệ có chủ đích nhưng phải theo dõi Chống abuse có thể chặn người dùng chung IP

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Throughput hợp lệ và tail latency dưới tải đã mô tả
- **domain:** Lưu lượng giữa dịch vụ; network team; Traffic vượt capacity hoặc cost budget
- **conditions:** Traffic vượt capacity hoặc cost budget
- **goal:** Đường kết nối chỉ mở cho quan hệ có chủ đích
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Queue, latency, drops, bill; bằng chứng test: Giữ request count, đổi workload sang loại đắt
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Chống abuse có thể chặn người dùng chung IP; Phụ thuộc upstream giới hạn nào không do mình điều khiển?
- **binding:** net-dos → điểm thực thi: Admission, quota và phân phối tài nguyên
