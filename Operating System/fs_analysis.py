"""
File System Analysis Script (Q2)
Lists files, checks disk usage, and prints EXT4 info if available.
"""
import os
import shutil

print("Files in current directory:", os.listdir('.'))
total, used, free = shutil.disk_usage('.')
print(f"Disk usage: {used // (2**30)} GB used / {total // (2**30)} GB total")
# For EXT4 info, run: sudo dumpe2fs /dev/sdXN | grep 'Filesystem'
