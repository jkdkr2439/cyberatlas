### k8s-identity — Danh tính workload

**Điều kiện:** Pod cần gọi API hay cloud.

- **I:** Service account token và audience
- **P:** Cấp quyền tối thiểu, giới hạn scope và lifetime
- **O:** Workload chỉ dùng quyền cần thiết
- **D:** Token mount, access logs và role binding

**Hằng trong frame:** Mọi Pod không cần cùng quyền API.

**Đường hỏng:** Token tự mount và role quá rộng. **Điểm can thiệp:** Tắt mount không cần; quyền theo workload.

**Phép đo ứng viên:** Workload giữ token không cần / workload review.

**Test phân biệt / bằng chứng cần:** Chạy app không dùng API với token mount bị tắt.

**Đánh đổi:** Tách identity tăng cấu hình và vận hành.

**OPEN:** Federation cloud có kiểm tra đúng subject/audience?

**Liên hệ có điều kiện:**

- `cry-key` — Credential workload có lifecycle và custody riêng.
- `F14` — Trust bundle và identity federation làm tăng hay giảm blast radius khi một control plane bị chiếm?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Workload chỉ dùng quyền cần thiết / Token tự mount và role quá rộng
- **domain:** Chốt population và giới hạn: Cluster và workload; platform/SRE; Pod cần gọi API hay cloud
- **mechanism:** Control có giữ invariant này không? Mọi Pod không cần cùng quyền API
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Chạy app không dùng API với token mount bị tắt
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Admission; runtime telemetry; đội vận hành; Admission mode; RBAC; CNI; token; runtime
- **consequence:** Đạt Quyền workload không mặc nhiên thành quyền node nhưng phải theo dõi Tách identity tăng cấu hình và vận hành

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Workload giữ token không cần / workload review
- **domain:** Cluster và workload; platform/SRE; Pod cần gọi API hay cloud
- **conditions:** Pod cần gọi API hay cloud
- **goal:** Quyền workload không mặc nhiên thành quyền node
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Token mount, access logs và role binding; bằng chứng test: Chạy app không dùng API với token mount bị tắt
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Tách identity tăng cấu hình và vận hành; Federation cloud có kiểm tra đúng subject/audience?
- **binding:** k8s-identity → điểm thực thi: Cấp quyền tối thiểu, giới hạn scope và lifetime
