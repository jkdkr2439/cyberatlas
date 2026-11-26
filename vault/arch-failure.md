### arch-failure — Fail-open và fail-closed

**Điều kiện:** Policy service mất kết nối.

- **I:** Yêu cầu mới và timeout
- **P:** Chọn hành vi theo mức nguy hại của thao tác
- **O:** Cho phép, từ chối hoặc giới hạn chức năng
- **D:** Lý do fallback và thời gian

**Hằng trong frame:** Chế độ lỗi là quyết định thiết kế có mục tiêu.

**Đường hỏng:** Timeout vô tình bỏ xác thực. **Điểm can thiệp:** Fallback riêng cho read/write và emergency path.

**Phép đo ứng viên:** Yêu cầu được cho phép ngoài chính sách khi dependency lỗi / yêu cầu thử.

**Test phân biệt / bằng chứng cần:** Gây timeout ở lab rồi thử thao tác mức rủi ro khác nhau.

**Đánh đổi:** Fail-closed có thể gây outage; fail-open tăng phơi nhiễm.

**OPEN:** Grace period nào phù hợp từng dữ liệu và đối tượng?

**Liên hệ có điều kiện:**

- `k8s-admission` — Webhook timeout cần policy lỗi rõ ràng.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Cho phép, từ chối hoặc giới hạn chức năng / Timeout vô tình bỏ xác thực
- **domain:** Chốt population và giới hạn: Dịch vụ phân tán; kiến trúc sư; Policy service mất kết nối
- **mechanism:** Control có giữ invariant này không? Chế độ lỗi là quyết định thiết kế có mục tiêu
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Gây timeout ở lab rồi thử thao tác mức rủi ro khác nhau
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Sơ đồ thực tế; test môi trường; năng lực vận hành; Tenant; đường mạng; failover; vị trí enforcement
- **consequence:** Đạt Sai lệch không được tự do lan sang miền khác nhưng phải theo dõi Fail-closed có thể gây outage; fail-open tăng phơi nhiễm

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Yêu cầu được cho phép ngoài chính sách khi dependency lỗi / yêu cầu thử
- **domain:** Dịch vụ phân tán; kiến trúc sư; Policy service mất kết nối
- **conditions:** Policy service mất kết nối
- **goal:** Sai lệch không được tự do lan sang miền khác
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Lý do fallback và thời gian; bằng chứng test: Gây timeout ở lab rồi thử thao tác mức rủi ro khác nhau
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Fail-closed có thể gây outage; fail-open tăng phơi nhiễm; Grace period nào phù hợp từng dữ liệu và đối tượng?
- **binding:** arch-failure → điểm thực thi: Chọn hành vi theo mức nguy hại của thao tác
