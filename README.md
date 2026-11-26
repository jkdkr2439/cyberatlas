# Cybersecurity — sơ đồ node cho AI

**Điểm vào: [AGENTS.md](AGENTS.md) và [AI_ENTRYPOINT.json](AI_ENTRYPOINT.json).** Không cần mở trình duyệt hay chạy server.

Đây là repo độc lập cho đồ thị node, CLI và bộ test. **Không kèm PDF hay bản đầy đủ của sách nguồn.** Nguồn ngoài repo được ghi bằng mã URN, hash và chỉ mục heading, không lưu đường dẫn máy cá nhân; đọc, cập nhật và kiểm tra graph không cần sách gốc.

Sau khi lấy repo:

```powershell
python -m pip install -r requirements.txt
python graph.py validate
python -m unittest test_graph validate test_hygiene -v
```

Chỉ phép đối chiếu hash với sách gốc sẽ được ghi nhận `skipped` nếu sách không có trên máy; các test graph vẫn chạy. `build.py` là công cụ dựng seed lịch sử, cần nguồn ngoài repo và không thuộc quy trình dùng repo bình thường. Repo đã chứa seed cùng các snapshot hiện hành, nên không cần chạy lại build/init.

Trước khi commit, có thể chạy `python scripts/verify_checkout.py` để kiểm tra các file đã stage trong một checkout tạm: kiểm graph, chạy test khi tắt truy cập sách nguồn, và xác nhận không đưa PDF/DOCX vào repo. Các snapshot có checksum được giữ nguyên byte qua Git bằng `.gitattributes`.

Chạy `python scripts/audit_repository.py --history` để rà path cá nhân, mẫu credential và file nguồn bị cấm trong repo/lịch sử Git. Xem [REPOSITORY_HYGIENE.md](REPOSITORY_HYGIENE.md) về phạm vi quét và cấu hình nguồn ngoài repo.

Đã mở sách **Hệ miễn dịch của thế giới số** bằng Metric Generation thành đồ thị có **233 node và 432 quan hệ**: 26 miền, 102 thẻ cơ chế (24 thẻ phân rã con), 8 hành trình với 64 bước, 32 frontier và một root. Có 102 metric sketch, 8 contract chi tiết. Các phép đếm này mô tả bản đồ, không đo mức an toàn.

Nguồn dữ liệu hiện hành là [graph/CURRENT](graph/CURRENT). Mỗi phiên bản chứa từng node trong một file JSON, các cạnh JSONL có kiểu/điều kiện, metric contracts, sources và các projection IO tách khỏi process/evidence. Cây sâu nhất hiện có 5 cạnh từ root (6 cấp); độ dài hành trình được đếm riêng.

**Tên của toàn bộ 233 node và 8 metric contract đã đổi sang tiếng Anh.** ID và 432 quan hệ được giữ nguyên. Tên Việt cũ nằm trong aliases để tìm kiếm; phần giải thích vẫn bằng tiếng Việt. Xem [NODE_INDEX.md](NODE_INDEX.md) để đọc nhanh tên và cấu trúc cha–con.

Một nhánh ví dụ:

```text
root
└─ session
   └─ ses-revoke
      ├─ revoke-fanout
      ├─ revoke-offline
      └─ revoke-cache
         ├─ revoke-version
         └─ revoke-race
            └─ revoke-cas
```

AI có thể đọc theo nhu cầu:

Runtime đã dùng: Python 3.12.10, jsonschema 4.23.0. Máy hiện tại đã có đủ dependency; file requirements.txt dùng để tái lập ở nơi khác.

```powershell
python graph.py search "thu hoi" --type mechanism
python graph.py get revoke-cas
python graph.py children ses-revoke
python graph.py metric M01
python graph.py validate
```

`get` trả node đầy đủ, ngữ cảnh cha, cạnh liên quan và tóm tắt hàng xóm; không buộc nạp cả atlas. Cập nhật bằng patch có `expected_revision`, kiểm schema/liên kết trước khi commit, giữ phiên bản cũ và từ chối cập nhật dựa trên phiên bản lỗi thời. Xem quy trình trong AGENTS.md.

- [Export JSONL cho AI](exports/cybersecurity.nodes.jsonl) — portable snapshot có ghi revision.
- [Kết quả test](VALIDATION.md) — kiểm cấu trúc, cập nhật, đọc cục bộ và ví dụ giả định.
- [Phương pháp](METHOD.md) — NMF/IPOD/CV/resources, sáu miền metric và giới hạn.
- [Sổ nguồn](SOURCES.md) — sách, Metric Generation và nguồn chuyên ngành, kèm phạm vi đã đọc.
- [Bản thuyết minh seed](ATLAS.md), [các hành trình](DEEP_DIVES.md), [metric contracts](METRIC_PROFILES.md), [frontier](FRONTIERS.md) — tài liệu lần import đầu; khi có cập nhật, graph/CURRENT được ưu tiên.

Chưa có dữ liệu hệ thống thực tế. Cơ chế và test trong node là phân tích/đề xuất; 9 ví dụ chạy bằng số liệu giả định. Nguồn sách gốc không bị sửa. Những nhánh chưa đủ chi tiết được giữ OPEN để AI tiếp tục đào có điều kiện.
