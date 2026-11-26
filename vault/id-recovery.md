### id-recovery — Khôi phục tài khoản

**Điều kiện:** Người dùng mất authenticator.

- **I:** Yêu cầu recovery, bằng chứng phụ
- **P:** Xác minh lại, giới hạn thay đổi và thông báo
- **O:** Authenticator mới hoặc từ chối
- **D:** Chuỗi bằng chứng và hành động support

**Hằng trong frame:** Recovery không được bỏ yêu cầu đảm bảo đã cam kết.

**Đường hỏng:** Helpdesk bị thuyết phục thay MFA không đủ căn cứ. **Điểm can thiệp:** Recovery có phân quyền, cooldown theo rủi ro, audit.

**Phép đo ứng viên:** Recovery sai được chấp nhận / tình huống sai trong bộ test.

**Test phân biệt / bằng chứng cần:** Đưa bằng chứng đúng tên nhưng không đủ quyền sở hữu.

**Đánh đổi:** Siết quá chặt khóa người dùng hợp lệ.

**OPEN:** Người dùng không còn bất kỳ thiết bị nào được hỗ trợ ra sao?

**Liên hệ có điều kiện:**

- `F26` — Control loại người dùng nào khỏi dịch vụ, có phương án giữ assurance mà giảm loại trừ không?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Authenticator mới hoặc từ chối / Helpdesk bị thuyết phục thay MFA không đủ căn cứ
- **domain:** Chốt population và giới hạn: Con người và workload; IAM team; Người dùng mất authenticator
- **mechanism:** Control có giữ invariant này không? Recovery không được bỏ yêu cầu đảm bảo đã cam kết
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đưa bằng chứng đúng tên nhưng không đủ quyền sở hữu
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? IdP; quy trình hỗ trợ; thiết bị; khả năng thu hồi; Authenticator; mất thiết bị; federation; tài khoản máy
- **consequence:** Đạt Gắn yêu cầu với đúng chủ thể trong mức bảo đảm đã chọn nhưng phải theo dõi Siết quá chặt khóa người dùng hợp lệ

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Recovery sai được chấp nhận / tình huống sai trong bộ test
- **domain:** Con người và workload; IAM team; Người dùng mất authenticator
- **conditions:** Người dùng mất authenticator
- **goal:** Gắn yêu cầu với đúng chủ thể trong mức bảo đảm đã chọn
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Chuỗi bằng chứng và hành động support; bằng chứng test: Đưa bằng chứng đúng tên nhưng không đủ quyền sở hữu
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Siết quá chặt khóa người dùng hợp lệ; Người dùng không còn bất kỳ thiết bị nào được hỗ trợ ra sao?
- **binding:** id-recovery → điểm thực thi: Xác minh lại, giới hạn thay đổi và thông báo
