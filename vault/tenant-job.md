### tenant-job — Authority qua hàng đợi

**Điều kiện:** Request được xử lý sau khi người dùng đổi quyền.

- **I:** Job payload và requester context
- **P:** Mang capability có scope hoặc reauthorize lúc chạy
- **O:** Job chỉ xử lý phạm vi được cho phép
- **D:** Requester, purpose, epoch và expiry

**Hằng trong frame:** Ambient service-admin không được thay quyền requester một cách ngầm định.

**Đường hỏng:** Worker bỏ tenant context vì có quyền toàn DB. **Điểm can thiệp:** Explicit job authority contract.

**Phép đo ứng viên:** Job trái scope được chạy / negative job fixtures.

**Test phân biệt / bằng chứng cần:** Gửi job rồi revoke quyền trước worker nhận.

**Đánh đổi:** Recheck làm job phụ thuộc policy online.

**OPEN:** Job dài đã làm nửa chừng khi quyền đổi phải xử lý sao?


## Sáu miền review

- **meaning:** Ambient service-admin không được thay quyền requester một cách ngầm định
- **domain:** API và kho dữ liệu; chủ sản phẩm; API xử lý ID của nhiều người/tenant; Request được xử lý sau khi người dùng đổi quyền
- **mechanism:** Mang capability có scope hoặc reauthorize lúc chạy; failure: Worker bỏ tenant context vì có quyền toàn DB
- **evidence:** Gửi job rồi revoke quyền trước worker nhận
- **operational:** Policy engine; test matrix; owner dữ liệu; Recheck làm job phụ thuộc policy online
- **consequence:** Chủ thể chỉ tác động đúng đối tượng và hành động được phép; Job dài đã làm nửa chừng khi quyền đổi phải xử lý sao?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Job trái scope được chạy / negative job fixtures
- **domain:** API và kho dữ liệu; chủ sản phẩm; API xử lý ID của nhiều người/tenant; Request được xử lý sau khi người dùng đổi quyền
- **conditions:** Request được xử lý sau khi người dùng đổi quyền
- **goal:** Chủ thể chỉ tác động đúng đối tượng và hành động được phép
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Requester, purpose, epoch và expiry
- **method:** Gửi job rồi revoke quyền trước worker nhận
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Recheck làm job phụ thuộc policy online; Job dài đã làm nửa chừng khi quyền đổi phải xử lý sao?
- **binding:** tenant-job → Mang capability có scope hoặc reauthorize lúc chạy
