# Phương pháp đọc và mở bản đồ

Bản đồ này dùng **Hệ miễn dịch của thế giới số** làm hạt giống và **A Fractal Model for Metric Generation / Lens** làm phương pháp mở ngữ cảnh. Nội dung mở rộng là phân tích do assistant biên soạn cho Kevin T.N.; các metric là đề xuất, không phải kết quả quan sát một tổ chức. Có thể sửa tên, frame, điều kiện và thước đo mà không phải giữ các giả định ban đầu.

## Từ mục tiêu tới phép đo

Trình tự là: mục tiêu → đối tượng và biên → trạng thái cần giữ → đường biến đổi → điều kiện sai lệch → control và giới hạn → khả năng quan sát → phương án xử lý → phép so sánh. Một nhãn như “MFA”, “Zero Trust” hay “AI security” chỉ mở câu hỏi; nó không tự trả lời câu hỏi hệ thống thực sự làm gì.

NMF là công cụ của **người quan sát**: gọi tên điều gì, hiểu nó theo nghĩa nào, trong frame nào? IPOD, C/V và tài nguyên mô tả **hệ thống được quan sát**. Không biến NMF thành một bộ phận vật lý tưởng tượng bên trong mọi hệ.

Mỗi thẻ cơ chế giữ Input có nguồn, Process có tác động, Output có người/hệ tiêu thụ, Data được giữ lại. Một receipt “success” là output của giao diện lệnh; trạng thái mục tiêu đã thay đổi hay chưa là một phép quan sát khác. Data có thể quay lại sửa policy, nhưng chỉ gọi là vòng phản hồi khi chỉ ra consumer và điều kiện cập nhật thực sự.

## Hằng, biến, nguồn lực và giả định

“Hằng” là invariant được chọn trong frame, không phải chân lý bất biến của mọi hệ. Ví dụ tenant isolation là hằng của một SaaS, nhưng chia sẻ có đồng ý giữa tenant là biến thể nghiệp vụ phải được đưa vào policy. Một giá trị từng cố định, như IP của workload, có thể đã trở thành biến khi chuyển sang cloud.

Mỗi miền cung cấp biến và nguồn lực chung; mỗi thẻ bổ sung điều kiện, invariant và failure riêng. Khi triển khai phải phân loại tiếp: đã biết/đo được; giả định tạm; chưa biết; biến bị bỏ sót; hằng đã lỗi thời. Nguồn lực được chia theo vận hành, bảo trì, phát triển và phục hồi: không chỉ CPU hay tiền mà còn authority, thời gian trực, quyền truy nguồn, kỹ năng và sự chú ý. Control cần người phê duyệt nhưng không có người trực là control chưa vận hành được.

Không suy “nhiều control hơn = an toàn hơn”. Mỗi control thêm dependency, latency, thao tác, dữ liệu lưu hoặc nguy cơ chặn nhầm. Có những lựa chọn cắt cùng một đường lỗi: đổi thứ tự check/commit, ràng điều kiện ở sink, giảm authority, bỏ tính năng không cần thiết, hoặc tăng khả năng quan sát. Chỉ thêm cơ chế mới khi các tổ hợp có sẵn không đạt mục tiêu và đã nêu phần còn thiếu.

## Sáu miền sinh metric

| Miền | Câu hỏi | Kiểu phép đo phù hợp | Không được suy ra |
|---|---|---|---|
| Meaning | Hai người có dùng “đã thu hồi”, “đã phục hồi”, “an toàn” cùng nghĩa? | Contract định nghĩa, rubric phân biệt ví dụ/phản ví dụ, case còn tranh chấp | Đếm định nghĩa không chứng minh hiểu đúng |
| Domain | Population, boundary và time window là gì? | Inventory reconciliation, known/unknown population, map coverage theo nguồn | Coverage trên phần đã biết không phải coverage toàn thực tại |
| Mechanism | Control cắt đường biến đổi nào và khi nào thất bại? | Negative/positive tests, counterfactual, condition matrix | Pass test hữu hạn không chứng minh không có bypass |
| Evidence | Có quan sát độc lập đủ để tin kết luận? | Provenance, freshness, completeness, unresolved cases | Hash/chữ ký không chứng minh nội dung là sự thật |
| Operational | Hệ làm việc trong tải và nguồn lực nào? | Latency distribution, queue age, cost, throughput, censored cases | Trung bình đẹp không bảo đảm tail hoặc ca chưa hoàn thành |
| Consequence | Người dùng/kinh doanh/an toàn được lợi hoặc thiệt gì? | Outage, data loss, sai chặn, giao dịch lệch, physical envelope | Điểm kỹ thuật không tự đổi thành tiền hay an toàn con người |

Các sáu miền là sáu góc kiểm tra, **không phải sáu con số bắt buộc**, không có phép lấy trung bình tạo “điểm nhận thức” hoặc “điểm bảo mật” chung. Trong từng thẻ, sáu câu hỏi được mở từ nội dung thẻ; chúng là câu hỏi review, không được đếm thành sáu phát hiện mới.

## Contract phép đo

