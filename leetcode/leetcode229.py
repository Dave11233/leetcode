class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        counter = Counter(nums)
        counter = list(
            sorted(
                list(zip(counter.keys(), counter.values())),
                key=lambda x: x[1]

            )
        )

        return [item[0] for item in counter[:2] if item[1] >= len(nums) / 3]
