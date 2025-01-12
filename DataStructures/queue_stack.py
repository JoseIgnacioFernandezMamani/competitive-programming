# Queues and stack with class colleactions 

# queue
# FIFO (first in, first out)
# [ (first) a ] (0) [ b ] (1) [ c ] (2) [ d ] (3) [ (last) e ] (4)

from collections import deque

# Implementation of queue

queue = deque()
queue.append("a")
queue.append("b")
queue.append("c")
queue.append("d")
queue.append("e")
queue.popleft()
print(queue)
queue.popleft()
print(queue)

# stack
# Stack

# LIFO (last in first out)
# [ (top) a ] (4)
# [ b ] (3)
# [ c ] (2)
# [ d ] (1)
# [ (bottom) e ] (0)

# Implementation of stack

stack = deque()
stack.appendleft("e")
stack.appendleft("d")
stack.appendleft("c")
stack.appendleft("b")
stack.appendleft("a")
print(stack)

# eliminar
stack.popleft()
print(stack)









