### build-cache — Cache xuyên mức tin trong CI

**Điều kiện:** Trusted và untrusted job dùng cache chung.

- **I:** Cached dependencies/artifacts và writer identity
- **P:** Phân vùng cache theo trust, integrity và key semantics
- **O:** Trusted job không dùng state không kiểm chứng
- **D:** Cache provenance và read/write scope

**Hằng trong frame:** Key cache đoán được không phải quyền ghi hợp lệ.

**Đường hỏng:** Untrusted job ghi thứ trusted job tự nhận là sạch. **Điểm can thiệp:** Trust-scoped cache và content validation.

**Phép đo ứng viên:** Trusted cache reads từ writer không phép / reads có provenance.

**Test phân biệt / bằng chứng cần:** Fixture untrusted ghi marker rồi trusted job thử đọc.

**Đánh đổi:** Giảm reuse làm build chậm.

**OPEN:** Shared compiler/tool cache có đường mutate riêng không?


## Sáu miền review

- **meaning:** Key cache đoán được không phải quyền ghi hợp lệ
- **domain:** Source, build, artifact, deploy; release team; CI nhận contribution không tin; Trusted và untrusted job dùng cache chung
- **mechanism:** Phân vùng cache theo trust, integrity và key semantics; failure: Untrusted job ghi thứ trusted job tự nhận là sạch
- **evidence:** Fixture untrusted ghi marker rồi trusted job thử đọc
- **operational:** Builder cô lập; chứng thực; kiểm tra ở deploy; Giảm reuse làm build chậm
- **consequence:** Artifact triển khai đúng nguồn và chính sách cho phép; Shared compiler/tool cache có đường mutate riêng không?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Trusted cache reads từ writer không phép / reads có provenance
- **domain:** Source, build, artifact, deploy; release team; CI nhận contribution không tin; Trusted và untrusted job dùng cache chung
- **conditions:** Trusted và untrusted job dùng cache chung
- **goal:** Artifact triển khai đúng nguồn và chính sách cho phép
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Cache provenance và read/write scope
- **method:** Fixture untrusted ghi marker rồi trusted job thử đọc
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Giảm reuse làm build chậm; Shared compiler/tool cache có đường mutate riêng không?
- **binding:** build-cache → Phân vùng cache theo trust, integrity và key semantics
