### det-base — Base rate và chất lượng cảnh báo

**Điều kiện:** Sự kiện thật hiếm.

- **I:** Alert, ground truth có giới hạn và population
- **P:** Tách TP,FP,FN cùng phạm vi nhãn
- **O:** Precision/recall theo bộ đánh giá
- **D:** Label provenance và unresolved cases

**Hằng trong frame:** Accuracy cao không đủ khi class mất cân bằng.

**Đường hỏng:** Hàng nghìn false positive nuốt analyst. **Điểm can thiệp:** Đánh giá theo workload và cost sai lầm.

**Phép đo ứng viên:** TP/(TP+FP); TP/(TP+FN) chỉ khi FN có ground truth.

**Test phân biệt / bằng chứng cần:** Đổi prevalence giữ sensitivity; precision phải đổi.

**Đánh đổi:** Giảm false positive có thể tăng bỏ sót.

**OPEN:** Bộ test khác phân bố production ra sao?

**Liên hệ có điều kiện:**

- `det-queue` — False positives và complexity quyết định workload, không chỉ alert count.
- `F21` — Ai có thể chạm honeypot hợp lệ, và tín hiệu phản ánh môi trường thật đến đâu?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Precision/recall theo bộ đánh giá / Hàng nghìn false positive nuốt analyst
- **domain:** Chốt population và giới hạn: Tín hiệu đến quyết định; SOC; Sự kiện thật hiếm
- **mechanism:** Control có giữ invariant này không? Accuracy cao không đủ khi class mất cân bằng
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đổi prevalence giữ sensitivity; precision phải đổi
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Analyst; rules; ground truth; diễn tập; Base rate; adversary drift; queue; nhãn chưa đầy đủ
- **consequence:** Đạt Nhận ra sự kiện cần xử lý với chi phí chấp nhận được nhưng phải theo dõi Giảm false positive có thể tăng bỏ sót

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** TP/(TP+FP); TP/(TP+FN) chỉ khi FN có ground truth
- **domain:** Tín hiệu đến quyết định; SOC; Sự kiện thật hiếm
- **conditions:** Sự kiện thật hiếm
- **goal:** Nhận ra sự kiện cần xử lý với chi phí chấp nhận được
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Label provenance và unresolved cases; bằng chứng test: Đổi prevalence giữ sensitivity; precision phải đổi
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Giảm false positive có thể tăng bỏ sót; Bộ test khác phân bố production ra sao?
- **binding:** det-base → điểm thực thi: Tách TP,FP,FN cùng phạm vi nhãn
