class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        hashmap = self.hashmap
        if key in hashmap:
            hashmap[key].append((value, timestamp))
        else:
            hashmap[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        hashmap = self.hashmap
        if key not in hashmap:
            return ""

        ls = hashmap[key]
        if timestamp < ls[0][1]:
            return ""
        
        
        l = 0
        r = len(ls) - 1

        while l <= r:
            m = (l + r) // 2

            if timestamp < ls[m][1]:
                r = m - 1
            elif timestamp > ls[m][1]:
                l = m + 1
            else:
                return ls[m][0]

        return ls[r][0]

        
