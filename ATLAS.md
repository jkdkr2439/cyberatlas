# Cybersecurity — bản đồ cơ chế

Biên soạn cho Kevin T.N. · 2026-11-26

Đọc [METHOD.md](METHOD.md) để biết frame và mức bằng chứng; dùng [AGENTS.md](AGENTS.md) và graph.py để load/update node. Đây là tài liệu của seed import; graph/CURRENT mới là phiên bản dữ liệu hiện hành. Các test dưới đây là đề xuất, chưa chạy trên hệ thật.

**26 miền · 102 thẻ cơ chế · 8 hành trình · 32 frontier OPEN.** Số lượng chỉ mô tả artifact, không đo mức an toàn.

## Quản trị, trách nhiệm và quyết định

**Frame / owner:** Doanh nghiệp; hội đồng rủi ro và chủ dịch vụ. **Mục tiêu:** Quyết định có người chịu trách nhiệm và có giới hạn.

**Biến:** Khẩu vị rủi ro; quy mô; thời hạn; nghĩa vụ. **Nguồn lực:** Thẩm quyền; thời gian đánh giá; ngân sách sửa sai.

**Nguồn ý tưởng trong sách:** Phần 05 — Ontology rủi ro: Threat, Vulnerability, Likelihood, Impact, Risk, dòng 5510–6625. Tham chiếu bối cảnh: csf, measure.

### gov-owner — Trách nhiệm quyết định

**Điều kiện:** Nhiều nhóm cùng quản một dịch vụ.

- **I:** Finding và tác động dự kiến
- **P:** Gắn người có quyền chấp nhận hoặc yêu cầu sửa
- **O:** Quyết định có thời hạn
- **D:** Owner, lý do, ngày xem lại

**Hằng trong frame:** Không có rủi ro được bỏ mặc vì không thuộc nhóm nào.

**Đường hỏng:** Ticket chuyển vòng nhưng không ai quyết. **Điểm can thiệp:** Owner theo dịch vụ và escalation.

**Phép đo ứng viên:** Số quyết định quá hạn không owner / số quyết định đến hạn.

**Test phân biệt / bằng chứng cần:** Đổi owner nhân sự rồi kiểm tra việc bàn giao.

**Đánh đổi:** Thêm phê duyệt kéo dài thời gian sửa.

**OPEN:** Ai có quyền chấp nhận hậu quả vượt ngân sách của nhóm?

**Liên hệ có điều kiện:**

- `F24` — Jurisdiction, loại dữ liệu, nghĩa vụ báo cáo và bằng chứng đáp ứng cụ thể là gì?

### gov-exception — Ngoại lệ có hạn dùng

**Điều kiện:** Control không thể áp ngay.

- **I:** Yêu cầu miễn trừ và lý do
- **P:** Đánh giá phạm vi, bù trừ và ngày hết hạn
- **O:** Ngoại lệ được giới hạn
- **D:** Registry ngoại lệ và review

**Hằng trong frame:** Ngoại lệ không được âm thầm thành mặc định.

**Đường hỏng:** Gia hạn tự động che nợ rủi ro. **Điểm can thiệp:** Expiry, owner, kiểm tra control bù.

**Phép đo ứng viên:** Ngoại lệ hết hạn còn hiệu lực / ngoại lệ hết hạn.

**Test phân biệt / bằng chứng cần:** Cho ngoại lệ hết hạn trong lab; kiểm tra enforcement.

**Đánh đổi:** Chặn đột ngột có thể ngừng nghiệp vụ.

**OPEN:** Cơ chế rollback nào giữ cả an toàn lẫn tính liên tục?

**Liên hệ có điều kiện:**

- `cld-drift` — Ngoại lệ đã duyệt có hạn khác với drift không được phép.

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

**Nhánh nghiên cứu chưa mở đủ:**

- Cyber insurance và economics: Hợp đồng chuyển loại tổn thất nào, còn incentive và correlated loss nào ở lại?
- Pháp luật và chứng nhận: Jurisdiction, loại dữ liệu, nghĩa vụ báo cáo và bằng chứng đáp ứng cụ thể là gì?

## Tài sản và phụ thuộc

**Frame / owner:** Hạ tầng và SaaS; chủ tài sản. **Mục tiêu:** Biết đối tượng nào cần bảo vệ và nó phụ thuộc gì.

**Biến:** Tài sản ngắn hạn; shadow IT; mua bán doanh nghiệp. **Nguồn lực:** Đầu nối inventory; quyền đọc; người xác nhận owner.

**Nguồn ý tưởng trong sách:** Phần 01 — ONTOLOGY CỦA BẢO MẬT, dòng 30–469. Tham chiếu bối cảnh: csf.

### inv-discovery — Phát hiện tài sản bị bỏ sót

**Điều kiện:** Có cloud, SaaS và tài sản ngắn hạn.

- **I:** CMDB, billing, DNS, endpoint và cloud API
- **P:** Đối soát nhiều nguồn theo định danh
- **O:** Tài sản có owner hoặc chưa rõ
- **D:** Lịch sử xuất hiện và nguồn phát hiện

**Hằng trong frame:** Inventory phải ghi độ bao phủ chưa biết.

**Đường hỏng:** Chỉ quét dải mạng đã biết nên bỏ shadow IT. **Điểm can thiệp:** Nhiều nguồn độc lập; giữ unknown riêng.

**Phép đo ứng viên:** Tài sản đối soát có owner / tài sản trong hợp nguồn quan sát.

**Test phân biệt / bằng chứng cần:** Cài một tài sản thử trong scope nhưng ngoài CMDB.

**Đánh đổi:** Quét sâu tăng chi phí và dữ liệu nhạy cảm.

**OPEN:** Tài sản không để dấu ở mọi nguồn đang dùng còn loại nào?

**Liên hệ có điều kiện:**

- `tel-coverage` — Nguồn cần quan sát phải xuất phát từ inventory; thiếu inventory làm coverage bị phóng đại.

### inv-dependency — Phụ thuộc quan trọng

**Điều kiện:** Một dịch vụ chứa nhiều thành phần.

- **I:** Trace, cấu hình, hợp đồng, phỏng vấn owner
- **P:** Nối dịch vụ với identity, DNS, key và nhà cung cấp
- **O:** Đồ thị phụ thuộc có điều kiện
- **D:** Phiên bản cạnh và độ chắc chắn

**Hằng trong frame:** Phụ thuộc dự phòng cũng phải được ghi.

**Đường hỏng:** Chỉ lập danh sách server mà bỏ IdP. **Điểm can thiệp:** Diễn tập mất từng dependency và xác nhận đường dự phòng.

**Phép đo ứng viên:** Quan hệ quan trọng được kiểm thử / quan hệ quan trọng đã nhận diện.

**Test phân biệt / bằng chứng cần:** Ngắt IdP trong lab dù app server còn khỏe.

**Đánh đổi:** Traces đầy đủ tăng chi phí và rủi ro riêng tư.

**OPEN:** Phụ thuộc nào chỉ xuất hiện vào kỳ quyết toán?

**Liên hệ có điều kiện:**

- `rec-objective` — RTO đầu cuối phụ thuộc các dịch vụ nền, không chỉ database.

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

## Kiến trúc và ranh giới tin cậy

**Frame / owner:** Dịch vụ phân tán; kiến trúc sư. **Mục tiêu:** Sai lệch không được tự do lan sang miền khác.

**Biến:** Tenant; đường mạng; failover; vị trí enforcement. **Nguồn lực:** Sơ đồ thực tế; test môi trường; năng lực vận hành.

**Nguồn ý tưởng trong sách:** Phần 06 — Zero Trust: ontology của quyền và niềm tin, dòng 6626–7585. Tham chiếu bối cảnh: zt.

### arch-boundary — Ranh giới tin cậy

**Điều kiện:** Dữ liệu đi qua chủ thể hoặc miền quản trị.

- **I:** Yêu cầu từ nguồn khác trust level
- **P:** Xác thực nguồn, schema và quyền tại điểm chuyển
- **O:** Đầu vào được giảm quyền và gắn nguồn
- **D:** Decision log và nhãn nguồn

**Hằng trong frame:** Vị trí nội bộ không tự cấp lòng tin.

**Đường hỏng:** Proxy hoặc service nâng dữ liệu thành quyền. **Điểm can thiệp:** Enforcement ở boundary; fail policy tường minh.

**Phép đo ứng viên:** Luồng qua boundary có quyết định được kiểm tra / luồng đã lập bản đồ.

**Test phân biệt / bằng chứng cần:** Cho request nội bộ mang danh tính không hợp lệ.

**Đánh đổi:** Nhiều điểm kiểm tăng độ trễ và chi phí quản trị.

**OPEN:** Boundary nào bị bypass bằng đường quản trị?

**Liên hệ có điều kiện:**

- `ai-instruction` — Nội dung từ miền thấp trust bị nâng thành quyền ở boundary.

### arch-blast — Phạm vi lan truyền

**Điều kiện:** Một principal hoặc workload bị chiếm.

- **I:** Đồ thị quyền và đường kết nối
- **P:** Tìm tài sản nhạy cảm còn reachable theo điều kiện
- **O:** Tập tài sản có thể bị ảnh hưởng
- **D:** Snapshot quyền và đường đi

**Hằng trong frame:** Một control chỉ giới hạn những đường nó thực sự cắt.

**Đường hỏng:** Phân mạng nhưng cùng admin và backup credential. **Điểm can thiệp:** Tách authority, segment, giảm quyền liên miền.

**Phép đo ứng viên:** Số tài sản quan trọng reachable từ principal thử; báo cả giả định.

**Test phân biệt / bằng chứng cần:** Bỏ một cạnh quyền, tính lại phạm vi lan truyền.

**Đánh đổi:** Cô lập mạnh tăng gánh vận hành và recovery.

**OPEN:** Đường gián tiếp qua CI hoặc support có được mô hình hóa?

**Liên hệ có điều kiện:**

- `cld-policy` — Phạm vi lan truyền chịu quyền sửa/cấp quyền của control plane.

### arch-failure — Fail-open và fail-closed

**Điều kiện:** Policy service mất kết nối.

- **I:** Yêu cầu mới và timeout
- **P:** Chọn hành vi theo mức nguy hại của thao tác
- **O:** Cho phép, từ chối hoặc giới hạn chức năng
- **D:** Lý do fallback và thời gian

**Hằng trong frame:** Chế độ lỗi là quyết định thiết kế có mục tiêu.

**Đường hỏng:** Timeout vô tình bỏ xác thực. **Điểm can thiệp:** Fallback riêng cho read/write và emergency path.

**Phép đo ứng viên:** Yêu cầu được cho phép ngoài chính sách khi dependency lỗi / yêu cầu thử.

**Test phân biệt / bằng chứng cần:** Gây timeout ở lab rồi thử thao tác mức rủi ro khác nhau.

**Đánh đổi:** Fail-closed có thể gây outage; fail-open tăng phơi nhiễm.

**OPEN:** Grace period nào phù hợp từng dữ liệu và đối tượng?

**Liên hệ có điều kiện:**

- `k8s-admission` — Webhook timeout cần policy lỗi rõ ràng.

## Danh tính và xác thực

**Frame / owner:** Con người và workload; IAM team. **Mục tiêu:** Gắn yêu cầu với đúng chủ thể trong mức bảo đảm đã chọn.

**Biến:** Authenticator; mất thiết bị; federation; tài khoản máy. **Nguồn lực:** IdP; quy trình hỗ trợ; thiết bị; khả năng thu hồi.

**Nguồn ý tưởng trong sách:** Phần 06 — Zero Trust: ontology của quyền và niềm tin, dòng 6626–7585. Tham chiếu bối cảnh: identity.

### id-proof — Gắn tài khoản với chủ thể

**Điều kiện:** Tạo hoặc liên kết tài khoản.

- **I:** Bằng chứng định danh và yêu cầu đăng ký
- **P:** Kiểm tra mức đảm bảo tương ứng mục tiêu
- **O:** Binding tài khoản-chủ thể
- **D:** Nguồn bằng chứng và vòng đời binding

**Hằng trong frame:** Đăng ký và đăng nhập là hai phép kiểm khác nhau.

**Đường hỏng:** Authenticator tốt gắn vào sai người. **Điểm can thiệp:** Proofing theo rủi ro; chống trùng và review ngoại lệ.

**Phép đo ứng viên:** Binding sai trong mẫu đã xác minh / mẫu có ground truth.

**Test phân biệt / bằng chứng cần:** Đưa trường hợp đồng tên hoặc đổi chủ tài khoản.

**Đánh đổi:** Thu thập thêm định danh gây chi phí riêng tư.

**OPEN:** Mức đảm bảo nào thật sự cần, có thể dùng pseudonym không?

**Liên hệ có điều kiện:**

- `id-recovery` — Recovery tạo binding mới nên không được quên mức đảm bảo cần thiết.

### id-mfa — MFA và chống phishing

**Điều kiện:** Luồng đăng nhập có nhiều cách xác thực.

- **I:** Challenge và phản hồi authenticator
- **P:** Kiểm chứng yếu tố và binding với đúng verifier
- **O:** Kết quả xác thực theo phương thức
- **D:** Auth method, origin và kết quả

**Hằng trong frame:** Không đánh đồng mọi MFA với chống phishing.

**Đường hỏng:** OTP bị relay; fallback yếu hơn chính luồng. **Điểm can thiệp:** Chọn protocol phù hợp và rà mọi đường fallback.

**Phép đo ứng viên:** Luồng nhạy cảm dùng phương thức đạt yêu cầu / luồng nhạy cảm quan sát.

**Test phân biệt / bằng chứng cần:** So sánh luồng chính và luồng fallback trong test được phép.

**Đánh đổi:** Thiết bị và hỗ trợ recovery ảnh hưởng khả dụng.

**OPEN:** Passkey sync và custody phù hợp đối tượng nào?

**Liên hệ có điều kiện:**

- `id-recovery` — Fallback yếu có thể làm luồng xác thực mạnh mất hiệu quả toàn hành trình.
- `ses-revoke` — Chống phishing lúc login không giải quyết mọi phiên bị lộ sau đó.

### id-recovery — Khôi phục tài khoản

**Điều kiện:** Người dùng mất authenticator.

- **I:** Yêu cầu recovery, bằng chứng phụ
- **P:** Xác minh lại, giới hạn thay đổi và thông báo
- **O:** Authenticator mới hoặc từ chối
- **D:** Chuỗi bằng chứng và hành động support

**Hằng trong frame:** Recovery không được bỏ yêu cầu đảm bảo đã cam kết.

**Đường hỏng:** Helpdesk bị thuyết phục thay MFA không đủ căn cứ. **Điểm can thiệp:** Recovery có phân quyền, cooldown theo rủi ro, audit.

**Phép đo ứng viên:** Recovery sai được chấp nhận / tình huống sai trong bộ test.

**Test phân biệt / bằng chứng cần:** Đưa bằng chứng đúng tên nhưng không đủ quyền sở hữu.

**Đánh đổi:** Siết quá chặt khóa người dùng hợp lệ.

**OPEN:** Người dùng không còn bất kỳ thiết bị nào được hỗ trợ ra sao?

**Liên hệ có điều kiện:**

- `F26` — Control loại người dùng nào khỏi dịch vụ, có phương án giữ assurance mà giảm loại trừ không?

## Phiên và vòng đời quyền

**Frame / owner:** Ứng dụng sau đăng nhập; IAM và app owner. **Mục tiêu:** Quyền không tồn tại vượt điều kiện được cấp.

