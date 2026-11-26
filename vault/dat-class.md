### dat-class — Phân loại theo vai trò dữ liệu

**Điều kiện:** Một pipeline trộn nhiều loại dữ liệu.

- **I:** Content, provenance và intended use
- **P:** Gắn sensitivity, authority và verified status riêng
- **O:** Dữ liệu có policy xử lý đúng chức năng
- **D:** Classification rationale và lineage

**Hằng trong frame:** Nhạy cảm và đáng tin là hai trục khác nhau.

**Đường hỏng:** Text công khai bị coi là instruction; secret vào log. **Điểm can thiệp:** Type/taint/provenance tách biệt và enforcement.

**Phép đo ứng viên:** Dataset thiếu nhãn bắt buộc / dataset trong catalog.

**Test phân biệt / bằng chứng cần:** Dữ liệu công khai nhưng chứa lệnh giả phải giữ untrusted.

**Đánh đổi:** Nhãn chi tiết khó duy trì qua biến đổi.

**OPEN:** Ai được đổi nhãn và theo bằng chứng gì?

**Liên hệ có điều kiện:**

- `ai-memory` — Provenance và trạng thái kiểm chứng phải đi cùng dữ liệu qua memory.
- `F16` — Các dataset riêng không nhạy cảm có thể kết hợp để suy ra điều gì, với đối thủ nào?
- `F18` — Ai có thể collude, output vẫn tiết lộ gì, và protocol bảo vệ khâu nào?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Dữ liệu có policy xử lý đúng chức năng / Text công khai bị coi là instruction; secret vào log
- **domain:** Chốt population và giới hạn: Vòng đời dataset; data owner; Một pipeline trộn nhiều loại dữ liệu
- **mechanism:** Control có giữ invariant này không? Nhạy cảm và đáng tin là hai trục khác nhau
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Dữ liệu công khai nhưng chứa lệnh giả phải giữ untrusted
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Catalog; redaction; xóa; khôi phục; pháp chế; Bản sao; cache; log; lineage; miền pháp lý
- **consequence:** Đạt Dùng đúng loại dữ liệu, mục đích và thời hạn nhưng phải theo dõi Nhãn chi tiết khó duy trì qua biến đổi

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Dataset thiếu nhãn bắt buộc / dataset trong catalog
- **domain:** Vòng đời dataset; data owner; Một pipeline trộn nhiều loại dữ liệu
- **conditions:** Một pipeline trộn nhiều loại dữ liệu
- **goal:** Dùng đúng loại dữ liệu, mục đích và thời hạn
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Classification rationale và lineage; bằng chứng test: Dữ liệu công khai nhưng chứa lệnh giả phải giữ untrusted
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Nhãn chi tiết khó duy trì qua biến đổi; Ai được đổi nhãn và theo bằng chứng gì?
- **binding:** dat-class → điểm thực thi: Gắn sensitivity, authority và verified status riêng
