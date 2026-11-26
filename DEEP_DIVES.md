# Tám hành trình đào sâu

Các bước là mô hình quá trình có điều kiện do assistant biên soạn; không phải dữ liệu incident thật. Quan hệ thứ tự không được dùng làm độ sâu ontology.

## J01 — Thu hồi quyền: vì sao disable account vẫn chưa xong?

**Mục tiêu:** Một chủ thể bị thu hồi không còn thực hiện hành động thuộc scope sau bound được chấp thuận.

**Biên:** IdP + app + API gateway + resource server + refresh store + cache đa vùng. Không giả định tất cả kiểm tra online.

### 1. Binding còn hiệu lực

Sự kiện HR hoặc incident chỉ tên người; phải resolve ra account, workload delegated và grant cụ thể. Bỏ alias tạo false completion.

**Observable cần có:** Danh sách principal và grant có owner; unknown identity ghi riêng.

### 2. Tập credential được nhận diện

Tách cookie, access token, refresh token, API key, OAuth grant và phiên support. Mỗi loại có consumer riêng.

**Observable cần có:** Inventory credential theo loại và điểm enforcement, không chỉ số user.

### 3. Epoch thu hồi được ghi

Ghi thời điểm và version thu hồi ở authority; receipt chỉ nói yêu cầu đã được tiếp nhận. Cần xác nhận state đã commit.

**Observable cần có:** t_revoke, version và nguồn đồng hồ; clock uncertainty.

### 4. Các consumer nhận state mới

Push invalidation có thể mất; pull có chu kỳ; token tự chứa có thể hợp lệ đến expiry. Không giả định logout IdP xóa app session.

**Observable cần có:** Timestamp nhận version ở từng consumer; consumer offline là unresolved.

### 5. Cache quyền hết cũ

Race: request đọc version cũ, revoke commit, request ghi lại cache cũ. Version monotonic hoặc commit check phải chặn việc hồi sinh quyền.

**Observable cần có:** Cache version, read/write order; test xen kẽ có lịch xác định.

### 6. Refresh không cấp quyền trở lại

Access bị hủy nhưng refresh hoặc token exchange còn sống có thể phát hành quyền mới. Thu hồi phải đi qua chuỗi cấp lại.

**Observable cần có:** Kết quả refresh/exchange sau revoke và lineage token.

### 7. Từng đường thử đã deny

Probe không gây tác hại trên mọi loại token/region thuộc scope; một lần deny không chứng minh deny bền khi cache đổi.

**Observable cần có:** Last allow, first sustained deny, khoảng probe, số đường chưa kiểm.

### 8. Hậu quả và sai chặn được đánh giá

Đo cả residual authority lẫn người hợp lệ bị khóa và tải dependency. Ca chưa deny trước hết window là right-censored, không được bỏ khỏi thống kê.

**Observable cần có:** Latency theo stratum, unknown/censored count, false revocation và recovery time.

**Đối chiếu + OPEN:**

- Online introspection: revocation nhanh hơn nhưng identity outage có thể chặn dịch vụ.
- Short-lived token: giới hạn cửa sổ nhưng phụ thuộc khả năng cấp mới và cách cache kiểm expiry.
- OPEN: offline consumer và hợp đồng bound tối đa cần quyết định riêng.

**Mở lại khi:** Có thêm loại credential, region, cache hoặc token exchange; incident cho thấy deny không bền.

**Thẻ nối:** id-mfa, id-recovery, ses-issue, ses-revoke, ses-concurrency, hum-offboard

## J02 — Cross-tenant: từ ID đầu vào đến cache và job bất đồng bộ

**Mục tiêu:** Không lộ hay sửa dữ liệu tenant khác, kể cả đường export, cache và background job.

**Biên:** SaaS nhiều tenant; quyền share hợp lệ phải được mô hình hóa. ID không cần bí mật để bảo vệ quyền.

### 1. Actor và tenant claim được nhận diện

Phân biệt tenant được xác nhận trong session với tenant_id do client gửi. Tenant context phải có nguồn authority rõ.

**Observable cần có:** Verified principal/tenant; input do client khai được đánh dấu không tin.

