### end-memory — An toàn bộ nhớ

**Điều kiện:** Native component xử lý dữ liệu.

- **I:** Buffer, length, lifetime và concurrency
- **P:** Thực thi theo ràng buộc biên và tuổi đối tượng
- **O:** Kết quả không vượt vùng nhớ
- **D:** Crash triage và sanitizer findings

**Hằng trong frame:** Input hợp schema vẫn có thể gây lỗi lifetime.

**Đường hỏng:** Use-after-free, out-of-bounds hoặc race. **Điểm can thiệp:** Memory-safe boundary, sanitizer, fuzz và hardening.

**Phép đo ứng viên:** Lỗi mới xác nhận trên corpus/version; không suy ra xác suất an toàn.

**Test phân biệt / bằng chứng cần:** Fuzz có coverage và giữ regression case độc lập.

**Đánh đổi:** Rewrite tốn nguồn lực; sanitizer khác production.

**OPEN:** Unsafe/FFI boundary và logic bug còn lại ở đâu?

**Liên hệ có điều kiện:**

- `sw-testing` — Fuzz/sanitizer cần corpus và regression riêng cho lỗi lifetime.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Kết quả không vượt vùng nhớ / Use-after-free, out-of-bounds hoặc race
- **domain:** Chốt population và giới hạn: Máy trạm, server; endpoint team; Native component xử lý dữ liệu
- **mechanism:** Control có giữ invariant này không? Input hợp schema vẫn có thể gây lỗi lifetime
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Fuzz có coverage và giữ regression case độc lập
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Quản trị thiết bị; cập nhật; bộ nhớ; hỗ trợ người dùng; BYOD; EDR health; kernel; ứng dụng cũ
- **consequence:** Đạt Mã và quyền thực thi phù hợp công việc nhưng phải theo dõi Rewrite tốn nguồn lực; sanitizer khác production

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Lỗi mới xác nhận trên corpus/version; không suy ra xác suất an toàn
- **domain:** Máy trạm, server; endpoint team; Native component xử lý dữ liệu
- **conditions:** Native component xử lý dữ liệu
- **goal:** Mã và quyền thực thi phù hợp công việc
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Crash triage và sanitizer findings; bằng chứng test: Fuzz có coverage và giữ regression case độc lập
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Rewrite tốn nguồn lực; sanitizer khác production; Unsafe/FFI boundary và logic bug còn lại ở đâu?
- **binding:** end-memory → điểm thực thi: Thực thi theo ràng buộc biên và tuổi đối tượng
