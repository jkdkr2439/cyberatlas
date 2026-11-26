# Nhánh OPEN

Không được tính các câu hỏi này là cơ chế đã giải thích.

## F01 — Side-channel và hardware root of trust

Đối thủ quan sát timing/power/cache trong mô hình truy cập nào, và control có tác dụng ở lớp nào?

Nối từ `cry-integrity`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F02 — Confidential computing và attestation

Attestation xác nhận binary/config nào, ai cung cấp freshness và ai được giải phóng secret?

Nối từ `cry-key`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F03 — Mật mã hậu lượng tử

Inventory dữ liệu bí mật dài hạn và protocol hybrid cần cách đo migration/compatibility nào?

Nối từ `cry-agility`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F04 — Wi-Fi, Bluetooth và mạng không dây

Trust boundary thay khi kênh truyền dùng chung môi trường vật lý ra sao?

Nối từ `net-segment`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F05 — Định tuyến liên miền và BGP

Sai lệch route đến từ cấu hình, authority hay compromise; nguồn nào đủ độc lập để nhận biết?

Nối từ `msg-dns`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F06 — Mobile và browser extension

Permission thực tế, sandbox, SDK và đường export dữ liệu trên từng platform là gì?

Nối từ `end-execution`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F07 — Firmware, boot và thiết bị ngoại vi

Chuỗi tin cậy từ boot tới runtime đứt ở đâu khi một thành phần firmware bị sửa?

Nối từ `end-execution`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F08 — Malware analysis và reverse engineering

Sandbox quan sát được hành vi nào, và hành vi né môi trường làm giới hạn kết luận ra sao?

Nối từ `det-behavior`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F09 — Browser isolation và cross-origin

Origin/site, cookie, storage và messaging tạo ranh giới khác nhau thế nào?

Nối từ `web-xss`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F10 — File upload và đa phương tiện

Parser, converter, metadata và antivirus tạo những process con với quyền gì?

Nối từ `web-parser`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F11 — GraphQL và query planning

Query hợp lệ có thể gây chi phí không tuyến tính hoặc lấy trường vượt quyền thế nào?

Nối từ `api-abuse`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F12 — Consensus và hệ phân tán

Byzantine faults, finality và khả năng quan sát thay đổi invariant giao dịch thế nào?

Nối từ `api-state`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F13 — Serverless và ephemeral workloads

Identity, telemetry và residual state được theo dõi thế nào khi vòng đời ngắn hơn scan cadence?

Nối từ `cld-drift`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F14 — Multi-cluster và service mesh

Trust bundle và identity federation làm tăng hay giảm blast radius khi một control plane bị chiếm?

Nối từ `k8s-identity`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F15 — Model và dataset supply chain

Dataset, checkpoint và evaluation provenance khác binary provenance ở chỗ nào?

Nối từ `sup-dependency`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F16 — Suy diễn riêng tư và tái định danh

Các dataset riêng không nhạy cảm có thể kết hợp để suy ra điều gì, với đối thủ nào?

Nối từ `dat-class`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F17 — Differential privacy và ngân sách riêng tư

Đơn vị bảo vệ, composition và utility tradeoff được định nghĩa ra sao trước khi chọn epsilon?

Nối từ `dat-egress`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F18 — MPC và federated learning

Ai có thể collude, output vẫn tiết lộ gì, và protocol bảo vệ khâu nào?

Nối từ `dat-class`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F19 — Disclosure và bug bounty

Scope, phối hợp vá, bằng chứng không gây hại và thời gian disclosure được quyết định thế nào?

Nối từ `vul-fix`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F20 — Threat intelligence

Indicator hết hạn khi nào, nguồn có độc lập không và intelligence có đổi quyết định thực tế không?

Nối từ `det-behavior`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F21 — Deception và honeypot

Ai có thể chạm honeypot hợp lệ, và tín hiệu phản ánh môi trường thật đến đâu?

Nối từ `det-base`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F22 — Crisis communication

Ai được nói điều gì với mức chắc chắn nào khi scope sự cố còn chưa biết?

Nối từ `ir-learn`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F23 — Cyber insurance và economics

Hợp đồng chuyển loại tổn thất nào, còn incentive và correlated loss nào ở lại?

Nối từ `gov-loss`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F24 — Pháp luật và chứng nhận

Jurisdiction, loại dữ liệu, nghĩa vụ báo cáo và bằng chứng đáp ứng cụ thể là gì?

Nối từ `gov-owner`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F25 — Insider và coercion

Quyền hợp lệ, động cơ, thiếu hỗ trợ và bị ép buộc tạo các giả thuyết phân biệt nào?

Nối từ `hum-report`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F26 — Accessibility và security usability

Control loại người dùng nào khỏi dịch vụ, có phương án giữ assurance mà giảm loại trừ không?

Nối từ `id-recovery`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F27 — Telecom, vệ tinh và hạ tầng quốc gia

Failure domain, đặc quyền vận hành và time horizon khác enterprise thông thường thế nào?

Nối từ `tp-concentration`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F28 — Thiết bị y tế và phương tiện

Safety case, vòng đời hỗ trợ và authority update thay đổi tiêu chí triển khai ra sao?

Nối từ `ot-safety`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F29 — Đầu độc model và data

Phân biệt training poisoning, retrieval poisoning và memory poisoning bằng cơ chế/observable nào?

Nối từ `ai-memory`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F30 — Model extraction và inference leakage

Ai truy cập output gì, budget truy vấn bao nhiêu, thiệt hại được định nghĩa thế nào?

Nối từ `dat-egress`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F31 — Agent nhiều bước và nhiều chủ thể

Authority có được cộng dồn sai khi output agent này làm input agent khác không?

Nối từ `ai-tool`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.

## F32 — Chi phí, dừng và vòng lặp tự động

Retry, tool recursion, memory growth và budget exhaustion có stop condition nào ngoài model?

Nối từ `api-retry`. Mở lại: Chọn scope cụ thể và nguồn chuyên ngành; trả lời câu hỏi trước khi sinh metric.
