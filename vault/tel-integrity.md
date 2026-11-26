### tel-integrity — Toàn vẹn bằng chứng

**Điều kiện:** Nguồn bị đối thủ kiểm soát.

- **I:** Log và metadata nguồn
- **P:** Truyền, bảo vệ lưu trữ và đối soát nguồn khác
- **O:** Bằng chứng có mức tin cậy nêu rõ
- **D:** Hash, access log và chain metadata

**Hằng trong frame:** Hash chứng minh dữ liệu không đổi sau mốc, không chứng minh sự thật ban đầu.

**Đường hỏng:** Máy bị chiếm tự tạo log sai. **Điểm can thiệp:** Remote logging và corroboration độc lập.

**Phép đo ứng viên:** Sự kiện trọng yếu có nguồn đối soát / sự kiện mẫu.

**Test phân biệt / bằng chứng cần:** Thay log nguồn và xem có phát hiện chênh.

**Đánh đổi:** Nhiều nguồn có thể cùng phụ thuộc một clock/agent.

**OPEN:** Độc lập của hai nguồn được kiểm tra ra sao?

**Liên hệ có điều kiện:**

- `ir-evidence` — Chuỗi nguồn và integrity là đầu vào đánh giá bằng chứng, không thay mọi thủ tục pháp lý.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Bằng chứng có mức tin cậy nêu rõ / Máy bị chiếm tự tạo log sai
- **domain:** Chốt population và giới hạn: Pipeline sự kiện; detection engineering; Nguồn bị đối thủ kiểm soát
- **mechanism:** Control có giữ invariant này không? Hash chứng minh dữ liệu không đổi sau mốc, không chứng minh sự thật ban đầu
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Thay log nguồn và xem có phát hiện chênh
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Collector; storage; schema; sức người điều tra; Sampling; clock; drops; parser; retention
- **consequence:** Đạt Không nhầm thiếu dữ liệu với không có sự kiện nhưng phải theo dõi Nhiều nguồn có thể cùng phụ thuộc một clock/agent

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Sự kiện trọng yếu có nguồn đối soát / sự kiện mẫu
- **domain:** Pipeline sự kiện; detection engineering; Nguồn bị đối thủ kiểm soát
- **conditions:** Nguồn bị đối thủ kiểm soát
- **goal:** Không nhầm thiếu dữ liệu với không có sự kiện
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Hash, access log và chain metadata; bằng chứng test: Thay log nguồn và xem có phát hiện chênh
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Nhiều nguồn có thể cùng phụ thuộc một clock/agent; Độc lập của hai nguồn được kiểm tra ra sao?
- **binding:** tel-integrity → điểm thực thi: Truyền, bảo vệ lưu trữ và đối soát nguồn khác
