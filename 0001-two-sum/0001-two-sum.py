class Solution(object):
    def twoSum(self, nums, target):
        seen ={}
        for index, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need],index]
            seen[num] = index

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna