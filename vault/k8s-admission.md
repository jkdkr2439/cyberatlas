### k8s-admission — Quyền tạo workload

**Điều kiện:** Principal được tạo Pod/deployment.

- **I:** Pod spec và RBAC permission
- **P:** Kiểm tra trường security-sensitive ở admission
- **O:** Workload được giới hạn trên node
- **D:** Admission decision và spec thực

**Hằng trong frame:** RBAC create không tự ràng mọi trường Pod.

**Đường hỏng:** Workload có quyền truy host hay identity ngoài intent. **Điểm can thiệp:** Admission enforce và policy theo namespace.

**Phép đo ứng viên:** Spec trái policy được nhận / spec trái policy thử.

**Test phân biệt / bằng chứng cần:** So warn/audit với enforce trong cluster lab.

**Đánh đổi:** Policy có thể chặn ứng dụng legacy.

**OPEN:** Webhook mất kết nối thì admission làm gì?

**Liên hệ có điều kiện:**

- `arch-blast` — Quyền tạo workload có thể mở đường tới node nếu thiếu admission phù hợp.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Workload được giới hạn trên node / Workload có quyền truy host hay identity ngoài intent
- **domain:** Chốt population và giới hạn: Cluster và workload; platform/SRE; Principal được tạo Pod/deployment
- **mechanism:** Control có giữ invariant này không? RBAC create không tự ràng mọi trường Pod
- **evidence:** Quan sát nào có thể bác bỏ kết luận? So warn/audit với enforce trong cluster lab
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Admission; runtime telemetry; đội vận hành; Admission mode; RBAC; CNI; token; runtime
- **consequence:** Đạt Quyền workload không mặc nhiên thành quyền node nhưng phải theo dõi Policy có thể chặn ứng dụng legacy

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Spec trái policy được nhận / spec trái policy thử
- **domain:** Cluster và workload; platform/SRE; Principal được tạo Pod/deployment
- **conditions:** Principal được tạo Pod/deployment
- **goal:** Quyền workload không mặc nhiên thành quyền node
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Admission decision và spec thực; bằng chứng test: So warn/audit với enforce trong cluster lab
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Policy có thể chặn ứng dụng legacy; Webhook mất kết nối thì admission làm gì?
- **binding:** k8s-admission → điểm thực thi: Kiểm tra trường security-sensitive ở admission
