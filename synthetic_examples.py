"""Discriminating measurement examples. All values are synthetic; no security scans."""
from pathlib import Path
import json, statistics

ROOT=Path(__file__).resolve().parent

def ratio(n,d):
    if n<0 or d<0 or n>d:
        raise ValueError('Invalid subset counts')
    return None if d==0 else n/d

def duration_union(intervals, start, end):
    clipped=sorted((max(a,start),min(b,end)) for a,b in intervals if max(a,start)<min(b,end))
    result=[]
    for a,b in clipped:
        if result and a<=result[-1][1]: result[-1]=(result[-1][0],max(b,result[-1][1]))
        else: result.append((a,b))
    return sum(b-a for a,b in result)

def run():
    examples=[]
    def add(name,inputs,outputs,lesson):
        examples.append(dict(name=name,inputs=inputs,outputs=outputs,lesson=lesson,synthetic=True))
    # Changing base rate while leaving detector characteristics fixed.
    def precision_at(prevalence):
        tp=100000*prevalence*.99; fp=100000*(1-prevalence)*.01
        return tp/(tp+fp)
    low=precision_at(.001); high=precision_at(.1)
    assert low<.1 and high>.9
    add('Cùng detector, khác prevalence',{'population':100000,'sensitivity':.99,'false_positive_rate':.01,'prevalence':[.001,.1]},
        {'precision_rare':low,'precision_common':high},'Precision đổi từ khoảng 9% lên 91,7% khi prevalence thay, dù sensitivity/FPR giữ nguyên. Không mang một tỷ lệ đẹp sang frame khác.')
    # Removing missing sources from denominator creates false coverage improvement.
    honest=ratio(9,10); biased=ratio(9,9)
    assert honest==.9 and biased==1 and ratio(0,0) is None
    add('Nguồn im lặng không phải nguồn an toàn',{'expected_sources':10,'healthy':9,'missing':1},
        {'honest_coverage':honest,'observed_only_bias':biased,'empty_population':ratio(0,0)},'Coverage thật trên registry là 90%, không phải 100%; chưa biết gì về sự kiện ở nguồn mất. D=0 là undefined.')
    # A KPI can improve while the critical scenario does not.
    critical=set(range(5)); all_assets=set(range(100)); plan_a=all_assets-critical; plan_b=critical
    a_critical_hours=len(critical-plan_a)*8; b_critical_hours=len(critical-plan_b)*8
    assert len(plan_a)>len(plan_b) and a_critical_hours>b_critical_hours
    add('Đóng nhiều ticket không đồng nghĩa giảm đúng phơi nhiễm',{'assets':100,'critical':5,'window_hours':8,'assumption':'Mỗi asset có cùng một vulnerability và reachable trong 8 giờ nếu chưa sửa'},
        {'A_patched_fraction':len(plan_a)/100,'B_patched_fraction':len(plan_b)/100,'A_critical_exposure_hours':a_critical_hours,'B_critical_exposure_hours':b_critical_hours},
        'A vá 95% nhưng để lại 40 giờ phơi nhiễm critical; B vá 5% và xóa phần phơi nhiễm critical trong giả định. Chưa kết luận B tối ưu toàn bộ vì chưa biết tổn thất/cost của 95 asset khác.')
    completed=[2,4]; censored_count=3; observation_end=30
    complete_median=statistics.median(completed)
    cohort_mean_lower_bound=(sum(completed)+censored_count*observation_end)/5
    assert complete_median==3 and cohort_mean_lower_bound==19.2
    add('Chỉ lấy ca hoàn thành làm thời gian thu hồi đẹp giả',{'completed_seconds':completed,'still_allowed_at_30s':censored_count},
        {'completed_only_median_seconds':complete_median,'cohort_mean_lower_bound_seconds':cohort_mean_lower_bound,'cohort_median':'chưa quan sát được; lớn hơn 30 giây'},
        'Median 3 giây chỉ thuộc hai ca xong. Ba ca còn quyền sau 30 giây làm median toàn cohort chưa xác định trong cửa sổ. Không loại ca xấu nhất khỏi mẫu.')
    total=duration_union([(0,3),(2,5)],0,8); unknown=duration_union([(5,8)],0,8)
    assert total==5 and unknown==3 and duration_union([(-3,1),(7,20)],0,8)==2
    add('Hợp interval và giữ unknown',{'exposed_intervals_hours':[[0,3],[2,5]],'unknown_intervals_hours':[[5,8]],'window':[0,8]},
        {'exposed_pair_hours':total,'unknown_pair_hours':unknown,'incorrect_raw_sum':6},
        'Hai quan sát overlap tạo 5 giờ phơi nhiễm, không phải 6. Ba giờ sau đó chưa biết, không được coi là hết phơi nhiễm. Các state loại trừ nhau phải được đối soát trước tổng hợp.')
    rto=60; server_up=30; business_accept=90; rpo=10; loss=5
    pass_recovery=business_accept<=rto and loss<=rpo
    assert server_up<=rto and not pass_recovery
    add('Server lên khác với nghiệp vụ phục hồi',{'RTO_minutes':rto,'RPO_minutes':rpo,'server_up_minutes':server_up,'business_acceptance_minutes':business_accept,'data_loss_minutes':loss},
        {'server_only_pass':True,'end_to_end_pass':pass_recovery},'Đạt RPO nhưng vượt RTO. Dùng mốc server-up sẽ đánh giá sai toàn bộ quá trình phục hồi.')
    enrolled=100; weak_recovery=20
    add('MFA enrollment và coverage của toàn hành trình',{'accounts':100,'MFA_enrolled':enrolled,'accounts_with_weak_recovery':weak_recovery},
        {'enrollment':1.0,'accounts_with_identified_recovery_gap':.2},'100% đăng ký MFA vẫn có 20% account mang đường recovery chưa đạt yêu cầu. Đây là gap cấu hình giả định, không phải xác suất bị chiếm là 20%.')
    bad_proposals=20; blocked=18; executed=bad_proposals-blocked
    assert executed==2
    add('Agent đề xuất sai và thực thi sai là hai kết quả',{'trials':100,'bad_tool_proposals':bad_proposals,'gateway_blocked':blocked},
        {'bad_proposal_rate':bad_proposals/100,'unauthorized_execution_rate':executed/100},'Gateway thay đổi hậu quả của proposal. Chỉ đo model refusal hoặc tool schema sẽ không đo đúng authority boundary.')
    # A signer check alone fails to enforce intended source identity.
    artifacts=[{'signed':True,'allowed_builder':True},{'signed':True,'allowed_builder':False}]
    naive=[a['signed'] for a in artifacts]; scoped=[a['signed'] and a['allowed_builder'] for a in artifacts]
    assert naive==[True,True] and scoped==[True,False]
    add('Chữ ký hợp lệ không thay deployment policy',{'artifacts':artifacts},
        {'signature_only_accept':naive,'signature_and_builder_accept':scoped},'Thay đúng một điều kiện builder làm policy tách hai artifact đều có chữ ký. Ví dụ Boolean này không xác minh chữ ký mật mã thực tế.')
    (ROOT/'data/synthetic_examples.json').write_text(json.dumps(examples,ensure_ascii=False,indent=2),encoding='utf-8')
    out=['# Phản ví dụ tính toán — toàn bộ số liệu giả định\n','Chương trình chỉ kiểm logic phép đo. Không có scan, thử tấn công hoặc đo hạ tầng thật.\n']
    for i,e in enumerate(examples,1):
        out += [f'## {i}. {e["name"]}\n','```json\n'+json.dumps({'input':e['inputs'],'output':e['outputs']},ensure_ascii=False,indent=2)+'\n```\n',e['lesson']+'\n']
    (ROOT/'SYNTHETIC_EXAMPLES.md').write_text('\n'.join(out),encoding='utf-8')
    return examples

if __name__=='__main__':
    print(json.dumps({'examples_passed':len(run()),'data':'synthetic_only'},ensure_ascii=False))
