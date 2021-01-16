class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            i = 0

            k = 0
            while i < len(nums):
                j = i + 1
                flag = False
                nums[k] = nums[i]
                while j < len(nums):
                    if nums[i] != nums[j]:
                        break
                    else:
                        flag = True
                        j += 1
                if flag:
                    k += 1
                    nums[k] = nums[i]
                    i = j
                else:
                    i += 1
                k += 1
            nums = nums[:k]
            print(nums)
            return k

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    print(solution.removeDuplicates(nums))
    print(nums)