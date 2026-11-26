### action-observe — Quan sát độc lập sau tác động

**Điều kiện:** Tool receipt không đủ để biết hệ đã đổi.

- **I:** Receipt và read-back từ hệ đích
- **P:** Đối chiếu đúng object/version, xét consistency delay
- **O:** Verified, contradicted hoặc unresolved outcome
- **D:** Read source, time, expected và observed

**Hằng trong frame:** Cùng chuỗi text tool trả không phải hai nguồn độc lập.

**Đường hỏng:** Agent dùng lời tool xác nhận chính lời tool. **Điểm can thiệp:** Independent read hoặc human review đúng scope.

**Phép đo ứng viên:** Outcome unresolved / actions cần hậu kiểm.

**Test phân biệt / bằng chứng cần:** Actuator giả báo done; sensor riêng báo chưa đổi.

**Đánh đổi:** Hậu kiểm có thể chậm và cũng có lỗi sensor.

**OPEN:** Nguồn đọc và nguồn ghi có common failure nào?


## Sáu miền review

- **meaning:** Cùng chuỗi text tool trả không phải hai nguồn độc lập
- **domain:** Ứng dụng LLM và automation; AI/platform owner; Model có khả năng ghi hoặc gửi; Gateway đã cho phép request; Tool receipt không đủ để biết hệ đã đổi
- **mechanism:** Đối chiếu đúng object/version, xét consistency delay; failure: Agent dùng lời tool xác nhận chính lời tool
- **evidence:** Actuator giả báo done; sensor riêng báo chưa đổi
- **operational:** Policy ngoài model; sandbox; review; provenance; Hậu kiểm có thể chậm và cũng có lỗi sensor
- **consequence:** Nội dung không đáng tin không được nâng thành authority; Nguồn đọc và nguồn ghi có common failure nào?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Outcome unresolved / actions cần hậu kiểm
- **domain:** Ứng dụng LLM và automation; AI/platform owner; Model có khả năng ghi hoặc gửi; Gateway đã cho phép request; Tool receipt không đủ để biết hệ đã đổi
- **conditions:** Tool receipt không đủ để biết hệ đã đổi
- **goal:** Nội dung không đáng tin không được nâng thành authority
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Read source, time, expected và observed
- **method:** Actuator giả báo done; sensor riêng báo chưa đổi
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Hậu kiểm có thể chậm và cũng có lỗi sensor; Nguồn đọc và nguồn ghi có common failure nào?
- **binding:** action-observe → Đối chiếu đúng object/version, xét consistency delay
