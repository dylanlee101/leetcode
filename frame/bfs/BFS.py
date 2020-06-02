'''
计算起点start 到 终点 target 的最近距离
'''
import queue
def BFS(start,target):
    q = queue.Queue()
    visited = set()

    q.put(start)
    visited.add(start)
    step = 0
    while not q.empty():
        sz = q.qsize()
        for i in range(sz):
            cur = q.get()
            if cur == target:
                return step
            for x in cur.adj():
                if x not in visited:
                    q.put(x)
                    visited.add(x)
        step += 1



