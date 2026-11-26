### net-segment — Phân vùng thực sự

**Điều kiện:** Một workload bị compromise.

- **I:** Source identity, destination và port/protocol
- **P:** Thực thi policy tại đường đi thật
- **O:** Kết nối cần thiết qua; kết nối khác bị chặn
- **D:** Policy và thử nghiệm connectivity

**Hằng trong frame:** Có VLAN không chứng minh cắt đường authority.

**Đường hỏng:** Đường quản trị hoặc IPv6 đi vòng. **Điểm can thiệp:** Deny-by-default theo luồng hợp lệ đã quan sát.

**Phép đo ứng viên:** Đường cấm còn kết nối / đường cấm đã thử.

**Test phân biệt / bằng chứng cần:** Thử route dự phòng, IPv6 và management plane.

**Đánh đổi:** Chặn nhầm ảnh hưởng dịch vụ và debug.

**OPEN:** Lưu lượng phát sinh theo mùa có được đưa vào model?

**Liên hệ có điều kiện:**

- `ot-legacy` — Cắt đường tiếp cận hỗ trợ thiết bị khó vá; không sửa lỗi nội tại.
- `F04` — Trust boundary thay khi kênh truyền dùng chung môi trường vật lý ra sao?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Kết nối cần thiết qua; kết nối khác bị chặn / Đường quản trị hoặc IPv6 đi vòng
- **domain:** Chốt population và giới hạn: Lưu lượng giữa dịch vụ; network team; Một workload bị compromise
- **mechanism:** Control có giữ invariant này không? Có VLAN không chứng minh cắt đường authority
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Thử route dự phòng, IPv6 và management plane
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Thiết bị mạng; bản đồ luồng; năng lực lọc; DNS; route; IPv6; proxy; lưu lượng mã hóa
- **consequence:** Đạt Đường kết nối chỉ mở cho quan hệ có chủ đích nhưng phải theo dõi Chặn nhầm ảnh hưởng dịch vụ và debug

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Đường cấm còn kết nối / đường cấm đã thử
- **domain:** Lưu lượng giữa dịch vụ; network team; Một workload bị compromise
- **conditions:** Một workload bị compromise
- **goal:** Đường kết nối chỉ mở cho quan hệ có chủ đích
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Policy và thử nghiệm connectivity; bằng chứng test: Thử route dự phòng, IPv6 và management plane
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Chặn nhầm ảnh hưởng dịch vụ và debug; Lưu lượng phát sinh theo mùa có được đưa vào model?
- **binding:** net-segment → điểm thực thi: Thực thi policy tại đường đi thật
