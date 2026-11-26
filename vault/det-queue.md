### det-queue — Năng lực xử lý SOC

**Điều kiện:** Alert đến nhanh hơn khả năng review.

- **I:** Arrival rate, complexity và analyst availability
- **P:** Ưu tiên, gom và escalation theo hậu quả
- **O:** Case được xử lý trước khi mất ý nghĩa
- **D:** Queue age, disposition và handoff

**Hằng trong frame:** Thời gian detect nhanh không có ích nếu không hành động.

**Đường hỏng:** Backlog tăng; ca khó bị bỏ lại. **Điểm can thiệp:** Capacity planning và ưu tiên có owner.

**Phép đo ứng viên:** Phân bố tuổi queue theo severity/context; unfinished báo riêng.

**Test phân biệt / bằng chứng cần:** Tăng tải ca khó nhưng giữ alert count.

**Đánh đổi:** Tự động đóng làm đẹp latency nhưng che bỏ sót.

**OPEN:** Mệt mỏi và ca trực ảnh hưởng chất lượng thế nào?

**Liên hệ có điều kiện:**

- `hum-report` — Triage chậm và phản hồi kém có thể làm người dùng ngừng báo cáo.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Case được xử lý trước khi mất ý nghĩa / Backlog tăng; ca khó bị bỏ lại
- **domain:** Chốt population và giới hạn: Tín hiệu đến quyết định; SOC; Alert đến nhanh hơn khả năng review
- **mechanism:** Control có giữ invariant này không? Thời gian detect nhanh không có ích nếu không hành động
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Tăng tải ca khó nhưng giữ alert count
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Analyst; rules; ground truth; diễn tập; Base rate; adversary drift; queue; nhãn chưa đầy đủ
- **consequence:** Đạt Nhận ra sự kiện cần xử lý với chi phí chấp nhận được nhưng phải theo dõi Tự động đóng làm đẹp latency nhưng che bỏ sót

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Phân bố tuổi queue theo severity/context; unfinished báo riêng
- **domain:** Tín hiệu đến quyết định; SOC; Alert đến nhanh hơn khả năng review
- **conditions:** Alert đến nhanh hơn khả năng review
- **goal:** Nhận ra sự kiện cần xử lý với chi phí chấp nhận được
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Queue age, disposition và handoff; bằng chứng test: Tăng tải ca khó nhưng giữ alert count
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Tự động đóng làm đẹp latency nhưng che bỏ sót; Mệt mỏi và ca trực ảnh hưởng chất lượng thế nào?
- **binding:** det-queue → điểm thực thi: Ưu tiên, gom và escalation theo hậu quả
