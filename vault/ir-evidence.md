### ir-evidence — Thu giữ và chuỗi bảo quản

**Điều kiện:** Có thể cần điều tra kỹ thuật/pháp lý.

- **I:** Volatile state, image, log và người thu thập
- **P:** Thu đúng scope, ghi thao tác và kiểm integrity
- **O:** Bằng chứng tái kiểm tra được
- **D:** Custody, timestamp uncertainty và hashes

**Hằng trong frame:** Hành vi thu thập có thể làm thay đổi hệ.

**Đường hỏng:** Reboot làm mất memory; copy không có nguồn. **Điểm can thiệp:** Runbook theo loại bằng chứng và kiểm custody.

**Phép đo ứng viên:** Artifact thiếu metadata thiết yếu / artifact đã thu.

**Test phân biệt / bằng chứng cần:** Đưa artifact đổi hash hoặc thiếu nguồn vào review.

**Đánh đổi:** Thu đầy đủ tốn thời gian và chạm riêng tư.

**OPEN:** Chuẩn pháp lý tại nơi xử lý yêu cầu gì?

**Liên hệ có điều kiện:**

- `dat-retention` — Retention và legal hold cần được hòa giải với mục tiêu điều tra theo luật áp dụng.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Bằng chứng tái kiểm tra được / Reboot làm mất memory; copy không có nguồn
- **domain:** Chốt population và giới hạn: Sự cố đã nghi ngờ; incident commander; Có thể cần điều tra kỹ thuật/pháp lý
- **mechanism:** Control có giữ invariant này không? Hành vi thu thập có thể làm thay đổi hệ
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đưa artifact đổi hash hoặc thiếu nguồn vào review
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Runbook; đội trực; kho chứng cứ; truyền thông; Thời điểm; phạm vi; authority; nguồn chứng cứ
- **consequence:** Đạt Giới hạn thiệt hại và giữ khả năng hiểu sự kiện nhưng phải theo dõi Thu đầy đủ tốn thời gian và chạm riêng tư

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Artifact thiếu metadata thiết yếu / artifact đã thu
- **domain:** Sự cố đã nghi ngờ; incident commander; Có thể cần điều tra kỹ thuật/pháp lý
- **conditions:** Có thể cần điều tra kỹ thuật/pháp lý
- **goal:** Giới hạn thiệt hại và giữ khả năng hiểu sự kiện
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Custody, timestamp uncertainty và hashes; bằng chứng test: Đưa artifact đổi hash hoặc thiếu nguồn vào review
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Thu đầy đủ tốn thời gian và chạm riêng tư; Chuẩn pháp lý tại nơi xử lý yêu cầu gì?
- **binding:** ir-evidence → điểm thực thi: Thu đúng scope, ghi thao tác và kiểm integrity
