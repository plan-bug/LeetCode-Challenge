# deque 사용
# queue 의 첫번째가 t-3000 보다 커질때 까지 queue 첫번째 요소 제거
class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        queue = self.queue
        queue.append(t)
        while(queue and queue[0] < t-3000):
            queue.popleft()
        return len(queue)
