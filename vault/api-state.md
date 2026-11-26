### api-state — Invariant nghiệp vụ

**Điều kiện:** Mua hàng, hoàn tiền, đặt chỗ.

- **I:** Hành động và trạng thái giao dịch
- **P:** Kiểm tra transition cùng điều kiện nghiệp vụ
- **O:** Trạng thái mới hợp lệ
- **D:** Ledger và lịch sử transition

**Hằng trong frame:** Mỗi bước hợp lệ riêng chưa chắc cả chuỗi hợp lệ.

**Đường hỏng:** Bỏ bước xác nhận hoặc hoàn tiền quá số đã trả. **Điểm can thiệp:** State machine và invariant ở commit.

**Phép đo ứng viên:** Transition vi phạm invariant / chuỗi thử.

**Test phân biệt / bằng chứng cần:** Đảo thứ tự, lặp bước và đổi giá giữa các bước.

**Đánh đổi:** Luật chặt có thể cản ngoại lệ cần xử lý tay.

**OPEN:** Những trường hợp nghiệp vụ hợp lệ chưa được mô hình hóa?

**Liên hệ có điều kiện:**

- `rec-consistency` — Khôi phục phải giữ invariant nghiệp vụ chứ không chỉ bảng dữ liệu.
- `F12` — Byzantine faults, finality và khả năng quan sát thay đổi invariant giao dịch thế nào?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Trạng thái mới hợp lệ / Bỏ bước xác nhận hoặc hoàn tiền quá số đã trả
- **domain:** Chốt population và giới hạn: API đồng bộ/bất đồng bộ; product team; Mua hàng, hoàn tiền, đặt chỗ
- **mechanism:** Control có giữ invariant này không? Mỗi bước hợp lệ riêng chưa chắc cả chuỗi hợp lệ
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đảo thứ tự, lặp bước và đổi giá giữa các bước
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Transaction store; rate budget; test nghiệp vụ; Retry; concurrency; tenant; giá; số lượng
- **consequence:** Đạt Giao dịch giữ đúng quyền, thứ tự và giới hạn nhưng phải theo dõi Luật chặt có thể cản ngoại lệ cần xử lý tay

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Transition vi phạm invariant / chuỗi thử
- **domain:** API đồng bộ/bất đồng bộ; product team; Mua hàng, hoàn tiền, đặt chỗ
- **conditions:** Mua hàng, hoàn tiền, đặt chỗ
- **goal:** Giao dịch giữ đúng quyền, thứ tự và giới hạn
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Ledger và lịch sử transition; bằng chứng test: Đảo thứ tự, lặp bước và đổi giá giữa các bước
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Luật chặt có thể cản ngoại lệ cần xử lý tay; Những trường hợp nghiệp vụ hợp lệ chưa được mô hình hóa?
- **binding:** api-state → điểm thực thi: Kiểm tra transition cùng điều kiện nghiệp vụ
