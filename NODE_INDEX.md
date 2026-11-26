# English node index

Revision: `r000002-fc8033e2e4fc67f3`. Canonical pointer: `graph/CURRENT`. Descriptions remain Vietnamese; previous labels are aliases.

| ID | English title | Type | Parent |
|---|---|---|---|
| `F01` | Side Channels and Hardware Roots of Trust | frontier | `crypto` |
| `F02` | Confidential Computing and Attestation | frontier | `crypto` |
| `F03` | Post-Quantum Cryptography | frontier | `crypto` |
| `F04` | Wi-Fi, Bluetooth, and Wireless Networks | frontier | `network` |
| `F05` | Interdomain Routing and BGP | frontier | `network` |
| `F06` | Mobile Platforms and Browser Extensions | frontier | `endpoint` |
| `F07` | Firmware, Boot, and Peripherals | frontier | `endpoint` |
| `F08` | Malware Analysis and Reverse Engineering | frontier | `endpoint` |
| `F09` | Browser Isolation and Cross-Origin Boundaries | frontier | `web` |
| `F10` | File Uploads and Multimedia Processing | frontier | `web` |
| `F11` | GraphQL and Query Planning | frontier | `api` |
| `F12` | Consensus and Distributed Systems | frontier | `api` |
| `F13` | Serverless and Ephemeral Workloads | frontier | `cloud` |
| `F14` | Multi-Cluster Systems and Service Meshes | frontier | `containers` |
| `F15` | Model and Dataset Supply Chains | frontier | `supply` |
| `F16` | Privacy Inference and Re-Identification | frontier | `data` |
| `F17` | Differential Privacy and Privacy Budgets | frontier | `data` |
| `F18` | Multiparty Computation and Federated Learning | frontier | `data` |
| `F19` | Vulnerability Disclosure and Bug Bounties | frontier | `vulnerability` |
| `F20` | Threat Intelligence | frontier | `detection` |
| `F21` | Deception and Honeypots | frontier | `detection` |
| `F22` | Crisis Communication | frontier | `response` |
| `F23` | Cyber Insurance and Security Economics | frontier | `governance` |
| `F24` | Legal Obligations and Certification | frontier | `governance` |
| `F25` | Insider Risk and Coercion | frontier | `human` |
| `F26` | Accessibility and Security Usability | frontier | `human` |
| `F27` | Telecommunications, Satellites, and National Infrastructure | frontier | `thirdparty` |
| `F28` | Medical Devices and Vehicles | frontier | `ot` |
| `F29` | Model and Data Poisoning | frontier | `agents` |
| `F30` | Model Extraction and Inference Leakage | frontier | `agents` |
| `F31` | Multi-Step and Multi-Principal Agents | frontier | `agents` |
| `F32` | Costs, Stop Conditions, and Automated Loops | frontier | `agents` |
| `J01` | End-to-End Authorization Revocation | journey | `identity` |
| `J01.1` | Identify Active Identity Bindings | step | `J01` |
| `J01.2` | Inventory Credentials and Grants | step | `J01` |
| `J01.3` | Commit the Revocation Epoch | step | `J01` |
| `J01.4` | Propagate State to Consumers | step | `J01` |
| `J01.5` | Invalidate Stale Authorization Caches | step | `J01` |
| `J01.6` | Prevent Refresh from Restoring Authority | step | `J01` |
| `J01.7` | Verify Denial across Tested Paths | step | `J01` |
| `J01.8` | Assess Consequences and False Denials | step | `J01` |
| `J02` | Cross-Tenant Authorization across Requests, Caches, and Jobs | journey | `authorization` |
| `J02.1` | Establish Actor and Tenant Claims | step | `J02` |
| `J02.2` | Resolve Objects within the Correct Domain | step | `J02` |
| `J02.3` | Evaluate Read, Write, and Share Permissions | step | `J02` |
| `J02.4` | Preserve Preconditions through Commit | step | `J02` |
| `J02.5` | Prevent Cross-Tenant Cache Reuse | step | `J02` |
| `J02.6` | Carry Scoped Authority into Asynchronous Jobs | step | `J02` |
| `J02.7` | Authorize Output Recipients | step | `J02` |
| `J02.8` | Retain Evidence Linking Actors to Actions | step | `J02` |
| `J03` | Supply Chain Integrity from Source to Runtime | journey | `supply` |
| `J03.1` | Pin Release Intent | step | `J03` |
| `J03.2` | Resolve Dependencies and Sources | step | `J03` |
| `J03.3` | Scope Builder Privileges | step | `J03` |
| `J03.4` | Bind Artifacts to Their Build Process | step | `J03` |
| `J03.5` | Evaluate Signing Trust and Residual Risk | step | `J03` |
| `J03.6` | Preserve Approved Artifact Identity | step | `J03` |
| `J03.7` | Enforce Policy at the Point of Use | step | `J03` |
| `J03.8` | Connect Runtime Inventory to Revocation | step | `J03` |
| `J04` | Ransomware Recovery and Shared Failure Domains | journey | `architecture` |
| `J04.1` | Define Critical Business Transactions | step | `J04` |
| `J04.2` | Identify Common Failure Domains | step | `J04` |
| `J04.3` | Select a Suitable Recovery Point | step | `J04` |
| `J04.4` | Bootstrap a Clean Recovery Environment | step | `J04` |
| `J04.5` | Recover Keys and Data | step | `J04` |
| `J04.6` | Reconcile Data Stores | step | `J04` |
| `J04.7` | Verify Business Operations End to End | step | `J04` |
| `J04.8` | Feed Recovery Findings into Design | step | `J04` |
| `J05` | From Events to Verified Response | journey | `telemetry` |
| `J05.1` | Define the Observation Population | step | `J05` |
| `J05.2` | Verify Sensor Signal Generation | step | `J05` |
| `J05.3` | Detect Transport Loss | step | `J05` |
| `J05.4` | Preserve Event Semantics through Parsing | step | `J05` |
| `J05.5` | Test Detection with Discriminating Cases | step | `J05` |
| `J05.6` | Manage Finite Alert Queues | step | `J05` |
| `J05.7` | Verify Response Effectiveness | step | `J05` |
| `J05.8` | Close the Observability Feedback Loop | step | `J05` |
| `J06` | Agent Authority from Untrusted Input to Observed Effects | journey | `agents` |
| `J06.1` | Define Task Authorization Scope | step | `J06` |
| `J06.2` | Keep External Sources Classified as Data | step | `J06` |
| `J06.3` | Treat Model Actions as Proposals | step | `J06` |
| `J06.4` | Enforce Authorization outside the Model | step | `J06` |
| `J06.5` | Bind Review to Immutable Action Content | step | `J06` |
| `J06.6` | Execute Tools within Resource Boundaries | step | `J06` |
| `J06.7` | Observe and Classify Outcomes | step | `J06` |
| `J06.8` | Prevent Unsupported Trust Promotion in Memory | step | `J06` |
| `J07` | From Scanner Findings to Contextual Priorities | journey | `vulnerability` |
| `J07.1` | Bind Findings to the Correct Assets | step | `J07` |
| `J07.2` | Verify Affected Components | step | `J07` |
| `J07.3` | Decompose Triggering Conditions | step | `J07` |
| `J07.4` | Establish Reachability Paths | step | `J07` |
| `J07.5` | Connect Controls to Consequences | step | `J07` |
| `J07.6` | Compare Remediation Options | step | `J07` |
| `J07.7` | Verify Post-Remediation State | step | `J07` |
| `J07.8` | Preserve Exposure History and Unknown Intervals | step | `J07` |
| `J08` | OT Commands and Physical State Transitions | journey | `ot` |
| `J08.1` | Define the Process and Safety Envelope | step | `J08` |
| `J08.2` | Bound Trust in Sensor Readings | step | `J08` |
| `J08.3` | Bind Commands to Actors and Purpose | step | `J08` |
| `J08.4` | Constrain Maintenance Access | step | `J08` |
| `J08.5` | Observe Controller and Actuator Effects | step | `J08` |
| `J08.6` | Define Safe Loss-of-Communication Behavior | step | `J08` |
| `J08.7` | Avoid New Hazards during Response | step | `J08` |
| `J08.8` | Verify Physical and Digital Recovery | step | `J08` |
| `action-approval` | Approval Bound to a Specific Action | mechanism | `ai-tool` |
| `action-digest` | Canonical Action Representation | mechanism | `action-approval` |
| `action-execution` | Tool Execution Contracts | mechanism | `ai-tool` |
| `action-observe` | Independent Post-Action Observation | mechanism | `action-execution` |
| `action-retry` | Retries after Ambiguous Outcomes | mechanism | `action-execution` |
| `action-toctou` | Post-Approval Context Changes | mechanism | `action-approval` |
| `agents` | AI Models and Tool-Using Agents | domain | `root` |
| `ai-instruction` | Prompt Injection and Authority | mechanism | `agents` |
| `ai-memory` | Memory, Retrieval, and Feedback | mechanism | `agents` |
| `ai-tool` | Agent Tool Invocation | mechanism | `agents` |
| `api` | APIs and Business Logic | domain | `root` |
| `api-abuse` | Abuse of Legitimate Functionality | mechanism | `api` |
| `api-retry` | Retries and Idempotency | mechanism | `api` |
| `api-state` | Business Invariants | mechanism | `api` |
| `arch-blast` | Blast Radius | mechanism | `architecture` |
| `arch-boundary` | Trust Boundary Enforcement | mechanism | `architecture` |
| `arch-failure` | Fail-Open and Fail-Closed Behavior | mechanism | `architecture` |
| `architecture` | Architecture and Trust Boundaries | domain | `root` |
| `auth-object` | Object-Level Authorization | mechanism | `authorization` |
| `auth-policy` | Effective Permissions | mechanism | `authorization` |
| `auth-race` | Commit-Time Authorization | mechanism | `authorization` |
| `authorization` | Authorization and Tenant Isolation | domain | `root` |
| `build-cache` | CI Caches across Trust Levels | mechanism | `sup-builder` |
| `build-secret` | Build-Stage Secret Grants | mechanism | `sup-builder` |
| `cld-drift` | Configuration Drift | mechanism | `cloud` |
| `cld-policy` | Control Plane Authority | mechanism | `cloud` |
| `cld-responsibility` | Cloud Shared Responsibility | mechanism | `cloud` |
| `cloud` | Cloud Control Planes | domain | `root` |
| `containers` | Containers and Kubernetes | domain | `root` |
| `cry-agility` | Cryptographic Agility | mechanism | `crypto` |
| `cry-integrity` | Encryption and Data Authentication | mechanism | `crypto` |
| `cry-key` | Key Lifecycle Management | mechanism | `crypto` |
| `crypto` | Cryptography and Key Lifecycles | domain | `root` |
| `dat-class` | Data Classification by Function | mechanism | `data` |
| `dat-egress` | Data Leakage at Output Boundaries | mechanism | `data` |
| `dat-retention` | Retention and Deletion | mechanism | `data` |
| `data` | Data, Privacy, and Retention | domain | `root` |
| `det-base` | Base Rates and Alert Quality | mechanism | `detection` |
| `det-behavior` | Behavior-Based Detection | mechanism | `detection` |
| `det-queue` | SOC Processing Capacity | mechanism | `detection` |
| `detection` | Detection and Signal Investigation | domain | `root` |
| `end-execution` | Execution Privileges and Isolation | mechanism | `endpoint` |
| `end-health` | Endpoint Control Health | mechanism | `endpoint` |
| `end-memory` | Memory Safety | mechanism | `endpoint` |
| `endpoint` | Endpoints and Execution Boundaries | domain | `root` |
| `gov-exception` | Time-Bounded Exceptions | mechanism | `governance` |
| `gov-loss` | Loss Scenarios | mechanism | `governance` |
| `gov-owner` | Decision Accountability | mechanism | `governance` |
| `governance` | Governance, Accountability, and Decisions | domain | `root` |
| `hum-access` | Physical Access and Device Custody | mechanism | `human` |
| `hum-offboard` | Offboarding and Role Changes | mechanism | `human` |
| `hum-report` | Incident Reporting Accessibility | mechanism | `human` |
| `human` | People and Physical Access | domain | `root` |
| `id-mfa` | MFA and Phishing Resistance | mechanism | `identity` |
| `id-proof` | Account-to-Subject Binding | mechanism | `identity` |
| `id-recovery` | Account Recovery | mechanism | `identity` |
| `identity` | Identity and Authentication | domain | `root` |
| `inv-dependency` | Critical Dependencies | mechanism | `inventory` |
| `inv-discovery` | Undiscovered Asset Detection | mechanism | `inventory` |
| `inv-lifecycle` | Asset Decommissioning | mechanism | `inventory` |
| `inventory` | Assets and Dependencies | domain | `root` |
| `ir-contain` | Authorized Containment | mechanism | `response` |
| `ir-evidence` | Evidence Collection and Chain of Custody | mechanism | `response` |
| `ir-learn` | Post-Incident Learning | mechanism | `response` |
| `k8s-admission` | Workload Creation and Admission | mechanism | `containers` |
| `k8s-identity` | Workload Identity | mechanism | `containers` |
| `k8s-network` | NetworkPolicy Enforcement | mechanism | `containers` |
| `messaging` | Email, DNS, and Messaging | domain | `root` |
| `msg-dns` | DNS Control Authority | mechanism | `messaging` |
| `msg-domain` | Sender Domain Authentication | mechanism | `messaging` |
| `msg-payment` | Payment Destination Changes | mechanism | `messaging` |
| `net-dos` | Resource Exhaustion and DDoS | mechanism | `network` |
| `net-egress` | Outbound Connection Control | mechanism | `network` |
| `net-segment` | Effective Network Segmentation | mechanism | `network` |
| `network` | Networks, Segmentation, and Egress | domain | `root` |
| `ot` | OT, IoT, and Physical Safety | domain | `root` |
| `ot-legacy` | Legacy Devices and Patch Constraints | mechanism | `ot` |
| `ot-remote` | Remote Maintenance | mechanism | `ot` |
| `ot-safety` | Safety under System Failure | mechanism | `ot` |
| `rec-backup` | Backup versus Recoverability | mechanism | `recovery` |
| `rec-consistency` | Recovery Consistency | mechanism | `recovery` |
| `rec-objective` | RTO, RPO, and Business Verification | mechanism | `recovery` |
| `recovery` | Recovery and Business Continuity | domain | `root` |
| `response` | Incident Response and Forensics | domain | `root` |
| `restore-cut` | Consistent Recovery Cuts across Stores | mechanism | `rec-consistency` |
| `restore-external` | External Side Effects during Recovery | mechanism | `rec-consistency` |
| `restore-reconcile` | Semantic Reconciliation after Restore | mechanism | `rec-consistency` |
| `revoke-cache` | Authorization Decision Caches | mechanism | `ses-revoke` |
| `revoke-cas` | Conditional Writes at Commit | mechanism | `revoke-race` |
| `revoke-fanout` | Revocation Consumer Coverage | mechanism | `ses-revoke` |
| `revoke-offline` | Offline Authorization Leases | mechanism | `ses-revoke` |
| `revoke-race` | Authorization Read and Cache Write Races | mechanism | `revoke-cache` |
| `revoke-version` | Authorization Version Monotonicity | mechanism | `revoke-cache` |
| `root` | Cybersecurity Mechanism Map | root | `—` |
| `ses-concurrency` | Sessions, Logout, and Devices | mechanism | `session` |
| `ses-issue` | Token Issuance and Audience Binding | mechanism | `session` |
| `ses-revoke` | Authorization Revocation Latency | mechanism | `session` |
| `session` | Sessions and Authorization Lifecycles | domain | `root` |
| `software` | Secure Software Development Lifecycle | domain | `root` |
| `sup-builder` | Build Integrity | mechanism | `supply` |
| `sup-dependency` | Dependencies and Source Trust | mechanism | `supply` |
| `sup-deploy` | Verification at Deployment | mechanism | `supply` |
| `supply` | Software Supply Chain | domain | `root` |
| `sw-design` | Security Requirements by Design | mechanism | `software` |
| `sw-release` | Release and Rollback | mechanism | `software` |
| `sw-testing` | Layered Security Testing | mechanism | `software` |
| `tel-coverage` | Observability Coverage | mechanism | `telemetry` |
| `tel-integrity` | Evidence Integrity | mechanism | `telemetry` |
| `tel-schema` | Event Semantics | mechanism | `telemetry` |
| `telemetry` | Observability and Evidence Reliability | domain | `root` |
| `tenant-cache` | Cache Keys and Authorization Dimensions | mechanism | `auth-object` |
| `tenant-context` | Tenant Context Authority | mechanism | `auth-object` |
| `tenant-delivery` | Authorization of Asynchronous Result Delivery | mechanism | `tenant-job` |
| `tenant-job` | Authority across Job Queues | mechanism | `auth-object` |
| `tenant-snapshot` | Submission-Time versus Execution-Time Authority | mechanism | `tenant-job` |
| `thirdparty` | Third Parties and Concentration Risk | domain | `root` |
| `tp-concentration` | Dependency Concentration | mechanism | `thirdparty` |
| `tp-exit` | Supplier Exit Capability | mechanism | `thirdparty` |
| `tp-scope` | Third-Party Permissions and Data Scope | mechanism | `thirdparty` |
| `verify-revocation` | Signer Revocation and Running Artifacts | mechanism | `sup-deploy` |
| `verify-root` | Verifier Trust Roots | mechanism | `sup-deploy` |
| `vul-context` | Severity versus Contextual Risk | mechanism | `vulnerability` |
| `vul-exposure` | Exposure Windows | mechanism | `vulnerability` |
| `vul-fix` | Remediation and Retesting | mechanism | `vulnerability` |
| `vulnerability` | Vulnerabilities and Exposure | domain | `root` |
| `web` | Web Applications and Input Interpretation | domain | `root` |
| `web-injection` | Data-to-Command Injection | mechanism | `web` |
| `web-parser` | Parser Discrepancies | mechanism | `web` |
| `web-xss` | Browser Output Contexts | mechanism | `web` |
