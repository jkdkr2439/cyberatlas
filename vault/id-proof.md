### id-proof — Gắn tài khoản với chủ thể

**Điều kiện:** Tạo hoặc liên kết tài khoản.

- **I:** Bằng chứng định danh và yêu cầu đăng ký
- **P:** Kiểm tra mức đảm bảo tương ứng mục tiêu
- **O:** Binding tài khoản-chủ thể
- **D:** Nguồn bằng chứng và vòng đời binding

**Hằng trong frame:** Đăng ký và đăng nhập là hai phép kiểm khác nhau.

**Đường hỏng:** Authenticator tốt gắn vào sai người. **Điểm can thiệp:** Proofing theo rủi ro; chống trùng và review ngoại lệ.

**Phép đo ứng viên:** Binding sai trong mẫu đã xác minh / mẫu có ground truth.

**Test phân biệt / bằng chứng cần:** Đưa trường hợp đồng tên hoặc đổi chủ tài khoản.

**Đánh đổi:** Thu thập thêm định danh gây chi phí riêng tư.

**OPEN:** Mức đảm bảo nào thật sự cần, có thể dùng pseudonym không?

**Liên hệ có điều kiện:**

- `id-recovery` — Recovery tạo binding mới nên không được quên mức đảm bảo cần thiết.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Binding tài khoản-chủ thể / Authenticator tốt gắn vào sai người
- **domain:** Chốt population và giới hạn: Con người và workload; IAM team; Tạo hoặc liên kết tài khoản
- **mechanism:** Control có giữ invariant này không? Đăng ký và đăng nhập là hai phép kiểm khác nhau
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đưa trường hợp đồng tên hoặc đổi chủ tài khoản
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? IdP; quy trình hỗ trợ; thiết bị; khả năng thu hồi; Authenticator; mất thiết bị; federation; tài khoản máy
- **consequence:** Đạt Gắn yêu cầu với đúng chủ thể trong mức bảo đảm đã chọn nhưng phải theo dõi Thu thập thêm định danh gây chi phí riêng tư

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Binding sai trong mẫu đã xác minh / mẫu có ground truth
- **domain:** Con người và workload; IAM team; Tạo hoặc liên kết tài khoản
- **conditions:** Tạo hoặc liên kết tài khoản
- **goal:** Gắn yêu cầu với đúng chủ thể trong mức bảo đảm đã chọn
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Nguồn bằng chứng và vòng đời binding; bằng chứng test: Đưa trường hợp đồng tên hoặc đổi chủ tài khoản
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Thu thập thêm định danh gây chi phí riêng tư; Mức đảm bảo nào thật sự cần, có thể dùng pseudonym không?
- **binding:** id-proof → điểm thực thi: Kiểm tra mức đảm bảo tương ứng mục tiêu
