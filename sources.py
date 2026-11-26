SOURCES = [
('book','Hệ miễn dịch của thế giới số — Kevin T.N.','urn:cyber-atlas:source:book','Local seed; toàn bộ heading được index, đọc các đoạn nền và các phần mẫu. Không tuyên bố thẩm định từng câu trong sách.'),
('metric','A Fractal Model for Metric Generation','urn:cyber-atlas:source:metric','Local method, 46 trang; phương pháp mở context trước khi sinh metric.'),
('lens','Lens framework','urn:cyber-atlas:source:lens','Đã đọc protocol/framework/template; vận dụng NMF, IPOD, C/V, resources, tradeoffs.'),
('csf','NIST Cybersecurity Framework','https://www.nist.gov/cyberframework','Trang tổng quan chính thức; dùng làm khung định hướng, không tuyên bố crosswalk mọi subcategory.'),
('measure','NIST SP 800-55 Vol. 1 (2024)','https://csrc.nist.gov/pubs/sp/800/55/v1/final','Trang xuất bản và abstract: lựa chọn/đánh giá phép đo. Các công thức atlas do tác giả bản đồ đề xuất, không gán cho NIST.'),
('zt','NIST SP 800-207 (2020)','https://csrc.nist.gov/pubs/sp/800/207/final','Trang xuất bản/tổng quan Zero Trust; khung liên quan, không claim từng card là yêu cầu tiêu chuẩn.'),
('identity','NIST SP 800-63B-4 (2025)','https://pages.nist.gov/800-63-4/sp800-63b.html','Đọc cụ thể §3.2.5 phishing resistance và đoạn replay resistance. Tách OTP khỏi protocol chống phishing; các kịch bản lifecycle là phần mở rộng phân tích.'),
('asvs','OWASP ASVS 5.0.0','https://asvs.owasp.org/','Trang dự án, stable release 2025-05-30; tài liệu để đào tiếp. Chưa map đến requirement ID.'),
('api','OWASP API Security Top 10 (2023)','https://api-security.owasp.org/editions/2023/en/0x11-t10/','Đọc danh sách rủi ro cấp tổng quan; các tình huống cache/race/async là mở rộng phân tích.'),
('attack','MITRE ATT&CK','https://attack.mitre.org/','Trang matrix trực tiếp; dùng như vocabulary hành vi, không copy toàn matrix hay khẳng định detection coverage. Taxonomy thay đổi nên cần pin release khi triển khai.'),
('ir','NIST SP 800-61 Rev. 3 (2025)','https://csrc.nist.gov/pubs/sp/800/61/r3/final','Trang xuất bản/abstract; bản 2025 thay rev2. Các drill trong atlas là đề xuất riêng.'),
('ssdf','NIST SP 800-218, SSDF v1.1 (2022)','https://csrc.nist.gov/pubs/sp/800/218/final','Pinned edition; trang xuất bản/tổng quan. Không tuyên bố đã rà mọi phiên bản draft mới.'),
('ot','NIST SP 800-82 Rev. 3 (2023)','https://csrc.nist.gov/pubs/sp/800/82/r3/final','Trang xuất bản nhấn mạnh performance/reliability/safety. Ngày rà có note Rev4 initial public draft, hạn góp ý 2026-11-30; atlas pin rev3, không trộn draft.'),
('cvss','FIRST CVSS v4.0 specification','https://www.first.org/cvss/v4.0/specification-document','Đọc Metrics/Assessment: CVSS là đầu vào, các yếu tố tổn thất kinh doanh ngoài phạm vi CVSS. Các công thức exposure-hours là đề xuất atlas.'),
('llm','OWASP Top 10 for LLM Applications (2025)','https://genai.owasp.org/llm-top-10/','Trang tổng quan các loại rủi ro; không coi danh sách này là threat model đầy đủ cho mọi agent.'),
('k8s','Kubernetes Security Checklist','https://kubernetes.io/docs/concepts/security/security-checklist/','Đọc cụ thể Pod security: RBAC và admission khác nhau; warn/audit khác enforce. Trang online thay đổi, cần pin version cluster khi áp dụng.'),
('slsa','SLSA v1.2','https://slsa.dev/spec/v1.2/','Trang approved specification overview/tracks/provenance; chưa thẩm định đủ điều kiện từng level. Không cấp chứng nhận SLSA qua atlas.')
]

