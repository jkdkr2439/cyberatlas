### tenant-cache — Cache key và chiều phân quyền

**Điều kiện:** Cache dùng chung response giữa request.

- **I:** Object local ID, tenant, role và policy epoch
- **P:** Tách cache theo các chiều làm thay đổi output/permission
- **O:** Không dùng response của người này cho người khác
- **D:** Key schema và source authorization

**Hằng trong frame:** Cùng object ID không có nghĩa cùng object xuyên tenant.

**Đường hỏng:** Key chỉ có path/ID; response chứa field theo role. **Điểm can thiệp:** Include security-relevant dimensions hoặc tránh cache output nhạy cảm.

**Phép đo ứng viên:** Cross-scope cache hits trả sai / paired tests.

**Test phân biệt / bằng chứng cần:** Hai tenant cùng local ID; hai role khác field quyền.

**Đánh đổi:** Thêm chiều key giảm hit rate.

**OPEN:** Revocation field-level có yêu cầu invalidation gì?


## Sáu miền review

- **meaning:** Cùng object ID không có nghĩa cùng object xuyên tenant
- **domain:** API và kho dữ liệu; chủ sản phẩm; API xử lý ID của nhiều người/tenant; Cache dùng chung response giữa request
- **mechanism:** Tách cache theo các chiều làm thay đổi output/permission; failure: Key chỉ có path/ID; response chứa field theo role
- **evidence:** Hai tenant cùng local ID; hai role khác field quyền
- **operational:** Policy engine; test matrix; owner dữ liệu; Thêm chiều key giảm hit rate
- **consequence:** Chủ thể chỉ tác động đúng đối tượng và hành động được phép; Revocation field-level có yêu cầu invalidation gì?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Cross-scope cache hits trả sai / paired tests
- **domain:** API và kho dữ liệu; chủ sản phẩm; API xử lý ID của nhiều người/tenant; Cache dùng chung response giữa request
- **conditions:** Cache dùng chung response giữa request
- **goal:** Chủ thể chỉ tác động đúng đối tượng và hành động được phép
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Key schema và source authorization
- **method:** Hai tenant cùng local ID; hai role khác field quyền
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Thêm chiều key giảm hit rate; Revocation field-level có yêu cầu invalidation gì?
- **binding:** tenant-cache → Tách cache theo các chiều làm thay đổi output/permission
