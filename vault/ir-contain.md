### ir-contain — Khoanh vùng có thẩm quyền

**Điều kiện:** Sự cố nghi ngờ đang diễn tiến.

- **I:** Evidence, asset owner và kill-switch scope
- **P:** Chọn hành động giới hạn thiệt hại theo rủi ro
- **O:** Containment được quan sát hiệu lực
- **D:** Decision, approval và outcome

**Hằng trong frame:** Gửi lệnh isolate chưa chứng minh đã isolate.

**Đường hỏng:** Tool báo success nhưng đường khác còn mở. **Điểm can thiệp:** Read-back, probe và owner escalation.

**Phép đo ứng viên:** Thời gian từ quyết định đến containment xác nhận.

**Test phân biệt / bằng chứng cần:** Giả lập actuator không thực thi; phải báo failure.

**Đánh đổi:** Isolate có thể ngắt dịch vụ quan trọng.

**OPEN:** Có trường hợp safety buộc ưu tiên khác không?

**Liên hệ có điều kiện:**

- `rec-objective` — Containment có thể kéo dài outage để giảm lan truyền; cần mục tiêu rõ.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Containment được quan sát hiệu lực / Tool báo success nhưng đường khác còn mở
- **domain:** Chốt population và giới hạn: Sự cố đã nghi ngờ; incident commander; Sự cố nghi ngờ đang diễn tiến
- **mechanism:** Control có giữ invariant này không? Gửi lệnh isolate chưa chứng minh đã isolate
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Giả lập actuator không thực thi; phải báo failure
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Runbook; đội trực; kho chứng cứ; truyền thông; Thời điểm; phạm vi; authority; nguồn chứng cứ
- **consequence:** Đạt Giới hạn thiệt hại và giữ khả năng hiểu sự kiện nhưng phải theo dõi Isolate có thể ngắt dịch vụ quan trọng

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Thời gian từ quyết định đến containment xác nhận
- **domain:** Sự cố đã nghi ngờ; incident commander; Sự cố nghi ngờ đang diễn tiến
- **conditions:** Sự cố nghi ngờ đang diễn tiến
- **goal:** Giới hạn thiệt hại và giữ khả năng hiểu sự kiện
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Decision, approval và outcome; bằng chứng test: Giả lập actuator không thực thi; phải báo failure
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Isolate có thể ngắt dịch vụ quan trọng; Có trường hợp safety buộc ưu tiên khác không?
- **binding:** ir-contain → điểm thực thi: Chọn hành động giới hạn thiệt hại theo rủi ro
