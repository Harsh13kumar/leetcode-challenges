class Solution(object):
    def isPalindrome(self, x):
        
        original = x
        reversed_num = 0
        if (x<0 ) :
            return False
        while x > 0:
            digit = x%10
            reversed_num = reversed_num *10 + digit
            x = x//10
        return (reversed_num == original)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna