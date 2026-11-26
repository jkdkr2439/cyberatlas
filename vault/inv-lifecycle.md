### inv-lifecycle — Tài sản hết vòng đời

**Điều kiện:** Thêm, chuyển hoặc loại bỏ thiết bị.

- **I:** Sự kiện cấp phát, thay owner, hủy dịch vụ
- **P:** Đồng bộ quyền, DNS, secret và dữ liệu
- **O:** Tài sản không còn authority dư
- **D:** Biên bản hủy và đối soát

**Hằng trong frame:** Hủy máy không đồng nghĩa hủy quyền.

**Đường hỏng:** DNS trỏ dịch vụ không còn owner; token vẫn sống. **Điểm can thiệp:** Workflow decommission và kiểm tra sau hủy.

**Phép đo ứng viên:** Tài sản đã hủy còn credential hợp lệ / tài sản hủy được kiểm tra.

**Test phân biệt / bằng chứng cần:** Xóa workload nhưng thử lại quyền máy đó trong lab.

**Đánh đổi:** Lưu dữ liệu phục hồi có thể trì hoãn xóa.

**OPEN:** Các bản sao bên nhà cung cấp xử lý thế nào?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Tài sản không còn authority dư / DNS trỏ dịch vụ không còn owner; token vẫn sống
- **domain:** Chốt population và giới hạn: Hạ tầng và SaaS; chủ tài sản; Thêm, chuyển hoặc loại bỏ thiết bị
- **mechanism:** Control có giữ invariant này không? Hủy máy không đồng nghĩa hủy quyền
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Xóa workload nhưng thử lại quyền máy đó trong lab
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Đầu nối inventory; quyền đọc; người xác nhận owner; Tài sản ngắn hạn; shadow IT; mua bán doanh nghiệp
- **consequence:** Đạt Biết đối tượng nào cần bảo vệ và nó phụ thuộc gì nhưng phải theo dõi Lưu dữ liệu phục hồi có thể trì hoãn xóa

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Tài sản đã hủy còn credential hợp lệ / tài sản hủy được kiểm tra
- **domain:** Hạ tầng và SaaS; chủ tài sản; Thêm, chuyển hoặc loại bỏ thiết bị
- **conditions:** Thêm, chuyển hoặc loại bỏ thiết bị
- **goal:** Biết đối tượng nào cần bảo vệ và nó phụ thuộc gì
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Biên bản hủy và đối soát; bằng chứng test: Xóa workload nhưng thử lại quyền máy đó trong lab
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Lưu dữ liệu phục hồi có thể trì hoãn xóa; Các bản sao bên nhà cung cấp xử lý thế nào?
- **binding:** inv-lifecycle → điểm thực thi: Đồng bộ quyền, DNS, secret và dữ liệu
