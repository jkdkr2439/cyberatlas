### ses-revoke — Thu hồi quyền có độ trễ

**Điều kiện:** Đổi role, nghỉ việc hoặc lộ token.

- **I:** Sự kiện revoke và các token/cache đang tồn tại
- **P:** Lan truyền thu hồi hoặc chờ expiry theo thiết kế
- **O:** Hành động cũ bị từ chối ở các điểm enforcement
- **D:** Thời điểm revoke và lần cho phép cuối

**Hằng trong frame:** Thu hồi tại IdP chưa chứng minh thu hồi toàn hệ.

**Đường hỏng:** Access token tự chứa và cache quyền vẫn dùng được. **Điểm can thiệp:** TTL, introspection, revocation và test đa vùng.

**Phép đo ứng viên:** Phân bố độ trễ từ revoke đến deny; ca chưa deny là censored.

**Test phân biệt / bằng chứng cần:** Thử cả access, refresh và đường offline sau revoke.

**Đánh đổi:** Thu hồi tức thời cần phụ thuộc online và tải thêm.

**OPEN:** Bound tối đa nào được bảo đảm khi mất mạng?

**Liên hệ có điều kiện:**

- `hum-offboard` — Offboarding chỉ xong khi quyền hiệu lực không còn ở các điểm dùng.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Hành động cũ bị từ chối ở các điểm enforcement / Access token tự chứa và cache quyền vẫn dùng được
- **domain:** Chốt population và giới hạn: Ứng dụng sau đăng nhập; IAM và app owner; Đổi role, nghỉ việc hoặc lộ token
- **mechanism:** Control có giữ invariant này không? Thu hồi tại IdP chưa chứng minh thu hồi toàn hệ
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Thử cả access, refresh và đường offline sau revoke
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Kho phiên; đồng hồ; kênh invalidation; telemetry; TTL; cache; offline; refresh token; nhiều vùng
- **consequence:** Đạt Quyền không tồn tại vượt điều kiện được cấp nhưng phải theo dõi Thu hồi tức thời cần phụ thuộc online và tải thêm

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Phân bố độ trễ từ revoke đến deny; ca chưa deny là censored
- **domain:** Ứng dụng sau đăng nhập; IAM và app owner; Đổi role, nghỉ việc hoặc lộ token
- **conditions:** Đổi role, nghỉ việc hoặc lộ token
- **goal:** Quyền không tồn tại vượt điều kiện được cấp
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Thời điểm revoke và lần cho phép cuối; bằng chứng test: Thử cả access, refresh và đường offline sau revoke
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Thu hồi tức thời cần phụ thuộc online và tải thêm; Bound tối đa nào được bảo đảm khi mất mạng?
- **binding:** ses-revoke → điểm thực thi: Lan truyền thu hồi hoặc chờ expiry theo thiết kế
