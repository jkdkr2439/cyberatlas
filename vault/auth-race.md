### auth-race — Quyền tại thời điểm commit

**Điều kiện:** Ownership thay đổi khi tác vụ đang chạy.

- **I:** Yêu cầu được duyệt trước và trạng thái mới
- **P:** Kiểm tra lại điều kiện cùng giao dịch thay đổi
- **O:** Commit hợp lệ hoặc rollback
- **D:** Version, lock hoặc precondition record

**Hằng trong frame:** Quyền tại đầu request không bảo đảm quyền lúc ghi.

**Đường hỏng:** TOCTOU giữa authorize và update. **Điểm can thiệp:** Atomic check-and-act hoặc version precondition.

**Phép đo ứng viên:** Commit trái quyền sau biến đổi trạng thái / test race.

**Test phân biệt / bằng chứng cần:** Đổi owner giữa check và commit trong môi trường test.

**Đánh đổi:** Khóa và retry ảnh hưởng throughput.

**OPEN:** Job dài và event queue giữ authority theo mốc nào?

**Liên hệ có điều kiện:**

- `ai-tool` — Trạng thái sau approval có thể khác trạng thái khi thực thi.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Commit hợp lệ hoặc rollback / TOCTOU giữa authorize và update
- **domain:** Chốt population và giới hạn: API và kho dữ liệu; chủ sản phẩm; Ownership thay đổi khi tác vụ đang chạy
- **mechanism:** Control có giữ invariant này không? Quyền tại đầu request không bảo đảm quyền lúc ghi
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đổi owner giữa check và commit trong môi trường test
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Policy engine; test matrix; owner dữ liệu; Role; thuộc tính; ownership; tenant; thời điểm commit
- **consequence:** Đạt Chủ thể chỉ tác động đúng đối tượng và hành động được phép nhưng phải theo dõi Khóa và retry ảnh hưởng throughput

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Commit trái quyền sau biến đổi trạng thái / test race
- **domain:** API và kho dữ liệu; chủ sản phẩm; Ownership thay đổi khi tác vụ đang chạy
- **conditions:** Ownership thay đổi khi tác vụ đang chạy
- **goal:** Chủ thể chỉ tác động đúng đối tượng và hành động được phép
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Version, lock hoặc precondition record; bằng chứng test: Đổi owner giữa check và commit trong môi trường test
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Khóa và retry ảnh hưởng throughput; Job dài và event queue giữ authority theo mốc nào?
- **binding:** auth-race → điểm thực thi: Kiểm tra lại điều kiện cùng giao dịch thay đổi
