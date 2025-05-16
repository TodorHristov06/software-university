from collections import deque

kids = input().split()
n = int(input())

queue = deque(kids)

while len(queue) > 1:
    queue.rotate(-n + 1)
    removed_kid = queue.popleft()
    print(f"Removed {removed_kid}")

print(f"Last is {queue[0]}")