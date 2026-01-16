import os
from datetime import datetime
import platform

# CONFIG
server = "google.com" 
log_file = "network_log.txt"

# Determine ping parameter based on OS
param = "-n" if platform.system().lower() == "windows" else "-c"

# FUNCTION
def check_network():
    # Run ping command
    response = os.system(f"ping {param} 2 {server} > nul 2>&1")
    if platform.system().lower() != "windows":
        response = os.system(f"ping {param} 2 {server} > /dev/null 2>&1")
    
    # Timestamp
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Determine status
    status = "Reachable" if response == 0 else "Unreachable"
    
    # Print to console
    print(f"[{now}] {server} is {status}")
    
    # Save to log
    with open(log_file, "a") as f:
        f.write(f"[{now}] {server} is {status}\n")

# MAIN
if __name__ == "__main__":
    check_network()
