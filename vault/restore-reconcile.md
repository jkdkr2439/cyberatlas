### restore-reconcile — Đối soát semantic sau restore

**Điều kiện:** Dữ liệu kỹ thuật đã load thành công.

- **I:** Ledgers, domain invariants và exception rules
- **P:** So nghĩa vụ nghiệp vụ rồi phân loại lệch/không rõ
- **O:** State hợp lệ hoặc backlog cần xử lý
- **D:** Diffs, decisions và owner

**Hằng trong frame:** Record count/hash bằng nhau chưa chứng minh business meaning đúng.

**Đường hỏng:** Thiếu transaction hoặc sai foreign relation vẫn vượt health check. **Điểm can thiệp:** Business reconciliation và owner sign-off.

**Phép đo ứng viên:** Unresolved mismatches / records trong scope đối soát.

**Test phân biệt / bằng chứng cần:** Giữ tổng số record nhưng đổi quan hệ payment-order.

**Đánh đổi:** Đối soát lớn tăng RTO và công sức.

**OPEN:** Có invariant nào không thể tự động quyết định đúng/sai?


## Sáu miền review

- **meaning:** Record count/hash bằng nhau chưa chứng minh business meaning đúng
- **domain:** Dịch vụ đầu cuối; business continuity; Nhiều store/queue khôi phục khác mốc; Dữ liệu kỹ thuật đã load thành công
- **mechanism:** So nghĩa vụ nghiệp vụ rồi phân loại lệch/không rõ; failure: Thiếu transaction hoặc sai foreign relation vẫn vượt health check
- **evidence:** Giữ tổng số record nhưng đổi quan hệ payment-order
- **operational:** Backup; clean room; key custody; người kiểm tra; Đối soát lớn tăng RTO và công sức
- **consequence:** Phục hồi trạng thái kinh doanh chấp nhận được; Có invariant nào không thể tự động quyết định đúng/sai?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Unresolved mismatches / records trong scope đối soát
- **domain:** Dịch vụ đầu cuối; business continuity; Nhiều store/queue khôi phục khác mốc; Dữ liệu kỹ thuật đã load thành công
- **conditions:** Dữ liệu kỹ thuật đã load thành công
- **goal:** Phục hồi trạng thái kinh doanh chấp nhận được
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Diffs, decisions và owner
- **method:** Giữ tổng số record nhưng đổi quan hệ payment-order
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Đối soát lớn tăng RTO và công sức; Có invariant nào không thể tự động quyết định đúng/sai?
- **binding:** restore-reconcile → So nghĩa vụ nghiệp vụ rồi phân loại lệch/không rõ
