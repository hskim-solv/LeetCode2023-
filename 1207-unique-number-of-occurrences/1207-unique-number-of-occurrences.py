class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #arr = Counter(arr).values()
        return len(Counter(arr).values()) == len(set(Counter(arr).values()))