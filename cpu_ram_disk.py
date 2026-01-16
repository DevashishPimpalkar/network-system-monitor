import psutil
from datetime import datetime
import socket

# CONFIG
log_file = "network_log.txt"

# SYSTEM INFO
try:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
except:
    hostname = "Unknown"
    ip_address = "Unknown"

# TIMESTAMP
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# SYSTEM METRICS
cpu_percent = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory()
ram_percent = ram.percent
disk = psutil.disk_usage('/')
disk_percent = disk.percent

# OUTPUT
print(f"[{now}] Host: {hostname} | IP: {ip_address}")
print(f"CPU: {cpu_percent}% | RAM: {ram_percent}% | Disk: {disk_percent}%")

# LOG
with open(log_file, "a") as f:
    f.write(f"[{now}] Host: {hostname} | IP: {ip_address} | CPU: {cpu_percent}% | RAM: {ram_percent}% | Disk: {disk_percent}%\n")
