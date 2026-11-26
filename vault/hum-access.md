### hum-access — Ra vào và custody thiết bị

**Điều kiện:** Có khách, sửa chữa hoặc thiết bị thất lạc.

- **I:** Visitor request, badge, device ID
- **P:** Xác nhận quyền và ghi chain custody
- **O:** Người/thiết bị đúng vùng
- **D:** Access/custody events

**Hằng trong frame:** Có badge không chứng minh đúng mục đích mọi vùng.

**Đường hỏng:** Tailgating hoặc thiết bị rời tổ chức chưa wipe. **Điểm can thiệp:** Escort theo risk, custody và remote lock phù hợp.

**Phép đo ứng viên:** Ngoại lệ custody chưa giải quyết / ngoại lệ phát sinh.

**Test phân biệt / bằng chứng cần:** Diễn tập thất lạc thiết bị không chứa dữ liệu thật.

**Đánh đổi:** Giám sát vật lý tác động riêng tư và trải nghiệm.

**OPEN:** Khả năng mở khóa khi khẩn cấp có conflict gì?

**Liên hệ có điều kiện:**

- `cry-key` — Mất thiết bị/custody có thể thay đổi giả định bí mật khóa.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Người/thiết bị đúng vùng / Tailgating hoặc thiết bị rời tổ chức chưa wipe
- **domain:** Chốt population và giới hạn: Nhân viên, khách, thiết bị; HR/IT/facilities; Có khách, sửa chữa hoặc thiết bị thất lạc
- **mechanism:** Control có giữ invariant này không? Có badge không chứng minh đúng mục đích mọi vùng
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Diễn tập thất lạc thiết bị không chứa dữ liệu thật
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Đào tạo theo vai; hỗ trợ; kiểm soát ra vào; Mệt mỏi; động cơ; accessibility; contractor; offboarding
- **consequence:** Đạt Quy trình có thể dùng an toàn trong áp lực thực tế nhưng phải theo dõi Giám sát vật lý tác động riêng tư và trải nghiệm

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Ngoại lệ custody chưa giải quyết / ngoại lệ phát sinh
- **domain:** Nhân viên, khách, thiết bị; HR/IT/facilities; Có khách, sửa chữa hoặc thiết bị thất lạc
- **conditions:** Có khách, sửa chữa hoặc thiết bị thất lạc
- **goal:** Quy trình có thể dùng an toàn trong áp lực thực tế
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Access/custody events; bằng chứng test: Diễn tập thất lạc thiết bị không chứa dữ liệu thật
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Giám sát vật lý tác động riêng tư và trải nghiệm; Khả năng mở khóa khi khẩn cấp có conflict gì?
- **binding:** hum-access → điểm thực thi: Xác nhận quyền và ghi chain custody
