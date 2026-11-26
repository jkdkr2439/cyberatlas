### ot-remote — Bảo trì từ xa

**Điều kiện:** Vendor cần can thiệp thiết bị.

- **I:** Yêu cầu support và phiên truy cập
- **P:** Cấp quyền có hạn, giám sát và thu hồi
- **O:** Phiên chỉ tác động tài sản đã duyệt
- **D:** Session record và work order

**Hằng trong frame:** Quyền vendor không được thường trực vô thời hạn.

**Đường hỏng:** Shared account và tunnel bỏ quên. **Điểm can thiệp:** Just-in-time access, jump path và xác nhận tại chỗ khi cần.

**Phép đo ứng viên:** Phiên vượt thời hạn/tài sản / phiên review.

**Test phân biệt / bằng chứng cần:** Đóng work order rồi thử lại quyền trong lab.

**Đánh đổi:** Cấp quyền chậm có thể kéo dài downtime.

**OPEN:** Mất internet khi đang bảo trì cần xử lý ra sao?

**Liên hệ có điều kiện:**

- `tp-scope` — Remote support là authority của vendor cần scope và expiry.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Phiên chỉ tác động tài sản đã duyệt / Shared account và tunnel bỏ quên
- **domain:** Chốt population và giới hạn: Thiết bị và quy trình vật lý; kỹ sư vận hành; Vendor cần can thiệp thiết bị
- **mechanism:** Control có giữ invariant này không? Quyền vendor không được thường trực vô thời hạn
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đóng work order rồi thử lại quyền trong lab
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Kỹ sư safety; lab; spare parts; vận hành tại chỗ; Chu kỳ điều khiển; tuổi thiết bị; vendor; maintenance window
- **consequence:** Đạt An toàn con người và tiến trình trong điều kiện tấn công/lỗi nhưng phải theo dõi Cấp quyền chậm có thể kéo dài downtime

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Phiên vượt thời hạn/tài sản / phiên review
- **domain:** Thiết bị và quy trình vật lý; kỹ sư vận hành; Vendor cần can thiệp thiết bị
- **conditions:** Vendor cần can thiệp thiết bị
- **goal:** An toàn con người và tiến trình trong điều kiện tấn công/lỗi
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Session record và work order; bằng chứng test: Đóng work order rồi thử lại quyền trong lab
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Cấp quyền chậm có thể kéo dài downtime; Mất internet khi đang bảo trì cần xử lý ra sao?
- **binding:** ot-remote → điểm thực thi: Cấp quyền có hạn, giám sát và thu hồi