**Biến:** TTL; cache; offline; refresh token; nhiều vùng. **Nguồn lực:** Kho phiên; đồng hồ; kênh invalidation; telemetry.

**Nguồn ý tưởng trong sách:** Phần 06 — Zero Trust: ontology của quyền và niềm tin, dòng 6626–7585. Tham chiếu bối cảnh: identity.

### ses-issue — Phát hành token đúng đối tượng

**Điều kiện:** Một IdP phục vụ nhiều ứng dụng.

- **I:** Auth result và requested audience
- **P:** Phát hành token ràng buộc issuer, audience và scope
- **O:** Token được ứng dụng đích chấp nhận đúng phạm vi
- **D:** Issuance metadata và key version

**Hằng trong frame:** Token hợp lệ mật mã chưa chắc đúng dịch vụ.

**Đường hỏng:** Chấp nhận token của audience khác. **Điểm can thiệp:** Xác minh claims và thuật toán theo allowlist.

**Phép đo ứng viên:** Token sai audience bị nhận / token sai audience đã thử.

**Test phân biệt / bằng chứng cần:** Đổi riêng audience, giữ chữ ký hợp lệ trong lab.

**Đánh đổi:** Nhiều kiểu token tăng độ phức tạp tương thích.

**OPEN:** Token exchange có làm nở quyền qua chuỗi không?

**Liên hệ có điều kiện:**

- `k8s-identity` — Audience/subject sai có thể làm token workload dùng vượt mục đích.

### ses-revoke — Thu hồi quyền có độ trễ

**Điều kiện:** Đổi role, nghỉ việc hoặc lộ token.

- **I:** Sự kiện revoke và các token/cache đang tồn tại
- **P:** Lan truyền thu hồi hoặc chờ expiry theo thiết kế
- **O:** Hành động cũ bị từ chối ở các điểm enforcement
- **D:** Thời điểm revoke và lần cho phép cuối

**Hằng trong frame:** Thu hồi tại IdP chưa chứng minh thu hồi toàn hệ.

**Đường hỏng:** Access token tự chứa và cache quyền vẫn dùng được. **Điểm can thiệp:** TTL, introspection, revocation và test đa vùng.

**Phép đo ứng viên:** Phân bố độ trễ từ revoke đến deny; ca chưa deny là censored.

**Test phân biệt / bằng chứng cần:** Thử cả access, refresh và đường offline sau revoke.

**Đánh đổi:** Thu hồi tức thời cần phụ thuộc online và tải thêm.

**OPEN:** Bound tối đa nào được bảo đảm khi mất mạng?

**Liên hệ có điều kiện:**

- `hum-offboard` — Offboarding chỉ xong khi quyền hiệu lực không còn ở các điểm dùng.

### ses-concurrency — Phiên, logout và thiết bị

**Điều kiện:** Một người có nhiều phiên.

- **I:** Logout, đổi mật khẩu, đăng nhập mới
- **P:** Áp chính sách hủy phiên theo thiết bị và rủi ro
- **O:** Tập phiên còn hợp lệ được giải thích
- **D:** Session inventory và lý do kết thúc

**Hằng trong frame:** Đóng giao diện không đồng nghĩa kết thúc phiên server.

**Đường hỏng:** Cookie còn dùng được sau logout. **Điểm can thiệp:** Hủy phiên phía server và kiểm tra replay an toàn.

**Phép đo ứng viên:** Phiên thuộc diện hủy còn dùng được / phiên đã thử.

**Test phân biệt / bằng chứng cần:** Logout một thiết bị rồi kiểm tra chính sách trên thiết bị khác.

**Đánh đổi:** Hủy toàn bộ dễ gián đoạn công việc.

**OPEN:** Khi nào cần step-up thay vì hủy phiên?

**Liên hệ có điều kiện:**

- `ir-contain` — Containment account cần xử lý toàn bộ phiên thuộc scope.

### revoke-fanout — Tập consumer của một lần thu hồi

**Điều kiện:** Quyền dùng ở nhiều service/region.

- **I:** Revoke event và authority graph
- **P:** Resolve toàn bộ điểm dùng quyền và đánh dấu acknowledgment
- **O:** Consumer đã cập nhật hoặc chưa rõ
- **D:** Event version, consumer list, ack times

**Hằng trong frame:** Ack của authority không thay ack của consumer.

**Đường hỏng:** Một vùng không nhận sự kiện nhưng batch được báo done. **Điểm can thiệp:** Fanout registry và reconciliation pull.

**Phép đo ứng viên:** Consumer chưa xác nhận / consumer thuộc scope.

**Test phân biệt / bằng chứng cần:** Bỏ một consumer khỏi đường push nhưng giữ trong registry.

**Đánh đổi:** Registry consumer cần bảo trì.

**OPEN:** Consumer được tạo sau revoke nhận state từ đâu?

### revoke-cache — Cache của quyết định phân quyền

**Điều kiện:** Quyết định được cache để giảm latency.

- **I:** Principal, resource, action và policy version
- **P:** Dùng cache chỉ khi key và freshness còn đúng
- **O:** Quyết định theo phiên bản quyền phù hợp
- **D:** Cache key, version, expiry và hit path

**Hằng trong frame:** Cache hợp lệ theo thời gian chưa chắc hợp lệ theo quyền mới.

**Đường hỏng:** Entry còn TTL nhưng policy đã đổi. **Điểm can thiệp:** Versioned cache key và invalidation.

**Phép đo ứng viên:** Cache hit dùng version cũ sau revoke / hits được kiểm.

**Test phân biệt / bằng chứng cần:** Đổi policy khi entry chưa hết TTL.

**Đánh đổi:** Freshness chặt tăng tải policy service.

**OPEN:** Cache âm và cache allow có cùng semantics không?

### revoke-version — Đơn điệu của phiên bản quyền

**Điều kiện:** State từ nhiều replica đến không theo thứ tự.

- **I:** Quyền cũ/mới kèm epoch
- **P:** Không cho cập nhật epoch thấp thay epoch cao
- **O:** State consumer không đi lùi
- **D:** Applied epoch và discarded events

**Hằng trong frame:** Một event đến muộn không được hồi sinh quyền cũ.

**Đường hỏng:** Arrival order bị coi là authority order. **Điểm can thiệp:** Monotonic epoch với nguồn authority rõ.

**Phép đo ứng viên:** Lần state đi lùi / update sequence thử.

**Test phân biệt / bằng chứng cần:** Phát revoke mới trước rồi phát event cũ sau.

**Đánh đổi:** Epoch ordering giữa nhiều authority cần thiết kế.

**OPEN:** Hợp nhất nhiều nguồn quyền có một thứ tự toàn phần không?

### revoke-race — Race giữa đọc quyền và ghi cache

**Điều kiện:** Request đang chạy khi revoke commit.

- **I:** Read cũ, revoke mới, cache write muộn
- **P:** Ràng write-back với version còn hiệu lực
- **O:** Cache không giữ allow đã lỗi thời
- **D:** Timeline read/check/write và version

**Hằng trong frame:** Kiểm freshness trước process chưa đủ cho write-back.

**Đường hỏng:** Request đọc allow cũ rồi ghi đè deny mới. **Điểm can thiệp:** Commit-time version guard.

**Phép đo ứng viên:** Write-back cũ được nhận / lịch race thử.

**Test phân biệt / bằng chứng cần:** Dùng barrier ép thứ tự read-old → revoke → write-old.

**Đánh đổi:** Đồng bộ hóa tăng latency và contention.

**OPEN:** Library cache có hỗ trợ conditional write không?

### revoke-cas — Conditional write ở điểm commit

**Điều kiện:** Cache/store có compare-and-set hoặc transaction.

- **I:** Expected version và new entry
- **P:** Commit chỉ khi authority epoch khớp precondition
- **O:** Write bị từ chối nếu context đã đổi
- **D:** Expected/current version và CAS outcome

**Hằng trong frame:** Phải so với đúng authority version, không chỉ entry-local version.

**Đường hỏng:** CAS đúng cú pháp nhưng so sai object/version. **Điểm can thiệp:** Version binding và retry có đọc lại authority.

**Phép đo ứng viên:** Stale commit được chấp nhận / stale-epoch fixtures.

**Test phân biệt / bằng chứng cần:** Giữ cache-entry version nhưng tăng policy epoch.

**Đánh đổi:** Retry storm dưới churn quyền.

**OPEN:** Khi authority không reachable thì commit được phép không?

### revoke-offline — Quyền sử dụng khi consumer offline

**Điều kiện:** Consumer không liên lạc được authority.

- **I:** Credential cũ, local clock và cached policy
- **P:** Thực thi grace/expiry theo contract đã duyệt
- **O:** Quyền dừng tại bound hoặc dịch vụ bị giới hạn
- **D:** Offline interval, clock bounds, last sync

**Hằng trong frame:** Không hứa thu hồi tức thời nếu không có kênh state.

**Đường hỏng:** Local clock lệch hoặc token không expiry. **Điểm can thiệp:** Bounded offline lease và chức năng dự phòng.

**Phép đo ứng viên:** Khoảng sử dụng quyền sau revoke theo clock uncertainty.

**Test phân biệt / bằng chứng cần:** Ngắt mạng, dịch đồng hồ lab trong giới hạn test.

**Đánh đổi:** Lease ngắn làm giảm khả dụng.

**OPEN:** Thiết bị offline bắt buộc dùng lâu có cơ chế trust khác không?

## Phân quyền và tenant

**Frame / owner:** API và kho dữ liệu; chủ sản phẩm. **Mục tiêu:** Chủ thể chỉ tác động đúng đối tượng và hành động được phép.

**Biến:** Role; thuộc tính; ownership; tenant; thời điểm commit. **Nguồn lực:** Policy engine; test matrix; owner dữ liệu.

**Nguồn ý tưởng trong sách:** Phần 03 — IPOD của bảo mật: Input, Process, Output, Data, dòng 1604–3533. Tham chiếu bối cảnh: api, asvs.

### auth-object — Quyền ở cấp đối tượng

**Điều kiện:** API xử lý ID của nhiều người/tenant.

- **I:** Principal, object ID và action
- **P:** Đối chiếu quyền với object thực ở server
- **O:** Dữ liệu hoặc thay đổi đúng người
- **D:** Principal-object-tenant decision log

**Hằng trong frame:** Biết ID không đồng nghĩa sở hữu đối tượng.

**Đường hỏng:** Chỉ kiểm đăng nhập; truy vấn thiếu tenant. **Điểm can thiệp:** Check object-level ở mọi đường đọc/ghi.

**Phép đo ứng viên:** Yêu cầu cross-tenant được phép / yêu cầu cross-tenant trong test.

**Test phân biệt / bằng chứng cần:** Đổi object ID, giữ login hợp lệ và kiểm tra cả async export.

**Đánh đổi:** Tập test tăng theo role, action, tenant.

**OPEN:** Chia sẻ hợp lệ và chuyển owner làm thay đổi luật thế nào?

**Liên hệ có điều kiện:**

- `dat-egress` — Export cũng phải kiểm quyền đối tượng và quyền xuất dữ liệu.

### auth-policy — Quyền hiệu lực

**Điều kiện:** Nhiều role và policy chồng nhau.

- **I:** Membership, resource policy và context
- **P:** Kết hợp luật theo precedence đã định
- **O:** Effective permissions
- **D:** Policy version và quyết định

**Hằng trong frame:** Quyền phải được xét sau mọi phép kế thừa.

**Đường hỏng:** Deny trong một lớp bị allow ở lớp khác hiểu sai. **Điểm can thiệp:** Policy simulation và test precedence.

**Phép đo ứng viên:** Đường quyền vượt intent / đường được kiểm thử.

**Test phân biệt / bằng chứng cần:** Kết hợp hai role riêng lẻ ít quyền nhưng hợp lại nguy hiểm.

**Đánh đổi:** Mô hình biểu đạt mạnh khó giải thích và bảo trì.

**OPEN:** Đường quyền nào phụ thuộc thuộc tính đã cũ?

**Liên hệ có điều kiện:**

- `cld-policy` — Quyền hiệu lực phụ thuộc kết hợp policy và đường cấp quyền.

### auth-race — Quyền tại thời điểm commit

**Điều kiện:** Ownership thay đổi khi tác vụ đang chạy.

- **I:** Yêu cầu được duyệt trước và trạng thái mới
- **P:** Kiểm tra lại điều kiện cùng giao dịch thay đổi
- **O:** Commit hợp lệ hoặc rollback
- **D:** Version, lock hoặc precondition record

**Hằng trong frame:** Quyền tại đầu request không bảo đảm quyền lúc ghi.

**Đường hỏng:** TOCTOU giữa authorize và update. **Điểm can thiệp:** Atomic check-and-act hoặc version precondition.

**Phép đo ứng viên:** Commit trái quyền sau biến đổi trạng thái / test race.

**Test phân biệt / bằng chứng cần:** Đổi owner giữa check và commit trong môi trường test.

**Đánh đổi:** Khóa và retry ảnh hưởng throughput.

**OPEN:** Job dài và event queue giữ authority theo mốc nào?

**Liên hệ có điều kiện:**

- `ai-tool` — Trạng thái sau approval có thể khác trạng thái khi thực thi.

### tenant-context — Nguồn authority của tenant context

**Điều kiện:** Client gửi tenant_id hoặc chọn workspace.

- **I:** Session binding, route và client tenant claim
- **P:** Chỉ dùng tenant context đã được quyền lựa chọn
- **O:** Context server được xác nhận
- **D:** Claim source và decision

**Hằng trong frame:** Tên tenant do client đưa không tự tạo membership.

**Đường hỏng:** Header tenant được tin vì request đã login. **Điểm can thiệp:** Resolve membership server-side.

**Phép đo ứng viên:** Context trái membership được chấp nhận / ca thử.

**Test phân biệt / bằng chứng cần:** Đổi header tenant, giữ token hợp lệ của tenant khác.

**Đánh đổi:** Membership lookup thêm dependency.

**OPEN:** Delegation và shared workspace được mô hình hóa ra sao?

### tenant-cache — Cache key và chiều phân quyền

**Điều kiện:** Cache dùng chung response giữa request.

- **I:** Object local ID, tenant, role và policy epoch
- **P:** Tách cache theo các chiều làm thay đổi output/permission
- **O:** Không dùng response của người này cho người khác
- **D:** Key schema và source authorization

**Hằng trong frame:** Cùng object ID không có nghĩa cùng object xuyên tenant.

**Đường hỏng:** Key chỉ có path/ID; response chứa field theo role. **Điểm can thiệp:** Include security-relevant dimensions hoặc tránh cache output nhạy cảm.

**Phép đo ứng viên:** Cross-scope cache hits trả sai / paired tests.

**Test phân biệt / bằng chứng cần:** Hai tenant cùng local ID; hai role khác field quyền.

**Đánh đổi:** Thêm chiều key giảm hit rate.

**OPEN:** Revocation field-level có yêu cầu invalidation gì?

### tenant-job — Authority qua hàng đợi

**Điều kiện:** Request được xử lý sau khi người dùng đổi quyền.

- **I:** Job payload và requester context
- **P:** Mang capability có scope hoặc reauthorize lúc chạy
- **O:** Job chỉ xử lý phạm vi được cho phép
- **D:** Requester, purpose, epoch và expiry

**Hằng trong frame:** Ambient service-admin không được thay quyền requester một cách ngầm định.

**Đường hỏng:** Worker bỏ tenant context vì có quyền toàn DB. **Điểm can thiệp:** Explicit job authority contract.

