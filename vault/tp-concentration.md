### tp-concentration — Phụ thuộc tập trung

**Điều kiện:** Nhiều dịch vụ cùng dùng một upstream.

- **I:** Supplier/dependency graph
- **P:** Tìm shared failure domains
- **O:** Kịch bản nhiều dịch vụ hỏng cùng lúc
- **D:** Assumptions và scenario results

**Hằng trong frame:** Nhiều hợp đồng không nhất thiết nhiều nguồn độc lập.

**Đường hỏng:** Hai nhà cung cấp cùng cloud/IdP. **Điểm can thiệp:** Đánh giá common cause và thử fallback.

**Phép đo ứng viên:** Dịch vụ trọng yếu cùng failure domain; không cộng xác suất độc lập.

**Test phân biệt / bằng chứng cần:** Cho common upstream unavailable trong tabletop.

**Đánh đổi:** Đa nhà cung cấp tăng độ phức tạp.

**OPEN:** Các lớp phụ thuộc bị vendor che có thể xác nhận thế nào?

**Liên hệ có điều kiện:**

- `F27` — Failure domain, đặc quyền vận hành và time horizon khác enterprise thông thường thế nào?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Kịch bản nhiều dịch vụ hỏng cùng lúc / Hai nhà cung cấp cùng cloud/IdP
- **domain:** Chốt population và giới hạn: Quan hệ ngoài tổ chức; procurement và service owner; Nhiều dịch vụ cùng dùng một upstream
- **mechanism:** Control có giữ invariant này không? Nhiều hợp đồng không nhất thiết nhiều nguồn độc lập
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Cho common upstream unavailable trong tabletop
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Hợp đồng; test; quyền xuất dữ liệu; nguồn thay thế; Subprocessor; outage chung; remote support; exit cost
- **consequence:** Đạt Authority, dữ liệu và khả năng phục hồi không mất kiểm soát nhưng phải theo dõi Đa nhà cung cấp tăng độ phức tạp

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Dịch vụ trọng yếu cùng failure domain; không cộng xác suất độc lập
- **domain:** Quan hệ ngoài tổ chức; procurement và service owner; Nhiều dịch vụ cùng dùng một upstream
- **conditions:** Nhiều dịch vụ cùng dùng một upstream
- **goal:** Authority, dữ liệu và khả năng phục hồi không mất kiểm soát
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Assumptions và scenario results; bằng chứng test: Cho common upstream unavailable trong tabletop
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Đa nhà cung cấp tăng độ phức tạp; Các lớp phụ thuộc bị vendor che có thể xác nhận thế nào?
- **binding:** tp-concentration → điểm thực thi: Tìm shared failure domains
