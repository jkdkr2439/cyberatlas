### ai-memory — Memory, retrieval và feedback

**Điều kiện:** Agent lưu thông tin qua nhiều lượt.

- **I:** Documents, previous outputs và reviewer feedback
- **P:** Ghi provenance, version và mức kiểm chứng
- **O:** Memory không nâng suy đoán thành sự thật
- **D:** Memory lineage và sửa/xóa

**Hằng trong frame:** Lặp lại một claim không phải nguồn độc lập mới.

**Đường hỏng:** Hallucination được lưu rồi tự viện dẫn. **Điểm can thiệp:** Typed memory, source-linked retrieval và correction path.

**Phép đo ứng viên:** Claim quyết định không truy nguồn / claim được audit.

**Test phân biệt / bằng chứng cần:** Gieo một memory sai có nhãn uncertain; kiểm có bị nâng cấp.

**Đánh đổi:** Giữ nhiều provenance tốn token/storage và riêng tư.

**OPEN:** Quy tắc quên, hết hạn và sửa ký ức xung đột ra sao?

**Liên hệ có điều kiện:**

- `tel-integrity` — Nguồn được lặp lại không trở thành xác minh độc lập.
- `F29` — Phân biệt training poisoning, retrieval poisoning và memory poisoning bằng cơ chế/observable nào?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Memory không nâng suy đoán thành sự thật / Hallucination được lưu rồi tự viện dẫn
- **domain:** Chốt population và giới hạn: Ứng dụng LLM và automation; AI/platform owner; Agent lưu thông tin qua nhiều lượt
- **mechanism:** Control có giữ invariant này không? Lặp lại một claim không phải nguồn độc lập mới
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Gieo một memory sai có nhãn uncertain; kiểm có bị nâng cấp
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Policy ngoài model; sandbox; review; provenance; Prompt; retrieval; memory; tool; chi phí; model change
- **consequence:** Đạt Nội dung không đáng tin không được nâng thành authority nhưng phải theo dõi Giữ nhiều provenance tốn token/storage và riêng tư

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Claim quyết định không truy nguồn / claim được audit
- **domain:** Ứng dụng LLM và automation; AI/platform owner; Agent lưu thông tin qua nhiều lượt
- **conditions:** Agent lưu thông tin qua nhiều lượt
- **goal:** Nội dung không đáng tin không được nâng thành authority
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Memory lineage và sửa/xóa; bằng chứng test: Gieo một memory sai có nhãn uncertain; kiểm có bị nâng cấp
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Giữ nhiều provenance tốn token/storage và riêng tư; Quy tắc quên, hết hạn và sửa ký ức xung đột ra sao?
- **binding:** ai-memory → điểm thực thi: Ghi provenance, version và mức kiểm chứng
