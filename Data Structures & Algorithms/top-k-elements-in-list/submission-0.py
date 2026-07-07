class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        for i in nums:
            count[i] += 1
        maximum = []
        for k in range(k):
            maximum.append(max(count))
            count.pop(max(count))
        return maximum