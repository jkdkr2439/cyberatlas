### tel-coverage — Bao phủ quan sát

**Điều kiện:** Nguồn log có thể im lặng.

- **I:** Expected sources, heartbeat và event counts
- **P:** Đối soát nguồn, liveness và test event
- **O:** Healthy/degraded/unknown cho từng nguồn
- **D:** Source registry và drop statistics

**Hằng trong frame:** Không có alert không chứng minh không có tấn công.

**Đường hỏng:** Collector chết nhưng dashboard vẫn xanh. **Điểm can thiệp:** Independent heartbeat và synthetic event.

**Phép đo ứng viên:** Nguồn đạt freshness+test / nguồn được yêu cầu; missing riêng.

**Test phân biệt / bằng chứng cần:** Ngắt pipeline và xem trạng thái đổi.

**Đánh đổi:** Test events và storage có chi phí.

**OPEN:** Shadow assets chưa trong expected set làm mẫu số thiếu bao nhiêu?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Healthy/degraded/unknown cho từng nguồn / Collector chết nhưng dashboard vẫn xanh
- **domain:** Chốt population và giới hạn: Pipeline sự kiện; detection engineering; Nguồn log có thể im lặng
- **mechanism:** Control có giữ invariant này không? Không có alert không chứng minh không có tấn công
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Ngắt pipeline và xem trạng thái đổi
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Collector; storage; schema; sức người điều tra; Sampling; clock; drops; parser; retention
- **consequence:** Đạt Không nhầm thiếu dữ liệu với không có sự kiện nhưng phải theo dõi Test events và storage có chi phí

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Nguồn đạt freshness+test / nguồn được yêu cầu; missing riêng
- **domain:** Pipeline sự kiện; detection engineering; Nguồn log có thể im lặng
- **conditions:** Nguồn log có thể im lặng
- **goal:** Không nhầm thiếu dữ liệu với không có sự kiện
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Source registry và drop statistics; bằng chứng test: Ngắt pipeline và xem trạng thái đổi
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Test events và storage có chi phí; Shadow assets chưa trong expected set làm mẫu số thiếu bao nhiêu?
- **binding:** tel-coverage → điểm thực thi: Đối soát nguồn, liveness và test event
