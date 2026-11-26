### det-behavior — Phát hiện theo hành vi

**Điều kiện:** Có chuỗi hành động qua nhiều hệ.

- **I:** Events, actor và timing
- **P:** Ghép chuỗi có điều kiện thay vì chỉ tên tool
- **O:** Tín hiệu gắn kịch bản cần điều tra
- **D:** Correlation evidence và mapping tham khảo

**Hằng trong frame:** Mapping ATT&CK không chứng minh detection hoạt động.

**Đường hỏng:** Rule có nhãn technique nhưng không thấy đường thực tế. **Điểm can thiệp:** Diễn tập hành vi an toàn và kiểm evidence chain.

**Phép đo ứng viên:** Kịch bản có tín hiệu đủ điều tra / kịch bản được thử.

**Test phân biệt / bằng chứng cần:** Đổi công cụ, giữ hành vi và kiểm detection.

**Đánh đổi:** Correlation tăng nhu cầu dữ liệu và false linkage.

**OPEN:** Technique/version mới làm mapping lỗi thời thế nào?

**Liên hệ có điều kiện:**

- `ir-contain` — Phát hiện chỉ tạo giá trị khi thông tin đủ cho quyết định và hành động.
- `F08` — Sandbox quan sát được hành vi nào, và hành vi né môi trường làm giới hạn kết luận ra sao?
- `F20` — Indicator hết hạn khi nào, nguồn có độc lập không và intelligence có đổi quyết định thực tế không?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Tín hiệu gắn kịch bản cần điều tra / Rule có nhãn technique nhưng không thấy đường thực tế
- **domain:** Chốt population và giới hạn: Tín hiệu đến quyết định; SOC; Có chuỗi hành động qua nhiều hệ
- **mechanism:** Control có giữ invariant này không? Mapping ATT&CK không chứng minh detection hoạt động
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Đổi công cụ, giữ hành vi và kiểm detection
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Analyst; rules; ground truth; diễn tập; Base rate; adversary drift; queue; nhãn chưa đầy đủ
- **consequence:** Đạt Nhận ra sự kiện cần xử lý với chi phí chấp nhận được nhưng phải theo dõi Correlation tăng nhu cầu dữ liệu và false linkage

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Kịch bản có tín hiệu đủ điều tra / kịch bản được thử
- **domain:** Tín hiệu đến quyết định; SOC; Có chuỗi hành động qua nhiều hệ
- **conditions:** Có chuỗi hành động qua nhiều hệ
- **goal:** Nhận ra sự kiện cần xử lý với chi phí chấp nhận được
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Correlation evidence và mapping tham khảo; bằng chứng test: Đổi công cụ, giữ hành vi và kiểm detection
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Correlation tăng nhu cầu dữ liệu và false linkage; Technique/version mới làm mapping lỗi thời thế nào?
- **binding:** det-behavior → điểm thực thi: Ghép chuỗi có điều kiện thay vì chỉ tên tool
