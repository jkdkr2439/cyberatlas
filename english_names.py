"""Reviewed English labels; stable IDs and analytical content remain unchanged."""
NAMES = '''
root|Cybersecurity Mechanism Map
governance|Governance, Accountability, and Decisions
inventory|Assets and Dependencies
architecture|Architecture and Trust Boundaries
identity|Identity and Authentication
session|Sessions and Authorization Lifecycles
authorization|Authorization and Tenant Isolation
crypto|Cryptography and Key Lifecycles
network|Networks, Segmentation, and Egress
messaging|Email, DNS, and Messaging
endpoint|Endpoints and Execution Boundaries
web|Web Applications and Input Interpretation
api|APIs and Business Logic
cloud|Cloud Control Planes
containers|Containers and Kubernetes
software|Secure Software Development Lifecycle
supply|Software Supply Chain
data|Data, Privacy, and Retention
vulnerability|Vulnerabilities and Exposure
telemetry|Observability and Evidence Reliability
detection|Detection and Signal Investigation
response|Incident Response and Forensics
recovery|Recovery and Business Continuity
ot|OT, IoT, and Physical Safety
human|People and Physical Access
thirdparty|Third Parties and Concentration Risk
agents|AI Models and Tool-Using Agents
gov-owner|Decision Accountability
gov-exception|Time-Bounded Exceptions
gov-loss|Loss Scenarios
inv-discovery|Undiscovered Asset Detection
inv-dependency|Critical Dependencies
inv-lifecycle|Asset Decommissioning
arch-boundary|Trust Boundary Enforcement
arch-blast|Blast Radius
arch-failure|Fail-Open and Fail-Closed Behavior
id-proof|Account-to-Subject Binding
id-mfa|MFA and Phishing Resistance
id-recovery|Account Recovery
ses-issue|Token Issuance and Audience Binding
ses-revoke|Authorization Revocation Latency
ses-concurrency|Sessions, Logout, and Devices
auth-object|Object-Level Authorization
auth-policy|Effective Permissions
auth-race|Commit-Time Authorization
cry-key|Key Lifecycle Management
cry-integrity|Encryption and Data Authentication
cry-agility|Cryptographic Agility
net-segment|Effective Network Segmentation
net-egress|Outbound Connection Control
net-dos|Resource Exhaustion and DDoS
msg-domain|Sender Domain Authentication
msg-payment|Payment Destination Changes
msg-dns|DNS Control Authority
end-health|Endpoint Control Health
end-execution|Execution Privileges and Isolation
end-memory|Memory Safety
web-injection|Data-to-Command Injection
web-xss|Browser Output Contexts
web-parser|Parser Discrepancies
api-state|Business Invariants
api-retry|Retries and Idempotency
api-abuse|Abuse of Legitimate Functionality
cld-responsibility|Cloud Shared Responsibility
cld-policy|Control Plane Authority
cld-drift|Configuration Drift
k8s-admission|Workload Creation and Admission
k8s-identity|Workload Identity
k8s-network|NetworkPolicy Enforcement
sw-design|Security Requirements by Design
sw-testing|Layered Security Testing
sw-release|Release and Rollback
sup-dependency|Dependencies and Source Trust
sup-builder|Build Integrity
sup-deploy|Verification at Deployment
dat-class|Data Classification by Function
dat-retention|Retention and Deletion
dat-egress|Data Leakage at Output Boundaries
vul-context|Severity versus Contextual Risk
vul-fix|Remediation and Retesting
vul-exposure|Exposure Windows
tel-coverage|Observability Coverage
tel-schema|Event Semantics
tel-integrity|Evidence Integrity
det-base|Base Rates and Alert Quality
det-behavior|Behavior-Based Detection
det-queue|SOC Processing Capacity
ir-contain|Authorized Containment
ir-evidence|Evidence Collection and Chain of Custody
ir-learn|Post-Incident Learning
rec-backup|Backup versus Recoverability
rec-objective|RTO, RPO, and Business Verification
rec-consistency|Recovery Consistency
ot-safety|Safety under System Failure
ot-legacy|Legacy Devices and Patch Constraints
ot-remote|Remote Maintenance
hum-report|Incident Reporting Accessibility
hum-access|Physical Access and Device Custody
hum-offboard|Offboarding and Role Changes
tp-scope|Third-Party Permissions and Data Scope
tp-concentration|Dependency Concentration
tp-exit|Supplier Exit Capability
ai-instruction|Prompt Injection and Authority
ai-tool|Agent Tool Invocation
ai-memory|Memory, Retrieval, and Feedback
revoke-fanout|Revocation Consumer Coverage
revoke-cache|Authorization Decision Caches
revoke-version|Authorization Version Monotonicity
revoke-race|Authorization Read and Cache Write Races
revoke-cas|Conditional Writes at Commit
revoke-offline|Offline Authorization Leases
tenant-context|Tenant Context Authority
tenant-cache|Cache Keys and Authorization Dimensions
tenant-job|Authority across Job Queues
tenant-snapshot|Submission-Time versus Execution-Time Authority
tenant-delivery|Authorization of Asynchronous Result Delivery
build-cache|CI Caches across Trust Levels
build-secret|Build-Stage Secret Grants
verify-root|Verifier Trust Roots
verify-revocation|Signer Revocation and Running Artifacts
action-approval|Approval Bound to a Specific Action
action-digest|Canonical Action Representation
action-toctou|Post-Approval Context Changes
action-execution|Tool Execution Contracts
action-retry|Retries after Ambiguous Outcomes
action-observe|Independent Post-Action Observation
restore-cut|Consistent Recovery Cuts across Stores
restore-reconcile|Semantic Reconciliation after Restore
restore-external|External Side Effects during Recovery
F01|Side Channels and Hardware Roots of Trust
F02|Confidential Computing and Attestation
F03|Post-Quantum Cryptography
F04|Wi-Fi, Bluetooth, and Wireless Networks
F05|Interdomain Routing and BGP
F06|Mobile Platforms and Browser Extensions
F07|Firmware, Boot, and Peripherals
F08|Malware Analysis and Reverse Engineering
F09|Browser Isolation and Cross-Origin Boundaries
F10|File Uploads and Multimedia Processing
F11|GraphQL and Query Planning
F12|Consensus and Distributed Systems
F13|Serverless and Ephemeral Workloads
F14|Multi-Cluster Systems and Service Meshes
F15|Model and Dataset Supply Chains
F16|Privacy Inference and Re-Identification
F17|Differential Privacy and Privacy Budgets
F18|Multiparty Computation and Federated Learning
F19|Vulnerability Disclosure and Bug Bounties
F20|Threat Intelligence
F21|Deception and Honeypots
F22|Crisis Communication
F23|Cyber Insurance and Security Economics
F24|Legal Obligations and Certification
F25|Insider Risk and Coercion
F26|Accessibility and Security Usability
F27|Telecommunications, Satellites, and National Infrastructure
F28|Medical Devices and Vehicles
F29|Model and Data Poisoning
F30|Model Extraction and Inference Leakage
F31|Multi-Step and Multi-Principal Agents
F32|Costs, Stop Conditions, and Automated Loops
J01|End-to-End Authorization Revocation
J01.1|Identify Active Identity Bindings
J01.2|Inventory Credentials and Grants
J01.3|Commit the Revocation Epoch
J01.4|Propagate State to Consumers
J01.5|Invalidate Stale Authorization Caches
J01.6|Prevent Refresh from Restoring Authority
J01.7|Verify Denial across Tested Paths
J01.8|Assess Consequences and False Denials
J02|Cross-Tenant Authorization across Requests, Caches, and Jobs
J02.1|Establish Actor and Tenant Claims
J02.2|Resolve Objects within the Correct Domain
J02.3|Evaluate Read, Write, and Share Permissions
J02.4|Preserve Preconditions through Commit
J02.5|Prevent Cross-Tenant Cache Reuse
J02.6|Carry Scoped Authority into Asynchronous Jobs
J02.7|Authorize Output Recipients
J02.8|Retain Evidence Linking Actors to Actions
J03|Supply Chain Integrity from Source to Runtime
J03.1|Pin Release Intent
J03.2|Resolve Dependencies and Sources
J03.3|Scope Builder Privileges
J03.4|Bind Artifacts to Their Build Process
J03.5|Evaluate Signing Trust and Residual Risk
J03.6|Preserve Approved Artifact Identity
J03.7|Enforce Policy at the Point of Use
J03.8|Connect Runtime Inventory to Revocation
J04|Ransomware Recovery and Shared Failure Domains
J04.1|Define Critical Business Transactions
J04.2|Identify Common Failure Domains
J04.3|Select a Suitable Recovery Point
J04.4|Bootstrap a Clean Recovery Environment
J04.5|Recover Keys and Data
J04.6|Reconcile Data Stores
J04.7|Verify Business Operations End to End
J04.8|Feed Recovery Findings into Design
J05|From Events to Verified Response
J05.1|Define the Observation Population
J05.2|Verify Sensor Signal Generation
J05.3|Detect Transport Loss
J05.4|Preserve Event Semantics through Parsing
J05.5|Test Detection with Discriminating Cases
J05.6|Manage Finite Alert Queues
J05.7|Verify Response Effectiveness
J05.8|Close the Observability Feedback Loop
J06|Agent Authority from Untrusted Input to Observed Effects
J06.1|Define Task Authorization Scope
J06.2|Keep External Sources Classified as Data
J06.3|Treat Model Actions as Proposals
J06.4|Enforce Authorization outside the Model
J06.5|Bind Review to Immutable Action Content
J06.6|Execute Tools within Resource Boundaries
J06.7|Observe and Classify Outcomes
J06.8|Prevent Unsupported Trust Promotion in Memory
J07|From Scanner Findings to Contextual Priorities
J07.1|Bind Findings to the Correct Assets
J07.2|Verify Affected Components
J07.3|Decompose Triggering Conditions
J07.4|Establish Reachability Paths
J07.5|Connect Controls to Consequences
J07.6|Compare Remediation Options
J07.7|Verify Post-Remediation State
J07.8|Preserve Exposure History and Unknown Intervals
J08|OT Commands and Physical State Transitions
J08.1|Define the Process and Safety Envelope
J08.2|Bound Trust in Sensor Readings
J08.3|Bind Commands to Actors and Purpose
J08.4|Constrain Maintenance Access
J08.5|Observe Controller and Actuator Effects
J08.6|Define Safe Loss-of-Communication Behavior
J08.7|Avoid New Hazards during Response
J08.8|Verify Physical and Digital Recovery
'''.strip()