# Frontiers are research questions, deliberately not asserted mechanisms.
FRONTIERS = '''
crypto|Side-channel và hardware root of trust|Đối thủ quan sát timing/power/cache trong mô hình truy cập nào, và control có tác dụng ở lớp nào?|cry-integrity
crypto|Confidential computing và attestation|Attestation xác nhận binary/config nào, ai cung cấp freshness và ai được giải phóng secret?|cry-key
crypto|Mật mã hậu lượng tử|Inventory dữ liệu bí mật dài hạn và protocol hybrid cần cách đo migration/compatibility nào?|cry-agility
network|Wi-Fi, Bluetooth và mạng không dây|Trust boundary thay khi kênh truyền dùng chung môi trường vật lý ra sao?|net-segment
network|Định tuyến liên miền và BGP|Sai lệch route đến từ cấu hình, authority hay compromise; nguồn nào đủ độc lập để nhận biết?|msg-dns
endpoint|Mobile và browser extension|Permission thực tế, sandbox, SDK và đường export dữ liệu trên từng platform là gì?|end-execution
endpoint|Firmware, boot và thiết bị ngoại vi|Chuỗi tin cậy từ boot tới runtime đứt ở đâu khi một thành phần firmware bị sửa?|end-execution
endpoint|Malware analysis và reverse engineering|Sandbox quan sát được hành vi nào, và hành vi né môi trường làm giới hạn kết luận ra sao?|det-behavior
web|Browser isolation và cross-origin|Origin/site, cookie, storage và messaging tạo ranh giới khác nhau thế nào?|web-xss
web|File upload và đa phương tiện|Parser, converter, metadata và antivirus tạo những process con với quyền gì?|web-parser
api|GraphQL và query planning|Query hợp lệ có thể gây chi phí không tuyến tính hoặc lấy trường vượt quyền thế nào?|api-abuse
api|Consensus và hệ phân tán|Byzantine faults, finality và khả năng quan sát thay đổi invariant giao dịch thế nào?|api-state
cloud|Serverless và ephemeral workloads|Identity, telemetry và residual state được theo dõi thế nào khi vòng đời ngắn hơn scan cadence?|cld-drift
containers|Multi-cluster và service mesh|Trust bundle và identity federation làm tăng hay giảm blast radius khi một control plane bị chiếm?|k8s-identity
supply|Model và dataset supply chain|Dataset, checkpoint và evaluation provenance khác binary provenance ở chỗ nào?|sup-dependency
data|Suy diễn riêng tư và tái định danh|Các dataset riêng không nhạy cảm có thể kết hợp để suy ra điều gì, với đối thủ nào?|dat-class
data|Differential privacy và ngân sách riêng tư|Đơn vị bảo vệ, composition và utility tradeoff được định nghĩa ra sao trước khi chọn epsilon?|dat-egress
data|MPC và federated learning|Ai có thể collude, output vẫn tiết lộ gì, và protocol bảo vệ khâu nào?|dat-class
vulnerability|Disclosure và bug bounty|Scope, phối hợp vá, bằng chứng không gây hại và thời gian disclosure được quyết định thế nào?|vul-fix
detection|Threat intelligence|Indicator hết hạn khi nào, nguồn có độc lập không và intelligence có đổi quyết định thực tế không?|det-behavior
detection|Deception và honeypot|Ai có thể chạm honeypot hợp lệ, và tín hiệu phản ánh môi trường thật đến đâu?|det-base
response|Crisis communication|Ai được nói điều gì với mức chắc chắn nào khi scope sự cố còn chưa biết?|ir-learn
governance|Cyber insurance và economics|Hợp đồng chuyển loại tổn thất nào, còn incentive và correlated loss nào ở lại?|gov-loss
governance|Pháp luật và chứng nhận|Jurisdiction, loại dữ liệu, nghĩa vụ báo cáo và bằng chứng đáp ứng cụ thể là gì?|gov-owner
human|Insider và coercion|Quyền hợp lệ, động cơ, thiếu hỗ trợ và bị ép buộc tạo các giả thuyết phân biệt nào?|hum-report
human|Accessibility và security usability|Control loại người dùng nào khỏi dịch vụ, có phương án giữ assurance mà giảm loại trừ không?|id-recovery
thirdparty|Telecom, vệ tinh và hạ tầng quốc gia|Failure domain, đặc quyền vận hành và time horizon khác enterprise thông thường thế nào?|tp-concentration
ot|Thiết bị y tế và phương tiện|Safety case, vòng đời hỗ trợ và authority update thay đổi tiêu chí triển khai ra sao?|ot-safety
agents|Đầu độc model và data|Phân biệt training poisoning, retrieval poisoning và memory poisoning bằng cơ chế/observable nào?|ai-memory
agents|Model extraction và inference leakage|Ai truy cập output gì, budget truy vấn bao nhiêu, thiệt hại được định nghĩa thế nào?|dat-egress
agents|Agent nhiều bước và nhiều chủ thể|Authority có được cộng dồn sai khi output agent này làm input agent khác không?|ai-tool
agents|Chi phí, dừng và vòng lặp tự động|Retry, tool recursion, memory growth và budget exhaustion có stop condition nào ngoài model?|api-retry
'''.strip()
