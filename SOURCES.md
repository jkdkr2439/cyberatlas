# Nguồn và provenance

Rà ngày 2026-11-26, Asia/Bangkok. Tham chiếu bối cảnh không đồng nghĩa từng câu đã được nguồn xác nhận. Các thẻ/metric mở rộng do assistant biên soạn; không gán cho NIST/OWASP/Pete hoặc tác giả sách.

## book — Hệ miễn dịch của thế giới số — Kevin T.N.

[Hệ miễn dịch của thế giới số — Kevin T.N.](urn:cyber-atlas:source:book)

Local seed; toàn bộ heading được index, đọc các đoạn nền và các phần mẫu. Không tuyên bố thẩm định từng câu trong sách.

SHA-256: `f5037432e708a0a2e84b7e2d123fb406f27aae81a3eb16a0eb3b028455ef197b`

## metric — A Fractal Model for Metric Generation

[A Fractal Model for Metric Generation](urn:cyber-atlas:source:metric)

Local method, 46 trang; phương pháp mở context trước khi sinh metric.

SHA-256: `8b6b291416049310fd5605811a5d249ab5a06cdeadd0b10b03ce2ec861cdffd5`

## lens — Lens framework

[Lens framework](urn:cyber-atlas:source:lens)

Đã đọc protocol/framework/template; vận dụng NMF, IPOD, C/V, resources, tradeoffs.

SHA-256: `bad41ea02251147a535518fe761743e08e6bbbe1fd6eed1d51f2f36cad34a5c4`

## csf — NIST Cybersecurity Framework

[NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

Trang tổng quan chính thức; dùng làm khung định hướng, không tuyên bố crosswalk mọi subcategory.

## measure — NIST SP 800-55 Vol. 1 (2024)

[NIST SP 800-55 Vol. 1 (2024)](https://csrc.nist.gov/pubs/sp/800/55/v1/final)

Trang xuất bản và abstract: lựa chọn/đánh giá phép đo. Các công thức atlas do tác giả bản đồ đề xuất, không gán cho NIST.

## zt — NIST SP 800-207 (2020)

[NIST SP 800-207 (2020)](https://csrc.nist.gov/pubs/sp/800/207/final)

Trang xuất bản/tổng quan Zero Trust; khung liên quan, không claim từng card là yêu cầu tiêu chuẩn.

## identity — NIST SP 800-63B-4 (2025)

[NIST SP 800-63B-4 (2025)](https://pages.nist.gov/800-63-4/sp800-63b.html)

Đọc cụ thể §3.2.5 phishing resistance và đoạn replay resistance. Tách OTP khỏi protocol chống phishing; các kịch bản lifecycle là phần mở rộng phân tích.

## asvs — OWASP ASVS 5.0.0

[OWASP ASVS 5.0.0](https://asvs.owasp.org/)

Trang dự án, stable release 2025-05-30; tài liệu để đào tiếp. Chưa map đến requirement ID.

## api — OWASP API Security Top 10 (2023)

[OWASP API Security Top 10 (2023)](https://api-security.owasp.org/editions/2023/en/0x11-t10/)

Đọc danh sách rủi ro cấp tổng quan; các tình huống cache/race/async là mở rộng phân tích.

## attack — MITRE ATT&CK

[MITRE ATT&CK](https://attack.mitre.org/)

Trang matrix trực tiếp; dùng như vocabulary hành vi, không copy toàn matrix hay khẳng định detection coverage. Taxonomy thay đổi nên cần pin release khi triển khai.

## ir — NIST SP 800-61 Rev. 3 (2025)

[NIST SP 800-61 Rev. 3 (2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

Trang xuất bản/abstract; bản 2025 thay rev2. Các drill trong atlas là đề xuất riêng.

## ssdf — NIST SP 800-218, SSDF v1.1 (2022)

[NIST SP 800-218, SSDF v1.1 (2022)](https://csrc.nist.gov/pubs/sp/800/218/final)

Pinned edition; trang xuất bản/tổng quan. Không tuyên bố đã rà mọi phiên bản draft mới.

## ot — NIST SP 800-82 Rev. 3 (2023)

[NIST SP 800-82 Rev. 3 (2023)](https://csrc.nist.gov/pubs/sp/800/82/r3/final)

Trang xuất bản nhấn mạnh performance/reliability/safety. Ngày rà có note Rev4 initial public draft, hạn góp ý 2026-11-30; atlas pin rev3, không trộn draft.

## cvss — FIRST CVSS v4.0 specification

[FIRST CVSS v4.0 specification](https://www.first.org/cvss/v4.0/specification-document)

Đọc Metrics/Assessment: CVSS là đầu vào, các yếu tố tổn thất kinh doanh ngoài phạm vi CVSS. Các công thức exposure-hours là đề xuất atlas.

## llm — OWASP Top 10 for LLM Applications (2025)

[OWASP Top 10 for LLM Applications (2025)](https://genai.owasp.org/llm-top-10/)

Trang tổng quan các loại rủi ro; không coi danh sách này là threat model đầy đủ cho mọi agent.

## k8s — Kubernetes Security Checklist

[Kubernetes Security Checklist](https://kubernetes.io/docs/concepts/security/security-checklist/)

Đọc cụ thể Pod security: RBAC và admission khác nhau; warn/audit khác enforce. Trang online thay đổi, cần pin version cluster khi áp dụng.

## slsa — SLSA v1.2

[SLSA v1.2](https://slsa.dev/spec/v1.2/)

Trang approved specification overview/tracks/provenance; chưa thẩm định đủ điều kiện từng level. Không cấp chứng nhận SLSA qua atlas.

## Giới hạn truy cập

CISA KEV catalog trả 403 ở lượt rà. Không dùng kết quả không truy cập được làm bằng chứng. Việc tìm kiếm KEV/exploitation intelligence khi áp vào môi trường thật vẫn là frontier dữ liệu.

## Index sách

Toàn bộ 502 heading được index bằng chương trình; việc này không đồng nghĩa đã kiểm định toàn bộ nội dung. Bản gốc không bị sửa.

| Phần | Dòng bắt đầu | Dòng kết thúc |
|---|---:|---:|
| Phần 01 — ONTOLOGY CỦA BẢO MẬT | 30 | 469 |
| Phần 02 — Cơ chế gốc: hằng và biến trong bảo mật | 470 | 1603 |
| Phần 03 — IPOD của bảo mật: Input, Process, Output, Data | 1604 | 3533 |
| Phần 04 — Phân loại lỗi bảo mật bằng hai trục IPOD và hằng/biến | 3534 | 5509 |
| Phần 05 — Ontology rủi ro: Threat, Vulnerability, Likelihood, Impact, Risk | 5510 | 6625 |
| Phần 06 — Zero Trust: ontology của quyền và niềm tin | 6626 | 7585 |
| Phần 07 — MITRE ATT&CK: ontology của hành vi attacker | 7586 | 8535 |
| Phần 08 — Data ontology cho agent bảo mật | 8536 | 10085 |
| Phần 09 — Agent ontology: từ chatbot đến hệ vận hành | 10086 | 11374 |
| Phần 10 — Agent bảo mật: quyền, data và human review | 11375 | 12408 |
| Phần 11 — Từ ontology sang hệ thống AI security agent | 12409 | 14030 |
| Phần 12 — Nhìn lại toàn bộ bản đồ | 14031 | 14983 |