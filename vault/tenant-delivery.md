### tenant-delivery — Quyền nhận kết quả sau khi job hoàn thành

**Điều kiện:** Report xuất ra file/link/email.

- **I:** Output object, người nhận và thời điểm tải
- **P:** Kiểm output ACL, destination và thời hạn truy cập
- **O:** Kết quả chỉ được đúng người lấy
- **D:** Delivery log, recipient và ACL version

**Hằng trong frame:** Quyền tạo report không thay kiểm quyền tải report.

**Đường hỏng:** Link chung hoặc bucket policy làm lộ export. **Điểm can thiệp:** Scoped delivery và recheck theo policy.

**Phép đo ứng viên:** Tải output trái scope thành công / download tests.

**Test phân biệt / bằng chứng cần:** Người khác tenant dùng link từ job hợp lệ.

**Đánh đổi:** Hạn dùng ngắn tăng yêu cầu chạy lại report.

**OPEN:** Link đã được tải/copy ra ngoài còn kiểm soát được gì?


## Sáu miền review

- **meaning:** Quyền tạo report không thay kiểm quyền tải report
- **domain:** API và kho dữ liệu; chủ sản phẩm; API xử lý ID của nhiều người/tenant; Request được xử lý sau khi người dùng đổi quyền; Report xuất ra file/link/email
- **mechanism:** Kiểm output ACL, destination và thời hạn truy cập; failure: Link chung hoặc bucket policy làm lộ export
- **evidence:** Người khác tenant dùng link từ job hợp lệ
- **operational:** Policy engine; test matrix; owner dữ liệu; Hạn dùng ngắn tăng yêu cầu chạy lại report
- **consequence:** Chủ thể chỉ tác động đúng đối tượng và hành động được phép; Link đã được tải/copy ra ngoài còn kiểm soát được gì?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Tải output trái scope thành công / download tests
- **domain:** API và kho dữ liệu; chủ sản phẩm; API xử lý ID của nhiều người/tenant; Request được xử lý sau khi người dùng đổi quyền; Report xuất ra file/link/email
- **conditions:** Report xuất ra file/link/email
- **goal:** Chủ thể chỉ tác động đúng đối tượng và hành động được phép
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Delivery log, recipient và ACL version
- **method:** Người khác tenant dùng link từ job hợp lệ
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Hạn dùng ngắn tăng yêu cầu chạy lại report; Link đã được tải/copy ra ngoài còn kiểm soát được gì?
- **binding:** tenant-delivery → Kiểm output ACL, destination và thời hạn truy cập
