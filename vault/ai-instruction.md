### ai-instruction — Prompt injection và authority

**Điều kiện:** Agent đọc nội dung bên ngoài.

- **I:** Trang web, tài liệu, email hoặc tool output
- **P:** Giữ nguồn như dữ liệu; policy thực thi ngoài model
- **O:** Không thực hiện hành động vượt nhiệm vụ
- **D:** Provenance, decision và tool request

**Hằng trong frame:** Văn bản thuyết phục không tạo quyền mới.

**Đường hỏng:** Nội dung được model coi là lệnh ưu tiên. **Điểm can thiệp:** Capability limits, sink authorization, dữ liệu tách instruction.

**Phép đo ứng viên:** Hành động vượt policy / ca untrusted-content test.

**Test phân biệt / bằng chứng cần:** Thay chỉ nội dung retrieved; authority phải giữ nguyên.

**Đánh đổi:** Giới hạn tool có thể giảm tác vụ tự động hợp lệ.

**OPEN:** Injection gián tiếp qua memory hoặc multimodal còn đường nào?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Không thực hiện hành động vượt nhiệm vụ / Nội dung được model coi là lệnh ưu tiên
- **domain:** Chốt population và giới hạn: Ứng dụng LLM và automation; AI/platform owner; Agent đọc nội dung bên ngoài
- **mechanism:** Control có giữ invariant này không? Văn bản thuyết phục không tạo quyền mới
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Thay chỉ nội dung retrieved; authority phải giữ nguyên
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Policy ngoài model; sandbox; review; provenance; Prompt; retrieval; memory; tool; chi phí; model change
- **consequence:** Đạt Nội dung không đáng tin không được nâng thành authority nhưng phải theo dõi Giới hạn tool có thể giảm tác vụ tự động hợp lệ

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Hành động vượt policy / ca untrusted-content test
- **domain:** Ứng dụng LLM và automation; AI/platform owner; Agent đọc nội dung bên ngoài
- **conditions:** Agent đọc nội dung bên ngoài
- **goal:** Nội dung không đáng tin không được nâng thành authority
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Provenance, decision và tool request; bằng chứng test: Thay chỉ nội dung retrieved; authority phải giữ nguyên
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Giới hạn tool có thể giảm tác vụ tự động hợp lệ; Injection gián tiếp qua memory hoặc multimodal còn đường nào?
- **binding:** ai-instruction → điểm thực thi: Giữ nguồn như dữ liệu; policy thực thi ngoài model
