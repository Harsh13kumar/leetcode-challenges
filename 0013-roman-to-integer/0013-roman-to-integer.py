class Solution(object):
    def romanToInt(self, s):
        total = 0
        skip = False
        set={"I":1,
               "V":5,
               "X":10,
               "L":50,
               "C":100,
               "D":500,
               "M":1000}
           
        for i in range(len(s)): 
            if skip:
                skip = False
                continue
            elif i < len(s)-1 :
                current = set[s[i]]
                next = set[s[i+1]]
                if current > next:
                    total += current
                elif current == next:
                    total += current
                else :
                    total += next - current
                    skip = True
              
            else :
                current = set[s[i]]
                total += current
        return(total)

       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna