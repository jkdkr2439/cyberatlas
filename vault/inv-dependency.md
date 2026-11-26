### inv-dependency — Phụ thuộc quan trọng

**Điều kiện:** Một dịch vụ chứa nhiều thành phần.

- **I:** Trace, cấu hình, hợp đồng, phỏng vấn owner
- **P:** Nối dịch vụ với identity, DNS, key và nhà cung cấp
- **O:** Đồ thị phụ thuộc có điều kiện
- **D:** Phiên bản cạnh và độ chắc chắn

**Hằng trong frame:** Phụ thuộc dự phòng cũng phải được ghi.

**Đường hỏng:** Chỉ lập danh sách server mà bỏ IdP. **Điểm can thiệp:** Diễn tập mất từng dependency và xác nhận đường dự phòng.

**Phép đo ứng viên:** Quan hệ quan trọng được kiểm thử / quan hệ quan trọng đã nhận diện.

**Test phân biệt / bằng chứng cần:** Ngắt IdP trong lab dù app server còn khỏe.

**Đánh đổi:** Traces đầy đủ tăng chi phí và rủi ro riêng tư.

**OPEN:** Phụ thuộc nào chỉ xuất hiện vào kỳ quyết toán?

**Liên hệ có điều kiện:**

- `rec-objective` — RTO đầu cuối phụ thuộc các dịch vụ nền, không chỉ database.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Đồ thị phụ thuộc có điều kiện / Chỉ lập danh sách server mà bỏ IdP
- **domain:** Chốt population và giới hạn: Hạ tầng và SaaS; chủ tài sản; Một dịch vụ chứa nhiều thành phần
- **mechanism:** Control có giữ invariant này không? Phụ thuộc dự phòng cũng phải được ghi
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Ngắt IdP trong lab dù app server còn khỏe
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Đầu nối inventory; quyền đọc; người xác nhận owner; Tài sản ngắn hạn; shadow IT; mua bán doanh nghiệp
- **consequence:** Đạt Biết đối tượng nào cần bảo vệ và nó phụ thuộc gì nhưng phải theo dõi Traces đầy đủ tăng chi phí và rủi ro riêng tư

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Quan hệ quan trọng được kiểm thử / quan hệ quan trọng đã nhận diện
- **domain:** Hạ tầng và SaaS; chủ tài sản; Một dịch vụ chứa nhiều thành phần
- **conditions:** Một dịch vụ chứa nhiều thành phần
- **goal:** Biết đối tượng nào cần bảo vệ và nó phụ thuộc gì
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Phiên bản cạnh và độ chắc chắn; bằng chứng test: Ngắt IdP trong lab dù app server còn khỏe
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Traces đầy đủ tăng chi phí và rủi ro riêng tư; Phụ thuộc nào chỉ xuất hiện vào kỳ quyết toán?
- **binding:** inv-dependency → điểm thực thi: Nối dịch vụ với identity, DNS, key và nhà cung cấp
