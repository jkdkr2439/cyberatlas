### inv-discovery — Phát hiện tài sản bị bỏ sót

**Điều kiện:** Có cloud, SaaS và tài sản ngắn hạn.

- **I:** CMDB, billing, DNS, endpoint và cloud API
- **P:** Đối soát nhiều nguồn theo định danh
- **O:** Tài sản có owner hoặc chưa rõ
- **D:** Lịch sử xuất hiện và nguồn phát hiện

**Hằng trong frame:** Inventory phải ghi độ bao phủ chưa biết.

**Đường hỏng:** Chỉ quét dải mạng đã biết nên bỏ shadow IT. **Điểm can thiệp:** Nhiều nguồn độc lập; giữ unknown riêng.

**Phép đo ứng viên:** Tài sản đối soát có owner / tài sản trong hợp nguồn quan sát.

**Test phân biệt / bằng chứng cần:** Cài một tài sản thử trong scope nhưng ngoài CMDB.

**Đánh đổi:** Quét sâu tăng chi phí và dữ liệu nhạy cảm.

**OPEN:** Tài sản không để dấu ở mọi nguồn đang dùng còn loại nào?

**Liên hệ có điều kiện:**

- `tel-coverage` — Nguồn cần quan sát phải xuất phát từ inventory; thiếu inventory làm coverage bị phóng đại.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Tài sản có owner hoặc chưa rõ / Chỉ quét dải mạng đã biết nên bỏ shadow IT
- **domain:** Chốt population và giới hạn: Hạ tầng và SaaS; chủ tài sản; Có cloud, SaaS và tài sản ngắn hạn
- **mechanism:** Control có giữ invariant này không? Inventory phải ghi độ bao phủ chưa biết
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Cài một tài sản thử trong scope nhưng ngoài CMDB
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Đầu nối inventory; quyền đọc; người xác nhận owner; Tài sản ngắn hạn; shadow IT; mua bán doanh nghiệp
- **consequence:** Đạt Biết đối tượng nào cần bảo vệ và nó phụ thuộc gì nhưng phải theo dõi Quét sâu tăng chi phí và dữ liệu nhạy cảm

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Tài sản đối soát có owner / tài sản trong hợp nguồn quan sát
- **domain:** Hạ tầng và SaaS; chủ tài sản; Có cloud, SaaS và tài sản ngắn hạn
- **conditions:** Có cloud, SaaS và tài sản ngắn hạn
- **goal:** Biết đối tượng nào cần bảo vệ và nó phụ thuộc gì
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Lịch sử xuất hiện và nguồn phát hiện; bằng chứng test: Cài một tài sản thử trong scope nhưng ngoài CMDB
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Quét sâu tăng chi phí và dữ liệu nhạy cảm; Tài sản không để dấu ở mọi nguồn đang dùng còn loại nào?
- **binding:** inv-discovery → điểm thực thi: Đối soát nhiều nguồn theo định danh
