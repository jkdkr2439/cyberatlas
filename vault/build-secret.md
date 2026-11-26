### build-secret — Cấp secret theo giai đoạn build

**Điều kiện:** CI có contribution từ bên ngoài.

- **I:** Job identity, trust level và secret request
- **P:** Chỉ cấp credential cho bước được phép và thời gian cần
- **O:** Build không tin không nhận secret release
- **D:** Grant scope, issue/expiry và consumer

**Hằng trong frame:** Mask log không đồng nghĩa secret không tới process.

**Đường hỏng:** Secret đưa vào env của mọi bước. **Điểm can thiệp:** Short-lived scoped credentials và tách release job.

**Phép đo ứng viên:** Bước không phép nhận credential / test job classes.

**Test phân biệt / bằng chứng cần:** Mock secret broker từ chối job untrusted dù workflow tên giống.

**Đánh đổi:** Tách job cần truyền artifact có kiểm chứng.

**OPEN:** Fork PR, reusable workflow và bot identity được phân loại thế nào?


## Sáu miền review

- **meaning:** Mask log không đồng nghĩa secret không tới process
- **domain:** Source, build, artifact, deploy; release team; CI nhận contribution không tin; CI có contribution từ bên ngoài
- **mechanism:** Chỉ cấp credential cho bước được phép và thời gian cần; failure: Secret đưa vào env của mọi bước
- **evidence:** Mock secret broker từ chối job untrusted dù workflow tên giống
- **operational:** Builder cô lập; chứng thực; kiểm tra ở deploy; Tách job cần truyền artifact có kiểm chứng
- **consequence:** Artifact triển khai đúng nguồn và chính sách cho phép; Fork PR, reusable workflow và bot identity được phân loại thế nào?

## Metric sketch

- **status:** candidate_missing_data
- **region:** owner_selects_from_six_regions
- **q:** Bước không phép nhận credential / test job classes
- **domain:** Source, build, artifact, deploy; release team; CI nhận contribution không tin; CI có contribution từ bên ngoài
- **conditions:** CI có contribution từ bên ngoài
- **goal:** Artifact triển khai đúng nguồn và chính sách cho phép
- **baseline:** Chọn baseline cùng population, phiên bản policy và điều kiện; owner chưa bind môi trường.
- **scale:** Theo đơn vị được nêu trong candidate; không gom thành điểm tổng.
- **time:** Cửa sổ và cadence cần owner chốt theo vòng đời/điều kiện của thẻ.
- **data:** Grant scope, issue/expiry và consumer
- **method:** Mock secret broker từ chối job untrusted dù workflow tên giống
- **missing:** Unknown/unrun/unresolved báo riêng. Nếu là tỷ lệ, D=0 → undefined; không loại missing khỏi population cần quan sát.
- **limitation:** Tách job cần truyền artifact có kiểm chứng; Fork PR, reusable workflow và bot identity được phân loại thế nào?
- **binding:** build-secret → Chỉ cấp credential cho bước được phép và thời gian cần
