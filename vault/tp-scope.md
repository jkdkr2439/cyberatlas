### tp-scope — Quyền và dữ liệu nhà cung cấp

**Điều kiện:** Bên ngoài xử lý dữ liệu hay hỗ trợ.

- **I:** Contract, integration scopes và actual traffic
- **P:** Đối soát lời hứa với đường truy cập thực
- **O:** Giới hạn quyền, dữ liệu và mục đích
- **D:** Supplier evidence và quyền hiệu lực

**Hằng trong frame:** Chứng nhận không tự bảo đảm mọi integration.

**Đường hỏng:** Scope OAuth rộng hơn nhu cầu hợp đồng. **Điểm can thiệp:** Least privilege và test hành vi theo integration.

**Phép đo ứng viên:** Integration vượt data/authority intent / integration review.

**Test phân biệt / bằng chứng cần:** Ngừng một tính năng; quyền tương ứng phải bị giảm.

**Đánh đổi:** Scope nhỏ có thể tăng cấu hình riêng.

**OPEN:** Subprocessor mới có làm thay ranh giới dữ liệu?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Giới hạn quyền, dữ liệu và mục đích / Scope OAuth rộng hơn nhu cầu hợp đồng
- **domain:** Chốt population và giới hạn: Quan hệ ngoài tổ chức; procurement và service owner; Bên ngoài xử lý dữ liệu hay hỗ trợ
- **mechanism:** Control có giữ invariant này không? Chứng nhận không tự bảo đảm mọi integration
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Ngừng một tính năng; quyền tương ứng phải bị giảm
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Hợp đồng; test; quyền xuất dữ liệu; nguồn thay thế; Subprocessor; outage chung; remote support; exit cost
- **consequence:** Đạt Authority, dữ liệu và khả năng phục hồi không mất kiểm soát nhưng phải theo dõi Scope nhỏ có thể tăng cấu hình riêng

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Integration vượt data/authority intent / integration review
- **domain:** Quan hệ ngoài tổ chức; procurement và service owner; Bên ngoài xử lý dữ liệu hay hỗ trợ
- **conditions:** Bên ngoài xử lý dữ liệu hay hỗ trợ
- **goal:** Authority, dữ liệu và khả năng phục hồi không mất kiểm soát
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Supplier evidence và quyền hiệu lực; bằng chứng test: Ngừng một tính năng; quyền tương ứng phải bị giảm
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Scope nhỏ có thể tăng cấu hình riêng; Subprocessor mới có làm thay ranh giới dữ liệu?
- **binding:** tp-scope → điểm thực thi: Đối soát lời hứa với đường truy cập thực
