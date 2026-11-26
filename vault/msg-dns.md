### msg-dns — Quyền điều khiển DNS

**Điều kiện:** Tên miền dẫn tới dịch vụ nhạy cảm.

- **I:** Đề nghị đổi record hoặc registrar setting
- **P:** Kiểm tra authority và phát hiện drift
- **O:** Resolution đúng dịch vụ
- **D:** Record history và registrar audit

**Hằng trong frame:** DNS control có thể chuyển hướng nhiều dịch vụ.

**Đường hỏng:** Tài khoản registrar yếu hơn tài khoản app. **Điểm can thiệp:** Bảo vệ registrar, least privilege, change alert.

**Phép đo ứng viên:** Thay đổi DNS không có owner-approved intent / thay đổi review.

**Test phân biệt / bằng chứng cần:** So cấu hình thực với ý định đã duyệt.

**Đánh đổi:** TTL ảnh hưởng tốc độ sửa và failover.

**OPEN:** Domain hết hạn và delegation bỏ quên được theo dõi ra sao?

**Liên hệ có điều kiện:**

- `sup-dependency` — Quyền điều khiển nguồn phân phối có thể đổi đích tải phần mềm.
- `F05` — Sai lệch route đến từ cấu hình, authority hay compromise; nguồn nào đủ độc lập để nhận biết?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Resolution đúng dịch vụ / Tài khoản registrar yếu hơn tài khoản app
- **domain:** Chốt population và giới hạn: Tên miền và hộp thư; IT/messaging; Tên miền dẫn tới dịch vụ nhạy cảm
- **mechanism:** Control có giữ invariant này không? DNS control có thể chuyển hướng nhiều dịch vụ
- **evidence:** Quan sát nào có thể bác bỏ kết luận? So cấu hình thực với ý định đã duyệt
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? DNS control; mail gateway; kênh xác minh độc lập; Forwarding; alias; dịch vụ gửi ngoài; tên gần giống
- **consequence:** Đạt Thông điệp không tự trở thành bằng chứng thẩm quyền nhưng phải theo dõi TTL ảnh hưởng tốc độ sửa và failover

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Thay đổi DNS không có owner-approved intent / thay đổi review
- **domain:** Tên miền và hộp thư; IT/messaging; Tên miền dẫn tới dịch vụ nhạy cảm
- **conditions:** Tên miền dẫn tới dịch vụ nhạy cảm
- **goal:** Thông điệp không tự trở thành bằng chứng thẩm quyền
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Record history và registrar audit; bằng chứng test: So cấu hình thực với ý định đã duyệt
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** TTL ảnh hưởng tốc độ sửa và failover; Domain hết hạn và delegation bỏ quên được theo dõi ra sao?
- **binding:** msg-dns → điểm thực thi: Kiểm tra authority và phát hiện drift
