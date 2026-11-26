### tenant-snapshot — Snapshot quyền hay quyền tại thời điểm chạy

**Điều kiện:** Nghiệp vụ có độ trễ đáng kể.

- **I:** Quyền lúc gửi và quyền hiện tại
- **P:** Chọn mốc authority theo ý nghĩa giao dịch, ghi rõ
- **O:** Quyết định nhất quán với contract nghiệp vụ
- **D:** Policy time semantics và consent record

**Hằng trong frame:** Không chọn mốc thời gian tùy tiện để làm request pass.

**Đường hỏng:** Dùng snapshot cho mọi thao tác dù consent đã rút. **Điểm can thiệp:** Per-action authority-time policy.

**Phép đo ứng viên:** Job dùng sai epoch-policy / case có đổi quyền.

**Test phân biệt / bằng chứng cần:** Cùng revoke nhưng phân biệt giao dịch đã cam kết với export chưa chạy.

**Đánh đổi:** Snapshot hỗ trợ ổn định nhưng kéo dài authority.

**OPEN:** Đồng ý đã rút có hiệu lực với nghĩa vụ pháp lý nào?


## Sáu miền review

- **meaning:** Không chọn mốc thời gian tùy tiện để làm request pass
- **domain:** API và kho dữ liệu; chủ sản phẩm; API xử lý ID của nhiều người/tenant; Request được xử lý sau khi người dùng đổi quyền; Nghiệp vụ có độ trễ đáng kể
- **mechanism:** Chọn mốc authority theo ý nghĩa giao dịch, ghi rõ; failure: Dùng snapshot cho mọi thao tác dù consent đã rút
- **evidence:** Cùng revoke nhưng phân biệt giao dịch đã cam kết với export chưa chạy
- **operational:** Policy engine; test matrix; owner dữ liệu; Snapshot hỗ trợ ổn định nhưng kéo dài authority
- **consequence:** Chủ thể chỉ tác động đúng đối tượng và hành động được phép; Đồng ý đã rút có hiệu lực với nghĩa vụ pháp lý nào?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Job dùng sai epoch-policy / case có đổi quyền
- **domain:** API và kho dữ liệu; chủ sản phẩm; API xử lý ID của nhiều người/tenant; Request được xử lý sau khi người dùng đổi quyền; Nghiệp vụ có độ trễ đáng kể
- **conditions:** Nghiệp vụ có độ trễ đáng kể
- **goal:** Chủ thể chỉ tác động đúng đối tượng và hành động được phép
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Policy time semantics và consent record
- **method:** Cùng revoke nhưng phân biệt giao dịch đã cam kết với export chưa chạy
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Snapshot hỗ trợ ổn định nhưng kéo dài authority; Đồng ý đã rút có hiệu lực với nghĩa vụ pháp lý nào?
- **binding:** tenant-snapshot → Chọn mốc authority theo ý nghĩa giao dịch, ghi rõ
