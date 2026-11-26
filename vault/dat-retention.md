### dat-retention — Lưu giữ và xóa

**Điều kiện:** Dữ liệu có nhiều bản sao.

- **I:** Purpose, thời hạn, replica/cache/backup map
- **P:** Áp retention theo mục đích và xử lý ngoại lệ
- **O:** Dữ liệu hết mục đích được xóa hoặc hạn chế đúng luật áp dụng
- **D:** Deletion evidence và residual copies

**Hằng trong frame:** Xóa primary row không chứng minh xóa toàn hệ.

**Đường hỏng:** Search index, logs, backup giữ bản cũ. **Điểm can thiệp:** Lineage, deletion workflow và restore-aware deletion.

**Phép đo ứng viên:** Bản sao thuộc scope chưa xử lý sau deadline / bản sao biết.

**Test phân biệt / bằng chứng cần:** Restore backup test rồi tái áp yêu cầu xóa.

**Đánh đổi:** Xóa mạnh xung đột recovery và legal hold.

**OPEN:** Yêu cầu theo từng jurisdiction cần pháp chế xác nhận gì?

**Liên hệ có điều kiện:**

- `rec-consistency` — Restore không được vô tình hồi sinh dữ liệu cần xóa ngoài ngoại lệ áp dụng.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Dữ liệu hết mục đích được xóa hoặc hạn chế đúng luật áp dụng / Search index, logs, backup giữ bản cũ
- **domain:** Chốt population và giới hạn: Vòng đời dataset; data owner; Dữ liệu có nhiều bản sao
- **mechanism:** Control có giữ invariant này không? Xóa primary row không chứng minh xóa toàn hệ
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Restore backup test rồi tái áp yêu cầu xóa
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Catalog; redaction; xóa; khôi phục; pháp chế; Bản sao; cache; log; lineage; miền pháp lý
- **consequence:** Đạt Dùng đúng loại dữ liệu, mục đích và thời hạn nhưng phải theo dõi Xóa mạnh xung đột recovery và legal hold

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Bản sao thuộc scope chưa xử lý sau deadline / bản sao biết
- **domain:** Vòng đời dataset; data owner; Dữ liệu có nhiều bản sao
- **conditions:** Dữ liệu có nhiều bản sao
- **goal:** Dùng đúng loại dữ liệu, mục đích và thời hạn
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Deletion evidence và residual copies; bằng chứng test: Restore backup test rồi tái áp yêu cầu xóa
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Xóa mạnh xung đột recovery và legal hold; Yêu cầu theo từng jurisdiction cần pháp chế xác nhận gì?
- **binding:** dat-retention → điểm thực thi: Áp retention theo mục đích và xử lý ngoại lệ