**Phép đo ứng viên:** Job trái scope được chạy / negative job fixtures.

**Test phân biệt / bằng chứng cần:** Gửi job rồi revoke quyền trước worker nhận.

**Đánh đổi:** Recheck làm job phụ thuộc policy online.

**OPEN:** Job dài đã làm nửa chừng khi quyền đổi phải xử lý sao?

### tenant-snapshot — Snapshot quyền hay quyền tại thời điểm chạy

**Điều kiện:** Nghiệp vụ có độ trễ đáng kể.

- **I:** Quyền lúc gửi và quyền hiện tại
- **P:** Chọn mốc authority theo ý nghĩa giao dịch, ghi rõ
- **O:** Quyết định nhất quán với contract nghiệp vụ
- **D:** Policy time semantics và consent record

**Hằng trong frame:** Không chọn mốc thời gian tùy tiện để làm request pass.

**Đường hỏng:** Dùng snapshot cho mọi thao tác dù consent đã rút. **Điểm can thiệp:** Per-action authority-time policy.

**Phép đo ứng viên:** Job dùng sai epoch-policy / case có đổi quyền.

**Test phân biệt / bằng chứng cần:** Cùng revoke nhưng phân biệt giao dịch đã cam kết với export chưa chạy.

**Đánh đổi:** Snapshot hỗ trợ ổn định nhưng kéo dài authority.

**OPEN:** Đồng ý đã rút có hiệu lực với nghĩa vụ pháp lý nào?

### tenant-delivery — Quyền nhận kết quả sau khi job hoàn thành

**Điều kiện:** Report xuất ra file/link/email.

- **I:** Output object, người nhận và thời điểm tải
- **P:** Kiểm output ACL, destination và thời hạn truy cập
- **O:** Kết quả chỉ được đúng người lấy
- **D:** Delivery log, recipient và ACL version

**Hằng trong frame:** Quyền tạo report không thay kiểm quyền tải report.

**Đường hỏng:** Link chung hoặc bucket policy làm lộ export. **Điểm can thiệp:** Scoped delivery và recheck theo policy.

**Phép đo ứng viên:** Tải output trái scope thành công / download tests.

**Test phân biệt / bằng chứng cần:** Người khác tenant dùng link từ job hợp lệ.

**Đánh đổi:** Hạn dùng ngắn tăng yêu cầu chạy lại report.

**OPEN:** Link đã được tải/copy ra ngoài còn kiểm soát được gì?

## Mật mã và vòng đời khóa

**Frame / owner:** Dữ liệu lưu và truyền; PKI/KMS owner. **Mục tiêu:** Bí mật và toàn vẹn theo mô hình đối thủ cụ thể.

**Biến:** Thuật toán; khóa; nonce; chứng thư; thời hạn bí mật. **Nguồn lực:** KMS/HSM; backup khóa; năng lực chuyển đổi.

**Nguồn ý tưởng trong sách:** Phần 08 — Data ontology cho agent bảo mật, dòng 8536–10085. Tham chiếu bối cảnh: asvs.

### cry-key — Vòng đời khóa

**Điều kiện:** Khóa dùng cho nhiều tài sản.

- **I:** Generate, distribute, rotate, revoke, destroy
- **P:** Ràng quyền sử dụng với mục đích và vòng đời
- **O:** Khóa hoạt động trong phạm vi cho phép
- **D:** Key inventory, audit và dependency

**Hằng trong frame:** Xóa khóa có thể đồng thời phá khả năng recovery.

**Đường hỏng:** Backup có ciphertext nhưng không còn key. **Điểm can thiệp:** Custody riêng, rotation có kiểm thử khôi phục.

**Phép đo ứng viên:** Tài sản mã hóa có key recovery được thử / tài sản cần recovery.

**Test phân biệt / bằng chứng cần:** Khôi phục backup sau một lần rotation.

**Đánh đổi:** Khóa dự phòng thêm bề mặt truy cập.

**OPEN:** Cryptographic erasure có bao phủ mọi bản sao khóa không?

**Liên hệ có điều kiện:**

- `rec-backup` — Backup mã hóa chỉ dùng được khi khôi phục đúng khóa.
- `F02` — Attestation xác nhận binary/config nào, ai cung cấp freshness và ai được giải phóng secret?

### cry-integrity — Mã hóa và xác thực dữ liệu

**Điều kiện:** Dữ liệu cần bí mật lẫn toàn vẹn.

- **I:** Plaintext, key, nonce và context
- **P:** Dùng primitive được thẩm định đúng điều kiện
- **O:** Ciphertext và kiểm tra integrity
- **D:** Key/nonce metadata theo thiết kế

**Hằng trong frame:** Bí mật không tự suy ra toàn vẹn hay đúng người gửi.

**Đường hỏng:** Nonce reuse hoặc bỏ kiểm tra tag. **Điểm can thiệp:** Thư viện chuẩn; quản nonce; bind context.

**Phép đo ứng viên:** Vi phạm uniqueness nonce theo key / thao tác có kiểm kê.

**Test phân biệt / bằng chứng cần:** Thử đổi ciphertext/context và yêu cầu từ chối.

**Đánh đổi:** Lưu metadata và xoay khóa có chi phí.

**OPEN:** Randomness, restart và nhiều node có làm trùng nonce?

**Liên hệ có điều kiện:**

- `tel-integrity` — Integrity sau ghi không chứng minh event ban đầu là sự thật.
- `F01` — Đối thủ quan sát timing/power/cache trong mô hình truy cập nào, và control có tác dụng ở lớp nào?

### cry-agility — Chuyển đổi mật mã

**Điều kiện:** Thuật toán, chứng thư hoặc key policy đổi.

- **I:** Inventory crypto và hạn bí mật dữ liệu
- **P:** Lập lộ trình thay đổi theo dependency
- **O:** Dịch vụ tương thích và dữ liệu còn đọc được
- **D:** Phiên bản protocol và migration result

**Hằng trong frame:** Đổi thuật toán không chỉ là sửa một tên cấu hình.

**Đường hỏng:** Client cũ buộc downgrade hoặc mất kết nối. **Điểm can thiệp:** Inventory, negotiation policy, staged migration.

**Phép đo ứng viên:** Dependency crypto đã thử migration / dependency nhận diện.

**Test phân biệt / bằng chứng cần:** Chặn thuật toán cũ trong lab có client legacy.

**Đánh đổi:** Tương thích và chi phí phần cứng.

**OPEN:** Dữ liệu giữ bí mật dài hạn cần lộ trình hậu lượng tử nào?

**Liên hệ có điều kiện:**

- `inv-dependency` — Migration cần biết mọi consumer và protocol bị ảnh hưởng.
- `F03` — Inventory dữ liệu bí mật dài hạn và protocol hybrid cần cách đo migration/compatibility nào?

**Nhánh nghiên cứu chưa mở đủ:**

- Side-channel và hardware root of trust: Đối thủ quan sát timing/power/cache trong mô hình truy cập nào, và control có tác dụng ở lớp nào?
- Confidential computing và attestation: Attestation xác nhận binary/config nào, ai cung cấp freshness và ai được giải phóng secret?
- Mật mã hậu lượng tử: Inventory dữ liệu bí mật dài hạn và protocol hybrid cần cách đo migration/compatibility nào?

## Mạng, phân vùng và egress

**Frame / owner:** Lưu lượng giữa dịch vụ; network team. **Mục tiêu:** Đường kết nối chỉ mở cho quan hệ có chủ đích.

**Biến:** DNS; route; IPv6; proxy; lưu lượng mã hóa. **Nguồn lực:** Thiết bị mạng; bản đồ luồng; năng lực lọc.

**Nguồn ý tưởng trong sách:** Phần 06 — Zero Trust: ontology của quyền và niềm tin, dòng 6626–7585. Tham chiếu bối cảnh: zt.

### net-segment — Phân vùng thực sự

**Điều kiện:** Một workload bị compromise.

- **I:** Source identity, destination và port/protocol
- **P:** Thực thi policy tại đường đi thật
- **O:** Kết nối cần thiết qua; kết nối khác bị chặn
- **D:** Policy và thử nghiệm connectivity

**Hằng trong frame:** Có VLAN không chứng minh cắt đường authority.

**Đường hỏng:** Đường quản trị hoặc IPv6 đi vòng. **Điểm can thiệp:** Deny-by-default theo luồng hợp lệ đã quan sát.

**Phép đo ứng viên:** Đường cấm còn kết nối / đường cấm đã thử.

**Test phân biệt / bằng chứng cần:** Thử route dự phòng, IPv6 và management plane.

**Đánh đổi:** Chặn nhầm ảnh hưởng dịch vụ và debug.

**OPEN:** Lưu lượng phát sinh theo mùa có được đưa vào model?

**Liên hệ có điều kiện:**

- `ot-legacy` — Cắt đường tiếp cận hỗ trợ thiết bị khó vá; không sửa lỗi nội tại.
- `F04` — Trust boundary thay khi kênh truyền dùng chung môi trường vật lý ra sao?

### net-egress — Kiểm soát đường ra

**Điều kiện:** Service cần gọi tài nguyên ngoài.

- **I:** Destination, DNS result và request context
- **P:** Xác minh đích ở thời điểm kết nối
- **O:** Kết nối đúng đích hoặc bị chặn
- **D:** Destination resolved, decision, byte counts

**Hằng trong frame:** Allowlist tên không đủ nếu địa chỉ/redirect đổi.

**Đường hỏng:** SSRF đi qua redirect hoặc DNS thay đổi. **Điểm can thiệp:** Kiểm tra từng hop, egress policy và quyền workload.

**Phép đo ứng viên:** Đích cấm reachable / ca thử đích cấm theo chính sách.

**Test phân biệt / bằng chứng cần:** Dùng đích mô phỏng đổi resolution/redirect trong lab.

**Đánh đổi:** Egress proxy tạo choke point và chi phí.

**OPEN:** Metadata service và dịch vụ nội bộ nào cần bảo vệ riêng?

**Liên hệ có điều kiện:**

- `ai-tool` — Tool outbound cần destination policy ngoài quyết định model.

### net-dos — Cạn tài nguyên và DDoS

**Điều kiện:** Traffic vượt capacity hoặc cost budget.

- **I:** Request volume, size, thời gian xử lý
- **P:** Admission, quota và phân phối tài nguyên
- **O:** Dịch vụ ưu tiên còn hoạt động
- **D:** Queue, latency, drops, bill

**Hằng trong frame:** Rate theo IP không đại diện chi phí xử lý.

**Đường hỏng:** Ít request đắt làm cạn worker. **Điểm can thiệp:** Budget theo chi phí và tenant; upstream protection.

**Phép đo ứng viên:** Throughput hợp lệ và tail latency dưới tải đã mô tả.

**Test phân biệt / bằng chứng cần:** Giữ request count, đổi workload sang loại đắt.

**Đánh đổi:** Chống abuse có thể chặn người dùng chung IP.

**OPEN:** Phụ thuộc upstream giới hạn nào không do mình điều khiển?

**Liên hệ có điều kiện:**

- `api-abuse` — Request hợp lệ vẫn có thể cạn tài nguyên và ngân sách.

**Nhánh nghiên cứu chưa mở đủ:**

- Wi-Fi, Bluetooth và mạng không dây: Trust boundary thay khi kênh truyền dùng chung môi trường vật lý ra sao?
- Định tuyến liên miền và BGP: Sai lệch route đến từ cấu hình, authority hay compromise; nguồn nào đủ độc lập để nhận biết?

## Email, DNS và thông điệp

**Frame / owner:** Tên miền và hộp thư; IT/messaging. **Mục tiêu:** Thông điệp không tự trở thành bằng chứng thẩm quyền.

**Biến:** Forwarding; alias; dịch vụ gửi ngoài; tên gần giống. **Nguồn lực:** DNS control; mail gateway; kênh xác minh độc lập.

**Nguồn ý tưởng trong sách:** Phần 02 — Cơ chế gốc: hằng và biến trong bảo mật, dòng 470–1603. Tham chiếu bối cảnh: csf.

### msg-domain — Xác thực miền gửi

**Điều kiện:** Nhiều dịch vụ gửi email.

- **I:** Envelope, headers, chữ ký và DNS policy
- **P:** Kiểm tra cơ chế xác thực/alignment được cấu hình
- **O:** Tín hiệu xác thực miền
- **D:** Authentication results và thay đổi DNS

**Hằng trong frame:** Miền gửi xác thực không bảo đảm nội dung lương thiện.

**Đường hỏng:** Account thật bị chiếm; lookalike domain hợp lệ. **Điểm can thiệp:** Domain policy kết hợp nội dung và xác minh giao dịch.

**Phép đo ứng viên:** Nguồn gửi hợp lệ sai alignment / nguồn gửi được kiểm thử.

**Test phân biệt / bằng chứng cần:** Thử forwarding và dịch vụ marketing được cho phép.

**Đánh đổi:** Siết policy có thể mất thư hợp lệ.

**OPEN:** Danh sách toàn bộ bên gửi thay mặt tổ chức đã đầy đủ chưa?

**Liên hệ có điều kiện:**

- `msg-payment` — Email từ domain xác thực không chứng minh yêu cầu chuyển tiền hợp lệ.

### msg-payment — Thay đổi tài khoản thanh toán

**Điều kiện:** Email yêu cầu chuyển tiền/đổi beneficiary.

- **I:** Yêu cầu và thông tin người gửi
- **P:** Xác nhận bằng kênh độc lập đã biết
- **O:** Thay đổi có kiểm soát
- **D:** Bằng chứng xác nhận và approver

**Hằng trong frame:** Cùng một hộp thư không phải hai nguồn độc lập.

**Đường hỏng:** Reply vào hộp thư đã compromise để xác minh. **Điểm can thiệp:** Dual control và callback qua danh bạ có trước.

**Phép đo ứng viên:** Thay đổi beneficiary không xác minh độc lập / thay đổi thử.

**Test phân biệt / bằng chứng cần:** Email từ tài khoản thật nhưng nội dung giả trong diễn tập.

**Đánh đổi:** Tăng thời gian thanh toán.

**OPEN:** Kênh xác minh dự phòng có chung điểm compromise không?

### msg-dns — Quyền điều khiển DNS

**Điều kiện:** Tên miền dẫn tới dịch vụ nhạy cảm.

- **I:** Đề nghị đổi record hoặc registrar setting
- **P:** Kiểm tra authority và phát hiện drift
- **O:** Resolution đúng dịch vụ
- **D:** Record history và registrar audit

**Hằng trong frame:** DNS control có thể chuyển hướng nhiều dịch vụ.

**Đường hỏng:** Tài khoản registrar yếu hơn tài khoản app. **Điểm can thiệp:** Bảo vệ registrar, least privilege, change alert.

**Phép đo ứng viên:** Thay đổi DNS không có owner-approved intent / thay đổi review.

**Test phân biệt / bằng chứng cần:** So cấu hình thực với ý định đã duyệt.

**Đánh đổi:** TTL ảnh hưởng tốc độ sửa và failover.

**OPEN:** Domain hết hạn và delegation bỏ quên được theo dõi ra sao?

**Liên hệ có điều kiện:**

- `sup-dependency` — Quyền điều khiển nguồn phân phối có thể đổi đích tải phần mềm.
- `F05` — Sai lệch route đến từ cấu hình, authority hay compromise; nguồn nào đủ độc lập để nhận biết?

## Endpoint và ranh giới thực thi

**Frame / owner:** Máy trạm, server; endpoint team. **Mục tiêu:** Mã và quyền thực thi phù hợp công việc.

