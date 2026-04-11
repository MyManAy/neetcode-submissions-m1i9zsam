class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def rec(built, visited):
            if len(built) == len(nums):
                res.append(built[:])
                return

            for num in nums:

                if num in visited:
                    continue

                built.append(num)
                visited.add(num)
                rec(built, visited)
                built.pop()
                visited.remove(num)

            return

        rec([], set())

        return res

            