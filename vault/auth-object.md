### auth-object — Quyền ở cấp đối tượng

**Điều kiện:** API xử lý ID của nhiều người/tenant.

- **I:** Principal, object ID và action
- **P:** Đối chiếu quyền với object thực ở server
- **O:** Dữ liệu hoặc thay đổi đúng người
- **D:** Principal-object-tenant decision log

**Hằng trong frame:** Biết ID không đồng nghĩa sở hữu đối tượng.

**Đường hỏng:** Chỉ kiểm đăng nhập; truy vấn thiếu tenant. **Điểm can thiệp:** Check object-level ở mọi đường đọc/ghi.

**Phép đo ứng viên:** Yêu cầu cross-tenant được phép / yêu cầu cross-tenant trong test.

**Test phân biệt / bằng chứng cần:** Đổi object ID, giữ login hợp lệ và kiểm tra cả async export.

**Đánh đổi:** Tập test tăng theo role, action, tenant.

**OPEN:** Chia sẻ hợp lệ và chuyển owner làm thay đổi luật thế nào?

**Liên hệ có điều kiện:**

- `dat-egress` — Export cũng phải kiểm quyền đối tượng và quyền xuất dữ liệu.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Dữ liệu hoặc thay đổi đúng người / Chỉ kiểm đăng nhập; truy vấn thiếu tenant
- **domain:** Chốt population và giới hạn: API và kho dữ liệu; chủ sản phẩm; API xử lý ID của nhiều người/tenant
- **mechanism:** Control có giữ invariant này không? Biết ID không đồng nghĩa sở hữu đối tượng
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đổi object ID, giữ login hợp lệ và kiểm tra cả async export
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Policy engine; test matrix; owner dữ liệu; Role; thuộc tính; ownership; tenant; thời điểm commit
- **consequence:** Đạt Chủ thể chỉ tác động đúng đối tượng và hành động được phép nhưng phải theo dõi Tập test tăng theo role, action, tenant

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Yêu cầu cross-tenant được phép / yêu cầu cross-tenant trong test
- **domain:** API và kho dữ liệu; chủ sản phẩm; API xử lý ID của nhiều người/tenant
- **conditions:** API xử lý ID của nhiều người/tenant
- **goal:** Chủ thể chỉ tác động đúng đối tượng và hành động được phép
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Principal-object-tenant decision log; bằng chứng test: Đổi object ID, giữ login hợp lệ và kiểm tra cả async export
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Tập test tăng theo role, action, tenant; Chia sẻ hợp lệ và chuyển owner làm thay đổi luật thế nào?
- **binding:** auth-object → điểm thực thi: Đối chiếu quyền với object thực ở server
