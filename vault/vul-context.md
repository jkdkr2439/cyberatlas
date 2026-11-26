### vul-context — Severity khác rủi ro

**Điều kiện:** Một CVE trên nhiều tài sản.

- **I:** CVSS, reachability, workload và business impact
- **P:** Đặt finding vào đường gây hại có điều kiện
- **O:** Ưu tiên gắn kịch bản
- **D:** Nguồn CVE và giả định local

**Hằng trong frame:** Không dùng severity như xác suất bị khai thác.

**Đường hỏng:** Patch dễ nhiều để làm đẹp KPI, bỏ hệ trọng yếu. **Điểm can thiệp:** Ưu tiên có context và kiểm chứng đường phơi nhiễm.

**Phép đo ứng viên:** Số/giờ cặp asset-lỗ hổng phơi nhiễm theo criticality strata.

**Test phân biệt / bằng chứng cần:** Đổi reachability, giữ CVSS; ưu tiên phải được xem lại.

**Đánh đổi:** Context tốn dữ liệu; không thể chờ hoàn hảo.

**OPEN:** Thiếu exploit telemetry thì uncertainty được trình bày sao?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Ưu tiên gắn kịch bản / Patch dễ nhiều để làm đẹp KPI, bỏ hệ trọng yếu
- **domain:** Chốt population và giới hạn: Asset-vulnerability pair; VM team; Một CVE trên nhiều tài sản
- **mechanism:** Control có giữ invariant này không? Không dùng severity như xác suất bị khai thác
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đổi reachability, giữ CVSS; ưu tiên phải được xem lại
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Scanner; inventory; change window; kiểm chứng sửa; Reachability; exploitability; control; tuổi tồn tại
- **consequence:** Đạt Giảm đường gây hại có ý nghĩa trong scope nhưng phải theo dõi Context tốn dữ liệu; không thể chờ hoàn hảo

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Số/giờ cặp asset-lỗ hổng phơi nhiễm theo criticality strata
- **domain:** Asset-vulnerability pair; VM team; Một CVE trên nhiều tài sản
- **conditions:** Một CVE trên nhiều tài sản
- **goal:** Giảm đường gây hại có ý nghĩa trong scope
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Nguồn CVE và giả định local; bằng chứng test: Đổi reachability, giữ CVSS; ưu tiên phải được xem lại
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Context tốn dữ liệu; không thể chờ hoàn hảo; Thiếu exploit telemetry thì uncertainty được trình bày sao?
- **binding:** vul-context → điểm thực thi: Đặt finding vào đường gây hại có điều kiện