**Biến:** BYOD; EDR health; kernel; ứng dụng cũ. **Nguồn lực:** Quản trị thiết bị; cập nhật; bộ nhớ; hỗ trợ người dùng.

**Nguồn ý tưởng trong sách:** Phần 04 — Phân loại lỗi bảo mật bằng hai trục IPOD và hằng/biến, dòng 3534–5509. Tham chiếu bối cảnh: csf.

### end-health — Control endpoint còn hoạt động

**Điều kiện:** Thiết bị được coi là có EDR.

- **I:** Agent heartbeat, version và telemetry test
- **P:** Phân biệt cài đặt, kết nối và thực sự quan sát
- **O:** Trạng thái control có freshness
- **D:** Heartbeat, sensor gaps và test receipt

**Hằng trong frame:** Có phần mềm không đồng nghĩa có bảo vệ hoạt động.

**Đường hỏng:** Agent cài nhưng im lặng hoặc bị vô hiệu. **Điểm can thiệp:** Health kiểm độc lập và test hành vi lành tính.

**Phép đo ứng viên:** Thiết bị đạt health+test / thiết bị trong scope.

**Test phân biệt / bằng chứng cần:** Ngắt sensor trong lab; dashboard phải báo unknown/degraded.

**Đánh đổi:** Telemetry liên tục dùng tài nguyên và có riêng tư.

**OPEN:** Máy offline dài ngày có được loại khỏi mẫu số không?

**Liên hệ có điều kiện:**

- `tel-coverage` — Sensor không hoạt động phải tạo tín hiệu thiếu quan sát.

### end-execution — Quyền thực thi và cô lập

**Điều kiện:** Ứng dụng xử lý input không tin.

- **I:** File, process, user token
- **P:** Áp sandbox, privilege và policy thực thi
- **O:** Process bị giới hạn khả năng
- **D:** Process tree và quyền hiệu lực

**Hằng trong frame:** Chạy được mã không nên đồng nghĩa quản toàn máy.

**Đường hỏng:** Ứng dụng chạy admin hoặc sandbox escape. **Điểm can thiệp:** Giảm quyền; isolation; cập nhật lớp nền.

**Phép đo ứng viên:** Hành động ngoài quyền bị chặn / hành động thử có kiểm soát.

**Test phân biệt / bằng chứng cần:** Thử thao tác vô hại ngoài sandbox trong lab.

**Đánh đổi:** Sandbox có thể làm hỏng tương thích.

**OPEN:** Kernel/driver nào vẫn nằm ngoài ranh giới cô lập?

**Liên hệ có điều kiện:**

- `sup-builder` — Runner không tin cần quyền và state tách biệt.
- `F06` — Permission thực tế, sandbox, SDK và đường export dữ liệu trên từng platform là gì?
- `F07` — Chuỗi tin cậy từ boot tới runtime đứt ở đâu khi một thành phần firmware bị sửa?

### end-memory — An toàn bộ nhớ

**Điều kiện:** Native component xử lý dữ liệu.

- **I:** Buffer, length, lifetime và concurrency
- **P:** Thực thi theo ràng buộc biên và tuổi đối tượng
- **O:** Kết quả không vượt vùng nhớ
- **D:** Crash triage và sanitizer findings

**Hằng trong frame:** Input hợp schema vẫn có thể gây lỗi lifetime.

**Đường hỏng:** Use-after-free, out-of-bounds hoặc race. **Điểm can thiệp:** Memory-safe boundary, sanitizer, fuzz và hardening.

**Phép đo ứng viên:** Lỗi mới xác nhận trên corpus/version; không suy ra xác suất an toàn.

**Test phân biệt / bằng chứng cần:** Fuzz có coverage và giữ regression case độc lập.

**Đánh đổi:** Rewrite tốn nguồn lực; sanitizer khác production.

**OPEN:** Unsafe/FFI boundary và logic bug còn lại ở đâu?

**Liên hệ có điều kiện:**

- `sw-testing` — Fuzz/sanitizer cần corpus và regression riêng cho lỗi lifetime.

**Nhánh nghiên cứu chưa mở đủ:**

- Mobile và browser extension: Permission thực tế, sandbox, SDK và đường export dữ liệu trên từng platform là gì?
- Firmware, boot và thiết bị ngoại vi: Chuỗi tin cậy từ boot tới runtime đứt ở đâu khi một thành phần firmware bị sửa?
- Malware analysis và reverse engineering: Sandbox quan sát được hành vi nào, và hành vi né môi trường làm giới hạn kết luận ra sao?

## Ứng dụng web và diễn giải input

**Frame / owner:** Parser và trình duyệt; AppSec. **Mục tiêu:** Dữ liệu không chuyển thành lệnh ngoài ý định.

**Biến:** Encoding; context; proxy; framework; phiên bản. **Nguồn lực:** Secure API; code review; kiểm thử ngữ cảnh.

**Nguồn ý tưởng trong sách:** Phần 03 — IPOD của bảo mật: Input, Process, Output, Data, dòng 1604–3533. Tham chiếu bối cảnh: asvs.

### web-injection — Dữ liệu thành lệnh

**Điều kiện:** Input đi vào interpreter.

- **I:** Giá trị từ user hoặc upstream
- **P:** Tách cú pháp lệnh khỏi tham số dữ liệu
- **O:** Truy vấn/thao tác giữ ý định chương trình
- **D:** Query template và validation result

**Hằng trong frame:** Kiểm tra chuỗi không thay thế ranh giới code-data.

**Đường hỏng:** Concatenation vào SQL, shell hoặc template. **Điểm can thiệp:** Parameterized API; tránh interpreter khi không cần.

**Phép đo ứng viên:** Sink dùng ranh giới code-data được kiểm chứng / sink đã inventory.

**Test phân biệt / bằng chứng cần:** Đổi dữ liệu đầu vào; cấu trúc lệnh phải không đổi.

**Đánh đổi:** API an toàn vẫn có giới hạn cho identifier động.

**OPEN:** Second-order input từ DB có đi lại vào sink?

**Liên hệ có điều kiện:**

- `ai-instruction` — Cùng hỏi dữ liệu có thành lệnh không; cơ chế LLM không đồng nhất parser SQL.

### web-xss — Ngữ cảnh output trình duyệt

**Điều kiện:** Dữ liệu hiển thị trong HTML/JS/URL.

- **I:** Untrusted content và vị trí render
- **P:** Encode/sanitize đúng context và policy
- **O:** Nội dung hiển thị không tự thực thi ngoài ý định
- **D:** Context và kiểm thử render

**Hằng trong frame:** Encode cho HTML không tự đúng trong JS hay URL.

**Đường hỏng:** Dữ liệu được đánh dấu safe sai hoặc DOM sink nguy hiểm. **Điểm can thiệp:** Context-aware escaping, safe DOM API, CSP bổ sung.

**Phép đo ứng viên:** Render context nguy hiểm đã test / context trong inventory.

**Test phân biệt / bằng chứng cần:** Kiểm tra cùng input ở text, attribute và script context.

**Đánh đổi:** Sanitize mạnh có thể bỏ nội dung hợp lệ.

**OPEN:** Stored content cũ và editor rich text được xử lý thế nào?

**Liên hệ có điều kiện:**

- `ses-concurrency` — Script ngoài ý định có thể hành động bằng phiên người dùng dù cookie khó đọc.
- `F09` — Origin/site, cookie, storage và messaging tạo ranh giới khác nhau thế nào?

### web-parser — Sai khác giữa các parser

**Điều kiện:** Proxy và backend cùng diễn giải request.

- **I:** Byte stream và metadata
- **P:** Chuẩn hóa theo một contract end-to-end
- **O:** Một cách hiểu nhất quán về request
- **D:** Raw/normalized correlation khi cần

**Hằng trong frame:** Các lớp phải thống nhất ranh giới và encoding.

**Đường hỏng:** Hai parser hiểu length hoặc path khác nhau. **Điểm can thiệp:** Giảm ambiguity, cập nhật parser và test xuyên lớp.

**Phép đo ứng viên:** Ca parser differential bất đồng / corpus được thử.

**Test phân biệt / bằng chứng cần:** Corpus không chứa dữ liệu thật; so frontend/backend interpretation.

**Đánh đổi:** Lưu raw request gây rủi ro dữ liệu.

**OPEN:** WebSocket, HTTP upgrade và protocol translation có khác?

**Liên hệ có điều kiện:**

- `net-egress` — Chuẩn hóa URL sai có thể làm policy và connector hiểu khác đích.
- `F10` — Parser, converter, metadata và antivirus tạo những process con với quyền gì?

**Nhánh nghiên cứu chưa mở đủ:**

- Browser isolation và cross-origin: Origin/site, cookie, storage và messaging tạo ranh giới khác nhau thế nào?
- File upload và đa phương tiện: Parser, converter, metadata và antivirus tạo những process con với quyền gì?

## API và nghiệp vụ

**Frame / owner:** API đồng bộ/bất đồng bộ; product team. **Mục tiêu:** Giao dịch giữ đúng quyền, thứ tự và giới hạn.

**Biến:** Retry; concurrency; tenant; giá; số lượng. **Nguồn lực:** Transaction store; rate budget; test nghiệp vụ.

**Nguồn ý tưởng trong sách:** Phần 04 — Phân loại lỗi bảo mật bằng hai trục IPOD và hằng/biến, dòng 3534–5509. Tham chiếu bối cảnh: api.

### api-state — Invariant nghiệp vụ

**Điều kiện:** Mua hàng, hoàn tiền, đặt chỗ.

- **I:** Hành động và trạng thái giao dịch
- **P:** Kiểm tra transition cùng điều kiện nghiệp vụ
- **O:** Trạng thái mới hợp lệ
- **D:** Ledger và lịch sử transition

**Hằng trong frame:** Mỗi bước hợp lệ riêng chưa chắc cả chuỗi hợp lệ.

**Đường hỏng:** Bỏ bước xác nhận hoặc hoàn tiền quá số đã trả. **Điểm can thiệp:** State machine và invariant ở commit.

**Phép đo ứng viên:** Transition vi phạm invariant / chuỗi thử.

**Test phân biệt / bằng chứng cần:** Đảo thứ tự, lặp bước và đổi giá giữa các bước.

**Đánh đổi:** Luật chặt có thể cản ngoại lệ cần xử lý tay.

**OPEN:** Những trường hợp nghiệp vụ hợp lệ chưa được mô hình hóa?

**Liên hệ có điều kiện:**

- `rec-consistency` — Khôi phục phải giữ invariant nghiệp vụ chứ không chỉ bảng dữ liệu.
- `F12` — Byzantine faults, finality và khả năng quan sát thay đổi invariant giao dịch thế nào?

### api-retry — Retry và idempotency

**Điều kiện:** Mạng timeout rồi client gửi lại.

- **I:** Operation ID, body và principal
- **P:** Deduplicate nguyên tử theo đúng scope
- **O:** Một hiệu ứng nghiệp vụ cho một ý định
- **D:** Idempotency record và kết quả gốc

**Hằng trong frame:** Cùng key khác nội dung phải có cách xử lý rõ.

**Đường hỏng:** Retry nhân đôi thanh toán hoặc key dùng xuyên tenant. **Điểm can thiệp:** Atomic uniqueness, body binding, TTL đủ dài.

**Phép đo ứng viên:** Hiệu ứng thừa / nhóm retry trong test.

**Test phân biệt / bằng chứng cần:** Gửi đồng thời và mô phỏng crash sau commit trước response.

**Đánh đổi:** Giữ record lâu tốn storage và dữ liệu.

**OPEN:** Exactly-once ở đâu chỉ là giả định của ứng dụng?

**Liên hệ có điều kiện:**

- `ir-contain` — Tự động ứng phó cần tránh retry gây hiệu ứng lặp ngoài ý định.
- `F32` — Retry, tool recursion, memory growth và budget exhaustion có stop condition nào ngoài model?

### api-abuse — Lạm dụng chức năng hợp lệ

**Điều kiện:** Endpoint đúng kỹ thuật nhưng có giá trị kinh tế.

- **I:** Nhiều yêu cầu hợp quyền
- **P:** Đánh giá quota theo actor, hành vi và cost
- **O:** Dịch vụ vẫn phục vụ người hợp lệ
- **D:** Cost, intent proxies và quyết định giới hạn

**Hằng trong frame:** Authentication không bảo đảm sử dụng không gây hại.

**Đường hỏng:** Scraping hoặc mua vét bằng tài khoản hợp lệ. **Điểm can thiệp:** Business limits, fairness và escalation.

**Phép đo ứng viên:** Cost theo actor cùng tỷ lệ người hợp lệ bị chặn.

**Test phân biệt / bằng chứng cần:** Thử traffic count bằng nhau nhưng phân bố actor khác.

**Đánh đổi:** Định danh sâu có chi phí riêng tư.

**OPEN:** Phân biệt tự động hóa được phép với abuse bằng tiêu chí nào?

**Liên hệ có điều kiện:**

- `gov-loss` — Chi phí và hậu quả giúp phân biệt traffic với thiệt hại có ý nghĩa.
- `F11` — Query hợp lệ có thể gây chi phí không tuyến tính hoặc lấy trường vượt quyền thế nào?

**Nhánh nghiên cứu chưa mở đủ:**

- GraphQL và query planning: Query hợp lệ có thể gây chi phí không tuyến tính hoặc lấy trường vượt quyền thế nào?
- Consensus và hệ phân tán: Byzantine faults, finality và khả năng quan sát thay đổi invariant giao dịch thế nào?

## Cloud control plane

**Frame / owner:** Account/project và dịch vụ cloud; platform. **Mục tiêu:** Chỉ thay đổi tài nguyên bằng authority được kiểm soát.

**Biến:** Shared responsibility; role chain; policy inheritance. **Nguồn lực:** Inventory đa account; audit log; sandbox test.

**Nguồn ý tưởng trong sách:** Phần 06 — Zero Trust: ontology của quyền và niềm tin, dòng 6626–7585. Tham chiếu bối cảnh: zt.

### cld-responsibility — Trách nhiệm cloud

**Điều kiện:** Dùng dịch vụ managed.

- **I:** Service contract và cấu hình tenant
- **P:** Chia việc provider bảo vệ với việc customer phải làm
- **O:** Control owner cho từng lớp
- **D:** Responsibility matrix có version

**Hằng trong frame:** Managed không có nghĩa mọi cấu hình đều an toàn.

**Đường hỏng:** Không ai quản dữ liệu, IAM hoặc exposure. **Điểm can thiệp:** Map trách nhiệm theo service và configuration.

**Phép đo ứng viên:** Control không owner / control áp dụng đã xác định.

**Test phân biệt / bằng chứng cần:** Chuyển từ VM sang managed rồi đối soát việc còn lại.

**Đánh đổi:** Nhà cung cấp che chi tiết làm giảm quan sát.

**OPEN:** Bằng chứng nào chứng minh lớp provider hoạt động?

**Liên hệ có điều kiện:**

- `tp-scope` — Managed service cần owner cho cả phần vendor lẫn customer.

### cld-policy — Authority control plane

**Điều kiện:** Role có thể tạo/chỉnh tài nguyên.

- **I:** Policy, role trust và resource access
- **P:** Tính quyền trực tiếp lẫn khả năng cấp quyền tiếp
- **O:** Tập thay đổi có thể thực hiện
- **D:** Role chain và audit control plane

**Hằng trong frame:** Quyền tạo role có thể quan trọng hơn quyền đọc data.

