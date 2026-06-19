class Solution(object):
  
    def largestAltitude(self, gain):
          current = 0
          highest = 0 
          for v in gain:
              current = current + v
              highest = max(highest,current)
          return highest
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna