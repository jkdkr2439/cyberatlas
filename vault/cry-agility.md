### cry-agility — Chuyển đổi mật mã

**Điều kiện:** Thuật toán, chứng thư hoặc key policy đổi.

- **I:** Inventory crypto và hạn bí mật dữ liệu
- **P:** Lập lộ trình thay đổi theo dependency
- **O:** Dịch vụ tương thích và dữ liệu còn đọc được
- **D:** Phiên bản protocol và migration result

**Hằng trong frame:** Đổi thuật toán không chỉ là sửa một tên cấu hình.

**Đường hỏng:** Client cũ buộc downgrade hoặc mất kết nối. **Điểm can thiệp:** Inventory, negotiation policy, staged migration.

**Phép đo ứng viên:** Dependency crypto đã thử migration / dependency nhận diện.

**Test phân biệt / bằng chứng cần:** Chặn thuật toán cũ trong lab có client legacy.

**Đánh đổi:** Tương thích và chi phí phần cứng.

**OPEN:** Dữ liệu giữ bí mật dài hạn cần lộ trình hậu lượng tử nào?

**Liên hệ có điều kiện:**

- `inv-dependency` — Migration cần biết mọi consumer và protocol bị ảnh hưởng.
- `F03` — Inventory dữ liệu bí mật dài hạn và protocol hybrid cần cách đo migration/compatibility nào?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Dịch vụ tương thích và dữ liệu còn đọc được / Client cũ buộc downgrade hoặc mất kết nối
- **domain:** Chốt population và giới hạn: Dữ liệu lưu và truyền; PKI/KMS owner; Thuật toán, chứng thư hoặc key policy đổi
- **mechanism:** Control có giữ invariant này không? Đổi thuật toán không chỉ là sửa một tên cấu hình
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Chặn thuật toán cũ trong lab có client legacy
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? KMS/HSM; backup khóa; năng lực chuyển đổi; Thuật toán; khóa; nonce; chứng thư; thời hạn bí mật
- **consequence:** Đạt Bí mật và toàn vẹn theo mô hình đối thủ cụ thể nhưng phải theo dõi Tương thích và chi phí phần cứng

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Dependency crypto đã thử migration / dependency nhận diện
- **domain:** Dữ liệu lưu và truyền; PKI/KMS owner; Thuật toán, chứng thư hoặc key policy đổi
- **conditions:** Thuật toán, chứng thư hoặc key policy đổi
- **goal:** Bí mật và toàn vẹn theo mô hình đối thủ cụ thể
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Phiên bản protocol và migration result; bằng chứng test: Chặn thuật toán cũ trong lab có client legacy
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Tương thích và chi phí phần cứng; Dữ liệu giữ bí mật dài hạn cần lộ trình hậu lượng tử nào?
- **binding:** cry-agility → điểm thực thi: Lập lộ trình thay đổi theo dependency
