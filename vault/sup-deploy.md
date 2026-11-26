### sup-deploy — Xác minh tại triển khai

**Điều kiện:** Artifact qua registry tới production.

- **I:** Digest, provenance và deployment intent
- **P:** Kiểm signer/builder/source policy tại điểm dùng
- **O:** Chỉ artifact được phép được chạy
- **D:** Verification decision và deployed digest

**Hằng trong frame:** Có chữ ký không chứng minh artifact an toàn.

**Đường hỏng:** Chữ ký hợp lệ từ nguồn không được phép hoặc tag đổi. **Điểm can thiệp:** Verify digest+identity+policy; pin deployment.

**Phép đo ứng viên:** Artifact trái policy được deploy / negative cases.

**Test phân biệt / bằng chứng cần:** Thay tag sau approve; deployment phải bám digest được duyệt.

**Đánh đổi:** Fail-closed làm release phụ thuộc verifier.

**OPEN:** Khi key/builder bị compromise sẽ thu hồi thế nào?

**Liên hệ có điều kiện:**

- `cry-key` — Signer bị compromise làm thay đổi mức tin vào artifact đã ký.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Chỉ artifact được phép được chạy / Chữ ký hợp lệ từ nguồn không được phép hoặc tag đổi
- **domain:** Chốt population và giới hạn: Source, build, artifact, deploy; release team; Artifact qua registry tới production
- **mechanism:** Control có giữ invariant này không? Có chữ ký không chứng minh artifact an toàn
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Thay tag sau approve; deployment phải bám digest được duyệt
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Builder cô lập; chứng thực; kiểm tra ở deploy; Dependency; runner; signer; registry; mutable tag
- **consequence:** Đạt Artifact triển khai đúng nguồn và chính sách cho phép nhưng phải theo dõi Fail-closed làm release phụ thuộc verifier

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Artifact trái policy được deploy / negative cases
- **domain:** Source, build, artifact, deploy; release team; Artifact qua registry tới production
- **conditions:** Artifact qua registry tới production
- **goal:** Artifact triển khai đúng nguồn và chính sách cho phép
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Verification decision và deployed digest; bằng chứng test: Thay tag sau approve; deployment phải bám digest được duyệt
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Fail-closed làm release phụ thuộc verifier; Khi key/builder bị compromise sẽ thu hồi thế nào?
- **binding:** sup-deploy → điểm thực thi: Kiểm signer/builder/source policy tại điểm dùng
