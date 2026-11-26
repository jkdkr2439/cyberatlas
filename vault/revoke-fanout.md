### revoke-fanout — Tập consumer của một lần thu hồi

**Điều kiện:** Quyền dùng ở nhiều service/region.

- **I:** Revoke event và authority graph
- **P:** Resolve toàn bộ điểm dùng quyền và đánh dấu acknowledgment
- **O:** Consumer đã cập nhật hoặc chưa rõ
- **D:** Event version, consumer list, ack times

**Hằng trong frame:** Ack của authority không thay ack của consumer.

**Đường hỏng:** Một vùng không nhận sự kiện nhưng batch được báo done. **Điểm can thiệp:** Fanout registry và reconciliation pull.

**Phép đo ứng viên:** Consumer chưa xác nhận / consumer thuộc scope.

**Test phân biệt / bằng chứng cần:** Bỏ một consumer khỏi đường push nhưng giữ trong registry.

**Đánh đổi:** Registry consumer cần bảo trì.

**OPEN:** Consumer được tạo sau revoke nhận state từ đâu?


## Sáu miền review

- **meaning:** Ack của authority không thay ack của consumer
- **domain:** Ứng dụng sau đăng nhập; IAM và app owner; Đổi role, nghỉ việc hoặc lộ token; Quyền dùng ở nhiều service/region
- **mechanism:** Resolve toàn bộ điểm dùng quyền và đánh dấu acknowledgment; failure: Một vùng không nhận sự kiện nhưng batch được báo done
- **evidence:** Bỏ một consumer khỏi đường push nhưng giữ trong registry
- **operational:** Kho phiên; đồng hồ; kênh invalidation; telemetry; Registry consumer cần bảo trì
- **consequence:** Quyền không tồn tại vượt điều kiện được cấp; Consumer được tạo sau revoke nhận state từ đâu?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Consumer chưa xác nhận / consumer thuộc scope
- **domain:** Ứng dụng sau đăng nhập; IAM và app owner; Đổi role, nghỉ việc hoặc lộ token; Quyền dùng ở nhiều service/region
- **conditions:** Quyền dùng ở nhiều service/region
- **goal:** Quyền không tồn tại vượt điều kiện được cấp
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Event version, consumer list, ack times
- **method:** Bỏ một consumer khỏi đường push nhưng giữ trong registry
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Registry consumer cần bảo trì; Consumer được tạo sau revoke nhận state từ đâu?
- **binding:** revoke-fanout → Resolve toàn bộ điểm dùng quyền và đánh dấu acknowledgment
