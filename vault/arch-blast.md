### arch-blast — Phạm vi lan truyền

**Điều kiện:** Một principal hoặc workload bị chiếm.

- **I:** Đồ thị quyền và đường kết nối
- **P:** Tìm tài sản nhạy cảm còn reachable theo điều kiện
- **O:** Tập tài sản có thể bị ảnh hưởng
- **D:** Snapshot quyền và đường đi

**Hằng trong frame:** Một control chỉ giới hạn những đường nó thực sự cắt.

**Đường hỏng:** Phân mạng nhưng cùng admin và backup credential. **Điểm can thiệp:** Tách authority, segment, giảm quyền liên miền.

**Phép đo ứng viên:** Số tài sản quan trọng reachable từ principal thử; báo cả giả định.

**Test phân biệt / bằng chứng cần:** Bỏ một cạnh quyền, tính lại phạm vi lan truyền.

**Đánh đổi:** Cô lập mạnh tăng gánh vận hành và recovery.

**OPEN:** Đường gián tiếp qua CI hoặc support có được mô hình hóa?

**Liên hệ có điều kiện:**

- `cld-policy` — Phạm vi lan truyền chịu quyền sửa/cấp quyền của control plane.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Tập tài sản có thể bị ảnh hưởng / Phân mạng nhưng cùng admin và backup credential
- **domain:** Chốt population và giới hạn: Dịch vụ phân tán; kiến trúc sư; Một principal hoặc workload bị chiếm
- **mechanism:** Control có giữ invariant này không? Một control chỉ giới hạn những đường nó thực sự cắt
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Bỏ một cạnh quyền, tính lại phạm vi lan truyền
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Sơ đồ thực tế; test môi trường; năng lực vận hành; Tenant; đường mạng; failover; vị trí enforcement
- **consequence:** Đạt Sai lệch không được tự do lan sang miền khác nhưng phải theo dõi Cô lập mạnh tăng gánh vận hành và recovery

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Số tài sản quan trọng reachable từ principal thử; báo cả giả định
- **domain:** Dịch vụ phân tán; kiến trúc sư; Một principal hoặc workload bị chiếm
- **conditions:** Một principal hoặc workload bị chiếm
- **goal:** Sai lệch không được tự do lan sang miền khác
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Snapshot quyền và đường đi; bằng chứng test: Bỏ một cạnh quyền, tính lại phạm vi lan truyền
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Cô lập mạnh tăng gánh vận hành và recovery; Đường gián tiếp qua CI hoặc support có được mô hình hóa?
- **binding:** arch-blast → điểm thực thi: Tìm tài sản nhạy cảm còn reachable theo điều kiện
