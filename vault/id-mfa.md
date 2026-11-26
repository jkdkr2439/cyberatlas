### id-mfa — MFA và chống phishing

**Điều kiện:** Luồng đăng nhập có nhiều cách xác thực.

- **I:** Challenge và phản hồi authenticator
- **P:** Kiểm chứng yếu tố và binding với đúng verifier
- **O:** Kết quả xác thực theo phương thức
- **D:** Auth method, origin và kết quả

**Hằng trong frame:** Không đánh đồng mọi MFA với chống phishing.

**Đường hỏng:** OTP bị relay; fallback yếu hơn chính luồng. **Điểm can thiệp:** Chọn protocol phù hợp và rà mọi đường fallback.

**Phép đo ứng viên:** Luồng nhạy cảm dùng phương thức đạt yêu cầu / luồng nhạy cảm quan sát.

**Test phân biệt / bằng chứng cần:** So sánh luồng chính và luồng fallback trong test được phép.

**Đánh đổi:** Thiết bị và hỗ trợ recovery ảnh hưởng khả dụng.

**OPEN:** Passkey sync và custody phù hợp đối tượng nào?

**Liên hệ có điều kiện:**

- `id-recovery` — Fallback yếu có thể làm luồng xác thực mạnh mất hiệu quả toàn hành trình.
- `ses-revoke` — Chống phishing lúc login không giải quyết mọi phiên bị lộ sau đó.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Kết quả xác thực theo phương thức / OTP bị relay; fallback yếu hơn chính luồng
- **domain:** Chốt population và giới hạn: Con người và workload; IAM team; Luồng đăng nhập có nhiều cách xác thực
- **mechanism:** Control có giữ invariant này không? Không đánh đồng mọi MFA với chống phishing
- **evidence:** Quan sát nào có thể bác bỏ kết luận? So sánh luồng chính và luồng fallback trong test được phép
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? IdP; quy trình hỗ trợ; thiết bị; khả năng thu hồi; Authenticator; mất thiết bị; federation; tài khoản máy
- **consequence:** Đạt Gắn yêu cầu với đúng chủ thể trong mức bảo đảm đã chọn nhưng phải theo dõi Thiết bị và hỗ trợ recovery ảnh hưởng khả dụng

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Luồng nhạy cảm dùng phương thức đạt yêu cầu / luồng nhạy cảm quan sát
- **domain:** Con người và workload; IAM team; Luồng đăng nhập có nhiều cách xác thực
- **conditions:** Luồng đăng nhập có nhiều cách xác thực
- **goal:** Gắn yêu cầu với đúng chủ thể trong mức bảo đảm đã chọn
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Auth method, origin và kết quả; bằng chứng test: So sánh luồng chính và luồng fallback trong test được phép
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Thiết bị và hỗ trợ recovery ảnh hưởng khả dụng; Passkey sync và custody phù hợp đối tượng nào?
- **binding:** id-mfa → điểm thực thi: Kiểm chứng yếu tố và binding với đúng verifier
