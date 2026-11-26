### rec-backup — Backup không phải recovery

**Điều kiện:** Dữ liệu và control plane bị hỏng.

- **I:** Backup, keys, identity và môi trường sạch
- **P:** Restore và kiểm toàn vẹn/đủ chức năng
- **O:** Dịch vụ có thể dùng thật
- **D:** Restore logs và business checks

**Hằng trong frame:** Job backup thành công không bảo đảm bản phục hồi sạch.

**Đường hỏng:** Bản sao cùng credential bị xóa cùng lúc. **Điểm can thiệp:** Cô lập authority, bản bảo vệ và restore drill.

**Phép đo ứng viên:** Recovery thành công theo tiêu chí nghiệp vụ / drill đã thử.

**Test phân biệt / bằng chứng cần:** Mất cả primary lẫn identity; thử recover bằng đường độc lập.

**Đánh đổi:** Cô lập backup làm restore khó hơn.

**OPEN:** Malware hoặc dữ liệu sai đã nằm trong backup chưa?

**Liên hệ có điều kiện:**

- `tp-concentration` — Backup trên cùng identity/provider có thể cùng failure domain.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Dịch vụ có thể dùng thật / Bản sao cùng credential bị xóa cùng lúc
- **domain:** Chốt population và giới hạn: Dịch vụ đầu cuối; business continuity; Dữ liệu và control plane bị hỏng
- **mechanism:** Control có giữ invariant này không? Job backup thành công không bảo đảm bản phục hồi sạch
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Mất cả primary lẫn identity; thử recover bằng đường độc lập
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Backup; clean room; key custody; người kiểm tra; RTO; RPO; dependency; corruption; identity outage
- **consequence:** Đạt Phục hồi trạng thái kinh doanh chấp nhận được nhưng phải theo dõi Cô lập backup làm restore khó hơn

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Recovery thành công theo tiêu chí nghiệp vụ / drill đã thử
- **domain:** Dịch vụ đầu cuối; business continuity; Dữ liệu và control plane bị hỏng
- **conditions:** Dữ liệu và control plane bị hỏng
- **goal:** Phục hồi trạng thái kinh doanh chấp nhận được
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Restore logs và business checks; bằng chứng test: Mất cả primary lẫn identity; thử recover bằng đường độc lập
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Cô lập backup làm restore khó hơn; Malware hoặc dữ liệu sai đã nằm trong backup chưa?
- **binding:** rec-backup → điểm thực thi: Restore và kiểm toàn vẹn/đủ chức năng
