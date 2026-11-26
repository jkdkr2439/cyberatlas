### gov-loss — Kịch bản thiệt hại

**Điều kiện:** Đang ưu tiên đầu tư.

- **I:** Tài sản, đường lỗi, hậu quả
- **P:** Tách tần suất, mức thiệt hại và bất định
- **O:** Khoảng hậu quả theo kịch bản
- **D:** Giả định và nguồn ước lượng

**Hằng trong frame:** Không biến CVSS thành xác suất mất tiền.

**Đường hỏng:** Cộng điểm ordinal như đại lượng tỷ lệ. **Điểm can thiệp:** Kịch bản và sensitivity analysis.

**Phép đo ứng viên:** Khoảng tổn thất có điều kiện; không xuất một xác suất khi thiếu dữ liệu.

**Test phân biệt / bằng chứng cần:** Thay giả định phơi nhiễm, kiểm tra thứ hạng đảo hay không.

**Đánh đổi:** Mô hình chi tiết tốn dữ liệu và công sức.

**OPEN:** Tổn thất gián tiếp và phụ thuộc chung được tính thế nào?

**Liên hệ có điều kiện:**

- `vul-context` — Ưu tiên sửa cần hậu quả ở đúng hệ và cửa sổ thời gian.
- `F23` — Hợp đồng chuyển loại tổn thất nào, còn incentive và correlated loss nào ở lại?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Khoảng hậu quả theo kịch bản / Cộng điểm ordinal như đại lượng tỷ lệ
- **domain:** Chốt population và giới hạn: Doanh nghiệp; hội đồng rủi ro và chủ dịch vụ; Đang ưu tiên đầu tư
- **mechanism:** Control có giữ invariant này không? Không biến CVSS thành xác suất mất tiền
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Thay giả định phơi nhiễm, kiểm tra thứ hạng đảo hay không
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Thẩm quyền; thời gian đánh giá; ngân sách sửa sai; Khẩu vị rủi ro; quy mô; thời hạn; nghĩa vụ
- **consequence:** Đạt Quyết định có người chịu trách nhiệm và có giới hạn nhưng phải theo dõi Mô hình chi tiết tốn dữ liệu và công sức

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Khoảng tổn thất có điều kiện; không xuất một xác suất khi thiếu dữ liệu
- **domain:** Doanh nghiệp; hội đồng rủi ro và chủ dịch vụ; Đang ưu tiên đầu tư
- **conditions:** Đang ưu tiên đầu tư
- **goal:** Quyết định có người chịu trách nhiệm và có giới hạn
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Giả định và nguồn ước lượng; bằng chứng test: Thay giả định phơi nhiễm, kiểm tra thứ hạng đảo hay không
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Mô hình chi tiết tốn dữ liệu và công sức; Tổn thất gián tiếp và phụ thuộc chung được tính thế nào?
- **binding:** gov-loss → điểm thực thi: Tách tần suất, mức thiệt hại và bất định
