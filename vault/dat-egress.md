### dat-egress — Rò dữ liệu ở output

**Điều kiện:** Có export, report, email và log.

- **I:** Data selection và destination
- **P:** Kiểm quyền, tối thiểu hóa và kiểm destination
- **O:** Output đúng người và mục đích
- **D:** Export audit và minimization result

**Hằng trong frame:** Được đọc không tự đồng nghĩa được xuất hàng loạt.

**Đường hỏng:** Service account hợp lệ xuất quá mức. **Điểm can thiệp:** Output authorization, hạn mức và review theo sensitivity.

**Phép đo ứng viên:** Export vượt policy / export được kiểm tra.

**Test phân biệt / bằng chứng cần:** Thử export bằng quyền chỉ xem từng record.

**Đánh đổi:** Kiểm sâu tăng latency và có thể false positive.

**OPEN:** Dữ liệu suy diễn hoặc kết hợp có nhạy cảm mới không?

**Liên hệ có điều kiện:**

- `tel-schema` — Log quá nhiều để quan sát có thể tự tạo kênh rò dữ liệu.
- `F17` — Đơn vị bảo vệ, composition và utility tradeoff được định nghĩa ra sao trước khi chọn epsilon?
- `F30` — Ai truy cập output gì, budget truy vấn bao nhiêu, thiệt hại được định nghĩa thế nào?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Output đúng người và mục đích / Service account hợp lệ xuất quá mức
- **domain:** Chốt population và giới hạn: Vòng đời dataset; data owner; Có export, report, email và log
- **mechanism:** Control có giữ invariant này không? Được đọc không tự đồng nghĩa được xuất hàng loạt
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Thử export bằng quyền chỉ xem từng record
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Catalog; redaction; xóa; khôi phục; pháp chế; Bản sao; cache; log; lineage; miền pháp lý
- **consequence:** Đạt Dùng đúng loại dữ liệu, mục đích và thời hạn nhưng phải theo dõi Kiểm sâu tăng latency và có thể false positive

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Export vượt policy / export được kiểm tra
- **domain:** Vòng đời dataset; data owner; Có export, report, email và log
- **conditions:** Có export, report, email và log
- **goal:** Dùng đúng loại dữ liệu, mục đích và thời hạn
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Export audit và minimization result; bằng chứng test: Thử export bằng quyền chỉ xem từng record
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Kiểm sâu tăng latency và có thể false positive; Dữ liệu suy diễn hoặc kết hợp có nhạy cảm mới không?
- **binding:** dat-egress → điểm thực thi: Kiểm quyền, tối thiểu hóa và kiểm destination
