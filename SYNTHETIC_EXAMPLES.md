# Phản ví dụ tính toán — toàn bộ số liệu giả định

Chương trình chỉ kiểm logic phép đo. Không có scan, thử tấn công hoặc đo hạ tầng thật.

## 1. Cùng detector, khác prevalence

```json
{
  "input": {
    "population": 100000,
    "sensitivity": 0.99,
    "false_positive_rate": 0.01,
    "prevalence": [
      0.001,
      0.1
    ]
  },
  "output": {
    "precision_rare": 0.09016393442622951,
    "precision_common": 0.9166666666666666
  }
}
```

Precision đổi từ khoảng 9% lên 91,7% khi prevalence thay, dù sensitivity/FPR giữ nguyên. Không mang một tỷ lệ đẹp sang frame khác.

## 2. Nguồn im lặng không phải nguồn an toàn

```json
{
  "input": {
    "expected_sources": 10,
    "healthy": 9,
    "missing": 1
  },
  "output": {
    "honest_coverage": 0.9,
    "observed_only_bias": 1.0,
    "empty_population": null
  }
}
```

Coverage thật trên registry là 90%, không phải 100%; chưa biết gì về sự kiện ở nguồn mất. D=0 là undefined.

## 3. Đóng nhiều ticket không đồng nghĩa giảm đúng phơi nhiễm

```json
{
  "input": {
    "assets": 100,
    "critical": 5,
    "window_hours": 8,
    "assumption": "Mỗi asset có cùng một vulnerability và reachable trong 8 giờ nếu chưa sửa"
  },
  "output": {
    "A_patched_fraction": 0.95,
    "B_patched_fraction": 0.05,
    "A_critical_exposure_hours": 40,
    "B_critical_exposure_hours": 0
  }
}
```

A vá 95% nhưng để lại 40 giờ phơi nhiễm critical; B vá 5% và xóa phần phơi nhiễm critical trong giả định. Chưa kết luận B tối ưu toàn bộ vì chưa biết tổn thất/cost của 95 asset khác.

## 4. Chỉ lấy ca hoàn thành làm thời gian thu hồi đẹp giả

```json
{
  "input": {
    "completed_seconds": [
      2,
      4
    ],
    "still_allowed_at_30s": 3
  },
  "output": {
    "completed_only_median_seconds": 3.0,
    "cohort_mean_lower_bound_seconds": 19.2,
    "cohort_median": "chưa quan sát được; lớn hơn 30 giây"
  }
}
```

Median 3 giây chỉ thuộc hai ca xong. Ba ca còn quyền sau 30 giây làm median toàn cohort chưa xác định trong cửa sổ. Không loại ca xấu nhất khỏi mẫu.

## 5. Hợp interval và giữ unknown

```json
{
  "input": {
    "exposed_intervals_hours": [
      [
        0,
        3
      ],
      [
        2,
        5
      ]
    ],
    "unknown_intervals_hours": [
      [
        5,
        8
      ]
    ],
    "window": [
      0,
      8
    ]
  },
  "output": {
    "exposed_pair_hours": 5,
    "unknown_pair_hours": 3,
    "incorrect_raw_sum": 6
  }
}
```

Hai quan sát overlap tạo 5 giờ phơi nhiễm, không phải 6. Ba giờ sau đó chưa biết, không được coi là hết phơi nhiễm. Các state loại trừ nhau phải được đối soát trước tổng hợp.

## 6. Server lên khác với nghiệp vụ phục hồi

```json
{
  "input": {
    "RTO_minutes": 60,
    "RPO_minutes": 10,
    "server_up_minutes": 30,
    "business_acceptance_minutes": 90,
    "data_loss_minutes": 5
  },
  "output": {
    "server_only_pass": true,
    "end_to_end_pass": false
  }
}
```

Đạt RPO nhưng vượt RTO. Dùng mốc server-up sẽ đánh giá sai toàn bộ quá trình phục hồi.

## 7. MFA enrollment và coverage của toàn hành trình

```json
{
  "input": {
    "accounts": 100,
    "MFA_enrolled": 100,
    "accounts_with_weak_recovery": 20
  },
  "output": {
    "enrollment": 1.0,
    "accounts_with_identified_recovery_gap": 0.2
  }
}
```

100% đăng ký MFA vẫn có 20% account mang đường recovery chưa đạt yêu cầu. Đây là gap cấu hình giả định, không phải xác suất bị chiếm là 20%.

## 8. Agent đề xuất sai và thực thi sai là hai kết quả

```json
{
  "input": {
    "trials": 100,
    "bad_tool_proposals": 20,
    "gateway_blocked": 18
  },
  "output": {
    "bad_proposal_rate": 0.2,
    "unauthorized_execution_rate": 0.02
  }
}
```

Gateway thay đổi hậu quả của proposal. Chỉ đo model refusal hoặc tool schema sẽ không đo đúng authority boundary.

## 9. Chữ ký hợp lệ không thay deployment policy

```json
{
  "input": {
    "artifacts": [
      {
        "signed": true,
        "allowed_builder": true
      },
      {
        "signed": true,
        "allowed_builder": false
      }
    ]
  },
  "output": {
    "signature_only_accept": [
      true,
      true
    ],
    "signature_and_builder_accept": [
      true,
      false
    ]
  }
}
```

Thay đúng một điều kiện builder làm policy tách hai artifact đều có chữ ký. Ví dụ Boolean này không xác minh chữ ký mật mã thực tế.
