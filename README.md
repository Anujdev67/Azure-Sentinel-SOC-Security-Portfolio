# 🛡️ Azure Sentinel & SOC Security Portfolio

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Azure](https://img.shields.io/badge/Azure-Sentinel-0078D4?logo=microsoft-azure)](https://azure.microsoft.com/en-us/products/microsoft-sentinel/)
[![KQL](https://img.shields.io/badge/Language-KQL-00A4EF)](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![SC-200](https://img.shields.io/badge/Exam-SC--200-green)](https://learn.microsoft.com/en-us/certifications/security-operations-analyst/)

A comprehensive, production-ready security portfolio for **SOC Analysts**, **Threat Hunters**, and **Cloud Security Engineers**. Perfect for **SC-200** and **Azure Security** certification preparation.

> **📌 Created by**: Security Operations Analyst | **Experience**: 1+ years SOC/Azure Security | **Focus**: Threat Hunting, Detection Engineering, Incident Response

---

## 🎯 Quick Links

- 📖 [KQL Hunting Queries](#kql-hunting-queries) - 20+ production-ready queries
- 🎯 [Detection Engineering](#detection-engineering) - Custom alert rules
- 🤖 [Automation Scripts](#automation-scripts) - Python security tools
- 🏗️ [Azure Infrastructure](#azure-infrastructure) - Terraform templates
- 📚 [SC-200 Study Guide](#sc-200-certification-guide) - Exam prep materials
- 🚨 [Incident Response](#incident-response-playbooks) - Real-world playbooks

---

## 📚 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [KQL Hunting Queries](#kql-hunting-queries)
- [Detection Engineering](#detection-engineering)
- [Automation Scripts](#automation-scripts)
- [Azure Security Infrastructure](#azure-security-infrastructure)
- [Getting Started](#getting-started)
- [SC-200 Certification Guide](#sc-200-certification-guide)
- [Incident Response Playbooks](#incident-response-playbooks)
- [Case Studies](#case-studies)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This repository contains **production-ready security detection rules, threat hunting queries, automation scripts, and infrastructure-as-code** for:

- ✅ **Azure Sentinel** - SIEM threat detection and hunting
- ✅ **Microsoft Defender XDR** - Advanced threat protection
- ✅ **Incident Response** - Automated response workflows
- ✅ **Threat Hunting** - Proactive threat discovery
- ✅ **Detection Engineering** - Custom detection rules
- ✅ **Azure Security** - Infrastructure hardening
- ✅ **Compliance** - CIS benchmarks, regulatory requirements
- ✅ **SC-200 Exam Prep** - Certification study materials

**Ideal for**: SOC Analysts, Threat Hunters, Security Operations Engineers, Cloud Security Engineers, and SIEM administrators.

---

## ⭐ Features

✅ **Production-Ready** - Tested in real SOC environments  
✅ **Well-Documented** - Comprehensive guides and examples  
✅ **MITRE ATT&CK Mapped** - Aligned with threat framework  
✅ **Compliance-Focused** - CIS, SOC 2, Azure security standards  
✅ **Certification-Ready** - SC-200 and Azure Security exam prep  
✅ **Community-Driven** - Contributions welcome  
✅ **GitHub Actions** - Automated testing and validation  
✅ **LinkedIn-Shareable** - Professional portfolio quality  

---

## 📁 Repository Structure

```
Azure-Sentinel-SOC-Security-Portfolio/
│
├── 📂 kql-queries/                    # KQL Hunting Queries (20+)
│   ├── threat-hunting/
│   │   ├── command_line_exploitation.kql
│   │   ├── lateral_movement_detection.kql
│   │   ├── privilege_escalation.kql
│   │   ├── data_exfiltration.kql
│   │   ├── reconnaissance_patterns.kql
│   │   └── README.md
│   ├── incident-response/
│   │   ├── user_account_investigation.kql
│   │   ├── account_timeline.kql
│   │   ├── evidence_collection.kql
│   │   └── threat_actor_profiling.kql
│   ├── detection-rules/
│   │   ├── mitre_attck_mapping.kql
│   │   ├── anomalous_authentication.kql
│   │   ├── network_exploitation.kql
│   │   └── persistence_techniques.kql
│   └── README.md
│
├── 📂 detection-engineering/          # Detection Rules & Configurations
│   ├── alert-rules/
│   │   ├── critical_alerts.json
│   │   ├── high_priority_alerts.json
│   │   └── incident_rules.yaml
│   ├── detection-templates/
│   │   ├── rule_template.json
│   │   └── validation_schema.json
│   └── README.md
│
├── 📂 automation-scripts/             # Python Automation
│   ├── incident-response/
│   │   ├── ir_automation.py
│   │   ├── evidence_collector.py
│   │   └── timeline_builder.py
│   ├── log-analysis/
│   │   ├── sentinel_log_parser.py
│   │   ├── threat_enrichment.py
│   │   └── anomaly_detector.py
│   ├── compliance/
│   │   ├── cis_scanner.py
│   │   └── compliance_reporter.py
│   ├── requirements.txt
│   └── README.md
│
├── 📂 azure-infrastructure/           # Terraform & Azure Policy
│   ├── terraform/
│   │   ├── main.tf
│   │   ├── network_security.tf
│   │   ├── rbac_policies.tf
│   │   ├── sentinel_setup.tf
│   │   └── variables.tf
│   ├── azure-policies/
│   │   ├── cis_benchmarks.json
│   │   ├── compliance_policies.json
│   │   └── security_policies.json
│   └── README.md
│
├── 📂 incident-response-playbooks/    # IR Workflows
│   ├── ransomware_investigation.md
│   ├── lateral_movement_response.md
│   ├── data_breach_playbook.md
│   ├── insider_threat_response.md
│   └── playbook_template.md
│
├── 📂 sc200-certification/            # Exam Preparation
│   ├── study-guide.md
│   ├── sentinel-configuration.md
│   ├── defender-xdr-guide.md
│   ├── azure-security-best-practices.md
│   ├── exam-checklist.md
│   └── resources.md
│
├── 📂 case-studies/                   # Real-World Scenarios
│   ├── ransomware_case_study.md
│   ├── apt_investigation.md
│   ├── insider_threat_case.md
│   └── breach_timeline.md
│
├── 📂 documentation/                  # Architecture & Guides
│   ├── architecture.md
│   ├── setup-guide.md
│   ├── best-practices.md
│   ├── query-documentation.md
│   └── troubleshooting.md
│
├── 📂 .github/
│   ├── workflows/
│   │   ├── kql-validation.yml
│   │   └── security-scan.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── query_request.md
│   └── pull_request_template.md
│
├── LICENSE
├── CONTRIBUTING.md
└── .gitignore
```

---

## 🔍 KQL Hunting Queries

**20+ production-ready Kusto Query Language (KQL) queries** for threat hunting and incident investigation.

### Query Categories

#### 1️⃣ **Threat Hunting**
- Command-line exploitation patterns
- Lateral movement detection
- Privilege escalation techniques
- Data exfiltration indicators
- Reconnaissance activity

#### 2️⃣ **Detection Rules**
- MITRE ATT&CK mapped queries
- Anomalous authentication patterns
- Network exploitation attempts
- Persistence mechanism detection

#### 3️⃣ **Incident Response**
- User account investigation
- Account timeline reconstruction
- Evidence collection queries
- Threat actor profiling

### Example: Detect Lateral Movement via Admin Shares

```kql
// Detects attempts to access administrative shares (C$, Admin$)
// Indicators of lateral movement in the network
SecurityEvent
| where EventID in (4688, 5140)
| where Process has_any ("net.exe", "cmd.exe") or CommandLine has_any ("\\\\*\\admin$", "\\\\*\\c$")
| extend AccountName = split(Account, "\\")[1]
| summarize AccessCount = count(), 
            FirstAccess = min(TimeGenerated),
            LastAccess = max(TimeGenerated)
            by Account, Computer, Process, CommandLine
| where AccessCount > 2
| sort by AccessCount desc
```

[📖 Full KQL Query Documentation](kql-queries/README.md)

---

## 🎯 Detection Engineering

Custom detection rules and alert configurations aligned with:
- ✅ MITRE ATT&CK Framework
- ✅ CIS Benchmarks
- ✅ Microsoft security best practices
- ✅ Real-world threat patterns

### Alert Rule Example

```json
{
  "name": "High Severity Authentication Failure",
  "description": "Detects multiple failed authentication attempts",
  "severity": "High",
  "mitre_attck": ["T1110.001"],
  "query": "SecurityEvent | where EventID == 4625 | summarize count() by Account",
  "threshold": 5,
  "time_window_minutes": 5
}
```

[📖 Detection Engineering Guide](detection-engineering/README.md)

---

## 🤖 Automation Scripts

**Python scripts** for:
- Incident response automation
- Log analysis and enrichment
- Threat indicator processing
- Compliance scanning
- Azure Sentinel API integration

### Example: Retrieve High-Severity Incidents

```python
from azure.monitor.query import LogsQueryClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
client = LogsQueryClient(credential)

query = """
SecurityAlert
| where AlertSeverity == "High"
| where TimeGenerated > ago(7d)
| summarize AlertCount = count() by AlertName, SourceComputerID
| sort by AlertCount desc
"""

results = client.query_workspace(workspace_id, query)
for row in results.tables[0].rows:
    print(f"Alert: {row[0]}, Count: {row[1]}")
```

[📖 Automation Scripts Guide](automation-scripts/README.md)

---

## 🏗️ Azure Security Infrastructure

**Terraform templates** for secure Azure infrastructure:
- Network segmentation
- RBAC configuration
- Sentinel deployment
- Defender setup
- Compliance enforcement

### Example: Deploy Sentinel Workspace

```hcl
resource "azurerm_log_analytics_workspace" "sentinel" {
  name                = "soc-sentinel-workspace"
  location            = var.location
  resource_group_name = azurerm_resource_group.security.name
  sku                 = "PerGB2018"
  retention_in_days   = 90

  tags = {
    Environment = "Production"
    Purpose     = "Security Operations"
  }
}

resource "azurerm_sentinel_log_analytics_workspace_onboarding" "example" {
  resource_group_name       = azurerm_resource_group.security.name
  workspace_name            = azurerm_log_analytics_workspace.sentinel.name
}
```

[📖 Infrastructure Guide](azure-infrastructure/README.md)

---

## 🚀 Getting Started

### Prerequisites

- ✅ Azure subscription with Sentinel enabled
- ✅ PowerShell or Azure CLI
- ✅ Python 3.9+
- ✅ Terraform (for infrastructure)
- ✅ Git

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/Anujdev67/Azure-Sentinel-SOC-Security-Portfolio.git
cd Azure-Sentinel-SOC-Security-Portfolio

# Install Python dependencies
pip install -r automation-scripts/requirements.txt

# Deploy infrastructure (optional)
cd azure-infrastructure/terraform
terraform init
terraform plan
terraform apply
```

[📖 Complete Setup Guide](documentation/setup-guide.md)

---

## 📚 SC-200 Certification Guide

Complete study materials for **Microsoft SC-200: Security Operations Analyst**:

- ✅ Sentinel configuration and management
- ✅ Defender XDR threat hunting
- ✅ Azure security architecture
- ✅ Incident investigation workflows
- ✅ SIEM deployment best practices
- ✅ Exam preparation checklist
- ✅ Sample exam questions
- ✅ Resource links

### Exam Topics Covered

1. **Mitigate Threats Using Microsoft Sentinel** (40-50%)
2. **Manage SIEM and XDR Security Operations** (50-60%)
   - Deploy and configure Sentinel
   - Hunting and investigation
   - Threat analysis

[📖 SC-200 Study Guide](sc200-certification/study-guide.md)

---

## 🚨 Incident Response Playbooks

Real-world playbooks for:

- 🔴 **Ransomware Investigation** - Detection, containment, recovery
- 🟡 **Lateral Movement Response** - Trace attacker movement, isolate systems
- 🟠 **Data Breach Handling** - Identify scope, preserve evidence
- 🔵 **Insider Threat Investigation** - Detection and investigation workflow

Each playbook includes:
- Detection queries
- Investigation steps
- Containment procedures
- Evidence collection
- Recovery procedures

[📖 Incident Response Playbooks](incident-response-playbooks/README.md)

---

## 📊 Case Studies

Real-world security scenarios:

1. **Ransomware Investigation**
   - Attack vector analysis
   - Lateral movement tracking
   - Encryption timeline
   - Recovery procedures

2. **APT Campaign Analysis**
   - Multi-stage attack timeline
   - Persistence mechanisms
   - Command & Control detection
   - Attribution indicators

3. **Insider Threat Detection**
   - Anomalous behavior patterns
   - Data exfiltration indicators
   - Investigation workflow
   - Containment strategies

4. **Breach Timeline Reconstruction**
   - Initial compromise
   - Privilege escalation
   - Lateral movement
   - Impact assessment

[📖 Case Studies](case-studies/README.md)

---

## 📋 Use Cases

- 🛡️ SOC Analyst role preparation
- 🔍 Threat hunting operations
- 📊 SIEM administration
- 🚨 Incident response automation
- 🏗️ Azure security hardening
- 📚 Certification study (SC-200, Azure Security)
- 🎓 Security training & mentoring
- 💼 Portfolio building for interviews

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-query`)
3. Commit your changes (`git commit -m 'Add amazing KQL query'`)
4. Push to the branch (`git push origin feature/amazing-query`)
5. Open a Pull Request

[📖 Contributing Guidelines](CONTRIBUTING.md)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support & Community

- 📧 Open an [Issue](https://github.com/Anujdev67/Azure-Sentinel-SOC-Security-Portfolio/issues) for bugs or questions
- 💬 Start a [Discussion](https://github.com/Anujdev67/Azure-Sentinel-SOC-Security-Portfolio/discussions) for ideas
- 🔗 LinkedIn: Share this repo to showcase your security expertise

---

## 🌟 Give This Repo Love!

If this repository helps you:
- ⭐ **Star this repository**
- 🔗 **Share on LinkedIn** - Great for your security career!
- 📢 **Tell your security friends**
- 🤝 **Contribute improvements**

### LinkedIn Post Template

```
🛡️ Just created a comprehensive Azure Sentinel & SOC Security Portfolio!

Includes:
✅ 20+ KQL threat hunting queries
✅ Detection engineering rules
✅ Python automation scripts
✅ Terraform infrastructure templates
✅ SC-200 exam study materials
✅ Real-world incident response playbooks

Perfect for SOC Analysts, Threat Hunters, and Security Engineers.

Check it out: [Your GitHub Link]
#CyberSecurity #AzureSecurity #SOC #ThreatHunting #Detection
```

---

## 🔐 Security Disclaimer

These queries and scripts are provided for **educational and authorized security testing purposes only**. Ensure you have proper authorization before running any queries or scripts in your environment.

---

## 📚 Related Resources

- [Microsoft Sentinel Documentation](https://learn.microsoft.com/en-us/azure/sentinel/)
- [KQL Language Reference](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [CIS Azure Benchmarks](https://www.cisecurity.org/benchmark/azure)
- [SC-200 Certification](https://learn.microsoft.com/en-us/certifications/security-operations-analyst/)
- [Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/)
- [Azure Security Best Practices](https://learn.microsoft.com/en-us/azure/security/)

---

**Last Updated**: June 2026 | **Version**: 1.0.0 | **Maintainer**: Security Operations Analyst

---

## 📊 Repository Stats

![GitHub stars](https://img.shields.io/github/stars/Anujdev67/Azure-Sentinel-SOC-Security-Portfolio?style=social)
![GitHub forks](https://img.shields.io/github/forks/Anujdev67/Azure-Sentinel-SOC-Security-Portfolio?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/Anujdev67/Azure-Sentinel-SOC-Security-Portfolio?style=social)

