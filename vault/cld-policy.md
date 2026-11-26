### cld-policy — Authority control plane

**Điều kiện:** Role có thể tạo/chỉnh tài nguyên.

- **I:** Policy, role trust và resource access
- **P:** Tính quyền trực tiếp lẫn khả năng cấp quyền tiếp
- **O:** Tập thay đổi có thể thực hiện
- **D:** Role chain và audit control plane

**Hằng trong frame:** Quyền tạo role có thể quan trọng hơn quyền đọc data.

**Đường hỏng:** Quyền tưởng nhỏ cho phép tự mở quyền lớn. **Điểm can thiệp:** Tách quyền quản policy và dùng dữ liệu; test effective access.

**Phép đo ứng viên:** Đường tới quyền đặc biệt ngoài intent / đường đã mô hình hóa.

**Test phân biệt / bằng chứng cần:** Kiểm tra cả role assumption và quyền sửa trust.

**Đánh đổi:** Policy cứng khó xử lý vận hành khẩn cấp.

**OPEN:** Service-linked role và cross-account được xét ra sao?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Tập thay đổi có thể thực hiện / Quyền tưởng nhỏ cho phép tự mở quyền lớn
- **domain:** Chốt population và giới hạn: Account/project và dịch vụ cloud; platform; Role có thể tạo/chỉnh tài nguyên
- **mechanism:** Control có giữ invariant này không? Quyền tạo role có thể quan trọng hơn quyền đọc data
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Kiểm tra cả role assumption và quyền sửa trust
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Inventory đa account; audit log; sandbox test; Shared responsibility; role chain; policy inheritance
- **consequence:** Đạt Chỉ thay đổi tài nguyên bằng authority được kiểm soát nhưng phải theo dõi Policy cứng khó xử lý vận hành khẩn cấp

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Đường tới quyền đặc biệt ngoài intent / đường đã mô hình hóa
- **domain:** Account/project và dịch vụ cloud; platform; Role có thể tạo/chỉnh tài nguyên
- **conditions:** Role có thể tạo/chỉnh tài nguyên
- **goal:** Chỉ thay đổi tài nguyên bằng authority được kiểm soát
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Role chain và audit control plane; bằng chứng test: Kiểm tra cả role assumption và quyền sửa trust
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Policy cứng khó xử lý vận hành khẩn cấp; Service-linked role và cross-account được xét ra sao?
- **binding:** cld-policy → điểm thực thi: Tính quyền trực tiếp lẫn khả năng cấp quyền tiếp
