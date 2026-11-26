### k8s-network — NetworkPolicy thực thi

**Điều kiện:** Nhiều workload dùng chung cluster.

- **I:** Pod labels, policy và traffic
- **P:** CNI thực thi luật ingress/egress
- **O:** Luồng bị giới hạn như intent
- **D:** Policy, CNI version và probe results

**Hằng trong frame:** Có manifest không chứng minh plugin thực thi.

**Đường hỏng:** Policy không supported hoặc selector không khớp. **Điểm can thiệp:** Test connectivity và kiểm selector/namespace.

**Phép đo ứng viên:** Đường cấm vẫn qua / probe đường cấm.

**Test phân biệt / bằng chứng cần:** Đổi label và thử lại cùng đường kết nối.

**Đánh đổi:** Policy DNS/egress dễ làm lỗi discovery.

**OPEN:** Host networking và traffic tới node có được bao phủ?

**Liên hệ có điều kiện:**

- `net-segment` — Policy cluster là một lớp phân vùng có giới hạn plugin và traffic.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Luồng bị giới hạn như intent / Policy không supported hoặc selector không khớp
- **domain:** Chốt population và giới hạn: Cluster và workload; platform/SRE; Nhiều workload dùng chung cluster
- **mechanism:** Control có giữ invariant này không? Có manifest không chứng minh plugin thực thi
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đổi label và thử lại cùng đường kết nối
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Admission; runtime telemetry; đội vận hành; Admission mode; RBAC; CNI; token; runtime
- **consequence:** Đạt Quyền workload không mặc nhiên thành quyền node nhưng phải theo dõi Policy DNS/egress dễ làm lỗi discovery

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Đường cấm vẫn qua / probe đường cấm
- **domain:** Cluster và workload; platform/SRE; Nhiều workload dùng chung cluster
- **conditions:** Nhiều workload dùng chung cluster
- **goal:** Quyền workload không mặc nhiên thành quyền node
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Policy, CNI version và probe results; bằng chứng test: Đổi label và thử lại cùng đường kết nối
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Policy DNS/egress dễ làm lỗi discovery; Host networking và traffic tới node có được bao phủ?
- **binding:** k8s-network → điểm thực thi: CNI thực thi luật ingress/egress