**Đường hỏng:** Quyền tưởng nhỏ cho phép tự mở quyền lớn. **Điểm can thiệp:** Tách quyền quản policy và dùng dữ liệu; test effective access.

**Phép đo ứng viên:** Đường tới quyền đặc biệt ngoài intent / đường đã mô hình hóa.

**Test phân biệt / bằng chứng cần:** Kiểm tra cả role assumption và quyền sửa trust.

**Đánh đổi:** Policy cứng khó xử lý vận hành khẩn cấp.

**OPEN:** Service-linked role và cross-account được xét ra sao?

### cld-drift — Sai lệch cấu hình

**Điều kiện:** IaC và console cùng sửa tài nguyên.

- **I:** Desired state và observed state
- **P:** So sánh ngữ nghĩa và áp remediation có kiểm soát
- **O:** Drift được xử lý hoặc chấp nhận có hạn
- **D:** Diff, actor và remediation receipt

**Hằng trong frame:** Apply thành công chưa chứng minh state thực đúng.

**Đường hỏng:** Console override hoặc resource ngoài IaC. **Điểm can thiệp:** Read-after-write và drift detection.

**Phép đo ứng viên:** Drift nguy hại tồn tại bao lâu; theo resource class.

**Test phân biệt / bằng chứng cần:** Sửa cấu hình lab ngoài pipeline rồi đo phát hiện/khôi phục.

**Đánh đổi:** Auto-fix có thể ghi đè hotfix hợp lệ.

**OPEN:** Eventual consistency gây false positive thế nào?

**Liên hệ có điều kiện:**

- `sw-release` — Kết quả thực tế sau deploy phản hồi về rollout và rollback.
- `F13` — Identity, telemetry và residual state được theo dõi thế nào khi vòng đời ngắn hơn scan cadence?

**Nhánh nghiên cứu chưa mở đủ:**

- Serverless và ephemeral workloads: Identity, telemetry và residual state được theo dõi thế nào khi vòng đời ngắn hơn scan cadence?

## Container và Kubernetes

**Frame / owner:** Cluster và workload; platform/SRE. **Mục tiêu:** Quyền workload không mặc nhiên thành quyền node.

**Biến:** Admission mode; RBAC; CNI; token; runtime. **Nguồn lực:** Admission; runtime telemetry; đội vận hành.

**Nguồn ý tưởng trong sách:** Phần 04 — Phân loại lỗi bảo mật bằng hai trục IPOD và hằng/biến, dòng 3534–5509. Tham chiếu bối cảnh: k8s.

### k8s-admission — Quyền tạo workload

**Điều kiện:** Principal được tạo Pod/deployment.

- **I:** Pod spec và RBAC permission
- **P:** Kiểm tra trường security-sensitive ở admission
- **O:** Workload được giới hạn trên node
- **D:** Admission decision và spec thực

**Hằng trong frame:** RBAC create không tự ràng mọi trường Pod.

**Đường hỏng:** Workload có quyền truy host hay identity ngoài intent. **Điểm can thiệp:** Admission enforce và policy theo namespace.

**Phép đo ứng viên:** Spec trái policy được nhận / spec trái policy thử.

**Test phân biệt / bằng chứng cần:** So warn/audit với enforce trong cluster lab.

**Đánh đổi:** Policy có thể chặn ứng dụng legacy.

**OPEN:** Webhook mất kết nối thì admission làm gì?

**Liên hệ có điều kiện:**

- `arch-blast` — Quyền tạo workload có thể mở đường tới node nếu thiếu admission phù hợp.

### k8s-identity — Danh tính workload

**Điều kiện:** Pod cần gọi API hay cloud.

- **I:** Service account token và audience
- **P:** Cấp quyền tối thiểu, giới hạn scope và lifetime
- **O:** Workload chỉ dùng quyền cần thiết
- **D:** Token mount, access logs và role binding

**Hằng trong frame:** Mọi Pod không cần cùng quyền API.

**Đường hỏng:** Token tự mount và role quá rộng. **Điểm can thiệp:** Tắt mount không cần; quyền theo workload.

**Phép đo ứng viên:** Workload giữ token không cần / workload review.

**Test phân biệt / bằng chứng cần:** Chạy app không dùng API với token mount bị tắt.

**Đánh đổi:** Tách identity tăng cấu hình và vận hành.

**OPEN:** Federation cloud có kiểm tra đúng subject/audience?

**Liên hệ có điều kiện:**

- `cry-key` — Credential workload có lifecycle và custody riêng.
- `F14` — Trust bundle và identity federation làm tăng hay giảm blast radius khi một control plane bị chiếm?

### k8s-network — NetworkPolicy thực thi

**Điều kiện:** Nhiều workload dùng chung cluster.

- **I:** Pod labels, policy và traffic
- **P:** CNI thực thi luật ingress/egress
- **O:** Luồng bị giới hạn như intent
- **D:** Policy, CNI version và probe results

**Hằng trong frame:** Có manifest không chứng minh plugin thực thi.

**Đường hỏng:** Policy không supported hoặc selector không khớp. **Điểm can thiệp:** Test connectivity và kiểm selector/namespace.

**Phép đo ứng viên:** Đường cấm vẫn qua / probe đường cấm.

**Test phân biệt / bằng chứng cần:** Đổi label và thử lại cùng đường kết nối.

**Đánh đổi:** Policy DNS/egress dễ làm lỗi discovery.

**OPEN:** Host networking và traffic tới node có được bao phủ?

**Liên hệ có điều kiện:**

- `net-segment` — Policy cluster là một lớp phân vùng có giới hạn plugin và traffic.

**Nhánh nghiên cứu chưa mở đủ:**

- Multi-cluster và service mesh: Trust bundle và identity federation làm tăng hay giảm blast radius khi một control plane bị chiếm?

## Vòng đời phát triển phần mềm

**Frame / owner:** Thiết kế đến vận hành; engineering. **Mục tiêu:** Yêu cầu bảo mật tồn tại qua các lần thay đổi.

**Biến:** Ngôn ngữ; framework; test quality; release pressure. **Nguồn lực:** Review; CI; test fixtures; owner khắc phục.

**Nguồn ý tưởng trong sách:** Phần 11 — Từ ontology sang hệ thống AI security agent, dòng 12409–14030. Tham chiếu bối cảnh: ssdf, asvs.

### sw-design — Yêu cầu bảo mật từ thiết kế

**Điều kiện:** Tính năng mới thay trust boundary.

- **I:** Use case, abuse case và data flow
- **P:** Chuyển hậu quả cần tránh thành yêu cầu testable
- **O:** Requirement gắn owner và acceptance
- **D:** Design decisions và security tests

**Hằng trong frame:** Checklist chung không thay yêu cầu nghiệp vụ.

**Đường hỏng:** Control được thêm sau khi thiết kế đã khóa. **Điểm can thiệp:** Threat modeling theo boundary và scenario.

**Phép đo ứng viên:** Requirement có test phản ví dụ / requirement đã cam kết.

**Test phân biệt / bằng chứng cần:** Đưa vai trò không hợp lệ vào một use case.

**Đánh đổi:** Phân tích sớm tốn thời gian nhưng giảm rework.

**OPEN:** Abuse case nào chưa có tiêu chí đúng/sai?

**Liên hệ có điều kiện:**

- `api-state` — Abuse case nghiệp vụ sinh invariant và test transition.

### sw-testing — Kiểm thử bảo mật đa lớp

**Điều kiện:** Code thay đổi thường xuyên.

- **I:** Source, build, endpoint và test cases
- **P:** Phối hợp SAST, DAST, SCA, fuzz, review theo mục tiêu
- **O:** Finding được xác minh và regression
- **D:** Version, tool config, finding disposition

**Hằng trong frame:** Tool chạy xong không đồng nghĩa đã test mọi cơ chế.

**Đường hỏng:** Chỉ đo số scan hoặc số finding. **Điểm can thiệp:** Map test tới requirement và lớp lỗi.

**Phép đo ứng viên:** Requirement đạt test xác định / requirement trong scope.

**Test phân biệt / bằng chứng cần:** Cố ý bỏ một control trong fixture rồi test phải fail.

**Đánh đổi:** Nhiều tool tăng noise và thời gian CI.

**OPEN:** Runtime-only và logic business thiếu ở đâu?

**Liên hệ có điều kiện:**

- `vul-fix` — Regression test hỗ trợ xác nhận sửa trong frame đã thử.

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

## Chuỗi cung ứng phần mềm

**Frame / owner:** Source, build, artifact, deploy; release team. **Mục tiêu:** Artifact triển khai đúng nguồn và chính sách cho phép.

**Biến:** Dependency; runner; signer; registry; mutable tag. **Nguồn lực:** Builder cô lập; chứng thực; kiểm tra ở deploy.

**Nguồn ý tưởng trong sách:** Phần 11 — Từ ontology sang hệ thống AI security agent, dòng 12409–14030. Tham chiếu bối cảnh: slsa, ssdf.

### sup-dependency — Dependency và nguồn tin

**Điều kiện:** Build dùng package bên ngoài.

- **I:** Tên, version, checksum, registry và dependency tree
- **P:** Resolve theo nguồn cho phép và kiểm provenance khi có
- **O:** Dependency cụ thể được đưa vào build
- **D:** Lockfile, inventory và nguồn thực

**Hằng trong frame:** Đúng tên package không chứng minh đúng tác giả/nguồn.

**Đường hỏng:** Namespace confusion hoặc update độc. **Điểm can thiệp:** Pin, registry policy, review update, SBOM hỗ trợ.

**Phép đo ứng viên:** Dependency resolve ngoài nguồn dự định / dependency resolved.

**Test phân biệt / bằng chứng cần:** Đổi registry ưu tiên trong fixture không có secret.

**Đánh đổi:** Pin giảm biến động nhưng trì hoãn patch.

**OPEN:** Transitive dependency và install script thực thi quyền gì?

**Liên hệ có điều kiện:**

- `vul-context` — Inventory dependency giúp biết CVE có nằm trong artifact đang chạy.
- `F15` — Dataset, checkpoint và evaluation provenance khác binary provenance ở chỗ nào?

### sup-builder — Tính toàn vẹn build

**Điều kiện:** CI nhận contribution không tin.

- **I:** Source revision, workflow và build secrets
- **P:** Cô lập job; chỉ cấp authority cần cho nhánh tin
- **O:** Artifact và thông tin build
- **D:** Logs, digest và builder identity

**Hằng trong frame:** Runner bị chiếm có thể tạo artifact khác source.

**Đường hỏng:** Untrusted job dùng signer hoặc credential production. **Điểm can thiệp:** Ephemeral runner, phân tầng trust và signer riêng.

**Phép đo ứng viên:** Build tin cậy chia state với job không tin / build review.

**Test phân biệt / bằng chứng cần:** Chạy fixture thử vượt job boundary không có credential thật.

**Đánh đổi:** Cô lập mạnh tăng thời gian build.

**OPEN:** Cache có truyền state độc giữa hai mức trust?

**Liên hệ có điều kiện:**

- `sup-deploy` — Provenance chỉ hữu ích khi điểm dùng xác minh identity và policy.

### sup-deploy — Xác minh tại triển khai

**Điều kiện:** Artifact qua registry tới production.

- **I:** Digest, provenance và deployment intent
- **P:** Kiểm signer/builder/source policy tại điểm dùng
- **O:** Chỉ artifact được phép được chạy
- **D:** Verification decision và deployed digest

**Hằng trong frame:** Có chữ ký không chứng minh artifact an toàn.

**Đường hỏng:** Chữ ký hợp lệ từ nguồn không được phép hoặc tag đổi. **Điểm can thiệp:** Verify digest+identity+policy; pin deployment.

**Phép đo ứng viên:** Artifact trái policy được deploy / negative cases.

**Test phân biệt / bằng chứng cần:** Thay tag sau approve; deployment phải bám digest được duyệt.

**Đánh đổi:** Fail-closed làm release phụ thuộc verifier.

**OPEN:** Khi key/builder bị compromise sẽ thu hồi thế nào?

**Liên hệ có điều kiện:**

- `cry-key` — Signer bị compromise làm thay đổi mức tin vào artifact đã ký.

### build-cache — Cache xuyên mức tin trong CI

**Điều kiện:** Trusted và untrusted job dùng cache chung.

- **I:** Cached dependencies/artifacts và writer identity
- **P:** Phân vùng cache theo trust, integrity và key semantics
- **O:** Trusted job không dùng state không kiểm chứng
- **D:** Cache provenance và read/write scope

**Hằng trong frame:** Key cache đoán được không phải quyền ghi hợp lệ.

**Đường hỏng:** Untrusted job ghi thứ trusted job tự nhận là sạch. **Điểm can thiệp:** Trust-scoped cache và content validation.

**Phép đo ứng viên:** Trusted cache reads từ writer không phép / reads có provenance.

**Test phân biệt / bằng chứng cần:** Fixture untrusted ghi marker rồi trusted job thử đọc.

**Đánh đổi:** Giảm reuse làm build chậm.

**OPEN:** Shared compiler/tool cache có đường mutate riêng không?

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

### verify-root — Gốc tin của verifier

**Điều kiện:** Verifier phải biết signer/builder nào hợp lệ.

- **I:** Trust policy, key metadata và attestation
- **P:** Kiểm nguồn phân phối policy và thẩm quyền sửa nó
- **O:** Quyết định dựa trên trust root được bảo vệ
- **D:** Policy revision, approver và root lineage

**Hằng trong frame:** Không lấy trust root từ chính artifact đang cần xác minh.

**Đường hỏng:** Artifact tự khai signer hợp lệ; attacker sửa allowlist. **Điểm can thiệp:** Protected root distribution và separation of duties.

**Phép đo ứng viên:** Policy change không được duyệt / changes được audit.

**Test phân biệt / bằng chứng cần:** Artifact đề nghị thêm signer vào trust root; phải bị bỏ qua.

**Đánh đổi:** Quản root chặt làm recovery signer khó hơn.

**OPEN:** Khôi phục trust root khi chính hệ phát hành bị chiếm?

### verify-revocation — Thu hồi signer và artifact đã chạy

**Điều kiện:** Key hoặc builder bị phát hiện compromise.

- **I:** Revocation statement và runtime inventory
- **P:** Xác định affected builds theo time/source scope, chặn mới và xử lý đang chạy
- **O:** Tập ảnh hưởng và remediation có owner
- **D:** Revoked identity, signed-at evidence và deployed digests

**Hằng trong frame:** Chặn deploy mới không sửa artifact đã tồn tại.

**Đường hỏng:** Verifier cập nhật nhưng runtime vẫn chạy bản bị nghi ngờ. **Điểm can thiệp:** Runtime reconciliation và rollback/replace plan.

**Phép đo ứng viên:** Instance affected chưa xử lý / instance affected biết.

**Test phân biệt / bằng chứng cần:** Mock revoke signer; kiểm cả deploy mới và inventory cũ.

**Đánh đổi:** Thu hồi rộng có thể ngừng nhiều dịch vụ sạch.

**OPEN:** Không biết thời điểm compromise thì phạm vi được mở thế nào?

**Nhánh nghiên cứu chưa mở đủ:**

- Model và dataset supply chain: Dataset, checkpoint và evaluation provenance khác binary provenance ở chỗ nào?

## Dữ liệu, riêng tư và lưu giữ

**Frame / owner:** Vòng đời dataset; data owner. **Mục tiêu:** Dùng đúng loại dữ liệu, mục đích và thời hạn.

**Biến:** Bản sao; cache; log; lineage; miền pháp lý. **Nguồn lực:** Catalog; redaction; xóa; khôi phục; pháp chế.

