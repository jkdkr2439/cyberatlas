### hum-report — Khả năng báo cáo sai sót

**Điều kiện:** Người dùng gặp nghi ngờ hoặc lỡ thao tác.

- **I:** Report của người dùng và bối cảnh
- **P:** Tiếp nhận không đổ lỗi, hướng dẫn và triage
- **O:** Thông tin đến người có thể xử lý
- **D:** Report timeline và feedback

**Hằng trong frame:** Không báo không chứng minh không có sự kiện.

**Đường hỏng:** Phạt người báo khiến sự cố bị giấu. **Điểm can thiệp:** Kênh đơn giản, phản hồi hữu ích và diễn tập.

**Phép đo ứng viên:** Thời gian từ nhận biết đến báo trong diễn tập; không suy ra production.

**Test phân biệt / bằng chứng cần:** Thử báo cáo ngoài giờ và kiểm phản hồi.

**Đánh đổi:** Thu nhiều report tăng tải triage.

**OPEN:** Người yếu thế/contractor có kênh an toàn tương đương?

**Liên hệ có điều kiện:**

- `F25` — Quyền hợp lệ, động cơ, thiếu hỗ trợ và bị ép buộc tạo các giả thuyết phân biệt nào?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Thông tin đến người có thể xử lý / Phạt người báo khiến sự cố bị giấu
- **domain:** Chốt population và giới hạn: Nhân viên, khách, thiết bị; HR/IT/facilities; Người dùng gặp nghi ngờ hoặc lỡ thao tác
- **mechanism:** Control có giữ invariant này không? Không báo không chứng minh không có sự kiện
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Thử báo cáo ngoài giờ và kiểm phản hồi
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Đào tạo theo vai; hỗ trợ; kiểm soát ra vào; Mệt mỏi; động cơ; accessibility; contractor; offboarding
- **consequence:** Đạt Quy trình có thể dùng an toàn trong áp lực thực tế nhưng phải theo dõi Thu nhiều report tăng tải triage

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Thời gian từ nhận biết đến báo trong diễn tập; không suy ra production
- **domain:** Nhân viên, khách, thiết bị; HR/IT/facilities; Người dùng gặp nghi ngờ hoặc lỡ thao tác
- **conditions:** Người dùng gặp nghi ngờ hoặc lỡ thao tác
- **goal:** Quy trình có thể dùng an toàn trong áp lực thực tế
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Report timeline và feedback; bằng chứng test: Thử báo cáo ngoài giờ và kiểm phản hồi
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Thu nhiều report tăng tải triage; Người yếu thế/contractor có kênh an toàn tương đương?
- **binding:** hum-report → điểm thực thi: Tiếp nhận không đổ lỗi, hướng dẫn và triage
