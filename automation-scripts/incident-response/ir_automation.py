#!/usr/bin/env python3
"""
Incident Response Automation Module
Automated detection, investigation, and response workflows
"""

import os
import json
from datetime import datetime, timedelta
from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient


class SentinelClient:
    """Azure Sentinel integration client"""
    
    def __init__(self):
        self.credential = DefaultAzureCredential()
        self.client = LogsQueryClient(self.credential)
        self.workspace_id = os.getenv("SENTINEL_WORKSPACE_ID")
    
    def get_high_severity_incidents(self, days=7):
        """
        Retrieve high-severity incidents from the past N days
        """
        query = f"""
        SecurityAlert
        | where AlertSeverity == "High" or AlertSeverity == "Critical"
        | where TimeGenerated > ago({days}d)
        | summarize AlertCount = count() by AlertName, SourceComputerID
        | sort by AlertCount desc
        """
        
        try:
            response = self.client.query_workspace(
                self.workspace_id,
                query,
                timespan=None
            )
            return response.tables[0].rows if response.tables else []
        except Exception as e:
            print(f"Error retrieving incidents: {e}")
            return []
    
    def investigate_account(self, account_name, days=30):
        """
        Investigate activities for a specific user account
        """
        query = f"""
        SecurityEvent
        | where Account == "{account_name}"
        | where TimeGenerated > ago({days}d)
        | summarize
            TotalEvents = count(),
            FailedLogins = countif(EventID == 4625),
            SuccessfulLogins = countif(EventID == 4624),
            ProcessCreations = countif(EventID == 4688)
            by Account
        """
        
        try:
            response = self.client.query_workspace(
                self.workspace_id,
                query,
                timespan=None
            )
            return response.tables[0].rows if response.tables else []
        except Exception as e:
            print(f"Error investigating account: {e}")
            return []
    
    def get_lateral_movement_indicators(self, hours=24):
        """
        Detect lateral movement indicators
        """
        query = f"""
        SecurityEvent
        | where EventID in (4688, 5140)
        | where Process has_any ("net.exe", "psexec.exe", "wmic.exe")
        | where TimeGenerated > ago({hours}h)
        | summarize count() by Account, Computer, Process
        | where count_ > 2
        """
        
        try:
            response = self.client.query_workspace(
                self.workspace_id,
                query,
                timespan=None
            )
            return response.tables[0].rows if response.tables else []
        except Exception as e:
            print(f"Error detecting lateral movement: {e}")
            return []
    
    def create_incident_summary(self, account_name):
        """
        Create a comprehensive incident summary
        """
        summary = {
            "timestamp": datetime.now().isoformat(),
            "account": account_name,
            "investigation": self.investigate_account(account_name),
            "lateral_movement": self.get_lateral_movement_indicators()
        }
        return summary


if __name__ == "__main__":
    client = SentinelClient()
    
    # Example: Get high-severity incidents
    incidents = client.get_high_severity_incidents()
    print(f"High-Severity Incidents: {incidents}")
    
    # Example: Create incident summary
    summary = client.create_incident_summary("domain\\username")
    print(json.dumps(summary, indent=2))