### 2. Object được resolve đúng miền

Nếu truy vấn lấy object trước rồi check sau, phải bảo đảm không có side effect hoặc metadata leak ở bước resolve. Composite key có thể giúp nhưng không thay policy.

**Observable cần có:** Object tenant từ storage; query scope; response behavior.

### 3. Quyền read/write/share được xét

Read permission không tự cấp export hoặc change-owner. Service account và admin support cần đường policy riêng.

**Observable cần có:** Decision tuple actor,action,object,tenant,policy-version.

### 4. Điều kiện được giữ tới commit

Ownership có thể đổi sau check. Dùng atomic predicate hoặc version guard để precondition gắn với thay đổi.

**Observable cần có:** State version trước/sau; kết quả race test có barrier.

### 5. Cache không nối nhầm tenant

Key thiếu tenant/permission dimension có thể trả dữ liệu đã authorize cho người trước. Invalidation phải phản ánh thay đổi scope.

**Observable cần có:** Cache key contract; test cùng object-local-ID ở hai tenant.

### 6. Async job mang authority giới hạn

Job chạy sau nhiều giờ không nên dùng ambient admin mà quên người yêu cầu. Quyết định dùng snapshot quyền hay recheck phải tường minh.

**Observable cần có:** Requester, purpose, scope, authorization epoch và expiry trên job.

### 7. Output được kiểm theo người nhận

Link tải, email, object storage export có vòng đời riêng; kiểm người nhận và hết hạn, không chỉ bước tạo report.

**Observable cần có:** Export ACL, signed-link policy, destination và thời điểm dùng.

### 8. Bằng chứng đủ nối hành động

Log chỉ ghi URL/status không đủ chứng minh boundary. Dùng negative cases và legitimate sharing cases; không suy recall từ log thiếu nhãn.

**Observable cần có:** Ma trận action × tenant relation × object state × delivery path; kết quả và gaps.

**Đối chiếu + OPEN:**

- Tenant filter trong DB: giảm bỏ sót query, nhưng background/admin path vẫn phải xét.
- App policy: biểu đạt nghiệp vụ tốt hơn nhưng mọi điểm gọi phải áp nhất quán.
- OPEN: cross-tenant sharing và data migration cần semantic contract riêng.

**Mở lại khi:** Thêm report/export, cache layer, support role, tenant merge hoặc job queue.

**Thẻ nối:** auth-object, auth-policy, auth-race, api-state, dat-egress, tel-schema

## J03 — Chuỗi cung ứng: source đúng không bảo đảm binary đúng

**Mục tiêu:** Production chạy artifact đúng nguồn, builder và policy được phê duyệt; có khả năng truy hồi và thu hồi.

**Biên:** Source control → dependency resolution → runner → signer → registry → deploy → runtime. Provenance không tự chứng minh mã không có lỗ hổng.

### 1. Ý định release được cố định

Chốt revision, workflow version và dependency resolution; branch/tag mutable chưa là identity ổn định.

**Observable cần có:** Commit/digest cụ thể và người có quyền duyệt.

### 2. Dependency được resolve

Tên và version phải gắn nguồn và nội dung cụ thể. SBOM là inventory, không phải kết luận mọi dependency an toàn.

**Observable cần có:** Resolved digest, registry, transitive tree và install steps.

### 3. Builder nhận quyền phù hợp

Contribution không tin không được cùng authority với release job. Tách persistent cache/state có thể bị đầu độc.

**Observable cần có:** Runner identity, job trust, state sharing và credential exposure review.

### 4. Artifact gắn với quá trình tạo

Lưu provenance với subject digest và builder/source inputs theo khả năng hệ. Metadata tự khai từ runner bị chiếm có mức tin hạn chế.

**Observable cần có:** Attestation identity và policy về builder được tin.

### 5. Ký không làm biến mất rủi ro

Signature xác nhận binding theo khóa; policy phải xét ai ký, vì sao được tin, key còn hợp lệ không.

**Observable cần có:** Signer scope, key validity, revocation và signing logs.

### 6. Registry không đổi đối tượng đã duyệt

