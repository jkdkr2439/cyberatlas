### ses-concurrency — Phiên, logout và thiết bị

**Điều kiện:** Một người có nhiều phiên.

- **I:** Logout, đổi mật khẩu, đăng nhập mới
- **P:** Áp chính sách hủy phiên theo thiết bị và rủi ro
- **O:** Tập phiên còn hợp lệ được giải thích
- **D:** Session inventory và lý do kết thúc

**Hằng trong frame:** Đóng giao diện không đồng nghĩa kết thúc phiên server.

**Đường hỏng:** Cookie còn dùng được sau logout. **Điểm can thiệp:** Hủy phiên phía server và kiểm tra replay an toàn.

**Phép đo ứng viên:** Phiên thuộc diện hủy còn dùng được / phiên đã thử.

**Test phân biệt / bằng chứng cần:** Logout một thiết bị rồi kiểm tra chính sách trên thiết bị khác.

**Đánh đổi:** Hủy toàn bộ dễ gián đoạn công việc.

**OPEN:** Khi nào cần step-up thay vì hủy phiên?

**Liên hệ có điều kiện:**

- `ir-contain` — Containment account cần xử lý toàn bộ phiên thuộc scope.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Tập phiên còn hợp lệ được giải thích / Cookie còn dùng được sau logout
- **domain:** Chốt population và giới hạn: Ứng dụng sau đăng nhập; IAM và app owner; Một người có nhiều phiên
- **mechanism:** Control có giữ invariant này không? Đóng giao diện không đồng nghĩa kết thúc phiên server
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Logout một thiết bị rồi kiểm tra chính sách trên thiết bị khác
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Kho phiên; đồng hồ; kênh invalidation; telemetry; TTL; cache; offline; refresh token; nhiều vùng
- **consequence:** Đạt Quyền không tồn tại vượt điều kiện được cấp nhưng phải theo dõi Hủy toàn bộ dễ gián đoạn công việc

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Phiên thuộc diện hủy còn dùng được / phiên đã thử
- **domain:** Ứng dụng sau đăng nhập; IAM và app owner; Một người có nhiều phiên
- **conditions:** Một người có nhiều phiên
- **goal:** Quyền không tồn tại vượt điều kiện được cấp
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Session inventory và lý do kết thúc; bằng chứng test: Logout một thiết bị rồi kiểm tra chính sách trên thiết bị khác
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Hủy toàn bộ dễ gián đoạn công việc; Khi nào cần step-up thay vì hủy phiên?
- **binding:** ses-concurrency → điểm thực thi: Áp chính sách hủy phiên theo thiết bị và rủi ro
