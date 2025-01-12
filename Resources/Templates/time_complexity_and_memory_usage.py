
import time
import psutil
import os


process = psutil.Process(os.getpid())
start_time = time.time()


end_time = time.time()
memory_usage = process.memory_info().rss / (1024 * 1024)

