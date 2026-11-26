### ot-safety — An toàn khi hệ bị lỗi

**Điều kiện:** Lệnh số tác động thiết bị vật lý.

- **I:** Sensor, setpoint và control command
- **P:** Đối chiếu giới hạn an toàn và trạng thái tiến trình
- **O:** Hành động trong envelope an toàn
- **D:** Process history và safety evidence

**Hằng trong frame:** Security shutdown chưa chắc là trạng thái an toàn.

**Đường hỏng:** Chặn mạng làm mất điều khiển cần thiết. **Điểm can thiệp:** Safety analysis với kỹ sư; lớp bảo vệ phù hợp.

**Phép đo ứng viên:** Deviation ngoài envelope trong mô phỏng được phê duyệt.

**Test phân biệt / bằng chứng cần:** Diễn tập trên mô hình/lab theo kỹ sư safety.

**Đánh đổi:** Availability, integrity và safety có thể xung đột.

**OPEN:** Envelope thay theo tải, môi trường và chế độ vận hành?

**Liên hệ có điều kiện:**

- `arch-failure` — Fail-closed mạng chưa chắc an toàn cho quy trình vật lý.
- `F28` — Safety case, vòng đời hỗ trợ và authority update thay đổi tiêu chí triển khai ra sao?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Hành động trong envelope an toàn / Chặn mạng làm mất điều khiển cần thiết
- **domain:** Chốt population và giới hạn: Thiết bị và quy trình vật lý; kỹ sư vận hành; Lệnh số tác động thiết bị vật lý
- **mechanism:** Control có giữ invariant này không? Security shutdown chưa chắc là trạng thái an toàn
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Diễn tập trên mô hình/lab theo kỹ sư safety
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Kỹ sư safety; lab; spare parts; vận hành tại chỗ; Chu kỳ điều khiển; tuổi thiết bị; vendor; maintenance window
- **consequence:** Đạt An toàn con người và tiến trình trong điều kiện tấn công/lỗi nhưng phải theo dõi Availability, integrity và safety có thể xung đột

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Deviation ngoài envelope trong mô phỏng được phê duyệt
- **domain:** Thiết bị và quy trình vật lý; kỹ sư vận hành; Lệnh số tác động thiết bị vật lý
- **conditions:** Lệnh số tác động thiết bị vật lý
- **goal:** An toàn con người và tiến trình trong điều kiện tấn công/lỗi
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Process history và safety evidence; bằng chứng test: Diễn tập trên mô hình/lab theo kỹ sư safety
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Availability, integrity và safety có thể xung đột; Envelope thay theo tải, môi trường và chế độ vận hành?
- **binding:** ot-safety → điểm thực thi: Đối chiếu giới hạn an toàn và trạng thái tiến trình
