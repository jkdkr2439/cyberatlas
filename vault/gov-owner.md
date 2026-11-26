### gov-owner — Trách nhiệm quyết định

**Điều kiện:** Nhiều nhóm cùng quản một dịch vụ.

- **I:** Finding và tác động dự kiến
- **P:** Gắn người có quyền chấp nhận hoặc yêu cầu sửa
- **O:** Quyết định có thời hạn
- **D:** Owner, lý do, ngày xem lại

**Hằng trong frame:** Không có rủi ro được bỏ mặc vì không thuộc nhóm nào.

**Đường hỏng:** Ticket chuyển vòng nhưng không ai quyết. **Điểm can thiệp:** Owner theo dịch vụ và escalation.

**Phép đo ứng viên:** Số quyết định quá hạn không owner / số quyết định đến hạn.

**Test phân biệt / bằng chứng cần:** Đổi owner nhân sự rồi kiểm tra việc bàn giao.

**Đánh đổi:** Thêm phê duyệt kéo dài thời gian sửa.

**OPEN:** Ai có quyền chấp nhận hậu quả vượt ngân sách của nhóm?

**Liên hệ có điều kiện:**

- `F24` — Jurisdiction, loại dữ liệu, nghĩa vụ báo cáo và bằng chứng đáp ứng cụ thể là gì?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Quyết định có thời hạn / Ticket chuyển vòng nhưng không ai quyết
- **domain:** Chốt population và giới hạn: Doanh nghiệp; hội đồng rủi ro và chủ dịch vụ; Nhiều nhóm cùng quản một dịch vụ
- **mechanism:** Control có giữ invariant này không? Không có rủi ro được bỏ mặc vì không thuộc nhóm nào
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đổi owner nhân sự rồi kiểm tra việc bàn giao
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Thẩm quyền; thời gian đánh giá; ngân sách sửa sai; Khẩu vị rủi ro; quy mô; thời hạn; nghĩa vụ
- **consequence:** Đạt Quyết định có người chịu trách nhiệm và có giới hạn nhưng phải theo dõi Thêm phê duyệt kéo dài thời gian sửa

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Số quyết định quá hạn không owner / số quyết định đến hạn
- **domain:** Doanh nghiệp; hội đồng rủi ro và chủ dịch vụ; Nhiều nhóm cùng quản một dịch vụ
- **conditions:** Nhiều nhóm cùng quản một dịch vụ
- **goal:** Quyết định có người chịu trách nhiệm và có giới hạn
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Owner, lý do, ngày xem lại; bằng chứng test: Đổi owner nhân sự rồi kiểm tra việc bàn giao
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Thêm phê duyệt kéo dài thời gian sửa; Ai có quyền chấp nhận hậu quả vượt ngân sách của nhóm?
- **binding:** gov-owner → điểm thực thi: Gắn người có quyền chấp nhận hoặc yêu cầu sửa
