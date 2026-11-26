### action-digest — Canonical representation của hành động

**Điều kiện:** Approval được bind bằng digest.

- **I:** Tool name, args, object refs và versions
- **P:** Chuẩn hóa có semantics rõ rồi tính digest cho nội dung cần khóa
- **O:** Cùng hành động cho cùng binding; đổi nghĩa thì binding đổi
- **D:** Canonical form version và digest

**Hằng trong frame:** Hash chuỗi path không khóa nội dung file thay đổi.

**Đường hỏng:** File cùng tên đổi sau review; JSON canonicalization sai. **Điểm can thiệp:** Bind immutable content/version cùng destination.

**Phép đo ứng viên:** Biến đổi ngữ nghĩa không đổi digest / mutation cases.

**Test phân biệt / bằng chứng cần:** Đổi nội dung file nhưng giữ path; phải invalid approval.

**Đánh đổi:** Hash dữ liệu lớn tốn IO và có dữ liệu động.

**OPEN:** Secret/redacted field được bind mà không lộ bằng cách nào?


## Sáu miền review

- **meaning:** Hash chuỗi path không khóa nội dung file thay đổi
- **domain:** Ứng dụng LLM và automation; AI/platform owner; Model có khả năng ghi hoặc gửi; Agent chuẩn bị hành động có hậu quả; Approval được bind bằng digest
- **mechanism:** Chuẩn hóa có semantics rõ rồi tính digest cho nội dung cần khóa; failure: File cùng tên đổi sau review; JSON canonicalization sai
- **evidence:** Đổi nội dung file nhưng giữ path; phải invalid approval
- **operational:** Policy ngoài model; sandbox; review; provenance; Hash dữ liệu lớn tốn IO và có dữ liệu động
- **consequence:** Nội dung không đáng tin không được nâng thành authority; Secret/redacted field được bind mà không lộ bằng cách nào?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Biến đổi ngữ nghĩa không đổi digest / mutation cases
- **domain:** Ứng dụng LLM và automation; AI/platform owner; Model có khả năng ghi hoặc gửi; Agent chuẩn bị hành động có hậu quả; Approval được bind bằng digest
- **conditions:** Approval được bind bằng digest
- **goal:** Nội dung không đáng tin không được nâng thành authority
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Canonical form version và digest
- **method:** Đổi nội dung file nhưng giữ path; phải invalid approval
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Hash dữ liệu lớn tốn IO và có dữ liệu động; Secret/redacted field được bind mà không lộ bằng cách nào?
- **binding:** action-digest → Chuẩn hóa có semantics rõ rồi tính digest cho nội dung cần khóa
