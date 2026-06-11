# 🎯 Detection Engineering

## Overview

Custom detection rules and alert configurations aligned with:
- ✅ MITRE ATT&CK Framework
- ✅ CIS Benchmarks
- ✅ Microsoft security best practices
- ✅ Real-world threat patterns

## Directory Structure

```
detection-engineering/
├── alert-rules/
│   ├── critical_alerts.json
│   ├── high_priority_alerts.json
│   └── incident_rules.yaml
├── detection-templates/
│   ├── rule_template.json
│   └── validation_schema.json
└── README.md
```

## Creating Detection Rules

### Basic Rule Structure

```json
{
  "name": "Suspicious PowerShell Execution",
  "description": "Detects suspicious PowerShell command execution patterns",
  "severity": "High",
  "enabled": true,
  "mitre_attck": [
    "T1059.001"
  ],
  "tactics": [
    "Execution"
  ],
  "query": "SecurityEvent | where EventID == 4688 | where CommandLine has_any ('powershell', '-enc', '-nop')",
  "threshold": 5,
  "time_window_minutes": 5
}
```

## Best Practices

1. **Test thoroughly** before deployment
2. **Start conservative** with thresholds
3. **Map to MITRE ATT&CK** techniques
4. **Document rationale** for rule creation
5. **Review and tune** based on alerts
6. **Update regularly** as threats evolve

