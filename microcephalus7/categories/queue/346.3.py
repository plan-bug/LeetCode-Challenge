# 나올떄까지 첫번째 요소만 없앤다
# list 는 도마 위의 무

class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        queue = self.queue
        queue.append(t)
        while(queue and queue[0] < t-3000):
            del queue[0]
        return len(queue)
