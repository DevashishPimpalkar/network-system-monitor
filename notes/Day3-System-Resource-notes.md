# Day 3 – System Resource Monitoring

**Date:** 16-Jan-2026  
**Goal:** Automate CPU, RAM, and Disk usage monitoring and append results to the centralized log.

---

## 1. Objective
- Extend Day 2 network monitoring by including **system resource metrics**.
- Log CPU %, RAM %, and Disk % along with **hostname and IP**.
- Build foundation for **mini DevOps / system monitoring tool**.

---

## 2. Steps Performed
1. Created `cpu_ram_disk.py` in project folder.
2. Wrote Python code to:
   - Get system **hostname and IP**
   - Check **CPU usage**, **RAM usage**, and **Disk usage**
   - Print results to console
   - Append results to **`network_log.txt`** with timestamp
3. Ran the script and verified:
   - Console output example:
     ```
     [2026-01-16 15:10:05] Host: Devashish-PC | IP: 192.168.1.5
     CPU: 23% | RAM: 45% | Disk: 60%
     ```
   - Log file updated correctly with same information
4. Committed `cpu_ram_disk.py` and updated `network_log.txt` to GitHub.
5. Updated `README.md` to reflect Day 3 progress.

---

## 3. Learning / Analysis
- Learned how to **automate system resource monitoring** using Python (`psutil` library).
- Learned best practices for **logging system data**.
- Centralized log approach makes it easy to **track system + network health together**.
- Foundation for **future DevOps projects**, such as alerts, dashboards, and integrated monitoring.

---

## 4. Next Steps
- Combine **network_check.py + cpu_ram_disk.py** into `main.py` for unified monitoring.
- Optional: add **alerts when CPU / RAM / Disk exceeds thresholds**.
- Optional: create **mini dashboard** or **visualization** for GitHub / portfolio.
