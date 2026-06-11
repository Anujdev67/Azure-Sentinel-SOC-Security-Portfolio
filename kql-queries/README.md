# 🔍 KQL Hunting Queries

## Overview

This directory contains **20+ production-ready Kusto Query Language (KQL) queries** for:
- Threat hunting
- Incident investigation
- Detection rule validation
- MITRE ATT&CK framework mapping

---

## Query Organization

### 📁 threat-hunting/
Proactive hunting queries for discovering threats

### 📁 incident-response/
Investigation queries for active incidents

### 📁 detection-rules/
Custom detection rules and automated alerts

---

## Quick Start Examples

### 1. Lateral Movement Detection
```kql
SecurityEvent
| where EventID in (4688, 5140)
| where Process has_any ("net.exe", "psexec.exe", "wmic.exe")
| extend TargetHost = extract(@'\\\\([^\\]+)\\', 1, CommandLine)
| summarize count() by Account, TargetHost, Computer
| where count_ > 1
```

### 2. Privilege Escalation
```kql
SecurityEvent
| where EventID == 4673
| summarize by Account, Computer, Process, TimeGenerated
```

### 3. Account Enumeration
```kql
SecurityEvent
| where EventID == 4738  // User account modified
| summarize ModificationCount = count() by Account
| where ModificationCount > 5
```

---

## How to Use

1. Copy query from respective file
2. Paste into Azure Sentinel Log Analytics
3. Adjust time range as needed
4. Run query
5. Analyze results

---

## MITRE ATT&CK Mapping

Queries are mapped to MITRE ATT&CK techniques:
- **T1110** - Brute Force
- **T1021** - Remote Services
- **T1071** - Application Layer Protocol
- **T1059** - Command and Scripting Interpreter
- **T1041** - Exfiltration Over C2 Channel

---

## Performance Tips

1. **Use time filters**: Reduce query scope
2. **Filter by EventID first**: Narrow down events
3. **Use materialized views**: For frequently run queries
4. **Optimize joins**: Reduce data volumes

---

## Contributing Queries

To contribute a new query:
1. Test thoroughly in your environment
2. Add comments explaining detection logic
3. Include MITRE ATT&CK mapping
4. Submit via PR with documentation