Tag có thể trỏ sang digest khác sau review. Chốt digest tại promote/deploy thay vì tin tên dễ đọc.

**Observable cần có:** Approved digest đối chiếu digest fetched/deployed.

### 7. Enforcement xảy ra ở điểm dùng

Chỉ verify trong CI không ngăn người có đường deploy khác. Admission/deployer phải áp policy và ghi deny/allow.

**Observable cần có:** Negative cases: sai nguồn, builder, signer, digest, policy version.

### 8. Runtime và thu hồi được nối lại

Xác nhận artifact đang chạy và tìm mọi instance khi provenance/key bị nghi ngờ. Rollback phải xét migration dữ liệu.

**Observable cần có:** Runtime digest inventory, affected instances và rehearsal rollback.

**Đối chiếu + OPEN:**

- Hosted builder: chuyển một phần trust sang provider; cần bằng chứng về isolation và identity.
- Self-hosted builder: chủ động control nhưng phải tự giữ sạch state và secrets.
- OPEN: reproducible build hỗ trợ đối soát nhưng không thay review ý định source.

**Mở lại khi:** Thay builder, signer, registry, dependency resolver hoặc đường deploy ngoài pipeline.

**Thẻ nối:** sup-dependency, sup-builder, sup-deploy, cry-key, sw-release, inv-lifecycle

## J04 — Ransomware và phục hồi: bản sao sống trong cùng miền thất bại

**Mục tiêu:** Khôi phục giao dịch quan trọng trong mục tiêu đã thỏa thuận, từ trạng thái có thể tin và đối soát.

**Biên:** Ứng dụng + identity + DNS + keys + database + queue + backup control plane + con người. Không mô phỏng mã độc.

### 1. Dịch vụ trọng yếu được định nghĩa

Tên app quá rộng; chọn giao dịch: đăng nhập, tìm đơn, thanh toán, xuất hóa đơn. Đặt RTO/RPO và điều kiện dữ liệu theo từng loại.

**Observable cần có:** Business acceptance, owner và mốc bắt đầu đo.

### 2. Common failure domain được mở

Primary và backup khác bucket nhưng cùng admin/key/IdP vẫn có điểm chết chung. Map cả quyền xóa và khả năng đổi retention.

**Observable cần có:** Authority graph tới data, backup và recovery credentials.

### 3. Bản phục hồi phù hợp được chọn

Snapshot gần nhất có thể chứa dữ liệu đã hỏng. Cần đánh giá tính sạch và khoảng thời gian cần quay lại, không chỉ tuổi backup.

**Observable cần có:** Integrity checks, incident timeline và uncertainty về thời điểm compromise.

### 4. Môi trường sạch có thể khởi động

Recovery phải dùng identity, network và công cụ không phụ thuộc hoàn toàn vào hệ đã mất. Break-glass cần kiểm soát và diễn tập.

**Observable cần có:** Clean-room prerequisites, custody và kết quả bootstrap.

### 5. Khóa và dữ liệu được khôi phục

Ciphertext phục hồi nhưng key mất thì không có dữ liệu hữu dụng. Kiểm cặp key version và backup sau rotation.

**Observable cần có:** Decryption/integrity result; không xuất secret ra báo cáo.

### 6. Các store được hòa giải

DB, queue và payment provider có thể ở mốc khác. Replay cần idempotency, reconciliation và xử lý side effect không đảo ngược.

**Observable cần có:** Ledger differences, unresolved records và phương án xử lý.

### 7. Nghiệp vụ được kiểm đầu cuối

Server healthy chỉ là tiền điều kiện. Người đại diện nghiệp vụ chạy test không gây giao dịch thật để xác nhận đủ chức năng.

**Observable cần có:** End-to-end checks, completion time, data-loss interval.

### 8. Recovery trở thành phản hồi thiết kế

Lưu bottleneck và chi phí, sửa dependency hoặc mục tiêu nếu không khả thi; lần sau kiểm lại đúng chỗ từng fail.

**Observable cần có:** RTO/RPO deviation, missing dependencies, action owner và retest.

**Đối chiếu + OPEN:**

