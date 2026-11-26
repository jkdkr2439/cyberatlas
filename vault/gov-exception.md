### gov-exception — Ngoại lệ có hạn dùng

**Điều kiện:** Control không thể áp ngay.

- **I:** Yêu cầu miễn trừ và lý do
- **P:** Đánh giá phạm vi, bù trừ và ngày hết hạn
- **O:** Ngoại lệ được giới hạn
- **D:** Registry ngoại lệ và review

**Hằng trong frame:** Ngoại lệ không được âm thầm thành mặc định.

**Đường hỏng:** Gia hạn tự động che nợ rủi ro. **Điểm can thiệp:** Expiry, owner, kiểm tra control bù.

**Phép đo ứng viên:** Ngoại lệ hết hạn còn hiệu lực / ngoại lệ hết hạn.

**Test phân biệt / bằng chứng cần:** Cho ngoại lệ hết hạn trong lab; kiểm tra enforcement.

**Đánh đổi:** Chặn đột ngột có thể ngừng nghiệp vụ.

**OPEN:** Cơ chế rollback nào giữ cả an toàn lẫn tính liên tục?

**Liên hệ có điều kiện:**

- `cld-drift` — Ngoại lệ đã duyệt có hạn khác với drift không được phép.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Ngoại lệ được giới hạn / Gia hạn tự động che nợ rủi ro
- **domain:** Chốt population và giới hạn: Doanh nghiệp; hội đồng rủi ro và chủ dịch vụ; Control không thể áp ngay
- **mechanism:** Control có giữ invariant này không? Ngoại lệ không được âm thầm thành mặc định
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Cho ngoại lệ hết hạn trong lab; kiểm tra enforcement
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Thẩm quyền; thời gian đánh giá; ngân sách sửa sai; Khẩu vị rủi ro; quy mô; thời hạn; nghĩa vụ
- **consequence:** Đạt Quyết định có người chịu trách nhiệm và có giới hạn nhưng phải theo dõi Chặn đột ngột có thể ngừng nghiệp vụ

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Ngoại lệ hết hạn còn hiệu lực / ngoại lệ hết hạn
- **domain:** Doanh nghiệp; hội đồng rủi ro và chủ dịch vụ; Control không thể áp ngay
- **conditions:** Control không thể áp ngay
- **goal:** Quyết định có người chịu trách nhiệm và có giới hạn
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Registry ngoại lệ và review; bằng chứng test: Cho ngoại lệ hết hạn trong lab; kiểm tra enforcement
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Chặn đột ngột có thể ngừng nghiệp vụ; Cơ chế rollback nào giữ cả an toàn lẫn tính liên tục?
- **binding:** gov-exception → điểm thực thi: Đánh giá phạm vi, bù trừ và ngày hết hạn
