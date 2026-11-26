### sw-release — Phát hành và rollback

**Điều kiện:** Bản mới ảnh hưởng quyền/dữ liệu.

- **I:** Artifact, config, migration và rollout plan
- **P:** Canary, kiểm outcome, rollback có điều kiện
- **O:** Dịch vụ mới vẫn giữ invariant
- **D:** Release evidence và state transition

**Hằng trong frame:** Rollback code chưa chắc rollback được dữ liệu.

**Đường hỏng:** Migration không tương thích phá recovery. **Điểm can thiệp:** Test forward/backward compatibility và rollback drill.

**Phép đo ứng viên:** Release có rollback end-to-end được thử / release cần rollback.

**Test phân biệt / bằng chứng cần:** Rollback sau migration trong staging.

**Đánh đổi:** Giữ tương thích tăng độ phức tạp.

**OPEN:** Thay đổi không đảo ngược phải có chiến lược nào?


## Sáu miền review

- **meaning:** Phân biệt trạng thái mong muốn với failure: Dịch vụ mới vẫn giữ invariant / Migration không tương thích phá recovery
- **domain:** Chốt population và giới hạn: Thiết kế đến vận hành; engineering; Bản mới ảnh hưởng quyền/dữ liệu
- **mechanism:** Control có giữ invariant này không? Rollback code chưa chắc rollback được dữ liệu
- **evidence:** Quan sát nào có thể bác bỏ kết luận? Rollback sau migration trong staging
- **operational:** Nguồn lực có đủ và điều kiện nào đổi? Review; CI; test fixtures; owner khắc phục; Ngôn ngữ; framework; test quality; release pressure
- **consequence:** Đạt Yêu cầu bảo mật tồn tại qua các lần thay đổi nhưng phải theo dõi Giữ tương thích tăng độ phức tạp

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Release có rollback end-to-end được thử / release cần rollback
- **domain:** Thiết kế đến vận hành; engineering; Bản mới ảnh hưởng quyền/dữ liệu
- **conditions:** Bản mới ảnh hưởng quyền/dữ liệu
- **goal:** Yêu cầu bảo mật tồn tại qua các lần thay đổi
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Release evidence và state transition; bằng chứng test: Rollback sau migration trong staging
- **method:** Operationalize candidate sau khi chốt denominator, ground truth và scope; dùng test phản ví dụ của thẻ.
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Giữ tương thích tăng độ phức tạp; Thay đổi không đảo ngược phải có chiến lược nào?
- **binding:** sw-release → điểm thực thi: Canary, kiểm outcome, rollback có điều kiện
