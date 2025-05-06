import subprocess
import time
import csv
from datetime import datetime
import os

# Configuration
OUTPUT_FILE = 'D:/Eclipse/python/output.txt'
PING_INTERVAL = 30  # seconds between pings
RUNTIME_MINUTES = 30  # total runtime in minutes

def ping_host(host="8.8.8.8"):
    try:
        # Run ping command and capture output
        output = subprocess.check_output(
            ["ping", "-n", "1", host],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        
        # Extract time from ping output
        for line in output.split('\n'):
            if "time=" in line:
                time_str = line.split("time=")[1].split("ms")[0]
                return float(time_str)
    except subprocess.CalledProcessError:
        return None

def main():
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(OUTPUT_FILE)
    os.makedirs(output_dir, exist_ok=True)
    
    end_time = time.time() + (RUNTIME_MINUTES * 60)  # convert minutes to seconds
    
    with open(OUTPUT_FILE, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["timestamp", "time_ms"])
        
        while time.time() < end_time:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ping_time = ping_host()
            
            if ping_time is not None:
                writer.writerow([timestamp, ping_time])
                csvfile.flush()  # Ensure data is written immediately
            
            # Wait for specified interval before next ping
            time.sleep(PING_INTERVAL)

if __name__ == "__main__":
    main() 