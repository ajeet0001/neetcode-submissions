class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        sorted_f = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        ans = []
        for v in sorted_f.keys():
            ans.append(v)
            k -= 1
            if k == 0:
                break
        return ans

