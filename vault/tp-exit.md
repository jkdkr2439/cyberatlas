### tp-exit — Khả năng rời nhà cung cấp

**Điều kiện:** Chấm dứt hợp đồng hoặc supplier outage.

- **I:** Export format, keys, data volume và exit terms
- **P:** Thử lấy dữ liệu và tái dựng trên môi trường khác
- **O:** Năng lực chuyển/tiếp tục có kiểm chứng
- **D:** Export/reimport test và residual access

**Hằng trong frame:** Có nút export không bảo đảm dùng lại được.

**Đường hỏng:** Thiếu metadata, khóa hoặc lịch sử giao dịch. **Điểm can thiệp:** Exit drill, format contract, revoke integrations.

**Phép đo ứng viên:** Tỷ lệ record nghiệp vụ tái dựng đúng / mẫu exit test.

**Test phân biệt / bằng chứng cần:** Xuất rồi nhập lại với reconciliation độc lập.

**Đánh đổi:** Duy trì portable format có chi phí.

**OPEN:** Nhà cung cấp biến mất trước export thì sao?

**Liên hệ có điều kiện:**

- `rec-backup` — Exit drill cần dữ liệu, key và khả năng dựng lại chứ không chỉ hợp đồng.


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Năng lực chuyển/tiếp tục có kiểm chứng / Thiếu metadata, khóa hoặc lịch sử giao dịch
- **domain:** Chốt population và giới hạn: Quan hệ ngoài tổ chức; procurement và service owner; Chấm dứt hợp đồng hoặc supplier outage
- **mechanism:** Control có giữ invariant này không? Có nút export không bảo đảm dùng lại được
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Xuất rồi nhập lại với reconciliation độc lập
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Hợp đồng; test; quyền xuất dữ liệu; nguồn thay thế; Subprocessor; outage chung; remote support; exit cost
- **consequence:** Đạt Authority, dữ liệu và khả năng phục hồi không mất kiểm soát nhưng phải theo dõi Duy trì portable format có chi phí

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Tỷ lệ record nghiệp vụ tái dựng đúng / mẫu exit test
- **domain:** Quan hệ ngoài tổ chức; procurement và service owner; Chấm dứt hợp đồng hoặc supplier outage
- **conditions:** Chấm dứt hợp đồng hoặc supplier outage
- **goal:** Authority, dữ liệu và khả năng phục hồi không mất kiểm soát
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Export/reimport test và residual access; bằng chứng test: Xuất rồi nhập lại với reconciliation độc lập
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Duy trì portable format có chi phí; Nhà cung cấp biến mất trước export thì sao?
- **binding:** tp-exit → điểm thực thi: Thử lấy dữ liệu và tái dựng trên môi trường khác
