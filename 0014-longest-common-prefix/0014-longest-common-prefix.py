class Solution(object):
    def longestCommonPrefix(self, strs):
       for i,v in enumerate(strs):
            if i ==0:
               prefix =strs[0]
            if v != prefix :  
               while not v.startswith(prefix):
                    prefix = prefix[:-1]
       return(prefix)  

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna