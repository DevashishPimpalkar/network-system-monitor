import os
from datetime import datetime
import platform
import socket

# CONFIG
server = "google.com"
log_file = "network_log.txt"

# Determine ping parameter based on OS
param = "-n" if platform.system().lower() == "windows" else "-c"

# FUNCTION
def check_network():
    # NETWORK INTERFACE INFO
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
    except:
        hostname = "Unknown"
        ip_address = "Unknown"

    # PING TEST
    ping_command = f"ping {param} 2 {server}"
    if platform.system().lower() == "windows":
        response = os.system(ping_command + " > nul 2>&1")
    else:
        response = os.system(ping_command + " > /dev/null 2>&1")

    status = "Reachable" if response == 0 else "Unreachable"

    # TIMESTAMP
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # PRINT
    print(f"[{now}] {server} is {status}")
    print(f"Hostname: {hostname} | IP: {ip_address}")

    # LOG
    with open(log_file, "a") as f:
        f.write(f"[{now}] {server} is {status} | Hostname: {hostname} | IP: {ip_address}\n")

# MAIN
if __name__ == "__main__":
    check_network()
