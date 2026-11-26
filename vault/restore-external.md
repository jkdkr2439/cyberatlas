### restore-external — Side effect đã ra ngoài hệ

**Điều kiện:** Email, tiền hoặc lệnh vật lý đã gửi trước sự cố.

- **I:** Local recovered state và external receipts
- **P:** Xác nhận trạng thái ngoài rồi chọn compensation/replay
- **O:** Không lặp hoặc bỏ nghĩa vụ ngoài ý định
- **D:** External references và reconciliation evidence

**Hằng trong frame:** Rollback DB không rollback thực tại bên ngoài.

**Đường hỏng:** Replay sự kiện đã thanh toán vì local state mất. **Điểm can thiệp:** External idempotency keys và compensation có thẩm quyền.

**Phép đo ứng viên:** Duplicate/missing external effect / cases đối soát.

**Test phân biệt / bằng chứng cần:** Restore trước mốc gửi nhưng provider đã nhận; phải reconcile.

**Đánh đổi:** Compensation có thể có phí hoặc không đảo được.

**OPEN:** Hệ ngoài mất liên lạc thì trạng thái tạm được biểu diễn thế nào?


## Sáu miền review

- **meaning:** Rollback DB không rollback thực tại bên ngoài
- **domain:** Dịch vụ đầu cuối; business continuity; Nhiều store/queue khôi phục khác mốc; Email, tiền hoặc lệnh vật lý đã gửi trước sự cố
- **mechanism:** Xác nhận trạng thái ngoài rồi chọn compensation/replay; failure: Replay sự kiện đã thanh toán vì local state mất
- **evidence:** Restore trước mốc gửi nhưng provider đã nhận; phải reconcile
- **operational:** Backup; clean room; key custody; người kiểm tra; Compensation có thể có phí hoặc không đảo được
- **consequence:** Phục hồi trạng thái kinh doanh chấp nhận được; Hệ ngoài mất liên lạc thì trạng thái tạm được biểu diễn thế nào?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Duplicate/missing external effect / cases đối soát
- **domain:** Dịch vụ đầu cuối; business continuity; Nhiều store/queue khôi phục khác mốc; Email, tiền hoặc lệnh vật lý đã gửi trước sự cố
- **conditions:** Email, tiền hoặc lệnh vật lý đã gửi trước sự cố
- **goal:** Phục hồi trạng thái kinh doanh chấp nhận được
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** External references và reconciliation evidence
- **method:** Restore trước mốc gửi nhưng provider đã nhận; phải reconcile
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Compensation có thể có phí hoặc không đảo được; Hệ ngoài mất liên lạc thì trạng thái tạm được biểu diễn thế nào?
- **binding:** restore-external → Xác nhận trạng thái ngoài rồi chọn compensation/replay
