#!/usr/bin/env python3
import psutil

#获取CPU信息
cpu_info = psutil.cpu_percent(interval = 1, percpu = True)
print(f"CPU Usage: {cpu_info}%")

#获取内存信息
memory_info = psutil.virtual_memory()
print(f"Memory Usage: {memory_info.percent}%")

# 获取所有进程列表
process_list = psutil.process_iter()
for process in process_list:
    print(f"Process ID: {process.pid} | Name: {process.name()}")

# 获取网络连接信息
connections = psutil.net_connections(kind='inet')
for conn in connections:
    print(f"Local Address: {conn.laddr} | Remote Address: {conn.raddr} | Status: {conn.status}")

# 获取磁盘使用情况
disk_usage = psutil.disk_usage('/')
print(f"Total Disk Space: {disk_usage.total} bytes | Free Disk Space: {disk_usage.free} bytes")