- Hot standby: phục hồi nhanh nhưng corruption/quyền xấu có thể lan đồng thời.
- Bản cô lập: giảm common failure nhưng chậm lấy lại và cần key/identity độc lập.
- OPEN: giao dịch với bên ngoài không thể tự ý replay hoặc đảo cần quy trình nghiệp vụ.

**Mở lại khi:** Đổi key, identity, backup retention, schema, nhà cung cấp hoặc mục tiêu kinh doanh.

**Thẻ nối:** arch-blast, rec-backup, rec-objective, rec-consistency, cry-key, tp-concentration

## J05 — Từ sự kiện đến phản ứng: nơi dashboard dễ nói dối

**Mục tiêu:** Sự kiện cần xử lý tạo ra quyết định và hành động đủ sớm, với mức bỏ sót/sai chặn được trình bày trung thực.

**Biên:** Sensor → transport → parse → correlate → alert → analyst → actuator → observed result. Ground truth production thường không đầy đủ.

### 1. Population cần quan sát được chốt

Lấy expected asset/event classes từ inventory, không lấy chính nguồn đã gửi log làm mẫu số.

**Observable cần có:** Expected registry, owner, nhóm chưa có sensor.

### 2. Sensor thật sự sinh tín hiệu

Heartbeat chỉ chứng minh agent sống; test event phải đi qua đường cần quan sát.

**Observable cần có:** Heartbeat age và synthetic event receipt riêng.

### 3. Transport không âm thầm mất

Queue overflow, sampling và rate limit có thể bỏ đúng giai đoạn traffic lớn.

**Observable cần có:** Drop counters, sequence gaps, buffer age và load condition.

### 4. Parser giữ đúng nghĩa

Actor/target/resource/time cần giữ nghĩa qua normalization; schema hợp lệ không đảm bảo semantic đúng.

**Observable cần có:** Fixtures có expected meaning; parser version và clock bounds.

### 5. Detection có bài kiểm phân biệt

Rule phải phân biệt legitimate và adversarial scenario trong frame; ATT&CK label chỉ là chỉ mục tham chiếu.

**Observable cần có:** TP/FP/FN trên bộ test có nhãn; unresolved giữ riêng.

### 6. Alert đi vào hàng đợi có hạn

Arrival và service rate theo độ khó quyết định backlog. Đừng loại ca chưa xong để làm MTTR đẹp.

**Observable cần có:** Queue age theo cohort, pending count và complexity.

### 7. Hành động được kiểm hiệu lực

Actuator success receipt không đảm bảo kết nối bị cắt hay quyền bị thu hồi.

**Observable cần có:** Read-back/probe từ đường độc lập và residual paths.

### 8. Feedback thay đổi hệ quan sát

Incident hoặc test miss làm đổi sensor/schema/rule/triage; kiểm lại sau thay đổi mới xác nhận learning loop.

**Observable cần có:** Versioned change, retest, cost và false-positive shift.

**Đối chiếu + OPEN:**

- Thu mọi log: thêm quan sát nhưng tăng chi phí, rò dữ liệu và triage.
- Thu chọn lọc: nhẹ hơn nhưng phải ghi lớp hành vi không còn quan sát.
- OPEN: không có nhãn FN production thì không công bố recall production.

**Mở lại khi:** Đổi schema, sensor, traffic mix, attack behavior, rule version hoặc nhân sự trực.

**Thẻ nối:** tel-coverage, tel-schema, tel-integrity, det-base, det-behavior, det-queue, ir-contain

## J06 — Agent: dữ liệu lạ → ý định → công cụ → hậu quả

**Mục tiêu:** Agent có thể dùng thông tin bên ngoài mà không trao authority cho chính thông tin đó.

**Biên:** User authorization, harness, model, retrieval, memory, tool gateway và hệ đích. Model không được coi là reference monitor duy nhất.

### 1. Nhiệm vụ có phạm vi authority

Tách mục tiêu người dùng khỏi danh sách hành động được phép. Quyền đọc tài liệu không tự cho phép gửi tài liệu đi.

**Observable cần có:** Intent record, assets, actions và destinations trong scope.

### 2. Nguồn ngoài giữ nhãn dữ liệu

