### revoke-cas — Conditional write ở điểm commit

**Điều kiện:** Cache/store có compare-and-set hoặc transaction.

- **I:** Expected version và new entry
- **P:** Commit chỉ khi authority epoch khớp precondition
- **O:** Write bị từ chối nếu context đã đổi
- **D:** Expected/current version và CAS outcome

**Hằng trong frame:** Phải so với đúng authority version, không chỉ entry-local version.

**Đường hỏng:** CAS đúng cú pháp nhưng so sai object/version. **Điểm can thiệp:** Version binding và retry có đọc lại authority.

**Phép đo ứng viên:** Stale commit được chấp nhận / stale-epoch fixtures.

**Test phân biệt / bằng chứng cần:** Giữ cache-entry version nhưng tăng policy epoch.

**Đánh đổi:** Retry storm dưới churn quyền.

**OPEN:** Khi authority không reachable thì commit được phép không?


## Sáu miền review

- **meaning:** Phải so với đúng authority version, không chỉ entry-local version
- **domain:** Ứng dụng sau đăng nhập; IAM và app owner; Đổi role, nghỉ việc hoặc lộ token; Quyết định được cache để giảm latency; Request đang chạy khi revoke commit; Cache/store có compare-and-set hoặc transaction
- **mechanism:** Commit chỉ khi authority epoch khớp precondition; failure: CAS đúng cú pháp nhưng so sai object/version
- **evidence:** Giữ cache-entry version nhưng tăng policy epoch
- **operational:** Kho phiên; đồng hồ; kênh invalidation; telemetry; Retry storm dưới churn quyền
- **consequence:** Quyền không tồn tại vượt điều kiện được cấp; Khi authority không reachable thì commit được phép không?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Stale commit được chấp nhận / stale-epoch fixtures
- **domain:** Ứng dụng sau đăng nhập; IAM và app owner; Đổi role, nghỉ việc hoặc lộ token; Quyết định được cache để giảm latency; Request đang chạy khi revoke commit; Cache/store có compare-and-set hoặc transaction
- **conditions:** Cache/store có compare-and-set hoặc transaction
- **goal:** Quyền không tồn tại vượt điều kiện được cấp
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Expected/current version và CAS outcome
- **method:** Giữ cache-entry version nhưng tăng policy epoch
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Retry storm dưới churn quyền; Khi authority không reachable thì commit được phép không?
- **binding:** revoke-cas → Commit chỉ khi authority epoch khớp precondition
