import copy

class Solution:
    def __init__(self):
        self.output = [[]]

    def subsets(self, nums):
        def combination(arr, r):
            # 1.
            arr = sorted(arr)
            used = [0 for _ in range(len(arr))]
            # 2.
            def generate(chosen):
                if len(chosen) == r:
                    self.output.append(copy.deepcopy(chosen))
                    return
                # 3.
                start = arr.index(chosen[-1]) + 1 if chosen else 0
                for nxt in range(start, len(arr)):
                    if used[nxt] == 0 and (nxt == 0 or arr[nxt - 1] != arr[nxt] or used[nxt - 1]):
                        chosen.append(arr[nxt])
                        used[nxt] = 1
                        generate(chosen)
                        chosen.pop()
                        used[nxt] = 0

            generate([])

        for i in range(1, len(nums) + 1):
            combination(nums, i)

        print(self.output)
        return self.output


nums = [1,2,3]
s = Solution()
s.subsets(nums)