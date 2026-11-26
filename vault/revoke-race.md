### revoke-race — Race giữa đọc quyền và ghi cache

**Điều kiện:** Request đang chạy khi revoke commit.

- **I:** Read cũ, revoke mới, cache write muộn
- **P:** Ràng write-back với version còn hiệu lực
- **O:** Cache không giữ allow đã lỗi thời
- **D:** Timeline read/check/write và version

**Hằng trong frame:** Kiểm freshness trước process chưa đủ cho write-back.

**Đường hỏng:** Request đọc allow cũ rồi ghi đè deny mới. **Điểm can thiệp:** Commit-time version guard.

**Phép đo ứng viên:** Write-back cũ được nhận / lịch race thử.

**Test phân biệt / bằng chứng cần:** Dùng barrier ép thứ tự read-old → revoke → write-old.

**Đánh đổi:** Đồng bộ hóa tăng latency và contention.

**OPEN:** Library cache có hỗ trợ conditional write không?


## Sáu miền review

- **meaning:** Kiểm freshness trước process chưa đủ cho write-back
- **domain:** Ứng dụng sau đăng nhập; IAM và app owner; Đổi role, nghỉ việc hoặc lộ token; Quyết định được cache để giảm latency; Request đang chạy khi revoke commit
- **mechanism:** Ràng write-back với version còn hiệu lực; failure: Request đọc allow cũ rồi ghi đè deny mới
- **evidence:** Dùng barrier ép thứ tự read-old → revoke → write-old
- **operational:** Kho phiên; đồng hồ; kênh invalidation; telemetry; Đồng bộ hóa tăng latency và contention
- **consequence:** Quyền không tồn tại vượt điều kiện được cấp; Library cache có hỗ trợ conditional write không?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Write-back cũ được nhận / lịch race thử
- **domain:** Ứng dụng sau đăng nhập; IAM và app owner; Đổi role, nghỉ việc hoặc lộ token; Quyết định được cache để giảm latency; Request đang chạy khi revoke commit
- **conditions:** Request đang chạy khi revoke commit
- **goal:** Quyền không tồn tại vượt điều kiện được cấp
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Timeline read/check/write và version
- **method:** Dùng barrier ép thứ tự read-old → revoke → write-old
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Đồng bộ hóa tăng latency và contention; Library cache có hỗ trợ conditional write không?
- **binding:** revoke-race → Ràng write-back với version còn hiệu lực
