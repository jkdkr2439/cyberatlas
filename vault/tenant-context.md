### tenant-context — Nguồn authority của tenant context

**Điều kiện:** Client gửi tenant_id hoặc chọn workspace.

- **I:** Session binding, route và client tenant claim
- **P:** Chỉ dùng tenant context đã được quyền lựa chọn
- **O:** Context server được xác nhận
- **D:** Claim source và decision

**Hằng trong frame:** Tên tenant do client đưa không tự tạo membership.

**Đường hỏng:** Header tenant được tin vì request đã login. **Điểm can thiệp:** Resolve membership server-side.

**Phép đo ứng viên:** Context trái membership được chấp nhận / ca thử.

**Test phân biệt / bằng chứng cần:** Đổi header tenant, giữ token hợp lệ của tenant khác.

**Đánh đổi:** Membership lookup thêm dependency.

**OPEN:** Delegation và shared workspace được mô hình hóa ra sao?


## Sáu miền review

- **meaning:** Tên tenant do client đưa không tự tạo membership
- **domain:** API và kho dữ liệu; chủ sản phẩm; API xử lý ID của nhiều người/tenant; Client gửi tenant_id hoặc chọn workspace
- **mechanism:** Chỉ dùng tenant context đã được quyền lựa chọn; failure: Header tenant được tin vì request đã login
- **evidence:** Đổi header tenant, giữ token hợp lệ của tenant khác
- **operational:** Policy engine; test matrix; owner dữ liệu; Membership lookup thêm dependency
- **consequence:** Chủ thể chỉ tác động đúng đối tượng và hành động được phép; Delegation và shared workspace được mô hình hóa ra sao?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Context trái membership được chấp nhận / ca thử
- **domain:** API và kho dữ liệu; chủ sản phẩm; API xử lý ID của nhiều người/tenant; Client gửi tenant_id hoặc chọn workspace
- **conditions:** Client gửi tenant_id hoặc chọn workspace
- **goal:** Chủ thể chỉ tác động đúng đối tượng và hành động được phép
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Claim source và decision
- **method:** Đổi header tenant, giữ token hợp lệ của tenant khác
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Membership lookup thêm dependency; Delegation và shared workspace được mô hình hóa ra sao?
- **binding:** tenant-context → Chỉ dùng tenant context đã được quyền lựa chọn
