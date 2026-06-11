# 🔴 Ransomware Investigation Playbook

## Incident Overview
- **Threat Type**: Ransomware
- **Severity**: Critical
- **Detection**: File encryption, ransom note, unusual file activity
- **Response Time**: Immediate

## Detection Signals

```kql
// Detect mass file encryption activity
DeviceProcessEvents
| where FileName has_any (".exe", ".dll")
| where InitiatingProcessCommandLine has_any (".bat", "cmd.exe", "powershell")
| where ActionType == "FileCreated"
| summarize FileCount = dcount(FileName) by DeviceId, InitiatingProcessFileName
| where FileCount > 100  // Threshold
```

## Investigation Steps

### Step 1: Identify Compromised Systems
1. Collect hostnames from alerts
2. Determine infection scope
3. Identify patient zero
4. Check connection logs

### Step 2: Preserve Evidence
1. Create forensic images
2. Export logs to secure location
3. Document chain of custody
4. Preserve memory dumps (if possible)

### Step 3: Containment
1. **Network Isolation**
   - Disconnect infected systems
   - Segment networks
   - Block C2 communications

2. **Account Lockdown**
   - Disable compromised accounts
   - Force password resets
   - Review access logs

### Step 4: Eradication
1. Remove malware
2. Patch vulnerabilities
3. Update security controls
4. Verify system integrity

### Step 5: Recovery
1. Restore from backups
2. Rebuild systems if needed
3. Validate data integrity
4. Restore to production

## Communication Template

**Initial Report**:
```
Incident Type: Ransomware
Severity: Critical
Affected Systems: [Count]
Data Risk: [High/Medium/Low]
Status: Investigating
```

