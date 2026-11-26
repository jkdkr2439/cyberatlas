### arch-boundary — Ranh giới tin cậy

**Điều kiện:** Dữ liệu đi qua chủ thể hoặc miền quản trị.

- **I:** Yêu cầu từ nguồn khác trust level
- **P:** Xác thực nguồn, schema và quyền tại điểm chuyển
- **O:** Đầu vào được giảm quyền và gắn nguồn
- **D:** Decision log và nhãn nguồn

**Hằng trong frame:** Vị trí nội bộ không tự cấp lòng tin.

**Đường hỏng:** Proxy hoặc service nâng dữ liệu thành quyền. **Điểm can thiệp:** Enforcement ở boundary; fail policy tường minh.

**Phép đo ứng viên:** Luồng qua boundary có quyết định được kiểm tra / luồng đã lập bản đồ.

**Test phân biệt / bằng chứng cần:** Cho request nội bộ mang danh tính không hợp lệ.

**Đánh đổi:** Nhiều điểm kiểm tăng độ trễ và chi phí quản trị.

**OPEN:** Boundary nào bị bypass bằng đường quản trị?

**Liên hệ có điều kiện:**

- `ai-instruction` — Nội dung từ miền thấp trust bị nâng thành quyền ở boundary.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Đầu vào được giảm quyền và gắn nguồn / Proxy hoặc service nâng dữ liệu thành quyền
- **domain:** Chốt population và giới hạn: Dịch vụ phân tán; kiến trúc sư; Dữ liệu đi qua chủ thể hoặc miền quản trị
- **mechanism:** Control có giữ invariant này không? Vị trí nội bộ không tự cấp lòng tin
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Cho request nội bộ mang danh tính không hợp lệ
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Sơ đồ thực tế; test môi trường; năng lực vận hành; Tenant; đường mạng; failover; vị trí enforcement
- **consequence:** Đạt Sai lệch không được tự do lan sang miền khác nhưng phải theo dõi Nhiều điểm kiểm tăng độ trễ và chi phí quản trị

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Luồng qua boundary có quyết định được kiểm tra / luồng đã lập bản đồ
- **domain:** Dịch vụ phân tán; kiến trúc sư; Dữ liệu đi qua chủ thể hoặc miền quản trị
- **conditions:** Dữ liệu đi qua chủ thể hoặc miền quản trị
- **goal:** Sai lệch không được tự do lan sang miền khác
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Decision log và nhãn nguồn; bằng chứng test: Cho request nội bộ mang danh tính không hợp lệ
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Nhiều điểm kiểm tăng độ trễ và chi phí quản trị; Boundary nào bị bypass bằng đường quản trị?
- **binding:** arch-boundary → điểm thực thi: Xác thực nguồn, schema và quyền tại điểm chuyển
