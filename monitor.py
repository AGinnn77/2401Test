#!/usr/bin/env python3
import psutil
import time

def monitor_system():
    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=1)
            io_counters = psutil.disk_io_counters()
            net_io_counters = psutil.net_io_counters()

            print(f"CPU Usage: {cpu_percent}%")
            print(f"I/O Count: {io_counters.read_count + io_counters.write_count}")
            print(f"Network Traffic - Sent: {net_io_counters.bytes_sent} bytes, Received: {net_io_counters.bytes_recv} bytes")
            
            print("-" * 40)
            time.sleep(5)
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    monitor_system()

