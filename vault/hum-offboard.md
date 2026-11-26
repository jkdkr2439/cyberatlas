### hum-offboard — Rời tổ chức và đổi vai

**Điều kiện:** Nhân sự hoặc contractor đổi nhiệm vụ.

- **I:** HR event và inventory quyền
- **P:** Thu hồi đồng bộ identity, physical và delegated access
- **O:** Quyền cũ kết thúc đúng hạn
- **D:** Acknowledgments và residual permissions

**Hằng trong frame:** Disable một tài khoản không xóa mọi authority.

**Đường hỏng:** API key, shared account, OAuth grant còn sống. **Điểm can thiệp:** Joiner-mover-leaver với đối soát hệ phụ.

**Phép đo ứng viên:** Authority dư sau deadline / authority đã kiểm kê.

**Test phân biệt / bằng chứng cần:** Cho người thử đổi vai, kiểm cả grant gián tiếp.

**Đánh đổi:** Thu hồi nhầm làm ngừng công việc hợp lệ.

**OPEN:** Tài sản ngoài inventory có giữ dữ liệu/quyền không?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Quyền cũ kết thúc đúng hạn / API key, shared account, OAuth grant còn sống
- **domain:** Chốt population và giới hạn: Nhân viên, khách, thiết bị; HR/IT/facilities; Nhân sự hoặc contractor đổi nhiệm vụ
- **mechanism:** Control có giữ invariant này không? Disable một tài khoản không xóa mọi authority
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Cho người thử đổi vai, kiểm cả grant gián tiếp
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Đào tạo theo vai; hỗ trợ; kiểm soát ra vào; Mệt mỏi; động cơ; accessibility; contractor; offboarding
- **consequence:** Đạt Quy trình có thể dùng an toàn trong áp lực thực tế nhưng phải theo dõi Thu hồi nhầm làm ngừng công việc hợp lệ

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Authority dư sau deadline / authority đã kiểm kê
- **domain:** Nhân viên, khách, thiết bị; HR/IT/facilities; Nhân sự hoặc contractor đổi nhiệm vụ
- **conditions:** Nhân sự hoặc contractor đổi nhiệm vụ
- **goal:** Quy trình có thể dùng an toàn trong áp lực thực tế
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Acknowledgments và residual permissions; bằng chứng test: Cho người thử đổi vai, kiểm cả grant gián tiếp
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Thu hồi nhầm làm ngừng công việc hợp lệ; Tài sản ngoài inventory có giữ dữ liệu/quyền không?
- **binding:** hum-offboard → điểm thực thi: Thu hồi đồng bộ identity, physical và delegated access
