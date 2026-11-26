### tel-schema — Ngữ nghĩa sự kiện

**Điều kiện:** Nhiều producer dùng schema khác.

- **I:** Raw event, parser version và timestamp
- **P:** Chuẩn hóa principal/action/resource mà giữ provenance
- **O:** Event truy vấn được và hiểu đúng
- **D:** Raw reference, normalization version và errors

**Hằng trong frame:** Parse thành công chưa chứng minh nghĩa đúng.

**Đường hỏng:** Actor/target đảo; clock lệch làm sai timeline. **Điểm can thiệp:** Schema contract, parser fixtures, time uncertainty.

**Phép đo ứng viên:** Event mất trường trọng yếu / event trong sample kiểm tra.

**Test phân biệt / bằng chứng cần:** Đổi format producer; parser phải fail rõ hoặc thích nghi đúng.

**Đánh đổi:** Giữ raw tăng riêng tư và storage.

**OPEN:** Định danh dịch vụ thay đổi được nối thế nào?

**Liên hệ có điều kiện:**

- `det-behavior` — Actor/resource sai phá correlation dù rule đúng.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Event truy vấn được và hiểu đúng / Actor/target đảo; clock lệch làm sai timeline
- **domain:** Chốt population và giới hạn: Pipeline sự kiện; detection engineering; Nhiều producer dùng schema khác
- **mechanism:** Control có giữ invariant này không? Parse thành công chưa chứng minh nghĩa đúng
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đổi format producer; parser phải fail rõ hoặc thích nghi đúng
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Collector; storage; schema; sức người điều tra; Sampling; clock; drops; parser; retention
- **consequence:** Đạt Không nhầm thiếu dữ liệu với không có sự kiện nhưng phải theo dõi Giữ raw tăng riêng tư và storage

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Event mất trường trọng yếu / event trong sample kiểm tra
- **domain:** Pipeline sự kiện; detection engineering; Nhiều producer dùng schema khác
- **conditions:** Nhiều producer dùng schema khác
- **goal:** Không nhầm thiếu dữ liệu với không có sự kiện
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Raw reference, normalization version và errors; bằng chứng test: Đổi format producer; parser phải fail rõ hoặc thích nghi đúng
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Giữ raw tăng riêng tư và storage; Định danh dịch vụ thay đổi được nối thế nào?
- **binding:** tel-schema → điểm thực thi: Chuẩn hóa principal/action/resource mà giữ provenance
