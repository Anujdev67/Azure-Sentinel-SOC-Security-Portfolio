# 🤖 Security Automation Scripts

## Overview

Production-ready Python scripts for:
- Incident response automation
- Log analysis and enrichment
- Threat indicator processing
- Compliance scanning
- Azure Sentinel API integration

## Directory Structure

### incident-response/
- `ir_automation.py` - Main incident response orchestration
- `evidence_collector.py` - Automated evidence collection
- `timeline_builder.py` - Incident timeline reconstruction

### log-analysis/
- `sentinel_log_parser.py` - Parse and process Sentinel logs
- `threat_enrichment.py` - Threat intelligence enrichment
- `anomaly_detector.py` - Anomaly detection algorithms

### compliance/
- `cis_scanner.py` - CIS benchmark scanner
- `compliance_reporter.py` - Generate compliance reports

## Installation

```bash
pip install -r requirements.txt
```

## Usage Examples

### Query Sentinel Data
```python
from incident_response.ir_automation import SentinelClient

client = SentinelClient()
incidents = client.get_high_severity_incidents()
for incident in incidents:
    print(f"Incident: {incident['name']}")
```

### Collect Evidence
```python
from incident_response.evidence_collector import EvidenceCollector

collector = EvidenceCollector()
evidence = collector.collect_for_incident("incident_id")
```

## Security Best Practices

1. Store credentials in environment variables
2. Use Azure Key Vault for secrets
3. Implement proper error handling
4. Log all actions for audit trail
5. Validate all inputs

