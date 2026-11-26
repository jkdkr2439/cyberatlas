### restore-cut — Mốc cắt nhất quán giữa nhiều store

**Điều kiện:** Backup được chụp ở các thời điểm khác nhau.

- **I:** Snapshots và event/transaction positions
- **P:** Chọn cut hoặc dựng lại quan hệ nhân quả nghiệp vụ
- **O:** State liên hệ không thiếu/nhân đôi giao dịch
- **D:** Checkpoint IDs và recovery lineage

**Hằng trong frame:** Timestamp gần nhau không bảo đảm cùng transaction cut.

**Đường hỏng:** Order được backup nhưng payment event chưa có. **Điểm can thiệp:** Consistent checkpoint hoặc replay/reconcile contract.

**Phép đo ứng viên:** Invariant sai sau cut / records đối soát.

**Test phân biệt / bằng chứng cần:** Tạo transaction đúng lúc hai snapshot lệch nhau.

**Đánh đổi:** Đồng bộ snapshot có thể gây pause hoặc tải.

**OPEN:** Hệ ngoài tổ chức không tham gia snapshot thì sao?


## Sáu miền review

- **meaning:** Timestamp gần nhau không bảo đảm cùng transaction cut
- **domain:** Dịch vụ đầu cuối; business continuity; Nhiều store/queue khôi phục khác mốc; Backup được chụp ở các thời điểm khác nhau
- **mechanism:** Chọn cut hoặc dựng lại quan hệ nhân quả nghiệp vụ; failure: Order được backup nhưng payment event chưa có
- **evidence:** Tạo transaction đúng lúc hai snapshot lệch nhau
- **operational:** Backup; clean room; key custody; người kiểm tra; Đồng bộ snapshot có thể gây pause hoặc tải
- **consequence:** Phục hồi trạng thái kinh doanh chấp nhận được; Hệ ngoài tổ chức không tham gia snapshot thì sao?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Invariant sai sau cut / records đối soát
- **domain:** Dịch vụ đầu cuối; business continuity; Nhiều store/queue khôi phục khác mốc; Backup được chụp ở các thời điểm khác nhau
- **conditions:** Backup được chụp ở các thời điểm khác nhau
- **goal:** Phục hồi trạng thái kinh doanh chấp nhận được
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Checkpoint IDs và recovery lineage
- **method:** Tạo transaction đúng lúc hai snapshot lệch nhau
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Đồng bộ snapshot có thể gây pause hoặc tải; Hệ ngoài tổ chức không tham gia snapshot thì sao?
- **binding:** restore-cut → Chọn cut hoặc dựng lại quan hệ nhân quả nghiệp vụ
