## Queues

### FIFO (first in first out)
### [ (front) 10 ] (0) [ 5 ] (1) [ 2 ] (2) [ 8 ] (3) [ (rear) 1 ] (4)

import time
import psutil
import os

from collections import deque

process = psutil.Process(os.getpid())
start_time = time.time()
my_queue = deque()
my_queue.append("a")
my_queue.append("b")
my_queue.append("c")
my_queue.append("d")
my_queue.append("e")
my_queue.popleft()
print(my_queue)
my_queue.popleft()
print(f"el resultado de la cola es: {my_queue}")


end_time = time.time()
memory_usage = process.memory_info().rss / (1024 * 1024)

print(f"tiempo: {(end_time - start_time):.10f} segundos, uso de memoria: {memory_usage:.2f} Mb" )






