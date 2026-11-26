### ir-learn — Học sau sự cố

**Điều kiện:** Dịch vụ đã ổn định.

- **I:** Timeline, quyết định và khoảng mù
- **P:** Phân biệt cause, contributing conditions và unknown
- **O:** Thay đổi control có owner
- **D:** Action register và retest

**Hằng trong frame:** Kết luận một người sơ suất không đủ cơ chế.

**Đường hỏng:** Viết postmortem nhưng control không đổi. **Điểm can thiệp:** Action có acceptance và diễn tập lại.

**Phép đo ứng viên:** Action đến hạn được retest hiệu lực / action đến hạn.

**Test phân biệt / bằng chứng cần:** Lặp scenario sau sửa để kiểm nguyên nhân còn hay không.

**Đánh đổi:** Tập trung một incident có thể bỏ rủi ro khác.

**OPEN:** Bài học chuyển sang hệ nào cần đổi frame?

**Liên hệ có điều kiện:**

- `sw-design` — Sự cố tạo yêu cầu thiết kế mới và kịch bản kiểm thử lại.
- `F22` — Ai được nói điều gì với mức chắc chắn nào khi scope sự cố còn chưa biết?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Thay đổi control có owner / Viết postmortem nhưng control không đổi
- **domain:** Chốt population và giới hạn: Sự cố đã nghi ngờ; incident commander; Dịch vụ đã ổn định
- **mechanism:** Control có giữ invariant này không? Kết luận một người sơ suất không đủ cơ chế
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Lặp scenario sau sửa để kiểm nguyên nhân còn hay không
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Runbook; đội trực; kho chứng cứ; truyền thông; Thời điểm; phạm vi; authority; nguồn chứng cứ
- **consequence:** Đạt Giới hạn thiệt hại và giữ khả năng hiểu sự kiện nhưng phải theo dõi Tập trung một incident có thể bỏ rủi ro khác

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Action đến hạn được retest hiệu lực / action đến hạn
- **domain:** Sự cố đã nghi ngờ; incident commander; Dịch vụ đã ổn định
- **conditions:** Dịch vụ đã ổn định
- **goal:** Giới hạn thiệt hại và giữ khả năng hiểu sự kiện
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Action register và retest; bằng chứng test: Lặp scenario sau sửa để kiểm nguyên nhân còn hay không
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Tập trung một incident có thể bỏ rủi ro khác; Bài học chuyển sang hệ nào cần đổi frame?
- **binding:** ir-learn → điểm thực thi: Phân biệt cause, contributing conditions và unknown
