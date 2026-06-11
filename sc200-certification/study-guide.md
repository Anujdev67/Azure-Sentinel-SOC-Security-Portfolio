# 📚 SC-200 Security Operations Analyst - Study Guide

## Exam Overview

**Exam**: Microsoft Security Operations Analyst (SC-200)  
**Duration**: 120 minutes  
**Questions**: 40-60 multiple choice  
**Passing Score**: 700/1000  
**Cost**: $165 USD  

## Exam Skills Measured

### Skill Area 1: Mitigate Threats Using Microsoft Sentinel (40-50%)

#### 1.1 Configure Microsoft Sentinel
- Create and manage Sentinel workspaces
- Configure data connectors
- Set up log retention policies
- Manage Sentinel roles and permissions

**Key Concepts**:
- Log Analytics workspace setup
- Data connector configuration (Office 365, Azure AD, Defender, etc.)
- Pricing and scaling
- RBAC configuration

**Practice**: Deploy a Sentinel workspace and connect 3+ data sources

#### 1.2 Create Detection Rules
- Build scheduled query rules
- Create Microsoft security analytics rules
- Configure anomaly detection
- Set alert thresholds and scheduling

**Key Concepts**:
- KQL query optimization
- Rule severity and MITRE ATT&CK mapping
- Alert tuning and false positive reduction
- Custom detection logic

**Practice Query Template**:
```kql
SecurityEvent
| where EventID == 4688
| where CommandLine has_any ("powershell", "cmd")
| summarize count() by Account, Computer
| where count_ > 5
```

#### 1.3 Configure Analytics Rules from Templates
- Deploy pre-built rule templates
- Customize rule parameters
- Enable/disable rules based on environment
- Monitor rule health

**Available Templates**:
- Brute Force Detection
- Impossible Travel
- Privilege Escalation
- Data Exfiltration
- Lateral Movement

#### 1.4 Manage Alerts and Incidents
- Configure alert suppression
- Set up incident automation
- Create automated response playbooks
- Manage alert groups

### Skill Area 2: Manage SIEM and XDR Security Operations (50-60%)

#### 2.1 Threat Hunting and Investigation
- Use KQL for advanced hunting
- Correlate events across data sources
- Build investigation timelines
- Identify attack patterns

**Common Threat Hunting Queries**:

**Brute Force Detection**:
```kql
SecurityEvent
| where EventID == 4625  // Failed login
| summarize FailureCount = count() by Account, Computer
| where FailureCount > 10
```

**Lateral Movement**:
```kql
SecurityEvent
| where EventID in (4688, 5140)
| where CommandLine has "admin$"
| summarize by Account, TargetComputer
```

#### 2.2 Azure Defender and Microsoft 365 Defender
- Configure Defender for Cloud
- Manage Defender for Endpoint
- Set up Defender for Office 365
- Integrate with Sentinel

#### 2.3 SOAR and Automation
- Create automated response playbooks
- Configure Logic Apps for response
- Implement entity mapping
- Test playbook workflows

**Playbook Example**:
- Trigger: High-severity alert
- Action 1: Isolate affected device
- Action 2: Disable user account
- Action 3: Collect evidence
- Action 4: Notify security team

#### 2.4 Incident Response
- Investigate security incidents
- Collect and preserve evidence
- Perform root cause analysis
- Document findings

---

## Key Topics Deep Dive

### 1. Kusto Query Language (KQL)

**Essential KQL Functions**:
```kql
// Summarize and count
| summarize count() by Account

// Filter results
| where EventID == 4625

// Join data sources
| join kind=inner (OtherTable) on Computer

// Create new columns
| extend NewColumn = case(Condition, Value1, Value2)

// Sort results
| sort by TimeGenerated desc

// Limit results
| limit 100

// Search across multiple columns
| search "keyword"

// Parse strings
| parse CommandLine with "prefix" * "suffix"
```

### 2. Data Connectors

**Priority Connectors**:
1. Azure Activity
2. Azure AD
3. Microsoft 365 Defender
4. Microsoft Defender for Cloud
5. Syslog (Linux security)
6. Windows Security Events

**Configuration Steps**:
1. Navigate to Data Connectors
2. Select connector type
3. Configure prerequisites
4. Set up collection rules
5. Verify data ingestion

### 3. Analytics Rules

**Rule Components**:
- **Query**: KQL query that identifies threats
- **Severity**: Critical, High, Medium, Low, Informational
- **MITRE ATT&CK**: Technique classification
- **Tactics**: Reconnaissance, Initial Access, etc.
- **Schedule**: Frequency of rule execution
- **Threshold**: Alert trigger condition
- **Response**: Automated actions

**Best Practices**:
- Test rules thoroughly before deployment
- Start with high sensitivity, tune based on false positives
- Map rules to MITRE ATT&CK framework
- Document rule purpose and scope
- Review and update rules quarterly

### 4. Incident Management

**Incident Lifecycle**:
1. **Detection**: Alert triggered
2. **Investigation**: Gather evidence
3. **Containment**: Isolate affected systems
4. **Eradication**: Remove threats
5. **Recovery**: Restore systems
6. **Lessons Learned**: Document findings

---

## Practice Exam Questions

### Q1: Alert Configuration
**Scenario**: You detect multiple failed login attempts from a single IP to multiple accounts. Configure a rule to alert on this pattern.

**Answer**:
```kql
SecurityEvent
| where EventID == 4625  // Failed login
| summarize FailureCount = count() by SourceIpAddress, Computer
| where FailureCount > 5  // Threshold
```

### Q2: Incident Investigation
**Scenario**: An employee's account shows suspicious PowerShell execution. Investigate the timeline.

**Answer**:
```kql
SecurityEvent
| where Account == "domain\\username"
| where EventID in (4688, 4103)  // Process creation, PowerShell
| project TimeGenerated, EventID, CommandLine, Computer
| sort by TimeGenerated asc
```

---

## Study Resources

### Microsoft Official
- [SC-200 Exam Page](https://learn.microsoft.com/en-us/certifications/security-operations-analyst/)
- [Sentinel Documentation](https://learn.microsoft.com/en-us/azure/sentinel/)
- [KQL Tutorial](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/)

### Practice Labs
- Set up free Azure trial
- Deploy Sentinel workspace
- Create sample detection rules
- Run threat hunting queries

### Books & Courses
- "Microsoft Sentinel Handbook" (official guide)
- Pluralsight courses on Azure Security
- A Cloud Guru Sentinel training

---

## Exam Day Tips

✅ **Do**:
- Read questions carefully
- Understand scenario-based questions
- Know KQL basics well
- Practice rule creation
- Understand incident lifecycle

❌ **Don't**:
- Memorize syntax (focus on concepts)
- Skip scenario understanding
- Rush through questions
- Leave questions blank

---

## After Certification

- Update LinkedIn profile
- Share certification on GitHub
- Join security communities
- Continue hands-on practice
- Explore advanced Azure security topics

---

**Study Time**: 4-6 weeks recommended  
**Difficulty**: Medium-High  
**Practical Focus**: 70% hands-on, 30% theory  

Good luck! 🚀
