### revoke-offline — Quyền sử dụng khi consumer offline

**Điều kiện:** Consumer không liên lạc được authority.

- **I:** Credential cũ, local clock và cached policy
- **P:** Thực thi grace/expiry theo contract đã duyệt
- **O:** Quyền dừng tại bound hoặc dịch vụ bị giới hạn
- **D:** Offline interval, clock bounds, last sync

**Hằng trong frame:** Không hứa thu hồi tức thời nếu không có kênh state.

**Đường hỏng:** Local clock lệch hoặc token không expiry. **Điểm can thiệp:** Bounded offline lease và chức năng dự phòng.

**Phép đo ứng viên:** Khoảng sử dụng quyền sau revoke theo clock uncertainty.

**Test phân biệt / bằng chứng cần:** Ngắt mạng, dịch đồng hồ lab trong giới hạn test.

**Đánh đổi:** Lease ngắn làm giảm khả dụng.

**OPEN:** Thiết bị offline bắt buộc dùng lâu có cơ chế trust khác không?


## Sáu miền review

- **meaning:** Không hứa thu hồi tức thời nếu không có kênh state
- **domain:** Ứng dụng sau đăng nhập; IAM và app owner; Đổi role, nghỉ việc hoặc lộ token; Consumer không liên lạc được authority
- **mechanism:** Thực thi grace/expiry theo contract đã duyệt; failure: Local clock lệch hoặc token không expiry
- **evidence:** Ngắt mạng, dịch đồng hồ lab trong giới hạn test
- **operational:** Kho phiên; đồng hồ; kênh invalidation; telemetry; Lease ngắn làm giảm khả dụng
- **consequence:** Quyền không tồn tại vượt điều kiện được cấp; Thiết bị offline bắt buộc dùng lâu có cơ chế trust khác không?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Khoảng sử dụng quyền sau revoke theo clock uncertainty
- **domain:** Ứng dụng sau đăng nhập; IAM và app owner; Đổi role, nghỉ việc hoặc lộ token; Consumer không liên lạc được authority
- **conditions:** Consumer không liên lạc được authority
- **goal:** Quyền không tồn tại vượt điều kiện được cấp
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Offline interval, clock bounds, last sync
- **method:** Ngắt mạng, dịch đồng hồ lab trong giới hạn test
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Lease ngắn làm giảm khả dụng; Thiết bị offline bắt buộc dùng lâu có cơ chế trust khác không?
- **binding:** revoke-offline → Thực thi grace/expiry theo contract đã duyệt
