class TimeMap:

    def __init__(self):
        self.s= {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.s:
            self.s[key] = {}
        if timestamp not in self.s[key]:
            self.s[key][timestamp] = []
        self.s[key][timestamp].append(value)
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.s:
            return ""
        seen = 0

        for time in self.s[key]:
            if time <= timestamp:
                seen = max(seen,time)
        return "" if seen == 0 else self.s[key][seen][-1]