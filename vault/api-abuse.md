### api-abuse — Lạm dụng chức năng hợp lệ

**Điều kiện:** Endpoint đúng kỹ thuật nhưng có giá trị kinh tế.

- **I:** Nhiều yêu cầu hợp quyền
- **P:** Đánh giá quota theo actor, hành vi và cost
- **O:** Dịch vụ vẫn phục vụ người hợp lệ
- **D:** Cost, intent proxies và quyết định giới hạn

**Hằng trong frame:** Authentication không bảo đảm sử dụng không gây hại.

**Đường hỏng:** Scraping hoặc mua vét bằng tài khoản hợp lệ. **Điểm can thiệp:** Business limits, fairness và escalation.

**Phép đo ứng viên:** Cost theo actor cùng tỷ lệ người hợp lệ bị chặn.

**Test phân biệt / bằng chứng cần:** Thử traffic count bằng nhau nhưng phân bố actor khác.

**Đánh đổi:** Định danh sâu có chi phí riêng tư.

**OPEN:** Phân biệt tự động hóa được phép với abuse bằng tiêu chí nào?

**Liên hệ có điều kiện:**

- `gov-loss` — Chi phí và hậu quả giúp phân biệt traffic với thiệt hại có ý nghĩa.
- `F11` — Query hợp lệ có thể gây chi phí không tuyến tính hoặc lấy trường vượt quyền thế nào?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Dịch vụ vẫn phục vụ người hợp lệ / Scraping hoặc mua vét bằng tài khoản hợp lệ
- **domain:** Chốt population và giới hạn: API đồng bộ/bất đồng bộ; product team; Endpoint đúng kỹ thuật nhưng có giá trị kinh tế
- **mechanism:** Control có giữ invariant này không? Authentication không bảo đảm sử dụng không gây hại
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Thử traffic count bằng nhau nhưng phân bố actor khác
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Transaction store; rate budget; test nghiệp vụ; Retry; concurrency; tenant; giá; số lượng
- **consequence:** Đạt Giao dịch giữ đúng quyền, thứ tự và giới hạn nhưng phải theo dõi Định danh sâu có chi phí riêng tư

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Cost theo actor cùng tỷ lệ người hợp lệ bị chặn
- **domain:** API đồng bộ/bất đồng bộ; product team; Endpoint đúng kỹ thuật nhưng có giá trị kinh tế
- **conditions:** Endpoint đúng kỹ thuật nhưng có giá trị kinh tế
- **goal:** Giao dịch giữ đúng quyền, thứ tự và giới hạn
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Cost, intent proxies và quyết định giới hạn; bằng chứng test: Thử traffic count bằng nhau nhưng phân bố actor khác
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Định danh sâu có chi phí riêng tư; Phân biệt tự động hóa được phép với abuse bằng tiêu chí nào?
- **binding:** api-abuse → điểm thực thi: Đánh giá quota theo actor, hành vi và cost
