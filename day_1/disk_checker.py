# import sys
import psutil

path = "/"
usage = psutil.disk_usage(path)
free_space = usage.free / (1024 * 1024 * 1024)
print(f"Available disk space: {free_space}")
