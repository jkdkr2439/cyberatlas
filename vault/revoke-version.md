### revoke-version — Đơn điệu của phiên bản quyền

**Điều kiện:** State từ nhiều replica đến không theo thứ tự.

- **I:** Quyền cũ/mới kèm epoch
- **P:** Không cho cập nhật epoch thấp thay epoch cao
- **O:** State consumer không đi lùi
- **D:** Applied epoch và discarded events

**Hằng trong frame:** Một event đến muộn không được hồi sinh quyền cũ.

**Đường hỏng:** Arrival order bị coi là authority order. **Điểm can thiệp:** Monotonic epoch với nguồn authority rõ.

**Phép đo ứng viên:** Lần state đi lùi / update sequence thử.

**Test phân biệt / bằng chứng cần:** Phát revoke mới trước rồi phát event cũ sau.

**Đánh đổi:** Epoch ordering giữa nhiều authority cần thiết kế.

**OPEN:** Hợp nhất nhiều nguồn quyền có một thứ tự toàn phần không?


## Sáu miền review

- **meaning:** Một event đến muộn không được hồi sinh quyền cũ
- **domain:** Ứng dụng sau đăng nhập; IAM và app owner; Đổi role, nghỉ việc hoặc lộ token; Quyết định được cache để giảm latency; State từ nhiều replica đến không theo thứ tự
- **mechanism:** Không cho cập nhật epoch thấp thay epoch cao; failure: Arrival order bị coi là authority order
- **evidence:** Phát revoke mới trước rồi phát event cũ sau
- **operational:** Kho phiên; đồng hồ; kênh invalidation; telemetry; Epoch ordering giữa nhiều authority cần thiết kế
- **consequence:** Quyền không tồn tại vượt điều kiện được cấp; Hợp nhất nhiều nguồn quyền có một thứ tự toàn phần không?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Lần state đi lùi / update sequence thử
- **domain:** Ứng dụng sau đăng nhập; IAM và app owner; Đổi role, nghỉ việc hoặc lộ token; Quyết định được cache để giảm latency; State từ nhiều replica đến không theo thứ tự
- **conditions:** State từ nhiều replica đến không theo thứ tự
- **goal:** Quyền không tồn tại vượt điều kiện được cấp
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Applied epoch và discarded events
- **method:** Phát revoke mới trước rồi phát event cũ sau
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Epoch ordering giữa nhiều authority cần thiết kế; Hợp nhất nhiều nguồn quyền có một thứ tự toàn phần không?
- **binding:** revoke-version → Không cho cập nhật epoch thấp thay epoch cao
