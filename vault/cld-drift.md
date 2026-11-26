### cld-drift — Sai lệch cấu hình

**Điều kiện:** IaC và console cùng sửa tài nguyên.

- **I:** Desired state và observed state
- **P:** So sánh ngữ nghĩa và áp remediation có kiểm soát
- **O:** Drift được xử lý hoặc chấp nhận có hạn
- **D:** Diff, actor và remediation receipt

**Hằng trong frame:** Apply thành công chưa chứng minh state thực đúng.

**Đường hỏng:** Console override hoặc resource ngoài IaC. **Điểm can thiệp:** Read-after-write và drift detection.

**Phép đo ứng viên:** Drift nguy hại tồn tại bao lâu; theo resource class.

**Test phân biệt / bằng chứng cần:** Sửa cấu hình lab ngoài pipeline rồi đo phát hiện/khôi phục.

**Đánh đổi:** Auto-fix có thể ghi đè hotfix hợp lệ.

**OPEN:** Eventual consistency gây false positive thế nào?

**Liên hệ có điều kiện:**

- `sw-release` — Kết quả thực tế sau deploy phản hồi về rollout và rollback.
- `F13` — Identity, telemetry và residual state được theo dõi thế nào khi vòng đời ngắn hơn scan cadence?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Drift được xử lý hoặc chấp nhận có hạn / Console override hoặc resource ngoài IaC
- **domain:** Chốt population và giới hạn: Account/project và dịch vụ cloud; platform; IaC và console cùng sửa tài nguyên
- **mechanism:** Control có giữ invariant này không? Apply thành công chưa chứng minh state thực đúng
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Sửa cấu hình lab ngoài pipeline rồi đo phát hiện/khôi phục
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Inventory đa account; audit log; sandbox test; Shared responsibility; role chain; policy inheritance
- **consequence:** Đạt Chỉ thay đổi tài nguyên bằng authority được kiểm soát nhưng phải theo dõi Auto-fix có thể ghi đè hotfix hợp lệ

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Drift nguy hại tồn tại bao lâu; theo resource class
- **domain:** Account/project và dịch vụ cloud; platform; IaC và console cùng sửa tài nguyên
- **conditions:** IaC và console cùng sửa tài nguyên
- **goal:** Chỉ thay đổi tài nguyên bằng authority được kiểm soát
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Diff, actor và remediation receipt; bằng chứng test: Sửa cấu hình lab ngoài pipeline rồi đo phát hiện/khôi phục
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Auto-fix có thể ghi đè hotfix hợp lệ; Eventual consistency gây false positive thế nào?
- **binding:** cld-drift → điểm thực thi: So sánh ngữ nghĩa và áp remediation có kiểm soát
