# CloudTrail Log Analyzer

This is a simple Python tool I built to analyze AWS CloudTrail logs and flag key security-related events. It’s designed to help detect:

- Failed login attempts (`ConsoleLogin`)
- IAM activity like user creation or policy attachments (`CreateUser`, `AttachUserPolicy`)

The goal is to understand how log analysis works and build something practical for early-stage threat detection or audit review.

---

## What It Does

- Scans AWS CloudTrail logs in JSON format
- Identifies failed login attempts and where they came from
- Detects IAM changes like creating users or assigning admin access
- Prints clear, readable results for each match

---

## Files Included

| File | Description |
|------|-------------|
| `analyze.py` | Python script that analyzes the log file |
| `cloudtrail_sample.json` | Sample AWS CloudTrail log entries for testing |

---

##  How to Run It

1. Clone or download this repo
2. Make sure Python 3 is installed
3. Open your terminal and run:

```bash
python analyze.py
