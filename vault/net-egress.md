### net-egress — Kiểm soát đường ra

**Điều kiện:** Service cần gọi tài nguyên ngoài.

- **I:** Destination, DNS result và request context
- **P:** Xác minh đích ở thời điểm kết nối
- **O:** Kết nối đúng đích hoặc bị chặn
- **D:** Destination resolved, decision, byte counts

**Hằng trong frame:** Allowlist tên không đủ nếu địa chỉ/redirect đổi.

**Đường hỏng:** SSRF đi qua redirect hoặc DNS thay đổi. **Điểm can thiệp:** Kiểm tra từng hop, egress policy và quyền workload.

**Phép đo ứng viên:** Đích cấm reachable / ca thử đích cấm theo chính sách.

**Test phân biệt / bằng chứng cần:** Dùng đích mô phỏng đổi resolution/redirect trong lab.

**Đánh đổi:** Egress proxy tạo choke point và chi phí.

**OPEN:** Metadata service và dịch vụ nội bộ nào cần bảo vệ riêng?

**Liên hệ có điều kiện:**

- `ai-tool` — Tool outbound cần destination policy ngoài quyết định model.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Kết nối đúng đích hoặc bị chặn / SSRF đi qua redirect hoặc DNS thay đổi
- **domain:** Chốt population và giới hạn: Lưu lượng giữa dịch vụ; network team; Service cần gọi tài nguyên ngoài
- **mechanism:** Control có giữ invariant này không? Allowlist tên không đủ nếu địa chỉ/redirect đổi
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Dùng đích mô phỏng đổi resolution/redirect trong lab
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Thiết bị mạng; bản đồ luồng; năng lực lọc; DNS; route; IPv6; proxy; lưu lượng mã hóa
- **consequence:** Đạt Đường kết nối chỉ mở cho quan hệ có chủ đích nhưng phải theo dõi Egress proxy tạo choke point và chi phí

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Đích cấm reachable / ca thử đích cấm theo chính sách
- **domain:** Lưu lượng giữa dịch vụ; network team; Service cần gọi tài nguyên ngoài
- **conditions:** Service cần gọi tài nguyên ngoài
- **goal:** Đường kết nối chỉ mở cho quan hệ có chủ đích
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Destination resolved, decision, byte counts; bằng chứng test: Dùng đích mô phỏng đổi resolution/redirect trong lab
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Egress proxy tạo choke point và chi phí; Metadata service và dịch vụ nội bộ nào cần bảo vệ riêng?
- **binding:** net-egress → điểm thực thi: Xác minh đích ở thời điểm kết nối