Retrieved text, OCR, tool output và memory cũ có provenance/mức trust. Nhãn không bảo đảm model sẽ tuân nên cần lớp thực thi.

**Observable cần có:** Source chain và vị trí dữ liệu được đưa vào context.

### 3. Đề xuất model là đề xuất

Model có thể bị nội dung dẫn lệch. Tool request phải được xem như input cần validate, không như quyết định đã được phê duyệt.

**Observable cần có:** Proposed action và lý do gắn với user intent.

### 4. Gateway kiểm quyền ngoài model

Kiểm principal, object, action, args, destination, cost và thời hạn. Schema đúng không đủ nếu mục tiêu hành động sai.

**Observable cần có:** Policy decision độc lập và capability được cấp cho request.

### 5. Review gắn với nội dung bất biến

Người duyệt cần thấy đúng dữ liệu, đích và hậu quả. Nếu args/state đổi sau review, approval phải kiểm lại theo contract.

**Observable cần có:** Approved action digest/version và execute-time comparison.

### 6. Tool chạy trong resource boundary

Giới hạn filesystem, network, credentials, thời gian và budget theo tác vụ; sandbox không sửa được policy sai nhưng hạn chế phạm vi.

**Observable cần có:** Effective capability, output scope, timeout/cost và denied operations.

### 7. Kết quả được quan sát và phân loại

Tool báo sent/updated phải đối chiếu state đích khi có thể. Output text không trở thành instruction tự động cho bước sau.

**Observable cần có:** Observed state, discrepancies và taint/provenance output.

### 8. Memory không tự tăng mức tin

Lưu kết luận cùng bằng chứng và trạng thái; sửa được khi nguồn đổi. Chặn vòng tự viện dẫn biến một suy đoán thành nhiều chứng cứ.

**Observable cần có:** Claim-source graph, expiry, correction và revalidation.

**Đối chiếu + OPEN:**

- Read-only assistant: ít hậu quả trực tiếp hơn nhưng vẫn có rò dữ liệu và tư vấn sai.
- Write-capable agent: cần authority, atomic approval và hậu kiểm tương ứng hậu quả.
- OPEN: tác vụ dài nhiều agent/ủy quyền cần map authority qua từng bước, không gán trust theo tên agent.

**Mở lại khi:** Thêm tool, quyền ghi, memory persistence, nguồn retrieval hoặc model/harness mới.

**Thẻ nối:** ai-instruction, ai-tool, ai-memory, dat-class, dat-egress, net-egress, auth-race

## J07 — Lỗ hổng: từ scanner finding đến ưu tiên có ý nghĩa

**Mục tiêu:** Giảm các đường gây hại ưu tiên trong ngân sách và thời hạn, không tối ưu số ticket đóng.

**Biên:** Asset-version-function-exposure-control-business outcome; finding có thể false positive hoặc thiếu context.

### 1. Finding gắn đúng asset

IP tái sử dụng hoặc container đã biến mất có thể làm nhầm host. Gắn stable ID và thời điểm quan sát.

**Observable cần có:** Asset ID, image/version, scan timestamp, confidence.

### 2. Thành phần lỗi có thật

Version match chưa chứng minh code path áp dụng; backport và build options có thể đổi kết luận.

**Observable cần có:** Vendor/build evidence và scope affected component.

### 3. Điều kiện kích hoạt được mở

Cần quyền nào, path nào, input nào, cấu hình nào? Không yêu cầu khai thác hệ thật để ghi điều kiện.

**Observable cần có:** Preconditions có nguồn; unknown thay vì tự gán impossible.

### 4. Đường tiếp cận được xác định

Reachability theo attacker position, route, identity và thời gian; public/private là quá thô.

**Observable cần có:** Path evidence, segmentation test và trust assumptions.

### 5. Control và hậu quả được nối

Mitigation có thể giảm path nhưng không xóa vulnerability; blast radius và business impact quyết định giá trị sửa.

**Observable cần có:** Control test, critical assets reachable và scenario outcome.

### 6. Phương án sửa được so sánh

Patch, isolate, disable feature, rotate key hoặc retire có thời gian và rủi ro vận hành khác nhau.

