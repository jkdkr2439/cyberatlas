### cry-key — Vòng đời khóa

**Điều kiện:** Khóa dùng cho nhiều tài sản.

- **I:** Generate, distribute, rotate, revoke, destroy
- **P:** Ràng quyền sử dụng với mục đích và vòng đời
- **O:** Khóa hoạt động trong phạm vi cho phép
- **D:** Key inventory, audit và dependency

**Hằng trong frame:** Xóa khóa có thể đồng thời phá khả năng recovery.

**Đường hỏng:** Backup có ciphertext nhưng không còn key. **Điểm can thiệp:** Custody riêng, rotation có kiểm thử khôi phục.

**Phép đo ứng viên:** Tài sản mã hóa có key recovery được thử / tài sản cần recovery.

**Test phân biệt / bằng chứng cần:** Khôi phục backup sau một lần rotation.

**Đánh đổi:** Khóa dự phòng thêm bề mặt truy cập.

**OPEN:** Cryptographic erasure có bao phủ mọi bản sao khóa không?

**Liên hệ có điều kiện:**

- `rec-backup` — Backup mã hóa chỉ dùng được khi khôi phục đúng khóa.
- `F02` — Attestation xác nhận binary/config nào, ai cung cấp freshness và ai được giải phóng secret?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Khóa hoạt động trong phạm vi cho phép / Backup có ciphertext nhưng không còn key
- **domain:** Chốt population và giới hạn: Dữ liệu lưu và truyền; PKI/KMS owner; Khóa dùng cho nhiều tài sản
- **mechanism:** Control có giữ invariant này không? Xóa khóa có thể đồng thời phá khả năng recovery
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Khôi phục backup sau một lần rotation
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? KMS/HSM; backup khóa; năng lực chuyển đổi; Thuật toán; khóa; nonce; chứng thư; thời hạn bí mật
- **consequence:** Đạt Bí mật và toàn vẹn theo mô hình đối thủ cụ thể nhưng phải theo dõi Khóa dự phòng thêm bề mặt truy cập

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Tài sản mã hóa có key recovery được thử / tài sản cần recovery
- **domain:** Dữ liệu lưu và truyền; PKI/KMS owner; Khóa dùng cho nhiều tài sản
- **conditions:** Khóa dùng cho nhiều tài sản
- **goal:** Bí mật và toàn vẹn theo mô hình đối thủ cụ thể
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Key inventory, audit và dependency; bằng chứng test: Khôi phục backup sau một lần rotation
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Khóa dự phòng thêm bề mặt truy cập; Cryptographic erasure có bao phủ mọi bản sao khóa không?
- **binding:** cry-key → điểm thực thi: Ràng quyền sử dụng với mục đích và vòng đời
