### msg-domain — Xác thực miền gửi

**Điều kiện:** Nhiều dịch vụ gửi email.

- **I:** Envelope, headers, chữ ký và DNS policy
- **P:** Kiểm tra cơ chế xác thực/alignment được cấu hình
- **O:** Tín hiệu xác thực miền
- **D:** Authentication results và thay đổi DNS

**Hằng trong frame:** Miền gửi xác thực không bảo đảm nội dung lương thiện.

**Đường hỏng:** Account thật bị chiếm; lookalike domain hợp lệ. **Điểm can thiệp:** Domain policy kết hợp nội dung và xác minh giao dịch.

**Phép đo ứng viên:** Nguồn gửi hợp lệ sai alignment / nguồn gửi được kiểm thử.

**Test phân biệt / bằng chứng cần:** Thử forwarding và dịch vụ marketing được cho phép.

**Đánh đổi:** Siết policy có thể mất thư hợp lệ.

**OPEN:** Danh sách toàn bộ bên gửi thay mặt tổ chức đã đầy đủ chưa?

**Liên hệ có điều kiện:**

- `msg-payment` — Email từ domain xác thực không chứng minh yêu cầu chuyển tiền hợp lệ.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Tín hiệu xác thực miền / Account thật bị chiếm; lookalike domain hợp lệ
- **domain:** Chốt population và giới hạn: Tên miền và hộp thư; IT/messaging; Nhiều dịch vụ gửi email
- **mechanism:** Control có giữ invariant này không? Miền gửi xác thực không bảo đảm nội dung lương thiện
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Thử forwarding và dịch vụ marketing được cho phép
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? DNS control; mail gateway; kênh xác minh độc lập; Forwarding; alias; dịch vụ gửi ngoài; tên gần giống
- **consequence:** Đạt Thông điệp không tự trở thành bằng chứng thẩm quyền nhưng phải theo dõi Siết policy có thể mất thư hợp lệ

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Nguồn gửi hợp lệ sai alignment / nguồn gửi được kiểm thử
- **domain:** Tên miền và hộp thư; IT/messaging; Nhiều dịch vụ gửi email
- **conditions:** Nhiều dịch vụ gửi email
- **goal:** Thông điệp không tự trở thành bằng chứng thẩm quyền
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Authentication results và thay đổi DNS; bằng chứng test: Thử forwarding và dịch vụ marketing được cho phép
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Siết policy có thể mất thư hợp lệ; Danh sách toàn bộ bên gửi thay mặt tổ chức đã đầy đủ chưa?
- **binding:** msg-domain → điểm thực thi: Kiểm tra cơ chế xác thực/alignment được cấu hình
