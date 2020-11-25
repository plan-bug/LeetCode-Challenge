# queue
# queue 자료 구조 생성 (list)
# queue 에서 범위보다 작은 수 index 구한 뒤 해당 인덱스에서 커팅
# 커팅된 queue 길이 return

class RecentCounter:
    queue = []

    def __init__(self):
        self.queue.clear()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        i = len(self.queue)-1
        while i >= 0:
            if self.queue[i] < t-3000:
                self.queue = self.queue[i+1:]
                break
            i -= 1
        return len(self.queue)
