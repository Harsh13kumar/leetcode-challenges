class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        best_land_finish = float('inf')
        best_water_finish  = float('inf')
        ans = float('inf')
        for i in range(len(landStartTime)):
            landfinish = landStartTime[i] + landDuration[i]
            best_land_finish = min(best_land_finish,landfinish)
        for j in range(len(waterStartTime)):
            
            water_start = max(best_land_finish, waterStartTime[j])
            waterfinish =water_start + waterDuration[j]
            ans = min(ans,waterfinish)

        for k in range(len(waterStartTime)):
            waterfinish = waterStartTime[k] + waterDuration[k]
            best_water_finish = min(best_water_finish ,waterfinish)
        for m in range(len(landStartTime)):
            
            land_start = max(best_water_finish, landStartTime[m])
            landfinish =land_start + landDuration[m]
            ans = min(ans,landfinish)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna