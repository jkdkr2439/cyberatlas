### rec-objective — RTO, RPO và kiểm tra nghiệp vụ

**Điều kiện:** Khôi phục dịch vụ nhiều thành phần.

- **I:** Mốc gián đoạn, điểm dữ liệu và mục tiêu đã duyệt
- **P:** Đo tới khi nghiệp vụ đạt điều kiện sử dụng
- **O:** Thời gian hồi phục và mất dữ liệu thực
- **D:** Timeline và reconciliation

**Hằng trong frame:** Server lên không đồng nghĩa đơn hàng hoạt động.

**Đường hỏng:** Database phục hồi nhưng queue/DNS/key chưa sẵn. **Điểm can thiệp:** Test end-to-end theo critical transaction.

**Phép đo ứng viên:** Recovery elapsed và data-loss interval; so mục tiêu riêng.

**Test phân biệt / bằng chứng cần:** Khôi phục DB nhưng cố tình thiếu queue; chưa được tính pass.

**Đánh đổi:** Mục tiêu gắt cần dự phòng và chi phí.

**OPEN:** Mục tiêu có thay đổi theo mùa hoặc nhóm khách?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Thời gian hồi phục và mất dữ liệu thực / Database phục hồi nhưng queue/DNS/key chưa sẵn
- **domain:** Chốt population và giới hạn: Dịch vụ đầu cuối; business continuity; Khôi phục dịch vụ nhiều thành phần
- **mechanism:** Control có giữ invariant này không? Server lên không đồng nghĩa đơn hàng hoạt động
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Khôi phục DB nhưng cố tình thiếu queue; chưa được tính pass
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Backup; clean room; key custody; người kiểm tra; RTO; RPO; dependency; corruption; identity outage
- **consequence:** Đạt Phục hồi trạng thái kinh doanh chấp nhận được nhưng phải theo dõi Mục tiêu gắt cần dự phòng và chi phí

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Recovery elapsed và data-loss interval; so mục tiêu riêng
- **domain:** Dịch vụ đầu cuối; business continuity; Khôi phục dịch vụ nhiều thành phần
- **conditions:** Khôi phục dịch vụ nhiều thành phần
- **goal:** Phục hồi trạng thái kinh doanh chấp nhận được
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Timeline và reconciliation; bằng chứng test: Khôi phục DB nhưng cố tình thiếu queue; chưa được tính pass
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Mục tiêu gắt cần dự phòng và chi phí; Mục tiêu có thay đổi theo mùa hoặc nhóm khách?
- **binding:** rec-objective → điểm thực thi: Đo tới khi nghiệp vụ đạt điều kiện sử dụng
