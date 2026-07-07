class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        for i in nums:
            count[i] += 1
        maximum = []
        for _ in range(k):
            top = max(count, key = count.get)
            maximum.append(top)
            count.pop(top)
        return maximum