METRIC_NAMES={
 'M01':'Revocation Latency by Authorization Path',
 'M02':'Verified Object Authorization Matrix',
 'M03':'Deployment-Time Provenance Enforcement',
 'M04':'End-to-End Business Transaction Recoverability',
 'M05':'Detection Quality and Observation Coverage',
 'M06':'Authority Invariance under Untrusted Content Changes',
 'M07':'Observed Exposure Hours and Unknown Intervals',
 'M08':'Physical Deviations after Commands and Communication Loss'
}

def prepare():
    import copy, json
    from pathlib import Path
    import graph
    pairs=[line.split('|') for line in NAMES.splitlines()]
    labels=dict(pairs)
    assert len(labels)==len(pairs),'duplicate translation IDs'
    revision,data=graph.load(graph.DEFAULT_STORE)
    assert set(labels)=={n['id'] for n in data['nodes']}, {'missing':set(n['id'] for n in data['nodes'])-set(labels),'extra':set(labels)-set(n['id'] for n in data['nodes'])}
    nodes=[]
    for old in data['nodes']:
        n=copy.deepcopy(old)
        n['aliases']=list(dict.fromkeys(n.get('aliases',[])+([n['title']] if n['title']!=labels[n['id']] else [])))
        n['title']=labels[n['id']];n['title_language']='en';n['content_language']='vi'
        nodes.append(n)
    metrics=[]
    for old in data['metrics']:
        m=copy.deepcopy(old);m['aliases']=list(dict.fromkeys(m.get('aliases',[])+([m['title']] if m['title']!=METRIC_NAMES[m['id']] else [])))
        m['title']=METRIC_NAMES[m['id']];m['title_language']='en';metrics.append(m)
    patch={'expected_revision':revision,'reason':'User requested English node names. Preserve IDs, relationships and analytical content; retain previous labels as search aliases.','upsert_nodes':nodes,'upsert_metrics':metrics}
    output=Path(__file__).resolve().parent/'patches/english-node-names.json'
    output.parent.mkdir(exist_ok=True);output.write_text(graph.pretty(patch),encoding='utf-8')
    print(json.dumps({'nodes':len(nodes),'metrics':len(metrics),'patch':str(output),'expected_revision':revision}))

if __name__=='__main__':prepare()