**Nguồn ý tưởng trong sách:** Phần 08 — Data ontology cho agent bảo mật, dòng 8536–10085. Tham chiếu bối cảnh: csf.

### dat-class — Phân loại theo vai trò dữ liệu

**Điều kiện:** Một pipeline trộn nhiều loại dữ liệu.

- **I:** Content, provenance và intended use
- **P:** Gắn sensitivity, authority và verified status riêng
- **O:** Dữ liệu có policy xử lý đúng chức năng
- **D:** Classification rationale và lineage

**Hằng trong frame:** Nhạy cảm và đáng tin là hai trục khác nhau.

**Đường hỏng:** Text công khai bị coi là instruction; secret vào log. **Điểm can thiệp:** Type/taint/provenance tách biệt và enforcement.

**Phép đo ứng viên:** Dataset thiếu nhãn bắt buộc / dataset trong catalog.

**Test phân biệt / bằng chứng cần:** Dữ liệu công khai nhưng chứa lệnh giả phải giữ untrusted.

**Đánh đổi:** Nhãn chi tiết khó duy trì qua biến đổi.

**OPEN:** Ai được đổi nhãn và theo bằng chứng gì?

**Liên hệ có điều kiện:**

- `ai-memory` — Provenance và trạng thái kiểm chứng phải đi cùng dữ liệu qua memory.
- `F16` — Các dataset riêng không nhạy cảm có thể kết hợp để suy ra điều gì, với đối thủ nào?
- `F18` — Ai có thể collude, output vẫn tiết lộ gì, và protocol bảo vệ khâu nào?

### dat-retention — Lưu giữ và xóa

**Điều kiện:** Dữ liệu có nhiều bản sao.

- **I:** Purpose, thời hạn, replica/cache/backup map
- **P:** Áp retention theo mục đích và xử lý ngoại lệ
- **O:** Dữ liệu hết mục đích được xóa hoặc hạn chế đúng luật áp dụng
- **D:** Deletion evidence và residual copies

**Hằng trong frame:** Xóa primary row không chứng minh xóa toàn hệ.

**Đường hỏng:** Search index, logs, backup giữ bản cũ. **Điểm can thiệp:** Lineage, deletion workflow và restore-aware deletion.

**Phép đo ứng viên:** Bản sao thuộc scope chưa xử lý sau deadline / bản sao biết.

**Test phân biệt / bằng chứng cần:** Restore backup test rồi tái áp yêu cầu xóa.

**Đánh đổi:** Xóa mạnh xung đột recovery và legal hold.

**OPEN:** Yêu cầu theo từng jurisdiction cần pháp chế xác nhận gì?

**Liên hệ có điều kiện:**

- `rec-consistency` — Restore không được vô tình hồi sinh dữ liệu cần xóa ngoài ngoại lệ áp dụng.

### dat-egress — Rò dữ liệu ở output

**Điều kiện:** Có export, report, email và log.

- **I:** Data selection và destination
- **P:** Kiểm quyền, tối thiểu hóa và kiểm destination
- **O:** Output đúng người và mục đích
- **D:** Export audit và minimization result

**Hằng trong frame:** Được đọc không tự đồng nghĩa được xuất hàng loạt.

**Đường hỏng:** Service account hợp lệ xuất quá mức. **Điểm can thiệp:** Output authorization, hạn mức và review theo sensitivity.

**Phép đo ứng viên:** Export vượt policy / export được kiểm tra.

**Test phân biệt / bằng chứng cần:** Thử export bằng quyền chỉ xem từng record.

**Đánh đổi:** Kiểm sâu tăng latency và có thể false positive.

**OPEN:** Dữ liệu suy diễn hoặc kết hợp có nhạy cảm mới không?

**Liên hệ có điều kiện:**

- `tel-schema` — Log quá nhiều để quan sát có thể tự tạo kênh rò dữ liệu.
- `F17` — Đơn vị bảo vệ, composition và utility tradeoff được định nghĩa ra sao trước khi chọn epsilon?
- `F30` — Ai truy cập output gì, budget truy vấn bao nhiêu, thiệt hại được định nghĩa thế nào?

**Nhánh nghiên cứu chưa mở đủ:**

- Suy diễn riêng tư và tái định danh: Các dataset riêng không nhạy cảm có thể kết hợp để suy ra điều gì, với đối thủ nào?
- Differential privacy và ngân sách riêng tư: Đơn vị bảo vệ, composition và utility tradeoff được định nghĩa ra sao trước khi chọn epsilon?
- MPC và federated learning: Ai có thể collude, output vẫn tiết lộ gì, và protocol bảo vệ khâu nào?

## Lỗ hổng và phơi nhiễm

**Frame / owner:** Asset-vulnerability pair; VM team. **Mục tiêu:** Giảm đường gây hại có ý nghĩa trong scope.

**Biến:** Reachability; exploitability; control; tuổi tồn tại. **Nguồn lực:** Scanner; inventory; change window; kiểm chứng sửa.

**Nguồn ý tưởng trong sách:** Phần 05 — Ontology rủi ro: Threat, Vulnerability, Likelihood, Impact, Risk, dòng 5510–6625. Tham chiếu bối cảnh: cvss.

### vul-context — Severity khác rủi ro

**Điều kiện:** Một CVE trên nhiều tài sản.

- **I:** CVSS, reachability, workload và business impact
- **P:** Đặt finding vào đường gây hại có điều kiện
- **O:** Ưu tiên gắn kịch bản
- **D:** Nguồn CVE và giả định local

**Hằng trong frame:** Không dùng severity như xác suất bị khai thác.

**Đường hỏng:** Patch dễ nhiều để làm đẹp KPI, bỏ hệ trọng yếu. **Điểm can thiệp:** Ưu tiên có context và kiểm chứng đường phơi nhiễm.

**Phép đo ứng viên:** Số/giờ cặp asset-lỗ hổng phơi nhiễm theo criticality strata.

**Test phân biệt / bằng chứng cần:** Đổi reachability, giữ CVSS; ưu tiên phải được xem lại.

**Đánh đổi:** Context tốn dữ liệu; không thể chờ hoàn hảo.

**OPEN:** Thiếu exploit telemetry thì uncertainty được trình bày sao?

### vul-fix — Sửa và kiểm lại

**Điều kiện:** Ticket được đánh dấu resolved.

- **I:** Patch/config và finding gốc
- **P:** Kiểm artifact/state thực và test lại điều kiện lỗi
- **O:** Finding thật sự không tái hiện trong scope
- **D:** Fix receipt, version và retest result

**Hằng trong frame:** Đóng ticket không phải bằng chứng sửa xong.

**Đường hỏng:** Patch chưa restart; node khác chưa cập nhật. **Điểm can thiệp:** Retest ở asset đúng và check drift.

**Phép đo ứng viên:** Finding reopen / finding từng xác nhận fixed.

**Test phân biệt / bằng chứng cần:** Một node cố tình chưa rollout trong lab.

**Đánh đổi:** Retest tăng thời gian và tải hệ.

**OPEN:** Mitigation tạm có hết hạn hoặc mất hiệu lực khi đổi route?

**Liên hệ có điều kiện:**

- `F19` — Scope, phối hợp vá, bằng chứng không gây hại và thời gian disclosure được quyết định thế nào?

### vul-exposure — Cửa sổ phơi nhiễm

**Điều kiện:** Tài sản đổi trạng thái theo thời gian.

- **I:** Vulnerability state và exposure intervals
- **P:** Ghép khoảng thời gian bằng asset identity
- **O:** Exposure duration theo đối tượng
- **D:** Timeline có gaps/unknowns

**Hằng trong frame:** Không quan sát không được tính thành an toàn.

**Đường hỏng:** Scanner hàng tuần bỏ khoảng phơi nhiễm ngắn. **Điểm can thiệp:** Event-based inventory bổ sung scan.

**Phép đo ứng viên:** Tổng giờ phơi nhiễm quan sát; unknown-hours báo riêng.

**Test phân biệt / bằng chứng cần:** Ẩn một đoạn telemetry; metric phải tăng unknown.

**Đánh đổi:** Lấy mẫu dày tăng chi phí.

**OPEN:** Khoảng trước lần phát hiện đầu được xử lý ra sao?

**Liên hệ có điều kiện:**

- `tel-coverage` — Khoảng không có sensor phải được báo unknown, không tính zero exposure.

**Nhánh nghiên cứu chưa mở đủ:**

- Disclosure và bug bounty: Scope, phối hợp vá, bằng chứng không gây hại và thời gian disclosure được quyết định thế nào?

## Quan sát và độ tin cậy bằng chứng

**Frame / owner:** Pipeline sự kiện; detection engineering. **Mục tiêu:** Không nhầm thiếu dữ liệu với không có sự kiện.

**Biến:** Sampling; clock; drops; parser; retention. **Nguồn lực:** Collector; storage; schema; sức người điều tra.

**Nguồn ý tưởng trong sách:** Phần 08 — Data ontology cho agent bảo mật, dòng 8536–10085. Tham chiếu bối cảnh: ir, measure.

### tel-coverage — Bao phủ quan sát

**Điều kiện:** Nguồn log có thể im lặng.

- **I:** Expected sources, heartbeat và event counts
- **P:** Đối soát nguồn, liveness và test event
- **O:** Healthy/degraded/unknown cho từng nguồn
- **D:** Source registry và drop statistics

**Hằng trong frame:** Không có alert không chứng minh không có tấn công.

**Đường hỏng:** Collector chết nhưng dashboard vẫn xanh. **Điểm can thiệp:** Independent heartbeat và synthetic event.

**Phép đo ứng viên:** Nguồn đạt freshness+test / nguồn được yêu cầu; missing riêng.

**Test phân biệt / bằng chứng cần:** Ngắt pipeline và xem trạng thái đổi.

**Đánh đổi:** Test events và storage có chi phí.

**OPEN:** Shadow assets chưa trong expected set làm mẫu số thiếu bao nhiêu?

### tel-schema — Ngữ nghĩa sự kiện

**Điều kiện:** Nhiều producer dùng schema khác.

- **I:** Raw event, parser version và timestamp
- **P:** Chuẩn hóa principal/action/resource mà giữ provenance
- **O:** Event truy vấn được và hiểu đúng
- **D:** Raw reference, normalization version và errors

**Hằng trong frame:** Parse thành công chưa chứng minh nghĩa đúng.

**Đường hỏng:** Actor/target đảo; clock lệch làm sai timeline. **Điểm can thiệp:** Schema contract, parser fixtures, time uncertainty.

**Phép đo ứng viên:** Event mất trường trọng yếu / event trong sample kiểm tra.

**Test phân biệt / bằng chứng cần:** Đổi format producer; parser phải fail rõ hoặc thích nghi đúng.

**Đánh đổi:** Giữ raw tăng riêng tư và storage.

**OPEN:** Định danh dịch vụ thay đổi được nối thế nào?

**Liên hệ có điều kiện:**

- `det-behavior` — Actor/resource sai phá correlation dù rule đúng.

### tel-integrity — Toàn vẹn bằng chứng

**Điều kiện:** Nguồn bị đối thủ kiểm soát.

- **I:** Log và metadata nguồn
- **P:** Truyền, bảo vệ lưu trữ và đối soát nguồn khác
- **O:** Bằng chứng có mức tin cậy nêu rõ
- **D:** Hash, access log và chain metadata

**Hằng trong frame:** Hash chứng minh dữ liệu không đổi sau mốc, không chứng minh sự thật ban đầu.

**Đường hỏng:** Máy bị chiếm tự tạo log sai. **Điểm can thiệp:** Remote logging và corroboration độc lập.

**Phép đo ứng viên:** Sự kiện trọng yếu có nguồn đối soát / sự kiện mẫu.

**Test phân biệt / bằng chứng cần:** Thay log nguồn và xem có phát hiện chênh.

**Đánh đổi:** Nhiều nguồn có thể cùng phụ thuộc một clock/agent.

**OPEN:** Độc lập của hai nguồn được kiểm tra ra sao?

**Liên hệ có điều kiện:**

- `ir-evidence` — Chuỗi nguồn và integrity là đầu vào đánh giá bằng chứng, không thay mọi thủ tục pháp lý.

## Phát hiện và điều tra tín hiệu

**Frame / owner:** Tín hiệu đến quyết định; SOC. **Mục tiêu:** Nhận ra sự kiện cần xử lý với chi phí chấp nhận được.

**Biến:** Base rate; adversary drift; queue; nhãn chưa đầy đủ. **Nguồn lực:** Analyst; rules; ground truth; diễn tập.

**Nguồn ý tưởng trong sách:** Phần 07 — MITRE ATT&CK: ontology của hành vi attacker, dòng 7586–8535. Tham chiếu bối cảnh: attack, ir.

### det-base — Base rate và chất lượng cảnh báo

**Điều kiện:** Sự kiện thật hiếm.

- **I:** Alert, ground truth có giới hạn và population
- **P:** Tách TP,FP,FN cùng phạm vi nhãn
- **O:** Precision/recall theo bộ đánh giá
- **D:** Label provenance và unresolved cases

**Hằng trong frame:** Accuracy cao không đủ khi class mất cân bằng.

**Đường hỏng:** Hàng nghìn false positive nuốt analyst. **Điểm can thiệp:** Đánh giá theo workload và cost sai lầm.

**Phép đo ứng viên:** TP/(TP+FP); TP/(TP+FN) chỉ khi FN có ground truth.

**Test phân biệt / bằng chứng cần:** Đổi prevalence giữ sensitivity; precision phải đổi.

**Đánh đổi:** Giảm false positive có thể tăng bỏ sót.

**OPEN:** Bộ test khác phân bố production ra sao?

**Liên hệ có điều kiện:**

- `det-queue` — False positives và complexity quyết định workload, không chỉ alert count.
- `F21` — Ai có thể chạm honeypot hợp lệ, và tín hiệu phản ánh môi trường thật đến đâu?

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

### det-queue — Năng lực xử lý SOC

**Điều kiện:** Alert đến nhanh hơn khả năng review.

- **I:** Arrival rate, complexity và analyst availability
- **P:** Ưu tiên, gom và escalation theo hậu quả
- **O:** Case được xử lý trước khi mất ý nghĩa
- **D:** Queue age, disposition và handoff

**Hằng trong frame:** Thời gian detect nhanh không có ích nếu không hành động.

**Đường hỏng:** Backlog tăng; ca khó bị bỏ lại. **Điểm can thiệp:** Capacity planning và ưu tiên có owner.

**Phép đo ứng viên:** Phân bố tuổi queue theo severity/context; unfinished báo riêng.

**Test phân biệt / bằng chứng cần:** Tăng tải ca khó nhưng giữ alert count.

**Đánh đổi:** Tự động đóng làm đẹp latency nhưng che bỏ sót.

**OPEN:** Mệt mỏi và ca trực ảnh hưởng chất lượng thế nào?

**Liên hệ có điều kiện:**

- `hum-report` — Triage chậm và phản hồi kém có thể làm người dùng ngừng báo cáo.

**Nhánh nghiên cứu chưa mở đủ:**

- Threat intelligence: Indicator hết hạn khi nào, nguồn có độc lập không và intelligence có đổi quyết định thực tế không?
- Deception và honeypot: Ai có thể chạm honeypot hợp lệ, và tín hiệu phản ánh môi trường thật đến đâu?

## Ứng phó và pháp chứng

**Frame / owner:** Sự cố đã nghi ngờ; incident commander. **Mục tiêu:** Giới hạn thiệt hại và giữ khả năng hiểu sự kiện.

