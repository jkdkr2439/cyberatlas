### rec-consistency — Nhất quán khi phục hồi

**Điều kiện:** Nhiều store/queue khôi phục khác mốc.

- **I:** Snapshots, event log và business ledger
- **P:** Đối soát, replay và giải quyết xung đột có rule
- **O:** Trạng thái không nhân đôi/mất nghĩa vụ
- **D:** Reconciliation và unresolved records

**Hằng trong frame:** Các backup riêng đúng chưa chắc toàn hệ đúng.

**Đường hỏng:** Đơn hàng có mà thanh toán không khớp. **Điểm can thiệp:** Consistent checkpoint hoặc reconciliation rõ ràng.

**Phép đo ứng viên:** Record lệch invariant / record đối soát.

**Test phân biệt / bằng chứng cần:** Restore hai store lệch thời gian trong lab.

**Đánh đổi:** Replay và đối soát kéo dài RTO.

**OPEN:** Những side effect ngoài hệ không đảo lại được xử lý thế nào?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Trạng thái không nhân đôi/mất nghĩa vụ / Đơn hàng có mà thanh toán không khớp
- **domain:** Chốt population và giới hạn: Dịch vụ đầu cuối; business continuity; Nhiều store/queue khôi phục khác mốc
- **mechanism:** Control có giữ invariant này không? Các backup riêng đúng chưa chắc toàn hệ đúng
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Restore hai store lệch thời gian trong lab
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Backup; clean room; key custody; người kiểm tra; RTO; RPO; dependency; corruption; identity outage
- **consequence:** Đạt Phục hồi trạng thái kinh doanh chấp nhận được nhưng phải theo dõi Replay và đối soát kéo dài RTO

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Record lệch invariant / record đối soát
- **domain:** Dịch vụ đầu cuối; business continuity; Nhiều store/queue khôi phục khác mốc
- **conditions:** Nhiều store/queue khôi phục khác mốc
- **goal:** Phục hồi trạng thái kinh doanh chấp nhận được
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Reconciliation và unresolved records; bằng chứng test: Restore hai store lệch thời gian trong lab
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Replay và đối soát kéo dài RTO; Những side effect ngoài hệ không đảo lại được xử lý thế nào?
- **binding:** rec-consistency → điểm thực thi: Đối soát, replay và giải quyết xung đột có rule
