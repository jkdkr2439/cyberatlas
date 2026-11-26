### ot-legacy — Thiết bị cũ khó vá

**Điều kiện:** Thiết bị không thể cập nhật thường xuyên.

- **I:** Firmware, network paths và maintenance plan
- **P:** Giảm đường tiếp cận và thử thay đổi ngoại tuyến
- **O:** Phơi nhiễm giảm trong giới hạn vận hành
- **D:** Inventory, compensating controls và lịch thay

**Hằng trong frame:** Không vá được không đồng nghĩa không có cách giảm rủi ro.

**Đường hỏng:** Agent/scan làm treo thiết bị cũ. **Điểm can thiệp:** Segmentation, allowlisting phù hợp, passive visibility.

**Phép đo ứng viên:** Đường truy cập không cần thiết còn mở / đường review.

**Test phân biệt / bằng chứng cần:** Kiểm trên digital twin/lab trước khi tác động thật.

**Đánh đổi:** Control bù có thể kéo dài nợ thay thiết bị.

**OPEN:** Khi nào control bù không còn đủ để vận hành?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Phơi nhiễm giảm trong giới hạn vận hành / Agent/scan làm treo thiết bị cũ
- **domain:** Chốt population và giới hạn: Thiết bị và quy trình vật lý; kỹ sư vận hành; Thiết bị không thể cập nhật thường xuyên
- **mechanism:** Control có giữ invariant này không? Không vá được không đồng nghĩa không có cách giảm rủi ro
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Kiểm trên digital twin/lab trước khi tác động thật
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Kỹ sư safety; lab; spare parts; vận hành tại chỗ; Chu kỳ điều khiển; tuổi thiết bị; vendor; maintenance window
- **consequence:** Đạt An toàn con người và tiến trình trong điều kiện tấn công/lỗi nhưng phải theo dõi Control bù có thể kéo dài nợ thay thiết bị

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Đường truy cập không cần thiết còn mở / đường review
- **domain:** Thiết bị và quy trình vật lý; kỹ sư vận hành; Thiết bị không thể cập nhật thường xuyên
- **conditions:** Thiết bị không thể cập nhật thường xuyên
- **goal:** An toàn con người và tiến trình trong điều kiện tấn công/lỗi
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Inventory, compensating controls và lịch thay; bằng chứng test: Kiểm trên digital twin/lab trước khi tác động thật
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Control bù có thể kéo dài nợ thay thiết bị; Khi nào control bù không còn đủ để vận hành?
- **binding:** ot-legacy → điểm thực thi: Giảm đường tiếp cận và thử thay đổi ngoại tuyến
