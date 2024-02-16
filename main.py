class Solution:
    def largestPerimeter(self, nums: [int]) -> int:
        nums.sort(reverse=True)

        index = -1
        for i in range(len(nums)-1):
            j = i + 1

            sum = 0
            x = j
            while x < len(nums):
                sum += nums[x]
                x += 1

            if sum <= nums[i]:
               index = i
            else:
                break

        if index >= 0:
            nums = nums[index + 1:]

        if len(nums) < 3:
            return -1

        sum = 0
        for n in nums:
            sum += n

        return sum

    def largestPerimeter2(self, nums: [int]) -> int:
        if len(nums) < 3:
            return -1

        nums.sort(reverse=True)
        total_sum = sum(nums)

        i = 0
        while i < len(nums):
            total_sum -= nums[i]

            if total_sum <= nums[i]:
                nums.pop(0)
                i -= 1
            else:
                break

            if len(nums) < 3:
                return -1
            i += 1

        return sum(nums)


if __name__ == '__main__':
    s = Solution()
    test = [1,12,1,2,5,50,3]
    test2 = [5,5,5]
    print(s.largestPerimeter2(test))
