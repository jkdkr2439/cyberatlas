### msg-payment — Thay đổi tài khoản thanh toán

**Điều kiện:** Email yêu cầu chuyển tiền/đổi beneficiary.

- **I:** Yêu cầu và thông tin người gửi
- **P:** Xác nhận bằng kênh độc lập đã biết
- **O:** Thay đổi có kiểm soát
- **D:** Bằng chứng xác nhận và approver

**Hằng trong frame:** Cùng một hộp thư không phải hai nguồn độc lập.

**Đường hỏng:** Reply vào hộp thư đã compromise để xác minh. **Điểm can thiệp:** Dual control và callback qua danh bạ có trước.

**Phép đo ứng viên:** Thay đổi beneficiary không xác minh độc lập / thay đổi thử.

**Test phân biệt / bằng chứng cần:** Email từ tài khoản thật nhưng nội dung giả trong diễn tập.

**Đánh đổi:** Tăng thời gian thanh toán.

**OPEN:** Kênh xác minh dự phòng có chung điểm compromise không?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Thay đổi có kiểm soát / Reply vào hộp thư đã compromise để xác minh
- **domain:** Chốt population và giới hạn: Tên miền và hộp thư; IT/messaging; Email yêu cầu chuyển tiền/đổi beneficiary
- **mechanism:** Control có giữ invariant này không? Cùng một hộp thư không phải hai nguồn độc lập
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Email từ tài khoản thật nhưng nội dung giả trong diễn tập
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? DNS control; mail gateway; kênh xác minh độc lập; Forwarding; alias; dịch vụ gửi ngoài; tên gần giống
- **consequence:** Đạt Thông điệp không tự trở thành bằng chứng thẩm quyền nhưng phải theo dõi Tăng thời gian thanh toán

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Thay đổi beneficiary không xác minh độc lập / thay đổi thử
- **domain:** Tên miền và hộp thư; IT/messaging; Email yêu cầu chuyển tiền/đổi beneficiary
- **conditions:** Email yêu cầu chuyển tiền/đổi beneficiary
- **goal:** Thông điệp không tự trở thành bằng chứng thẩm quyền
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Bằng chứng xác nhận và approver; bằng chứng test: Email từ tài khoản thật nhưng nội dung giả trong diễn tập
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Tăng thời gian thanh toán; Kênh xác minh dự phòng có chung điểm compromise không?
- **binding:** msg-payment → điểm thực thi: Xác nhận bằng kênh độc lập đã biết
