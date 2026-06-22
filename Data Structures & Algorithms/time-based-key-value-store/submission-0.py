from bisect import bisect_right
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        history = self.timeMap[key]
        idx = bisect_right(history, [timestamp, chr(127)]) - 1
        if idx < 0:
            return ""
        return history[idx][1]
        