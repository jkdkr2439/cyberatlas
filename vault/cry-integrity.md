### cry-integrity — Mã hóa và xác thực dữ liệu

**Điều kiện:** Dữ liệu cần bí mật lẫn toàn vẹn.

- **I:** Plaintext, key, nonce và context
- **P:** Dùng primitive được thẩm định đúng điều kiện
- **O:** Ciphertext và kiểm tra integrity
- **D:** Key/nonce metadata theo thiết kế

**Hằng trong frame:** Bí mật không tự suy ra toàn vẹn hay đúng người gửi.

**Đường hỏng:** Nonce reuse hoặc bỏ kiểm tra tag. **Điểm can thiệp:** Thư viện chuẩn; quản nonce; bind context.

**Phép đo ứng viên:** Vi phạm uniqueness nonce theo key / thao tác có kiểm kê.

**Test phân biệt / bằng chứng cần:** Thử đổi ciphertext/context và yêu cầu từ chối.

**Đánh đổi:** Lưu metadata và xoay khóa có chi phí.

**OPEN:** Randomness, restart và nhiều node có làm trùng nonce?

**Liên hệ có điều kiện:**

- `tel-integrity` — Integrity sau ghi không chứng minh event ban đầu là sự thật.
- `F01` — Đối thủ quan sát timing/power/cache trong mô hình truy cập nào, và control có tác dụng ở lớp nào?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Ciphertext và kiểm tra integrity / Nonce reuse hoặc bỏ kiểm tra tag
- **domain:** Chốt population và giới hạn: Dữ liệu lưu và truyền; PKI/KMS owner; Dữ liệu cần bí mật lẫn toàn vẹn
- **mechanism:** Control có giữ invariant này không? Bí mật không tự suy ra toàn vẹn hay đúng người gửi
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Thử đổi ciphertext/context và yêu cầu từ chối
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? KMS/HSM; backup khóa; năng lực chuyển đổi; Thuật toán; khóa; nonce; chứng thư; thời hạn bí mật
- **consequence:** Đạt Bí mật và toàn vẹn theo mô hình đối thủ cụ thể nhưng phải theo dõi Lưu metadata và xoay khóa có chi phí

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Vi phạm uniqueness nonce theo key / thao tác có kiểm kê
- **domain:** Dữ liệu lưu và truyền; PKI/KMS owner; Dữ liệu cần bí mật lẫn toàn vẹn
- **conditions:** Dữ liệu cần bí mật lẫn toàn vẹn
- **goal:** Bí mật và toàn vẹn theo mô hình đối thủ cụ thể
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Key/nonce metadata theo thiết kế; bằng chứng test: Thử đổi ciphertext/context và yêu cầu từ chối
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Lưu metadata và xoay khóa có chi phí; Randomness, restart và nhiều node có làm trùng nonce?
- **binding:** cry-integrity → điểm thực thi: Dùng primitive được thẩm định đúng điều kiện