**Biến:** Thời điểm; phạm vi; authority; nguồn chứng cứ. **Nguồn lực:** Runbook; đội trực; kho chứng cứ; truyền thông.

**Nguồn ý tưởng trong sách:** Phần 10 — Agent bảo mật: quyền, data và human review, dòng 11375–12408. Tham chiếu bối cảnh: ir.

### ir-contain — Khoanh vùng có thẩm quyền

**Điều kiện:** Sự cố nghi ngờ đang diễn tiến.

- **I:** Evidence, asset owner và kill-switch scope
- **P:** Chọn hành động giới hạn thiệt hại theo rủi ro
- **O:** Containment được quan sát hiệu lực
- **D:** Decision, approval và outcome

**Hằng trong frame:** Gửi lệnh isolate chưa chứng minh đã isolate.

**Đường hỏng:** Tool báo success nhưng đường khác còn mở. **Điểm can thiệp:** Read-back, probe và owner escalation.

**Phép đo ứng viên:** Thời gian từ quyết định đến containment xác nhận.

**Test phân biệt / bằng chứng cần:** Giả lập actuator không thực thi; phải báo failure.

**Đánh đổi:** Isolate có thể ngắt dịch vụ quan trọng.

**OPEN:** Có trường hợp safety buộc ưu tiên khác không?

**Liên hệ có điều kiện:**

- `rec-objective` — Containment có thể kéo dài outage để giảm lan truyền; cần mục tiêu rõ.

### ir-evidence — Thu giữ và chuỗi bảo quản

**Điều kiện:** Có thể cần điều tra kỹ thuật/pháp lý.

- **I:** Volatile state, image, log và người thu thập
- **P:** Thu đúng scope, ghi thao tác và kiểm integrity
- **O:** Bằng chứng tái kiểm tra được
- **D:** Custody, timestamp uncertainty và hashes

**Hằng trong frame:** Hành vi thu thập có thể làm thay đổi hệ.

**Đường hỏng:** Reboot làm mất memory; copy không có nguồn. **Điểm can thiệp:** Runbook theo loại bằng chứng và kiểm custody.

**Phép đo ứng viên:** Artifact thiếu metadata thiết yếu / artifact đã thu.

**Test phân biệt / bằng chứng cần:** Đưa artifact đổi hash hoặc thiếu nguồn vào review.

**Đánh đổi:** Thu đầy đủ tốn thời gian và chạm riêng tư.

**OPEN:** Chuẩn pháp lý tại nơi xử lý yêu cầu gì?

**Liên hệ có điều kiện:**

- `dat-retention` — Retention và legal hold cần được hòa giải với mục tiêu điều tra theo luật áp dụng.

### ir-learn — Học sau sự cố

**Điều kiện:** Dịch vụ đã ổn định.

- **I:** Timeline, quyết định và khoảng mù
- **P:** Phân biệt cause, contributing conditions và unknown
- **O:** Thay đổi control có owner
- **D:** Action register và retest

**Hằng trong frame:** Kết luận một người sơ suất không đủ cơ chế.

**Đường hỏng:** Viết postmortem nhưng control không đổi. **Điểm can thiệp:** Action có acceptance và diễn tập lại.

**Phép đo ứng viên:** Action đến hạn được retest hiệu lực / action đến hạn.

**Test phân biệt / bằng chứng cần:** Lặp scenario sau sửa để kiểm nguyên nhân còn hay không.

**Đánh đổi:** Tập trung một incident có thể bỏ rủi ro khác.

**OPEN:** Bài học chuyển sang hệ nào cần đổi frame?

**Liên hệ có điều kiện:**

- `sw-design` — Sự cố tạo yêu cầu thiết kế mới và kịch bản kiểm thử lại.
- `F22` — Ai được nói điều gì với mức chắc chắn nào khi scope sự cố còn chưa biết?

**Nhánh nghiên cứu chưa mở đủ:**

- Crisis communication: Ai được nói điều gì với mức chắc chắn nào khi scope sự cố còn chưa biết?

## Khôi phục và khả năng tiếp tục

**Frame / owner:** Dịch vụ đầu cuối; business continuity. **Mục tiêu:** Phục hồi trạng thái kinh doanh chấp nhận được.

**Biến:** RTO; RPO; dependency; corruption; identity outage. **Nguồn lực:** Backup; clean room; key custody; người kiểm tra.

**Nguồn ý tưởng trong sách:** Phần 05 — Ontology rủi ro: Threat, Vulnerability, Likelihood, Impact, Risk, dòng 5510–6625. Tham chiếu bối cảnh: ir.

### rec-backup — Backup không phải recovery

**Điều kiện:** Dữ liệu và control plane bị hỏng.

- **I:** Backup, keys, identity và môi trường sạch
- **P:** Restore và kiểm toàn vẹn/đủ chức năng
- **O:** Dịch vụ có thể dùng thật
- **D:** Restore logs và business checks

**Hằng trong frame:** Job backup thành công không bảo đảm bản phục hồi sạch.

**Đường hỏng:** Bản sao cùng credential bị xóa cùng lúc. **Điểm can thiệp:** Cô lập authority, bản bảo vệ và restore drill.

**Phép đo ứng viên:** Recovery thành công theo tiêu chí nghiệp vụ / drill đã thử.

**Test phân biệt / bằng chứng cần:** Mất cả primary lẫn identity; thử recover bằng đường độc lập.

**Đánh đổi:** Cô lập backup làm restore khó hơn.

**OPEN:** Malware hoặc dữ liệu sai đã nằm trong backup chưa?

**Liên hệ có điều kiện:**

- `tp-concentration` — Backup trên cùng identity/provider có thể cùng failure domain.

### rec-objective — RTO, RPO và kiểm tra nghiệp vụ

**Điều kiện:** Khôi phục dịch vụ nhiều thành phần.

- **I:** Mốc gián đoạn, điểm dữ liệu và mục tiêu đã duyệt
- **P:** Đo tới khi nghiệp vụ đạt điều kiện sử dụng
- **O:** Thời gian hồi phục và mất dữ liệu thực
- **D:** Timeline và reconciliation

**Hằng trong frame:** Server lên không đồng nghĩa đơn hàng hoạt động.

**Đường hỏng:** Database phục hồi nhưng queue/DNS/key chưa sẵn. **Điểm can thiệp:** Test end-to-end theo critical transaction.

**Phép đo ứng viên:** Recovery elapsed và data-loss interval; so mục tiêu riêng.

**Test phân biệt / bằng chứng cần:** Khôi phục DB nhưng cố tình thiếu queue; chưa được tính pass.

**Đánh đổi:** Mục tiêu gắt cần dự phòng và chi phí.

**OPEN:** Mục tiêu có thay đổi theo mùa hoặc nhóm khách?

### rec-consistency — Nhất quán khi phục hồi

**Điều kiện:** Nhiều store/queue khôi phục khác mốc.

- **I:** Snapshots, event log và business ledger
- **P:** Đối soát, replay và giải quyết xung đột có rule
- **O:** Trạng thái không nhân đôi/mất nghĩa vụ
- **D:** Reconciliation và unresolved records

**Hằng trong frame:** Các backup riêng đúng chưa chắc toàn hệ đúng.

**Đường hỏng:** Đơn hàng có mà thanh toán không khớp. **Điểm can thiệp:** Consistent checkpoint hoặc reconciliation rõ ràng.

**Phép đo ứng viên:** Record lệch invariant / record đối soát.

**Test phân biệt / bằng chứng cần:** Restore hai store lệch thời gian trong lab.

**Đánh đổi:** Replay và đối soát kéo dài RTO.

**OPEN:** Những side effect ngoài hệ không đảo lại được xử lý thế nào?

### restore-cut — Mốc cắt nhất quán giữa nhiều store

**Điều kiện:** Backup được chụp ở các thời điểm khác nhau.

- **I:** Snapshots và event/transaction positions
- **P:** Chọn cut hoặc dựng lại quan hệ nhân quả nghiệp vụ
- **O:** State liên hệ không thiếu/nhân đôi giao dịch
- **D:** Checkpoint IDs và recovery lineage

**Hằng trong frame:** Timestamp gần nhau không bảo đảm cùng transaction cut.

**Đường hỏng:** Order được backup nhưng payment event chưa có. **Điểm can thiệp:** Consistent checkpoint hoặc replay/reconcile contract.

**Phép đo ứng viên:** Invariant sai sau cut / records đối soát.

**Test phân biệt / bằng chứng cần:** Tạo transaction đúng lúc hai snapshot lệch nhau.

**Đánh đổi:** Đồng bộ snapshot có thể gây pause hoặc tải.

**OPEN:** Hệ ngoài tổ chức không tham gia snapshot thì sao?

### restore-reconcile — Đối soát semantic sau restore

**Điều kiện:** Dữ liệu kỹ thuật đã load thành công.

- **I:** Ledgers, domain invariants và exception rules
- **P:** So nghĩa vụ nghiệp vụ rồi phân loại lệch/không rõ
- **O:** State hợp lệ hoặc backlog cần xử lý
- **D:** Diffs, decisions và owner

**Hằng trong frame:** Record count/hash bằng nhau chưa chứng minh business meaning đúng.

**Đường hỏng:** Thiếu transaction hoặc sai foreign relation vẫn vượt health check. **Điểm can thiệp:** Business reconciliation và owner sign-off.

**Phép đo ứng viên:** Unresolved mismatches / records trong scope đối soát.

**Test phân biệt / bằng chứng cần:** Giữ tổng số record nhưng đổi quan hệ payment-order.

**Đánh đổi:** Đối soát lớn tăng RTO và công sức.

**OPEN:** Có invariant nào không thể tự động quyết định đúng/sai?

### restore-external — Side effect đã ra ngoài hệ

**Điều kiện:** Email, tiền hoặc lệnh vật lý đã gửi trước sự cố.

- **I:** Local recovered state và external receipts
- **P:** Xác nhận trạng thái ngoài rồi chọn compensation/replay
- **O:** Không lặp hoặc bỏ nghĩa vụ ngoài ý định
- **D:** External references và reconciliation evidence

**Hằng trong frame:** Rollback DB không rollback thực tại bên ngoài.

**Đường hỏng:** Replay sự kiện đã thanh toán vì local state mất. **Điểm can thiệp:** External idempotency keys và compensation có thẩm quyền.

**Phép đo ứng viên:** Duplicate/missing external effect / cases đối soát.

**Test phân biệt / bằng chứng cần:** Restore trước mốc gửi nhưng provider đã nhận; phải reconcile.

**Đánh đổi:** Compensation có thể có phí hoặc không đảo được.

**OPEN:** Hệ ngoài mất liên lạc thì trạng thái tạm được biểu diễn thế nào?

## OT, IoT và an toàn vật lý

**Frame / owner:** Thiết bị và quy trình vật lý; kỹ sư vận hành. **Mục tiêu:** An toàn con người và tiến trình trong điều kiện tấn công/lỗi.

**Biến:** Chu kỳ điều khiển; tuổi thiết bị; vendor; maintenance window. **Nguồn lực:** Kỹ sư safety; lab; spare parts; vận hành tại chỗ.

**Nguồn ý tưởng trong sách:** Phần 01 — ONTOLOGY CỦA BẢO MẬT, dòng 30–469. Tham chiếu bối cảnh: ot.

### ot-safety — An toàn khi hệ bị lỗi

**Điều kiện:** Lệnh số tác động thiết bị vật lý.

- **I:** Sensor, setpoint và control command
- **P:** Đối chiếu giới hạn an toàn và trạng thái tiến trình
- **O:** Hành động trong envelope an toàn
- **D:** Process history và safety evidence

**Hằng trong frame:** Security shutdown chưa chắc là trạng thái an toàn.

**Đường hỏng:** Chặn mạng làm mất điều khiển cần thiết. **Điểm can thiệp:** Safety analysis với kỹ sư; lớp bảo vệ phù hợp.

**Phép đo ứng viên:** Deviation ngoài envelope trong mô phỏng được phê duyệt.

**Test phân biệt / bằng chứng cần:** Diễn tập trên mô hình/lab theo kỹ sư safety.

**Đánh đổi:** Availability, integrity và safety có thể xung đột.

**OPEN:** Envelope thay theo tải, môi trường và chế độ vận hành?

**Liên hệ có điều kiện:**

- `arch-failure` — Fail-closed mạng chưa chắc an toàn cho quy trình vật lý.
- `F28` — Safety case, vòng đời hỗ trợ và authority update thay đổi tiêu chí triển khai ra sao?

### ot-legacy — Thiết bị cũ khó vá

**Điều kiện:** Thiết bị không thể cập nhật thường xuyên.

- **I:** Firmware, network paths và maintenance plan
- **P:** Giảm đường tiếp cận và thử thay đổi ngoại tuyến
- **O:** Phơi nhiễm giảm trong giới hạn vận hành
- **D:** Inventory, compensating controls và lịch thay

**Hằng trong frame:** Không vá được không đồng nghĩa không có cách giảm rủi ro.

**Đường hỏng:** Agent/scan làm treo thiết bị cũ. **Điểm can thiệp:** Segmentation, allowlisting phù hợp, passive visibility.

**Phép đo ứng viên:** Đường truy cập không cần thiết còn mở / đường review.

**Test phân biệt / bằng chứng cần:** Kiểm trên digital twin/lab trước khi tác động thật.

**Đánh đổi:** Control bù có thể kéo dài nợ thay thiết bị.

**OPEN:** Khi nào control bù không còn đủ để vận hành?

### ot-remote — Bảo trì từ xa

**Điều kiện:** Vendor cần can thiệp thiết bị.

- **I:** Yêu cầu support và phiên truy cập
- **P:** Cấp quyền có hạn, giám sát và thu hồi
- **O:** Phiên chỉ tác động tài sản đã duyệt
- **D:** Session record và work order

**Hằng trong frame:** Quyền vendor không được thường trực vô thời hạn.

**Đường hỏng:** Shared account và tunnel bỏ quên. **Điểm can thiệp:** Just-in-time access, jump path và xác nhận tại chỗ khi cần.

**Phép đo ứng viên:** Phiên vượt thời hạn/tài sản / phiên review.

**Test phân biệt / bằng chứng cần:** Đóng work order rồi thử lại quyền trong lab.

**Đánh đổi:** Cấp quyền chậm có thể kéo dài downtime.

**OPEN:** Mất internet khi đang bảo trì cần xử lý ra sao?

**Liên hệ có điều kiện:**

- `tp-scope` — Remote support là authority của vendor cần scope và expiry.

**Nhánh nghiên cứu chưa mở đủ:**

- Thiết bị y tế và phương tiện: Safety case, vòng đời hỗ trợ và authority update thay đổi tiêu chí triển khai ra sao?

## Con người và quyền truy cập vật lý

**Frame / owner:** Nhân viên, khách, thiết bị; HR/IT/facilities. **Mục tiêu:** Quy trình có thể dùng an toàn trong áp lực thực tế.

**Biến:** Mệt mỏi; động cơ; accessibility; contractor; offboarding. **Nguồn lực:** Đào tạo theo vai; hỗ trợ; kiểm soát ra vào.

**Nguồn ý tưởng trong sách:** Phần 02 — Cơ chế gốc: hằng và biến trong bảo mật, dòng 470–1603. Tham chiếu bối cảnh: csf.

### hum-report — Khả năng báo cáo sai sót

**Điều kiện:** Người dùng gặp nghi ngờ hoặc lỡ thao tác.

