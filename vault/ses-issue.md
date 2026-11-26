### ses-issue — Phát hành token đúng đối tượng

**Điều kiện:** Một IdP phục vụ nhiều ứng dụng.

- **I:** Auth result và requested audience
- **P:** Phát hành token ràng buộc issuer, audience và scope
- **O:** Token được ứng dụng đích chấp nhận đúng phạm vi
- **D:** Issuance metadata và key version

**Hằng trong frame:** Token hợp lệ mật mã chưa chắc đúng dịch vụ.

**Đường hỏng:** Chấp nhận token của audience khác. **Điểm can thiệp:** Xác minh claims và thuật toán theo allowlist.

**Phép đo ứng viên:** Token sai audience bị nhận / token sai audience đã thử.

**Test phân biệt / bằng chứng cần:** Đổi riêng audience, giữ chữ ký hợp lệ trong lab.

**Đánh đổi:** Nhiều kiểu token tăng độ phức tạp tương thích.

**OPEN:** Token exchange có làm nở quyền qua chuỗi không?

**Liên hệ có điều kiện:**

- `k8s-identity` — Audience/subject sai có thể làm token workload dùng vượt mục đích.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Token được ứng dụng đích chấp nhận đúng phạm vi / Chấp nhận token của audience khác
- **domain:** Chốt population và giới hạn: Ứng dụng sau đăng nhập; IAM và app owner; Một IdP phục vụ nhiều ứng dụng
- **mechanism:** Control có giữ invariant này không? Token hợp lệ mật mã chưa chắc đúng dịch vụ
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đổi riêng audience, giữ chữ ký hợp lệ trong lab
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Kho phiên; đồng hồ; kênh invalidation; telemetry; TTL; cache; offline; refresh token; nhiều vùng
- **consequence:** Đạt Quyền không tồn tại vượt điều kiện được cấp nhưng phải theo dõi Nhiều kiểu token tăng độ phức tạp tương thích

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Token sai audience bị nhận / token sai audience đã thử
- **domain:** Ứng dụng sau đăng nhập; IAM và app owner; Một IdP phục vụ nhiều ứng dụng
- **conditions:** Một IdP phục vụ nhiều ứng dụng
- **goal:** Quyền không tồn tại vượt điều kiện được cấp
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Issuance metadata và key version; bằng chứng test: Đổi riêng audience, giữ chữ ký hợp lệ trong lab
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Nhiều kiểu token tăng độ phức tạp tương thích; Token exchange có làm nở quyền qua chuỗi không?
- **binding:** ses-issue → điểm thực thi: Phát hành token ràng buộc issuer, audience và scope
