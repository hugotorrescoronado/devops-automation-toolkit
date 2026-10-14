# DevOps Automation Toolkit

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

DevOps automation toolkit demonstrating Python, PowerShell, Bash, AWS inventory reporting, operational reporting, GitHub Actions CI/CD, and Platform Engineering practices.

---

## Overview

This repository contains automation utilities commonly used by:

- DevOps Engineers
- Platform Engineers
- Cloud Engineers
- Site Reliability Engineers (SREs)
- Automation Engineers

The project demonstrates operational automation, reporting, inventory management, health monitoring, and CI/CD practices.

---

## Features

✅ Python Automation

✅ PowerShell Automation

✅ Bash Automation

✅ System Health Monitoring

✅ Log Analysis

✅ AWS Inventory Reporting

✅ CSV Report Generation

✅ HTML Report Generation

✅ GitHub Actions CI/CD

✅ Automated Validation

✅ Infrastructure Reporting

⏳ Security & DevSecOps

---

## Screenshots

### Python Health Check

System health monitoring using Python.

![Python Health Check](docs/health-check-output.png)

---

### PowerShell Health Check

Windows infrastructure reporting using PowerShell.

![PowerShell Health Check](docs/powershell-health-check.png)

---

✅ CSV Report Generation

✅ HTML Report Generation

✅ Operational Reporting

✅ Infrastructure Reporting

Automated log parsing and reporting.

![Log Analysis](docs/log-analysis-output.png)

---

### AWS Inventory Reporting

AWS inventory reporting using Boto3 and sample inventory data.

![AWS Inventory Reporting](docs/aws-inventory-output.png)

---

### HTML System Report

Generated infrastructure report.

![HTML System Report](docs/html-report.png)

---

## Repository Structure

```text
devops-automation-toolkit
│
├── .github/
│   └── workflows/
│       ├── python-validation.yml
│       ├── powershell-validation.yml
│       ├── bash-validation.yml
│       └── python-lint.yml
│
├── python/
│   ├── health_check.py
│   ├── log_analyzer.py
│   ├── aws_inventory.py
│   └── system_report.py
│
├── powershell/
│   └── health-check.ps1
│
├── bash/
│   └── health-check.sh
│
├── sample-data/
│   └── ec2_inventory.json
│
├── sample-logs/
│   └── app.log
│
├── reports/
│
├── docs/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Installation

Clone the repository:

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

## Health Monitoring

Run:

```bash
python python/health_check.py
```

Example output:

```text
=== SYSTEM HEALTH REPORT ===

Hostname: DESKTOP-XXXXXXX

Operating System: Windows

CPU Usage: 20.3%

Memory Usage: 88%

Disk Usage: 10.9%
```

---

## Log Analysis

Run:

```bash
python python/log_analyzer.py
```

Example output:

```text
=== LOG ANALYSIS REPORT ===

INFO Messages: 3

WARNING Messages: 1

ERROR Messages: 2
```

---

## AWS Inventory Reporting

Run:

```bash
python python/aws_inventory.py
```

Example output:

```text
AWS unavailable. Using sample inventory data.

=== AWS INVENTORY REPORT ===

i-0123456789abcdef0 | t3.micro | running

i-0987654321abcdef0 | t3.small | stopped
```

Generated CSV:

```text
reports/aws_inventory.csv
```

---

## System Reporting

Generate system reports:

```bash
python python/system_report.py
```

Generated files:

```text
reports/system_report.csv

reports/system_report.html
```

---

## GitHub Actions

The project automatically validates scripts on every:

```text
Push
Pull Request
```

Workflows:

### Python Validation

```text
health_check.py
log_analyzer.py
aws_inventory.py
system_report.py
```

### PowerShell Validation

```text
health-check.ps1
```

### Bash Validation

```text
health-check.sh
```

### Python Lint

```text
flake8
```

---

## Local Validation

Python:

```bash
python python/health_check.py

python python/log_analyzer.py

python python/aws_inventory.py

python python/system_report.py
```

PowerShell:

```powershell
.\powershell\health-check.ps1
```

Bash:

```bash
bash bash/health-check.sh
```

---

## Roadmap

### Phase 1 – Health Monitoring

- [x] Python Health Check
- [x] PowerShell Health Check
- [x] Bash Health Check

### Phase 2 – Log Analysis

- [x] Log Parsing
- [x] Error Reporting
- [x] Warning Reporting

### Phase 3 – AWS Inventory Reporting

- [x] AWS Inventory Utility
- [x] Sample Inventory Data
- [x] CSV Export

### Phase 4 – System Reporting

- [x] CSV Reports
- [x] HTML Reports
- [x] Infrastructure Reporting

### Phase 5 – GitHub Actions

- [x] Python Validation
- [x] PowerShell Validation
- [x] Bash Validation
- [x] Linting
- [x] CI/CD Automation

### Phase 6 – Security

- [ ] Gitleaks
- [ ] Dependency Scanning
- [ ] Secret Detection
- [ ] Security Workflow
- [ ] DevSecOps Controls

---

## Technologies

- Python
- PowerShell
- Bash
- AWS SDK (Boto3)
- GitHub Actions
- CSV Reporting
- HTML Reporting
- Log Analysis
- DevOps Automation
- Cloud Operations
- Platform Engineering
- Infrastructure Automation
- CI/CD

---

## Status

✅ Phase 5 Complete

Next Phase:

🚧 Security & DevSecOps