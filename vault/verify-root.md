### verify-root — Gốc tin của verifier

**Điều kiện:** Verifier phải biết signer/builder nào hợp lệ.

- **I:** Trust policy, key metadata và attestation
- **P:** Kiểm nguồn phân phối policy và thẩm quyền sửa nó
- **O:** Quyết định dựa trên trust root được bảo vệ
- **D:** Policy revision, approver và root lineage

**Hằng trong frame:** Không lấy trust root từ chính artifact đang cần xác minh.

**Đường hỏng:** Artifact tự khai signer hợp lệ; attacker sửa allowlist. **Điểm can thiệp:** Protected root distribution và separation of duties.

**Phép đo ứng viên:** Policy change không được duyệt / changes được audit.

**Test phân biệt / bằng chứng cần:** Artifact đề nghị thêm signer vào trust root; phải bị bỏ qua.

**Đánh đổi:** Quản root chặt làm recovery signer khó hơn.

**OPEN:** Khôi phục trust root khi chính hệ phát hành bị chiếm?


## Sáu miền review

- **meaning:** Không lấy trust root từ chính artifact đang cần xác minh
- **domain:** Source, build, artifact, deploy; release team; Artifact qua registry tới production; Verifier phải biết signer/builder nào hợp lệ
- **mechanism:** Kiểm nguồn phân phối policy và thẩm quyền sửa nó; failure: Artifact tự khai signer hợp lệ; attacker sửa allowlist
- **evidence:** Artifact đề nghị thêm signer vào trust root; phải bị bỏ qua
- **operational:** Builder cô lập; chứng thực; kiểm tra ở deploy; Quản root chặt làm recovery signer khó hơn
- **consequence:** Artifact triển khai đúng nguồn và chính sách cho phép; Khôi phục trust root khi chính hệ phát hành bị chiếm?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Policy change không được duyệt / changes được audit
- **domain:** Source, build, artifact, deploy; release team; Artifact qua registry tới production; Verifier phải biết signer/builder nào hợp lệ
- **conditions:** Verifier phải biết signer/builder nào hợp lệ
- **goal:** Artifact triển khai đúng nguồn và chính sách cho phép
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Policy revision, approver và root lineage
- **method:** Artifact đề nghị thêm signer vào trust root; phải bị bỏ qua
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Quản root chặt làm recovery signer khó hơn; Khôi phục trust root khi chính hệ phát hành bị chiếm?
- **binding:** verify-root → Kiểm nguồn phân phối policy và thẩm quyền sửa nó
