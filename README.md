# DevOps Automation Toolkit

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

DevOps automation toolkit demonstrating Python, PowerShell, Bash, AWS inventory reporting, health checks, log analysis, reporting, and CI/CD automation.

---

## Overview

This repository contains practical automation utilities commonly used by DevOps Engineers, Platform Engineers, Cloud Engineers, and Site Reliability Engineers (SREs).

The project focuses on operational tooling and automation practices including:

- System Health Checks
- Log Analysis
- AWS Inventory Reporting
- Infrastructure Reporting
- GitHub Actions Automation
- Python Automation
- PowerShell Automation
- Bash Automation

---

## Features

✅ Python Automation

✅ PowerShell Automation

✅ Bash Automation

✅ System Health Checks

✅ Log Analysis

✅ AWS Inventory Reporting

✅ CSV Report Generation

✅ GitHub Actions

⏳ HTML Reporting

⏳ Security Scanning

⏳ Infrastructure Dashboards

---

## Repository Structure

```text
devops-automation-toolkit
│
├── python/
│   ├── health_check.py
│   ├── log_analyzer.py
│   └── aws_inventory.py
│
├── powershell/
│   └── health-check.ps1
│
├── bash/
│   └── health-check.sh
│
├── sample-logs/
│   └── app.log
│
├── sample-data/
│   └── ec2_inventory.json
│
├── reports/
│
├── .github/
│   └── workflows/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Branch Strategy

The project follows a feature branch workflow.

```text
main

feature/health-checks

feature/log-analysis

feature/aws-inventory

feature/system-reporting

feature/github-actions

feature/security-scanning
```

---

# Phase 1 - Health Checks

Automated system health monitoring using multiple scripting languages.

### Python

```bash
python python/health_check.py
```

### PowerShell

```powershell
.\powershell\health-check.ps1
```

### Bash

```bash
bash bash/health-check.sh
```

Example output:

```text
=== SYSTEM HEALTH REPORT ===

Hostname: DESKTOP-XXXXXXX

Operating System: Windows

CPU Usage: 12%

Memory Usage: 43%

Disk Usage: 61%
```

---

# Phase 2 - Log Analysis

Analyze log files and generate error statistics.

Sample log:

```text
INFO Application started
WARNING Low disk space
ERROR Database connection failed
INFO Retry initiated
ERROR Timeout detected
```

Run:

```bash
python python/log_analyzer.py
```

Output:

```text
=== LOG ANALYSIS REPORT ===

INFO Messages: 3

WARNING Messages: 1

ERROR Messages: 2
```

---

# Phase 3 - AWS Inventory Reporting

Generates EC2 inventory reports.

The utility operates in two modes:

### Mode 1

Uses real AWS resources through:

```text
AWS SDK (Boto3)
```

when credentials are configured.

### Mode 2

Uses sample inventory data:

```text
sample-data/ec2_inventory.json
```

allowing anyone to run the repository without AWS credentials.

Run:

```bash
python python/aws_inventory.py
```

Example output:

```text
=== AWS INVENTORY REPORT ===

i-0123456789abcdef0 | t3.micro | running

i-0987654321abcdef0 | t3.small | stopped
```

Generated report:

```text
reports/aws_inventory.csv
```

Example:

```csv
InstanceId,InstanceType,State
i-0123456789abcdef0,t3.micro,running
i-0987654321abcdef0,t3.small,stopped
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/hugotorrescoronado/devops-automation-toolkit.git

cd devops-automation-toolkit
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Dependencies

```text
psutil
boto3
```

Install manually:

```bash
pip install psutil boto3
```

---

## Roadmap

### Phase 1 - Health Checks

- [x] Python Health Check
- [x] PowerShell Health Check
- [x] Bash Health Check

### Phase 2 - Log Analysis

- [x] Log Parsing
- [x] Error Reporting
- [x] Warning Reporting

### Phase 3 - AWS Inventory Reporting

- [x] AWS Inventory Utility
- [x] Sample Inventory Data
- [x] CSV Export

### Phase 4 - System Reporting

- [ ] CSV Reports
- [ ] HTML Reports
- [ ] Historical Reporting

### Phase 5 - GitHub Actions

- [ ] Python Validation
- [ ] Linting
- [ ] Automated Testing

### Phase 6 - Security

- [ ] Gitleaks
- [ ] Dependency Scanning
- [ ] Secrets Detection

---

## Technologies

- Python
- PowerShell
- Bash
- AWS SDK (Boto3)
- GitHub Actions
- CSV Reporting
- Log Analysis
- DevOps Automation
- Platform Engineering
- Cloud Operations
- Infrastructure Automation

---

## Status

🚧 Phase 3 In Progress