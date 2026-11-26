### revoke-cache — Cache của quyết định phân quyền

**Điều kiện:** Quyết định được cache để giảm latency.

- **I:** Principal, resource, action và policy version
- **P:** Dùng cache chỉ khi key và freshness còn đúng
- **O:** Quyết định theo phiên bản quyền phù hợp
- **D:** Cache key, version, expiry và hit path

**Hằng trong frame:** Cache hợp lệ theo thời gian chưa chắc hợp lệ theo quyền mới.

**Đường hỏng:** Entry còn TTL nhưng policy đã đổi. **Điểm can thiệp:** Versioned cache key và invalidation.

**Phép đo ứng viên:** Cache hit dùng version cũ sau revoke / hits được kiểm.

**Test phân biệt / bằng chứng cần:** Đổi policy khi entry chưa hết TTL.

**Đánh đổi:** Freshness chặt tăng tải policy service.

**OPEN:** Cache âm và cache allow có cùng semantics không?


## Sáu miền review

- **meaning:** Cache hợp lệ theo thời gian chưa chắc hợp lệ theo quyền mới
- **domain:** Ứng dụng sau đăng nhập; IAM và app owner; Đổi role, nghỉ việc hoặc lộ token; Quyết định được cache để giảm latency
- **mechanism:** Dùng cache chỉ khi key và freshness còn đúng; failure: Entry còn TTL nhưng policy đã đổi
- **evidence:** Đổi policy khi entry chưa hết TTL
- **operational:** Kho phiên; đồng hồ; kênh invalidation; telemetry; Freshness chặt tăng tải policy service
- **consequence:** Quyền không tồn tại vượt điều kiện được cấp; Cache âm và cache allow có cùng semantics không?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Cache hit dùng version cũ sau revoke / hits được kiểm
- **domain:** Ứng dụng sau đăng nhập; IAM và app owner; Đổi role, nghỉ việc hoặc lộ token; Quyết định được cache để giảm latency
- **conditions:** Quyết định được cache để giảm latency
- **goal:** Quyền không tồn tại vượt điều kiện được cấp
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Cache key, version, expiry và hit path
- **method:** Đổi policy khi entry chưa hết TTL
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Freshness chặt tăng tải policy service; Cache âm và cache allow có cùng semantics không?
- **binding:** revoke-cache → Dùng cache chỉ khi key và freshness còn đúng