Dùng cấu trúc của Metric Generation: `m = <q, Ω, Γ, G, B, S, τ, D>`: đại lượng/quan hệ; miền; điều kiện; mục tiêu; baseline; thang đo/phương pháp; khoảng thời gian; dữ liệu cần. Atlas bổ sung missing-data rule, bias, consequence và binding vào điểm thực thi để người dùng có thể thu thập đúng dữ liệu.

102 phép đo trong thẻ là **candidate sketch**: đã chỉ ra quan hệ cần nhìn nhưng còn cần owner chốt population, thời gian và baseline thực tế. Tám contract M01–M08 phân rã chi tiết hơn, đủ để thiết kế collector/test khi đã bind môi trường. Tất cả đều chưa có dữ liệu tổ chức. Không có ngưỡng “tốt” tùy tiện. Những ngưỡng như RTO, TTL, freshness hay safe pressure phải đến từ mục tiêu/thiết kế của hệ cụ thể.

Với tỷ lệ, báo numerator, denominator và unit of analysis; mẫu số bằng 0 là **undefined**, không phải 0% hay 100%. Không xóa unknown để làm tỷ lệ đẹp. Nếu có dữ liệu bị kiểm duyệt theo thời gian, báo ca đang chờ/censored. Không cộng các đơn vị không tương thích. Nếu cần phân nhóm, giữ strata như criticality, loại credential, region hay loại nghiệp vụ; việc chọn trọng số cần lập luận về giá trị và uncertainty riêng.

## Ba lớp của bản đồ

1. `graph/revisions/<CURRENT>/nodes/*.json` và `edges.jsonl`: containment và các quan hệ có nhãn giữa khái niệm, thẻ, hành trình và frontier. Một crosslink ghi điều kiện hoặc giới hạn; analogy không được coi là cơ chế đồng nhất. `data/atlas.json` chỉ là seed import đầu, không ghi đè bản hiện hành.
2. `io_map.json`: chỉ có phenomenon nodes, frame và cạnh `I_TO_O`. Không nhét evidence hoặc process vào canonical edge. Đây là một export theo nguyên tắc Pete, không phải thay đổi cơ sở dữ liệu Pete.
3. `mechanisms.json` và `evidence.json`: giải thích sự biến đổi, control, hypothesis và nguồn riêng. `metrics.json` giữ tám contract; candidate sketch nằm trong thẻ.

Hành trình 8 bước là độ phân giải **quá trình**, không phải “độ sâu ontology = 8”. Hierarchy giao diện và số node không được dùng làm bằng chứng hiểu biết. 32 frontier là câu hỏi nghiên cứu chưa được giải, được đếm riêng khỏi cơ chế đã viết.

## Mở tiếp một node như thế nào?

Chọn một failure hoặc điều kiện chưa rõ, hỏi đối tượng thật ở đó là gì, rồi phân rã lại Input/Process/Output/Data. Chẳng hạn “cache quyền cũ” có thể mở thành: cache key; state version; read path; invalidation delivery; write-back race; expiry; replica consistency; quan sát version. Sau đó chọn hai trường hợp đối chiếu có ý nghĩa và một OPEN, không ép mọi vấn đề vào đúng hai khả năng.

Ví dụ thu hồi: có online check so với token tự chứa; OPEN là consumer offline. Cả hai có thể hợp lý tùy mục tiêu. Phải ghi cách trường hợp mới thay đổi yêu cầu và cách đo. Dừng cục bộ khi đã biết quyết định cần đưa ra, điều kiện áp dụng, test có thể phân biệt và điều gì sẽ buộc mở lại. Không đóng frontier chỉ vì viết được một câu trôi chảy.

## Trạng thái bằng chứng

Source discovered ≠ source read ≠ mechanism mapped ≠ test proposed ≠ test run ≠ production observed. Sổ nguồn ghi rõ nguồn nào mới đọc tổng quan, nguồn nào đã xem phần cụ thể. Tham chiếu một chương sách chỉ chỉ ra **nguồn ý tưởng**, không khẳng định mọi chi tiết kỹ thuật mở rộng đều có trong chương đó. Những đề xuất test là cho lab/diễn tập có phạm vi phù hợp; bản atlas không tự chạy scan, exploit hoặc tác động hệ thật.

`synthetic_examples.py` chỉ chạy phép tính và phản ví dụ bằng dữ liệu giả định. Nó kiểm tra logic đo, không kiểm tra tính hiệu lực của firewall, IAM, EDR hay agent production. Các test bỏ mắt xích nhân quả sẽ cho thấy một chỉ số thay đổi hay không; đó là bằng chứng về mô hình phép đo trong ví dụ, chưa phải định luật thực nghiệm về mọi tổ chức.

## Giới hạn cụ thể

Đây là atlas phân tích nền enterprise/app/cloud/agent với một nhánh OT, không phải catalog mọi CVE, toàn bộ ATT&CK hay tài liệu triển khai cho mọi hãng. Mobile, wireless, firmware, side-channel, privacy-preserving computation, telecom, sector-specific systems và một số nhánh AI còn ở frontier. Không có dữ liệu hạ tầng người dùng, calibrated probability, loss estimate, chứng nhận tuân thủ hoặc xác nhận control production. Việc mở rộng đã tạo nhiều câu hỏi có thể kiểm hơn, không xóa những giới hạn này.
