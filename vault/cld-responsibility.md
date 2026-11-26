### cld-responsibility — Trách nhiệm cloud

**Điều kiện:** Dùng dịch vụ managed.

- **I:** Service contract và cấu hình tenant
- **P:** Chia việc provider bảo vệ với việc customer phải làm
- **O:** Control owner cho từng lớp
- **D:** Responsibility matrix có version

**Hằng trong frame:** Managed không có nghĩa mọi cấu hình đều an toàn.

**Đường hỏng:** Không ai quản dữ liệu, IAM hoặc exposure. **Điểm can thiệp:** Map trách nhiệm theo service và configuration.

**Phép đo ứng viên:** Control không owner / control áp dụng đã xác định.

**Test phân biệt / bằng chứng cần:** Chuyển từ VM sang managed rồi đối soát việc còn lại.

**Đánh đổi:** Nhà cung cấp che chi tiết làm giảm quan sát.

**OPEN:** Bằng chứng nào chứng minh lớp provider hoạt động?

**Liên hệ có điều kiện:**

- `tp-scope` — Managed service cần owner cho cả phần vendor lẫn customer.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Control owner cho từng lớp / Không ai quản dữ liệu, IAM hoặc exposure
- **domain:** Chốt population và giới hạn: Account/project và dịch vụ cloud; platform; Dùng dịch vụ managed
- **mechanism:** Control có giữ invariant này không? Managed không có nghĩa mọi cấu hình đều an toàn
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Chuyển từ VM sang managed rồi đối soát việc còn lại
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Inventory đa account; audit log; sandbox test; Shared responsibility; role chain; policy inheritance
- **consequence:** Đạt Chỉ thay đổi tài nguyên bằng authority được kiểm soát nhưng phải theo dõi Nhà cung cấp che chi tiết làm giảm quan sát

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Control không owner / control áp dụng đã xác định
- **domain:** Account/project và dịch vụ cloud; platform; Dùng dịch vụ managed
- **conditions:** Dùng dịch vụ managed
- **goal:** Chỉ thay đổi tài nguyên bằng authority được kiểm soát
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Responsibility matrix có version; bằng chứng test: Chuyển từ VM sang managed rồi đối soát việc còn lại
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Nhà cung cấp che chi tiết làm giảm quan sát; Bằng chứng nào chứng minh lớp provider hoạt động?
- **binding:** cld-responsibility → điểm thực thi: Chia việc provider bảo vệ với việc customer phải làm
