from heapq import heappop, heappush

tasks = []
heappush(tasks, (30, 'work out'))
heappush(tasks, (10, 'wake out'))
heappush(tasks, (21,  'hello'))
heappush(tasks, (20, 'feed cat'))
heappush(tasks, (20, 'write book'))

print("-------------")
while tasks:
    _, payload = heappop(tasks) # <label id="code.pop" />
    print(payload)
print("-------------")
