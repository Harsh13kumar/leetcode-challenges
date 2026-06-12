class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        unique = 1
        pointer = nums[0]
        while i < len(nums) - 1:
            if i !=len(nums) - 1 and pointer == nums[i+1]:
                i = i+1
            else:
                nums[unique]=nums[i+1]
                unique+=1
                pointer= nums[i+1] 
                i = i+1
                
        return unique
    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna