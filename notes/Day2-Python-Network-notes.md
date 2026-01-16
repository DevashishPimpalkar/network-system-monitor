# Day 2 – Python Automation

**Date:** 16-Jan-2026  
**Goal:** Automate network ping checks and log system info

---

## 1. Objective
- Turn manual network observations from Day 1 into an **automated Python script**.
- Log network reachability, timestamp, hostname, and IP address.
- Build foundation for **system automation / DevOps journey**.

---

## 2. Steps Performed
1. Created `network_check.py` in project folder.
2. Wrote Python code to:
   - Ping a server (`google.com`)
   - Capture success/failure (Reachable / Unreachable)
   - Get system hostname and IP address
   - Log all results into `network_log.txt` with timestamp
3. Ran the script to verify output:
   - Output example:
     ```
     [2026-01-16 19:45:12] google.com is Reachable | Hostname: Devashish-PC | IP: 192.168.1.5
     ```
4. Checked `network_log.txt` → confirmed all logs are recorded correctly.
5. Committed `network_check.py` and `network_log.txt` to GitHub.
6. Updated `README.md` to reflect Day 2 progress.

---

## 3. Learning / Analysis
- Learned **how to integrate Python + system commands** for automation.
- Learned **logging best practices**.
- Foundation for **future DevOps / system monitoring scripts**.
- Realized importance of **cross-platform compatibility** (Windows vs Linux ping).

---

## 4. Next Steps
- Automate **CPU, RAM, and Disk usage monitoring** (Day 3)
- Combine scripts into `main.py` for **unified system monitoring**
- Start building **portfolio-ready project**