- **I:** Report của người dùng và bối cảnh
- **P:** Tiếp nhận không đổ lỗi, hướng dẫn và triage
- **O:** Thông tin đến người có thể xử lý
- **D:** Report timeline và feedback

**Hằng trong frame:** Không báo không chứng minh không có sự kiện.

**Đường hỏng:** Phạt người báo khiến sự cố bị giấu. **Điểm can thiệp:** Kênh đơn giản, phản hồi hữu ích và diễn tập.

**Phép đo ứng viên:** Thời gian từ nhận biết đến báo trong diễn tập; không suy ra production.

**Test phân biệt / bằng chứng cần:** Thử báo cáo ngoài giờ và kiểm phản hồi.

**Đánh đổi:** Thu nhiều report tăng tải triage.

**OPEN:** Người yếu thế/contractor có kênh an toàn tương đương?

**Liên hệ có điều kiện:**

- `F25` — Quyền hợp lệ, động cơ, thiếu hỗ trợ và bị ép buộc tạo các giả thuyết phân biệt nào?

### hum-access — Ra vào và custody thiết bị

**Điều kiện:** Có khách, sửa chữa hoặc thiết bị thất lạc.

- **I:** Visitor request, badge, device ID
- **P:** Xác nhận quyền và ghi chain custody
- **O:** Người/thiết bị đúng vùng
- **D:** Access/custody events

**Hằng trong frame:** Có badge không chứng minh đúng mục đích mọi vùng.

**Đường hỏng:** Tailgating hoặc thiết bị rời tổ chức chưa wipe. **Điểm can thiệp:** Escort theo risk, custody và remote lock phù hợp.

**Phép đo ứng viên:** Ngoại lệ custody chưa giải quyết / ngoại lệ phát sinh.

**Test phân biệt / bằng chứng cần:** Diễn tập thất lạc thiết bị không chứa dữ liệu thật.

**Đánh đổi:** Giám sát vật lý tác động riêng tư và trải nghiệm.

**OPEN:** Khả năng mở khóa khi khẩn cấp có conflict gì?

**Liên hệ có điều kiện:**

- `cry-key` — Mất thiết bị/custody có thể thay đổi giả định bí mật khóa.

### hum-offboard — Rời tổ chức và đổi vai

**Điều kiện:** Nhân sự hoặc contractor đổi nhiệm vụ.

- **I:** HR event và inventory quyền
- **P:** Thu hồi đồng bộ identity, physical và delegated access
- **O:** Quyền cũ kết thúc đúng hạn
- **D:** Acknowledgments và residual permissions

**Hằng trong frame:** Disable một tài khoản không xóa mọi authority.

**Đường hỏng:** API key, shared account, OAuth grant còn sống. **Điểm can thiệp:** Joiner-mover-leaver với đối soát hệ phụ.

**Phép đo ứng viên:** Authority dư sau deadline / authority đã kiểm kê.

**Test phân biệt / bằng chứng cần:** Cho người thử đổi vai, kiểm cả grant gián tiếp.

**Đánh đổi:** Thu hồi nhầm làm ngừng công việc hợp lệ.

**OPEN:** Tài sản ngoài inventory có giữ dữ liệu/quyền không?

**Nhánh nghiên cứu chưa mở đủ:**

- Insider và coercion: Quyền hợp lệ, động cơ, thiếu hỗ trợ và bị ép buộc tạo các giả thuyết phân biệt nào?
- Accessibility và security usability: Control loại người dùng nào khỏi dịch vụ, có phương án giữ assurance mà giảm loại trừ không?

## Nhà cung cấp và rủi ro tập trung

**Frame / owner:** Quan hệ ngoài tổ chức; procurement và service owner. **Mục tiêu:** Authority, dữ liệu và khả năng phục hồi không mất kiểm soát.

**Biến:** Subprocessor; outage chung; remote support; exit cost. **Nguồn lực:** Hợp đồng; test; quyền xuất dữ liệu; nguồn thay thế.

**Nguồn ý tưởng trong sách:** Phần 05 — Ontology rủi ro: Threat, Vulnerability, Likelihood, Impact, Risk, dòng 5510–6625. Tham chiếu bối cảnh: csf.

### tp-scope — Quyền và dữ liệu nhà cung cấp

**Điều kiện:** Bên ngoài xử lý dữ liệu hay hỗ trợ.

- **I:** Contract, integration scopes và actual traffic
- **P:** Đối soát lời hứa với đường truy cập thực
- **O:** Giới hạn quyền, dữ liệu và mục đích
- **D:** Supplier evidence và quyền hiệu lực

**Hằng trong frame:** Chứng nhận không tự bảo đảm mọi integration.

**Đường hỏng:** Scope OAuth rộng hơn nhu cầu hợp đồng. **Điểm can thiệp:** Least privilege và test hành vi theo integration.

**Phép đo ứng viên:** Integration vượt data/authority intent / integration review.

**Test phân biệt / bằng chứng cần:** Ngừng một tính năng; quyền tương ứng phải bị giảm.

**Đánh đổi:** Scope nhỏ có thể tăng cấu hình riêng.

**OPEN:** Subprocessor mới có làm thay ranh giới dữ liệu?

### tp-concentration — Phụ thuộc tập trung

**Điều kiện:** Nhiều dịch vụ cùng dùng một upstream.

- **I:** Supplier/dependency graph
- **P:** Tìm shared failure domains
- **O:** Kịch bản nhiều dịch vụ hỏng cùng lúc
- **D:** Assumptions và scenario results

**Hằng trong frame:** Nhiều hợp đồng không nhất thiết nhiều nguồn độc lập.

**Đường hỏng:** Hai nhà cung cấp cùng cloud/IdP. **Điểm can thiệp:** Đánh giá common cause và thử fallback.

**Phép đo ứng viên:** Dịch vụ trọng yếu cùng failure domain; không cộng xác suất độc lập.

**Test phân biệt / bằng chứng cần:** Cho common upstream unavailable trong tabletop.

**Đánh đổi:** Đa nhà cung cấp tăng độ phức tạp.

**OPEN:** Các lớp phụ thuộc bị vendor che có thể xác nhận thế nào?

**Liên hệ có điều kiện:**

- `F27` — Failure domain, đặc quyền vận hành và time horizon khác enterprise thông thường thế nào?

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

**Nhánh nghiên cứu chưa mở đủ:**

- Telecom, vệ tinh và hạ tầng quốc gia: Failure domain, đặc quyền vận hành và time horizon khác enterprise thông thường thế nào?

## AI, mô hình và agent có công cụ

**Frame / owner:** Ứng dụng LLM và automation; AI/platform owner. **Mục tiêu:** Nội dung không đáng tin không được nâng thành authority.

**Biến:** Prompt; retrieval; memory; tool; chi phí; model change. **Nguồn lực:** Policy ngoài model; sandbox; review; provenance.

**Nguồn ý tưởng trong sách:** Phần 09 — Agent ontology: từ chatbot đến hệ vận hành, dòng 10086–11374. Tham chiếu bối cảnh: llm.

### ai-instruction — Prompt injection và authority

**Điều kiện:** Agent đọc nội dung bên ngoài.

- **I:** Trang web, tài liệu, email hoặc tool output
- **P:** Giữ nguồn như dữ liệu; policy thực thi ngoài model
- **O:** Không thực hiện hành động vượt nhiệm vụ
- **D:** Provenance, decision và tool request

**Hằng trong frame:** Văn bản thuyết phục không tạo quyền mới.

**Đường hỏng:** Nội dung được model coi là lệnh ưu tiên. **Điểm can thiệp:** Capability limits, sink authorization, dữ liệu tách instruction.

**Phép đo ứng viên:** Hành động vượt policy / ca untrusted-content test.

**Test phân biệt / bằng chứng cần:** Thay chỉ nội dung retrieved; authority phải giữ nguyên.

**Đánh đổi:** Giới hạn tool có thể giảm tác vụ tự động hợp lệ.

**OPEN:** Injection gián tiếp qua memory hoặc multimodal còn đường nào?

### ai-tool — Agent gọi công cụ

**Điều kiện:** Model có khả năng ghi hoặc gửi.

- **I:** Tool args, user intent và current state
- **P:** Kiểm schema, quyền, preview và approval theo rủi ro
- **O:** Hành động đúng phạm vi hoặc bị từ chối
- **D:** Intent-action binding và observed outcome

**Hằng trong frame:** Approval phải gắn đúng hành động đang thực thi.

**Đường hỏng:** Model đổi args sau review hoặc tool có quyền quá rộng. **Điểm can thiệp:** Narrow capability, immutable approved intent, read-back.

**Phép đo ứng viên:** Hành động lệch approved intent / hành động thử.

**Test phân biệt / bằng chứng cần:** Đổi destination sau approval; enforcement phải chặn.

**Đánh đổi:** Human review quá nhiều gây mệt mỏi và rubber stamp.

**OPEN:** Approval hết hạn khi môi trường thay đổi thế nào?

**Liên hệ có điều kiện:**

- `det-queue` — Human review dày đặc có thể tạo queue và giảm chất lượng phê duyệt.
- `F31` — Authority có được cộng dồn sai khi output agent này làm input agent khác không?

### ai-memory — Memory, retrieval và feedback

**Điều kiện:** Agent lưu thông tin qua nhiều lượt.

- **I:** Documents, previous outputs và reviewer feedback
- **P:** Ghi provenance, version và mức kiểm chứng
- **O:** Memory không nâng suy đoán thành sự thật
- **D:** Memory lineage và sửa/xóa

**Hằng trong frame:** Lặp lại một claim không phải nguồn độc lập mới.

**Đường hỏng:** Hallucination được lưu rồi tự viện dẫn. **Điểm can thiệp:** Typed memory, source-linked retrieval và correction path.

**Phép đo ứng viên:** Claim quyết định không truy nguồn / claim được audit.

**Test phân biệt / bằng chứng cần:** Gieo một memory sai có nhãn uncertain; kiểm có bị nâng cấp.

**Đánh đổi:** Giữ nhiều provenance tốn token/storage và riêng tư.

**OPEN:** Quy tắc quên, hết hạn và sửa ký ức xung đột ra sao?

**Liên hệ có điều kiện:**

- `tel-integrity` — Nguồn được lặp lại không trở thành xác minh độc lập.
- `F29` — Phân biệt training poisoning, retrieval poisoning và memory poisoning bằng cơ chế/observable nào?

### action-approval — Phê duyệt gắn hành động cụ thể

**Điều kiện:** Agent chuẩn bị hành động có hậu quả.

- **I:** Preview args, target và user intent
- **P:** Cho reviewer xem đúng dữ liệu/đích/hậu quả rồi bind approval
- **O:** Approval có scope, version và expiry
- **D:** Approved action representation

**Hằng trong frame:** “Đồng ý” chung không cấp quyền cho mọi hành động về sau.

**Đường hỏng:** Review mô tả một việc, tool thực thi việc khác. **Điểm can thiệp:** Immutable approval contract.

**Phép đo ứng viên:** Execute khác approved intent / approval tests.

**Test phân biệt / bằng chứng cần:** Duyệt gửi bản A đến B rồi đổi file hoặc người nhận.

**Đánh đổi:** Preview đầy đủ có thể lộ dữ liệu cho reviewer không phù hợp.

**OPEN:** Ai có quyền duyệt dữ liệu của người khác?

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

### action-toctou — Môi trường đổi sau approval

**Điều kiện:** Giữa review và execution có thời gian.

- **I:** Approved snapshot và target state hiện tại
- **P:** Kiểm lại precondition quan trọng tại commit
- **O:** Hành động chỉ chạy nếu context còn khớp
- **D:** Resource version và expiry result

**Hằng trong frame:** Approval đúng quá khứ không tự đúng hiện tại.

**Đường hỏng:** Target owner/quyền/giá trị đổi nhưng lệnh vẫn chạy. **Điểm can thiệp:** Precondition, expiry và re-approval khi cần.

**Phép đo ứng viên:** Hành động commit với precondition lỗi / race fixtures.

**Test phân biệt / bằng chứng cần:** Đổi owner hoặc target version sau review.

**Đánh đổi:** Kiểm lại nhiều dễ gây review fatigue.

**OPEN:** Điều kiện nào đổi là vô hại, điều kiện nào bắt buộc hỏi lại?

### action-execution — Hợp đồng thực thi tool

**Điều kiện:** Gateway đã cho phép request.

- **I:** Capability, tool args và resource budget
- **P:** Thực thi trong quyền/budget được cấp, kiểm trạng thái đích
- **O:** Hậu quả cụ thể hoặc lỗi có phân loại
- **D:** Execution ID, side effects và outcome

**Hằng trong frame:** Authorization không chứng minh execution đúng.

**Đường hỏng:** Tool trả success nhưng tác động khác hoặc một phần. **Điểm can thiệp:** Narrow executor, structured result và read-back.

**Phép đo ứng viên:** Outcome lệch intent / executions có verification.

**Test phân biệt / bằng chứng cần:** Mock tool trả success nhưng không đổi state; phải detected.

**Đánh đổi:** Read-back có chi phí và eventual consistency.

**OPEN:** Khi kết quả không đọc lại được thì mức bằng chứng là gì?

### action-retry — Retry sau kết quả không rõ

**Điều kiện:** Tool timeout có thể đã tạo side effect.

- **I:** Execution ID và trạng thái commit chưa biết
- **P:** Đối soát hoặc dùng idempotency trước retry
- **O:** Không lặp hậu quả ngoài ý định
- **D:** Operation key, receipt và observed state

**Hằng trong frame:** Timeout không đồng nghĩa không thực thi.

**Đường hỏng:** Agent retry gửi/chi tiền hai lần. **Điểm can thiệp:** Idempotency scope và reconciliation.

**Phép đo ứng viên:** Side effects thừa / retry groups.

**Test phân biệt / bằng chứng cần:** Mock commit rồi mất response; retry không được nhân đôi.

**Đánh đổi:** Giữ dedup state tốn tài nguyên và cần expiry.

**OPEN:** Hệ đích không hỗ trợ idempotency thì ai giải quyết ambiguity?

### action-observe — Quan sát độc lập sau tác động

**Điều kiện:** Tool receipt không đủ để biết hệ đã đổi.

- **I:** Receipt và read-back từ hệ đích
- **P:** Đối chiếu đúng object/version, xét consistency delay
- **O:** Verified, contradicted hoặc unresolved outcome
- **D:** Read source, time, expected và observed

**Hằng trong frame:** Cùng chuỗi text tool trả không phải hai nguồn độc lập.

**Đường hỏng:** Agent dùng lời tool xác nhận chính lời tool. **Điểm can thiệp:** Independent read hoặc human review đúng scope.

**Phép đo ứng viên:** Outcome unresolved / actions cần hậu kiểm.

**Test phân biệt / bằng chứng cần:** Actuator giả báo done; sensor riêng báo chưa đổi.

**Đánh đổi:** Hậu kiểm có thể chậm và cũng có lỗi sensor.

**OPEN:** Nguồn đọc và nguồn ghi có common failure nào?

**Nhánh nghiên cứu chưa mở đủ:**

- Đầu độc model và data: Phân biệt training poisoning, retrieval poisoning và memory poisoning bằng cơ chế/observable nào?
- Model extraction và inference leakage: Ai truy cập output gì, budget truy vấn bao nhiêu, thiệt hại được định nghĩa thế nào?
- Agent nhiều bước và nhiều chủ thể: Authority có được cộng dồn sai khi output agent này làm input agent khác không?
- Chi phí, dừng và vòng lặp tự động: Retry, tool recursion, memory growth và budget exhaustion có stop condition nào ngoài model?
