### sup-dependency — Dependency và nguồn tin

**Điều kiện:** Build dùng package bên ngoài.

- **I:** Tên, version, checksum, registry và dependency tree
- **P:** Resolve theo nguồn cho phép và kiểm provenance khi có
- **O:** Dependency cụ thể được đưa vào build
- **D:** Lockfile, inventory và nguồn thực

**Hằng trong frame:** Đúng tên package không chứng minh đúng tác giả/nguồn.

**Đường hỏng:** Namespace confusion hoặc update độc. **Điểm can thiệp:** Pin, registry policy, review update, SBOM hỗ trợ.

**Phép đo ứng viên:** Dependency resolve ngoài nguồn dự định / dependency resolved.

**Test phân biệt / bằng chứng cần:** Đổi registry ưu tiên trong fixture không có secret.

**Đánh đổi:** Pin giảm biến động nhưng trì hoãn patch.

**OPEN:** Transitive dependency và install script thực thi quyền gì?

**Liên hệ có điều kiện:**

- `vul-context` — Inventory dependency giúp biết CVE có nằm trong artifact đang chạy.
- `F15` — Dataset, checkpoint và evaluation provenance khác binary provenance ở chỗ nào?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Dependency cụ thể được đưa vào build / Namespace confusion hoặc update độc
- **domain:** Chốt population và giới hạn: Source, build, artifact, deploy; release team; Build dùng package bên ngoài
- **mechanism:** Control có giữ invariant này không? Đúng tên package không chứng minh đúng tác giả/nguồn
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đổi registry ưu tiên trong fixture không có secret
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Builder cô lập; chứng thực; kiểm tra ở deploy; Dependency; runner; signer; registry; mutable tag
- **consequence:** Đạt Artifact triển khai đúng nguồn và chính sách cho phép nhưng phải theo dõi Pin giảm biến động nhưng trì hoãn patch

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Dependency resolve ngoài nguồn dự định / dependency resolved
- **domain:** Source, build, artifact, deploy; release team; Build dùng package bên ngoài
- **conditions:** Build dùng package bên ngoài
- **goal:** Artifact triển khai đúng nguồn và chính sách cho phép
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Lockfile, inventory và nguồn thực; bằng chứng test: Đổi registry ưu tiên trong fixture không có secret
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Pin giảm biến động nhưng trì hoãn patch; Transitive dependency và install script thực thi quyền gì?
- **binding:** sup-dependency → điểm thực thi: Resolve theo nguồn cho phép và kiểm provenance khi có
