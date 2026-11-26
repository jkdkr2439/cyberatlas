### sup-builder — Tính toàn vẹn build

**Điều kiện:** CI nhận contribution không tin.

- **I:** Source revision, workflow và build secrets
- **P:** Cô lập job; chỉ cấp authority cần cho nhánh tin
- **O:** Artifact và thông tin build
- **D:** Logs, digest và builder identity

**Hằng trong frame:** Runner bị chiếm có thể tạo artifact khác source.

**Đường hỏng:** Untrusted job dùng signer hoặc credential production. **Điểm can thiệp:** Ephemeral runner, phân tầng trust và signer riêng.

**Phép đo ứng viên:** Build tin cậy chia state với job không tin / build review.

**Test phân biệt / bằng chứng cần:** Chạy fixture thử vượt job boundary không có credential thật.

**Đánh đổi:** Cô lập mạnh tăng thời gian build.

**OPEN:** Cache có truyền state độc giữa hai mức trust?

**Liên hệ có điều kiện:**

- `sup-deploy` — Provenance chỉ hữu ích khi điểm dùng xác minh identity và policy.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Artifact và thông tin build / Untrusted job dùng signer hoặc credential production
- **domain:** Chốt population và giới hạn: Source, build, artifact, deploy; release team; CI nhận contribution không tin
- **mechanism:** Control có giữ invariant này không? Runner bị chiếm có thể tạo artifact khác source
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Chạy fixture thử vượt job boundary không có credential thật
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Builder cô lập; chứng thực; kiểm tra ở deploy; Dependency; runner; signer; registry; mutable tag
- **consequence:** Đạt Artifact triển khai đúng nguồn và chính sách cho phép nhưng phải theo dõi Cô lập mạnh tăng thời gian build

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Build tin cậy chia state với job không tin / build review
- **domain:** Source, build, artifact, deploy; release team; CI nhận contribution không tin
- **conditions:** CI nhận contribution không tin
- **goal:** Artifact triển khai đúng nguồn và chính sách cho phép
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Logs, digest và builder identity; bằng chứng test: Chạy fixture thử vượt job boundary không có credential thật
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Cô lập mạnh tăng thời gian build; Cache có truyền state độc giữa hai mức trust?
- **binding:** sup-builder → điểm thực thi: Cô lập job; chỉ cấp authority cần cho nhánh tin
