### verify-revocation — Thu hồi signer và artifact đã chạy

**Điều kiện:** Key hoặc builder bị phát hiện compromise.

- **I:** Revocation statement và runtime inventory
- **P:** Xác định affected builds theo time/source scope, chặn mới và xử lý đang chạy
- **O:** Tập ảnh hưởng và remediation có owner
- **D:** Revoked identity, signed-at evidence và deployed digests

**Hằng trong frame:** Chặn deploy mới không sửa artifact đã tồn tại.

**Đường hỏng:** Verifier cập nhật nhưng runtime vẫn chạy bản bị nghi ngờ. **Điểm can thiệp:** Runtime reconciliation và rollback/replace plan.

**Phép đo ứng viên:** Instance affected chưa xử lý / instance affected biết.

**Test phân biệt / bằng chứng cần:** Mock revoke signer; kiểm cả deploy mới và inventory cũ.

**Đánh đổi:** Thu hồi rộng có thể ngừng nhiều dịch vụ sạch.

**OPEN:** Không biết thời điểm compromise thì phạm vi được mở thế nào?


## Sáu miền review

- **meaning:** Chặn deploy mới không sửa artifact đã tồn tại
- **domain:** Source, build, artifact, deploy; release team; Artifact qua registry tới production; Key hoặc builder bị phát hiện compromise
- **mechanism:** Xác định affected builds theo time/source scope, chặn mới và xử lý đang chạy; failure: Verifier cập nhật nhưng runtime vẫn chạy bản bị nghi ngờ
- **evidence:** Mock revoke signer; kiểm cả deploy mới và inventory cũ
- **operational:** Builder cô lập; chứng thực; kiểm tra ở deploy; Thu hồi rộng có thể ngừng nhiều dịch vụ sạch
- **consequence:** Artifact triển khai đúng nguồn và chính sách cho phép; Không biết thời điểm compromise thì phạm vi được mở thế nào?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Instance affected chưa xử lý / instance affected biết
- **domain:** Source, build, artifact, deploy; release team; Artifact qua registry tới production; Key hoặc builder bị phát hiện compromise
- **conditions:** Key hoặc builder bị phát hiện compromise
- **goal:** Artifact triển khai đúng nguồn và chính sách cho phép
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Revoked identity, signed-at evidence và deployed digests
- **method:** Mock revoke signer; kiểm cả deploy mới và inventory cũ
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Thu hồi rộng có thể ngừng nhiều dịch vụ sạch; Không biết thời điểm compromise thì phạm vi được mở thế nào?
- **binding:** verify-revocation → Xác định affected builds theo time/source scope, chặn mới và xử lý đang chạy