**Observable cần có:** Cost, deadline, residual path và rollback option.

### 7. State sau sửa được xác nhận

Ticket done không đủ. Kiểm đúng artifact và node, test điều kiện gốc và theo dõi rollback làm lỗi quay lại.

**Observable cần có:** Read-back version, retest và residual unknown.

### 8. Exposure window được giữ

Ghép các interval observed vulnerable/reachable; gaps là unknown, không nối mặc định thành an toàn.

**Observable cần có:** Exposure-hours theo lớp quan trọng; unknown-hours và censoring.

**Đối chiếu + OPEN:**

- Patch nhanh: loại một nguyên nhân nhưng có regression và maintenance constraints.
- Control bù: có thể cắt đường sớm hơn nhưng cần expiry và test drift.
- OPEN: thiếu dữ liệu exploit không phải xác suất bằng không.

**Mở lại khi:** Có exploitation evidence mới, đổi route/control, dữ liệu criticality hoặc bản vá bị rollback.

**Thẻ nối:** vul-context, vul-fix, vul-exposure, inv-discovery, gov-loss, arch-blast

## J08 — OT: một lệnh số đi tới trạng thái vật lý

**Mục tiêu:** Giữ quy trình trong envelope an toàn khi gặp sai lệch số, với quyết định do chuyên gia vận hành xác nhận.

**Biên:** Sensor → controller → actuator → physical process → sensor feedback; IT policy không tự quyết trạng thái safety.

### 1. Tiến trình và envelope được mô tả

Nhiệt độ, áp suất, tốc độ hoặc vị trí có giới hạn phụ thuộc chế độ. Ngưỡng phải từ thiết kế/kỹ sư, không tự phát minh.

**Observable cần có:** Approved operating limits và mode definitions.

### 2. Sensor được đặt trong giới hạn tin

Giá trị hợp range vẫn có thể stale, bias hoặc bị giả. Cần freshness và đối soát phù hợp thiết kế.

**Observable cần có:** Time, calibration, quality flags và independent observations nếu có.

### 3. Lệnh gắn chủ thể và mục đích

Setpoint đúng cú pháp có thể sai chế độ. Kiểm cả nguồn, authority và phase vận hành.

**Observable cần có:** Command source, work order, mode và decision.

### 4. Đường bảo trì được giới hạn

Vendor remote access có thể bỏ qua interface vận hành. Quyền tạm phải giới hạn asset, thao tác và thời gian.

**Observable cần có:** Session scope, expiry, revocation và local coordination.

### 5. Controller/actuator thực thi được quan sát

Ack không chứng minh valve/motor đã đạt trạng thái mong muốn. Đo phản hồi vật lý theo độ trễ chấp nhận.

**Observable cần có:** Command receipt và measured response; disagreement alarm.

### 6. Mất liên lạc có cách xử lý an toàn

Giữ trạng thái, shutdown hoặc manual mode là quyết định theo hazard analysis. Không áp fail-closed mạng một cách mù.

**Observable cần có:** Safety-engineered loss-of-comms behavior và rehearsal evidence.

### 7. Ứng phó không tạo hazard mới

Isolate, restart hay scan có thể làm sai thời gian điều khiển. Thử trong lab/twin và cần kỹ sư cho tác động thực.

**Observable cần có:** Approved intervention envelope và stop conditions.

### 8. Khôi phục xác nhận cả vật lý lẫn số

Đúng firmware/config chưa đủ: setpoint, sensor calibration và tiến trình phải trở lại trạng thái được phép.

**Observable cần có:** Configuration baseline, physical checks và sign-off của owner.

**Đối chiếu + OPEN:**

- Passive observation: ít tác động hệ cũ nhưng không thấy mọi state nội bộ.
- Active validation: nhiều bằng chứng hơn nhưng phải nằm trong maintenance/safety constraints.
- OPEN: hệ safety có common cause với control network hay identity không?

**Mở lại khi:** Đổi process mode, firmware, sensor, nhà cung cấp hoặc safety requirements.

**Thẻ nối:** ot-safety, ot-legacy, ot-remote, arch-failure, net-segment, ir-contain
