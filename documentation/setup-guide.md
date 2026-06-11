# 🚀 Setup Guide

## Prerequisites

- Azure subscription
- PowerShell or Azure CLI
- Git
- Python 3.9+
- Terraform (optional)

## Step 1: Clone Repository

```bash
git clone https://github.com/Anujdev67/Azure-Sentinel-SOC-Security-Portfolio.git
cd Azure-Sentinel-SOC-Security-Portfolio
```

## Step 2: Install Dependencies

```bash
pip install -r automation-scripts/requirements.txt
```

## Step 3: Configure Azure Credentials

```bash
az login
az account set --subscription "Your Subscription ID"
```

## Step 4: Deploy Sentinel (Optional)

```bash
cd azure-infrastructure/terraform
terraform init
terraform plan
terraform apply
```

## Step 5: Import Queries

1. Open Azure Sentinel
2. Navigate to Logs
3. Copy KQL queries from `kql-queries/` directory
4. Test queries in your environment

## Step 6: Configure Automation Scripts

```bash
export SENTINEL_WORKSPACE_ID="your-workspace-id"
python automation-scripts/incident-response/ir_automation.py
```

## Validation

✅ Verify Sentinel is ingesting data  
✅ Test KQL queries  
✅ Validate automation scripts  
✅ Review detection rules  

## Troubleshooting

See [troubleshooting.md](troubleshooting.md) for common issues.

